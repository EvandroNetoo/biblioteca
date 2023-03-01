from django import template
from datetime import timedelta


register = template.Library()


@register.filter
def mostra_duracao(value1, value2):
    if not value1:
        return f'Livro ainda não devolvido'

    temp = value1 - value2
    zero = timedelta(0)
    trinta = timedelta(30)

    if temp >= trinta:
        meses = int(temp / trinta)
        dias = (temp % trinta).days

        txt_m = 'Mês' if meses == 1 else 'Meses'
        txt_d = 'Dia' if dias == 1 else 'Dias'
        return f'{meses} {txt_m} e {dias} {txt_d}'

    txt = 'Dia' if (value1 - value2).days == 1 else 'Dias'
    return f'{(value1 - value2).days} {txt}'


