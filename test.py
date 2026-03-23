import random

def shuffle_words_preserve_spaces(text):
    result = []
    for word in text.split(' '):
        if word == '':
            result.append('')
        else:
            letters = list(word)
            random.shuffle(letters)
            result.append(''.join(letters))
    return ' '.join(result).lower()



print(shuffle_words_preserve_spaces('Lionel Messi'))