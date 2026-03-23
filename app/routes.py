from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db, login_manager
from app.models import Player, User
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm import sessionmaker
from app.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint, shuffle, sample
import unicodedata


def shuffle_words_preserve_spaces(text):
    result = []
    for word in text.split(' '):
        if word == '':
            result.append('')
        else:
            letters = list(word)
            shuffle(letters)
            result.append(''.join(letters))
    return ' '.join(result).lower()




def remove_diacritics(text):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', text)
        if not unicodedata.combining(c)
    )




def clear_session():
    session.pop('player_id', None)
    session.pop('revealed_hints', None)
    session.pop('shuffled_indexes', None)
    session.pop('score', None)
    session.pop('round', None)
    session.pop('final_score', None)
    session.pop('round_history', None)
    session.pop('tries_left', None)
    session.pop('round_number', None)
    session.pop('player_history', None)
    session.pop('display_answer', None)
    session.pop('correct_answers', None)
    session.pop('_flashes', None)  # Usuwa wszystkie niewyświetlone komunikaty flash




login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():  # dopiero po kliknięciu "Zaloguj"
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))  # lub inna strona po zalogowaniu
        else: flash("Niepoprawny Email lub hasło.")
        

    return render_template('login.html', form=form)



@app.route('/logout')
@login_required
def logout():
    session.clear()
    session.pop('_flashes', None)  # Usuwa wszystkie niewyświetlone komunikaty flash
    logout_user()
    return redirect(url_for('login'))

    
@app.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
    clear_session()
    session.pop('_flashes', None)  # Usuwa wszystkie niewyświetlone komunikaty flash
    return render_template('dashboard.html')





@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
        
        

    return render_template('register.html', form=form)








@app.route('/card_game', methods=['GET', 'POST'])
@login_required
def card_game():
    if 'round' not in session:
        session['round'] = 1
        session['score'] = 10
        session['final_score'] = 0
        session['wrong_answer'] = False
        session['round_history'] = {}

    

    if request.method == 'POST':
        player_id = session.get('player_id')
        random_player = Player.query.get(player_id)
        answer1 = f"{random_player.first_name} {random_player.last_name}".lower()
        answer2 = remove_diacritics(answer1)
        answer3 = None
        if random_player.nickname:
            answer3 = remove_diacritics(random_player.nickname).lower()

        correct_answers = [answer1, answer2]
        if answer3:
            correct_answers.append(answer3)
        user_answer = request.form.get('answer', '').strip().lower()

        if user_answer in correct_answers:
            round_history = session['round_history']
            round_number = int(session['round'])  
            round_score = session['score']
            round_history[str(round_number)] = f'Runda {round_number}: {random_player.first_name} {random_player.last_name} - {round_score} punktów'
            session['round_history'] = round_history  
            session['score'] = 10  # resetujemy punkty na nową rundę
            session['final_score'] = session.get('final_score', 0) + round_score  
            session['round'] = round_number + 1
            session.pop('player_id', None)
            session.pop('revealed_hints', None)
            


            # Jeśli była to 3. runda, przechodzimy do zakończenia gry
            if round_number >= 3:
                return redirect(url_for('end_game', final_score=session['final_score']))  # końcowa strona
            else:
                flash(f"✅ Dobrze! Zdobywasz {round_score} punktów w rundzie {round_number}.")
                return redirect(url_for('card_game'))

        else:
            flash("❌ Błędna odpowiedź. Spróbuj ponownie.")
            session['wrong_answer'] = True
            return redirect(url_for('reveal_hint')) 

    # GET — nowa runda lub pierwsze wejście
    if 'player_id' not in session:
        player_count = Player.query.count()
        random_number = randint(1, player_count)
        random_player = Player.query.get(random_number)
        session['player_id'] = random_player.id

        # NOWE: zapisujemy przetasowaną kolejność kafelków
        indexes = list(range(10))
        shuffle(indexes)
        session['shuffled_indexes'] = indexes

        # Nowe losowanie 3 odkrytych podpowiedzi na start
        revealed = sample(indexes, 3)
        session['revealed_hints'] = revealed
    else:
        random_player = Player.query.get(session['player_id'])    

    return render_template(
        'card_game.html',
        random_player=random_player,
        player_info=random_player.get_info_list(),
        revealed_indexes=session['revealed_hints'],
        shuffled_indexes=session['shuffled_indexes'],
        score=session['score'],
        round=session['round'],
        points=session['final_score']
    )


