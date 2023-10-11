"""
📌Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌Возвращается строка в нижнем регистре.
"""
from string import ascii_lowercase


def clear_text(text):
    """
    >>> clear_text('TExt пробный proba')
    'text  proba'
    >>> clear_text('TExt') == 'text'
    True
    >>> clear_text('TEвыпыпю...xt') == 'text'
    True
    """
    result = ''
    if text is not None:
        for i in text:
            if i.lower() in ascii_lowercase + ' ':
                result += i
        return result.lower()
    raise ValueError('Incorect text')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



