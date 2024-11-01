from datetime import date
from django import template

register = template.Library()

@register.filter()
def mostra_duracao(data_devolucao):
    dias_restantes = (data_devolucao - date.today()).days
    return dias_restantes if dias_restantes > 0 else 0