@app.route('/reveal_hint', methods=['POST', 'GET'])
@login_required
def reveal_hint():
    if not session.get('wrong_answer', False):    
        hint_key = request.form.get('hint_key')

        if hint_key is None:
            flash("Nieprawidłowa podpowiedź.")
            return redirect(url_for('card_game'))

        try:
            hint_key = int(hint_key)
        except ValueError:
            flash("Nieprawidłowa wartość podpowiedzi.")
            return redirect(url_for('card_game'))

        revealed = session.get('revealed_hints', [])

        if hint_key not in revealed:
            revealed.append(hint_key)
            session['revealed_hints'] = revealed

            score = session.get('score', 10)
            session['score'] = max(0, score - 1)

        return redirect(url_for('card_game'))
    
    
    
    revealed = session.get('revealed_hints', [])
    for _ in range(9):
        hint_key = randint(0, 9)
        if hint_key not in revealed:
            revealed.append(hint_key)
            session['revealed_hints'] = revealed
            break
    session['wrong_answer'] = False
    score = session.get('score', 10)
    session['score'] = max(0, score - 1)

    return redirect(url_for('card_game'))




@app.route('/end_game')
@login_required
def end_game():
    round_history = session.get('round_history', {})
    final_score = request.args.get('final_score', 0)
    clear_session()
    session.pop('_flashes', None)  # Usuwa wszystkie niewyświetlone komunikaty flash
    return render_template('end_game.html', final_score=final_score, round_history=round_history)




@app.route('/choose_game', methods=['GET', 'POST'])
@login_required
def choose_game():
    return render_template('choose_game.html')



#LOSOWANIE GRACZA DO PUZZLE
def set_random_player():
    player_count = Player.query.count()
    random_number = randint(1, player_count)
    random_player = Player.query.get(random_number)
    session['player_id'] = random_player.id
    player_name = f"{random_player.first_name} {random_player.last_name}".lower()
    answer1 = player_name
    answer2 = remove_diacritics(answer1)
    correct_answers = [answer1, answer2]
    if random_player.nickname:
        answer3 = remove_diacritics(random_player.nickname).lower()
        correct_answers.append(answer3)
    session['correct_answers'] = correct_answers
    session['display_answer'] = shuffle_words_preserve_spaces(correct_answers[0]) if len(correct_answers) < 3 else shuffle_words_preserve_spaces(correct_answers[2])



@app.route('/puzzle_game', methods=['GET', 'POST'])
@login_required
def puzzle_game():
    if 'player_history' not in session:
        session['player_history'] = []
    if 'round_number' not in session:
        session['round_number'] = 1
    if 'tries_left' not in session:
        session['tries_left'] = 3
    if 'player_id' not in session:
        set_random_player()

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        correct_answers = [ans.strip().lower() for ans in session.get('correct_answers', [])]

        if user_answer in correct_answers:
            history = session.get('player_history', [])
            history.append([session['round_number'], correct_answers[0], True])
            session['player_history'] = history

            session['round_number'] += 1
            session['tries_left'] = 3
            set_random_player()
            flash("✅ Dobrze! To poprawna odpowiedź.")
        else:
            session['tries_left'] -= 1
            if session['tries_left'] <= 0:
                history = session.get('player_history', [])
                history.append([session['round_number'], correct_answers[0], False])
                session['player_history'] = history

                session['round_number'] += 1
                session['tries_left'] = 3
                set_random_player()
                flash("❌ Niestety, nie udało się odgadnąć. Oto kolejny przykład.")
            else:
                flash("❌ Błędna odpowiedź. Spróbuj ponownie.")

        if session['round_number'] > 3:
            return redirect(url_for('end_game_puzzle'))

    return render_template(
        'puzzle_game.html',
        round_number=session['round_number'],
        tries_left=session['tries_left'],
        display_answer=session['display_answer']
    )







@app.route('/end_game_puzzle')
@login_required
def end_game_puzzle():
    player_history = session.get('player_history', [])
    clear_session()
    session.pop('_flashes', None)  # Usuwa wszystkie niewyświetlone komunikaty flash
    return render_template('end_game_puzzle.html', player_history=player_history)