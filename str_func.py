def func():
    """функция переводит буквы в заглавные"""
    text = input("Введите слово: ").upper()
    print(text)

func()

def up_words():
    """Функция которая делает первые буквы слова заглавными"""
    word = input("Введите текст: ")
    word = ' '.join(word.capitalize() for word in word.split())
    print(word)

up_words()