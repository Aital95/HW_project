def to_uppercase(s):
    """Принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return s.upper()


def convert_to_uppercase(string):
    """Преобразовывает заданную строку в верхний регистр"""
    return string.upper()


def capitalize_first_letters(string):
    """Преобразовывает заглавные первые буквы каждого слова в строке"""
    words = string.split()
    capitalized_words = [word.capitalized() for word in words]
    return ' '.join(capitalized_words)
