from app import app, db
from app.models import Player

def seed_players():
    players_data = [
        Player(first_name="Lionel", last_name="Messi", nationality="Argentina", position="Forward", current_club="Inter Miami", previous_club="PSG", goals=821, assists=361, appearances=1045, league_titles=12, national_titles=7, ucl_titles=4, nickname="La Pulga"),
        Player(first_name="Cristiano", last_name="Ronaldo", nationality="Portugal", position="Forward", current_club="Al Nassr", previous_club="Manchester United", goals=873, assists=249, appearances=1200, league_titles=7, national_titles=6, ucl_titles=5, nickname="CR7"),
        Player(first_name="Robert", last_name="Lewandowski", nationality="Poland", position="Striker", current_club="FC Barcelona", previous_club="Bayern Munich", goals=640, assists=150, appearances=900, league_titles=12, national_titles=5, ucl_titles=1, nickname="Lewy"),
        Player(first_name="Kylian", last_name="Mbappe", nationality="France", position="Forward", current_club="PSG", previous_club="Monaco", goals=320, assists=130, appearances=420, league_titles=6, national_titles=4, ucl_titles=0, nickname="Donatello"),
        Player(first_name="Erling", last_name="Haaland", nationality="Norway", position="Striker", current_club="Manchester City", previous_club="Borussia Dortmund", goals=240, assists=50, appearances=290, league_titles=3, national_titles=2, ucl_titles=1, nickname="Terminator"),
        Player(first_name="Kevin", last_name="De Bruyne", nationality="Belgium", position="Midfielder", current_club="Manchester City", previous_club="Wolfsburg", goals=150, assists=280, appearances=650, league_titles=5, national_titles=6, ucl_titles=1, nickname="KDB"),
        Player(first_name="Neymar", last_name="Jr", nationality="Brazil", position="Forward", current_club="Al Hilal", previous_club="PSG", goals=430, assists=250, appearances=700, league_titles=7, national_titles=4, ucl_titles=1, nickname=None),
        Player(first_name="Mohamed", last_name="Salah", nationality="Egypt", position="Forward", current_club="Liverpool", previous_club="AS Roma", goals=330, assists=140, appearances=600, league_titles=3, national_titles=2, ucl_titles=1, nickname="Egyptian King"),
        Player(first_name="Luka", last_name="Modric", nationality="Croatia", position="Midfielder", current_club="Real Madrid", previous_club="Tottenham", goals=100, assists=160, appearances=950, league_titles=3, national_titles=2, ucl_titles=5, nickname="Cruyff of the Balkans"),
        Player(first_name="Virgil", last_name="van Dijk", nationality="Netherlands", position="Defender", current_club="Liverpool", previous_club="Southampton", goals=50, assists=20, appearances=550, league_titles=2, national_titles=1, ucl_titles=1, nickname=None),
        Player(first_name="Karim", last_name="Benzema", nationality="France", position="Striker", current_club="Al-Ittihad", previous_club="Real Madrid", goals=460, assists=190, appearances=850, league_titles=8, national_titles=3, ucl_titles=5, nickname="Coco"),
        Player(first_name="Toni", last_name="Kroos", nationality="Germany", position="Midfielder", current_club="Real Madrid", previous_club="Bayern Munich", goals=70, assists=160, appearances=800, league_titles=6, national_titles=4, ucl_titles=5, nickname="Sniper"),
        Player(first_name="Vinicius", last_name="Junior", nationality="Brazil", position="Forward", current_club="Real Madrid", previous_club="Flamengo", goals=90, assists=80, appearances=300, league_titles=2, national_titles=1, ucl_titles=1, nickname="Vini"),
        Player(first_name="Jude", last_name="Bellingham", nationality="England", position="Midfielder", current_club="Real Madrid", previous_club="Borussia Dortmund", goals=60, assists=50, appearances=250, league_titles=0, national_titles=1, ucl_titles=0, nickname=None),
        Player(first_name="Harry", last_name="Kane", nationality="England", position="Striker", current_club="Bayern Munich", previous_club="Tottenham", goals=380, assists=110, appearances=600, league_titles=0, national_titles=0, ucl_titles=0, nickname="HurriKane"),
        Player(first_name="Antoine", last_name="Griezmann", nationality="France", position="Forward", current_club="Atletico Madrid", previous_club="FC Barcelona", goals=280, assists=130, appearances=700, league_titles=0, national_titles=1, ucl_titles=0, nickname="Grizou"),
        Player(first_name="Manuel", last_name="Neuer", nationality="Germany", position="Goalkeeper", current_club="Bayern Munich", previous_club="Schalke 04", goals=0, assists=7, appearances=850, league_titles=11, national_titles=6, ucl_titles=2, nickname="Sweeper Keeper"),
        Player(first_name="Gianluigi", last_name="Buffon", nationality="Italy", position="Goalkeeper", current_club=None, previous_club="Juventus", goals=0, assists=0, appearances=1151, league_titles=10, national_titles=6, ucl_titles=0, nickname="Gigi"),
        Player(first_name="Ronaldo", last_name="Nazario", nationality="Brazil", position="Striker", current_club=None, previous_club="Real Madrid", goals=414, assists=104, appearances=616, league_titles=2, national_titles=3, ucl_titles=0, nickname="Il Fenomeno"),
        Player(first_name="Zinedine", last_name="Zidane", nationality="France", position="Midfielder", current_club=None, previous_club="Real Madrid", goals=156, assists=146, appearances=797, league_titles=3, national_titles=0, ucl_titles=1, nickname="Zizou"),
        Player(first_name="Diego", last_name="Maradona", nationality="Argentina", position="Midfielder", current_club=None, previous_club="Napoli", goals=344, assists=150, appearances=680, league_titles=3, national_titles=2, ucl_titles=0, nickname="El Pibe de Oro"),
        Player(first_name="Edson", last_name="Pele", nationality="Brazil", position="Forward", current_club=None, previous_club="Santos", goals=1281, assists=0, appearances=1363, league_titles=6, national_titles=0, ucl_titles=2, nickname="O Rei"),
        Player(first_name="Johan", last_name="Cruyff", nationality="Netherlands", position="Forward", current_club=None, previous_club="Ajax", goals=433, assists=150, appearances=752, league_titles=9, national_titles=6, ucl_titles=3, nickname="El Salvador"),
        Player(first_name="Paolo", last_name="Maldini", nationality="Italy", position="Defender", current_club=None, previous_club="AC Milan", goals=45, assists=0, appearances=1041, league_titles=7, national_titles=1, ucl_titles=5, nickname="Il Capitano"),
        Player(first_name="Sergio", last_name="Ramos", nationality="Spain", position="Defender", current_club="Sevilla", previous_club="PSG", goals=133, assists=42, appearances=950, league_titles=5, national_titles=2, ucl_titles=4, nickname="El Cuqui"),
        Player(first_name="Xavi", last_name="Hernandez", nationality="Spain", position="Midfielder", current_club=None, previous_club="FC Barcelona", goals=121, assists=238, appearances=1035, league_titles=8, national_titles=3, ucl_titles=4, nickname="The Puppet Master"),
        Player(first_name="Andres", last_name="Iniesta", nationality="Spain", position="Midfielder", current_club="Emirates Club", previous_club="Vissel Kobe", goals=93, assists=191, appearances=950, league_titles=9, national_titles=6, ucl_titles=4, nickname="El Ilusionista"),
        Player(first_name="Zlatan", last_name="Ibrahimovic", nationality="Sweden", position="Striker", current_club=None, previous_club="AC Milan", goals=573, assists=227, appearances=988, league_titles=12, national_titles=3, ucl_titles=0, nickname="Ibra"),
        Player(first_name="Luis", last_name="Suarez", nationality="Uruguay", position="Striker", current_club="Inter Miami", previous_club="Gremio", goals=555, assists=300, appearances=900, league_titles=7, national_titles=2, ucl_titles=1, nickname="El Pistolero"),
        Player(first_name="Wayne", last_name="Rooney", nationality="England", position="Striker", current_club=None, previous_club="Manchester United", goals=366, assists=188, appearances=883, league_titles=5, national_titles=1, ucl_titles=1, nickname="Wazza")
    ]

    with app.app_context():
        # Zabezpieczenie: ładujemy dane tylko jeśli tabela jest pusta
        if Player.query.count() == 0:
            db.session.add_all(players_data)
            db.session.commit()
            print("Zakończono: 30 zawodników zostało pomyślnie dodanych do bazy.")
        else:
            print("Uwaga: Tabela piłkarzy nie jest pusta. Pomijam dodawanie.")

if __name__ == "__main__":
    seed_players()