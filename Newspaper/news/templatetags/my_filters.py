from django import template

register = template.Library()


@register.filter()
def censor(value):
    if isinstance(value, str):
        censored_words = ['редиска', 'Редиска']
        for word in censored_words:
           value = value.replace(word[1:], '*' * (len(word)-1))
        return value