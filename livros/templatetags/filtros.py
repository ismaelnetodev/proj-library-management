from datetime import date
from django import template

register = template.Library()

@register.filter()
def mostra_duracao(data_devolucao):
    if data_devolucao is not None:
        dias_restantes = (data_devolucao - date.today()).days
        if dias_restantes < 0:
            return "Vencido"
        elif dias_restantes == 0:
            return "Vence hoje"
        else:
            return f"{dias_restantes} Dias"
    return "Data não definida"