def classifier2(s):

    if (s['tendencia'] == 'bajista' and s['status'] == 'Neutral' and s['Cruce_stoch'] == 'continuacion'):
        return '5 stars'

    if (s['tendencia'] == 'bajista' and s['status'] == 'Neutral' and s['Cruce_stoch'] == 'posible reversion'):
        return '4 stars'

    if (s['tendencia'] == 'bajista' and s['status'] == 'sobrecompra' and s['Cruce_stoch'] == 'continuacion'):
        return '4 stars'

    if (s['tendencia'] == 'bajista' and s['status'] == 'sobrecompra' and s['Cruce_stoch'] == 'posible reversion'):
        return '4 stars'

    if (s['tendencia'] == 'bajista' and s['status'] == 'sobreventa' and s['Cruce_stoch'] == 'continuacion'):
        return '4 stars'

    if (s['tendencia'] == 'bajista' and s['status'] == 'sobreventa' and s['Cruce_stoch'] == 'posible reversion'):
        return '3 stars'

    if (s['tendencia'] == 'alcista' and s['status'] == 'Neutral' and s['Cruce_stoch'] == 'continuacion'):
        return '3 stars'

    if (s['tendencia'] == 'alcista' and s['status'] == 'Neutral' and s['Cruce_stoch'] == 'posible reversion'):
        return '5 stars'

    if (s['tendencia'] == 'alcista' and s['status'] == 'sobrecompra' and s['Cruce_stoch'] == 'continuacion'):
        return '5 stars'

    if (s['tendencia'] == 'alcista' and s['status'] == 'sobrecompra' and s['Cruce_stoch'] == 'posible reversion'):
        return '5 stars'

    if (s['tendencia'] == 'alcista' and s['status'] == 'sobreventa' and s['Cruce_stoch'] == 'continuacion'):
        return '3 stars'

    if (s['tendencia'] == 'alcista' and s['status'] == 'sobreventa' and s['Cruce_stoch'] == 'posible reversion'):
        return '4 stars'