import pandas as pd
from email_functions import telegram_sender, telegram_sender_principia, telegram_sender_quant, telegram_sender_bono6m
from rating_class import clasificador, summary

#Riesgo-beneficio, TPs
rb = 2


def df_reversal_calc(list, list2, list3):

    if (list != []):

        # Create dataframe
        df = pd.DataFrame(list)
        #change column names, MAs = TPs
        df.columns = ['Crypto', 'Precio_Entrada','TP3']


        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)

        # Calculate TP/SL% and R/B
        df['Distancia_TP'] = df.apply(lambda x: (x['TP3'] - x['Precio_Entrada']),axis=1)
        df['TP2'] = df.apply(lambda x: (x['TP3'] - (x['Distancia_TP'] * 0.3)), axis=1)
        df['TP1'] = df.apply(lambda x: (x['TP3'] - (x['Distancia_TP'] * 0.7)), axis=1)
        df['TP_porcentaje'] = df.apply(lambda x:((x['Distancia_TP'] / x['Precio_Entrada'] * 100)), axis=1)
        df['Precio_SL'] = df.apply(lambda x: (x['Precio_Entrada'] - (x['Distancia_TP'] / rb)), axis=1)
        df['Distancia_SL_porcentaje'] = df.apply(lambda x: (((x['Precio_SL'] / x['Precio_Entrada']) - 1) * 100), axis=1)

        # Drop columns
        df = df.drop(['Distancia_TP', 'Distancia_SL_porcentaje','TP_porcentaje'],axis=1)
        print(df)
        print('----------------------------------------')

        # Calculate 4hr dataframe conditions

        df_4horas = pd.DataFrame(list2)
        df_4horas.columns = ['Crypto', 'stoch_k', 'stoch_d']
        df_4horas['Diferencia_stochs'] = abs(df_4horas['stoch_k'] - df_4horas['stoch_d'])
        df_4horas['tendencia'] = df_4horas.apply(lambda x: 'bajista' if x['stoch_k'] < x['stoch_d'] else ('alcista' if x['stoch_k'] > x['stoch_d'] else 'iguales'), axis=1)
        df_4horas['status'] = df_4horas.apply(lambda x: 'sobrecompra' if x['stoch_k'] > 85 and x['stoch_d'] > 85 else ('sobreventa' if x['stoch_k'] < 15 and x['stoch_d'] < 15 else 'Neutral'), axis=1)
        df_4horas['Cruce_stoch'] = df_4horas.apply(lambda x: 'posible reversion' if x['Diferencia_stochs'] < 4 else 'continuacion', axis=1)
        df_4horas['Calificacion'] = df_4horas.apply(clasificador.classifier,axis=1)
        print(df_4horas)
        print('-----------------------------------------')


        # Calculate 1D dataframe conditions
        df_1dia = pd.DataFrame(list3)
        df_1dia.columns = ['Crypto', 'stoch_k', 'stoch_d']
        df_1dia['Diferencia_stochs'] = abs(df_1dia['stoch_k'] - df_1dia['stoch_d'])
        df_1dia['tendencia'] = df_1dia.apply(lambda x: 'bajista' if x['stoch_k'] < x['stoch_d'] else ('alcista' if x['stoch_k'] > x['stoch_d'] else 'iguales'), axis=1)
        df_1dia['status'] = df_1dia.apply(lambda x: 'sobrecompra' if x['stoch_k'] > 85 and x['stoch_d'] > 85 else ('sobreventa' if x['stoch_k'] < 15 and x['stoch_d'] < 15 else 'Neutral'), axis=1)
        df_1dia['Cruce_stoch'] = df_1dia.apply(lambda x: 'posible reversion' if x['Diferencia_stochs'] < 4 else 'continuacion', axis=1)
        df_1dia['Calificacion'] = df_1dia.apply(clasificador.classifier, axis=1)
        print(df_1dia)

        df['4hr'] = df_4horas['Calificacion']
        df['1dia'] = df_1dia['Calificacion']

        df['Rating'] = df.apply(summary.summary_stars,axis=1)


        #Final DF signals

        df = df.applymap(lambda x: round(x, 4) if isinstance(x, (int, float)) else x)
        df = df.drop(['4hr', '1dia'], axis=1)
        #ricci_group_1_emails.ricci_sender_1(df, 'Reversal Trades 1 hr long')
        #ricci_group_2_emails.ricci_sender_2(df, 'Reversal Trades 1 hr long')
        #principia_1_emails.principia_sender_1(df, 'Reversal Trades 1 hr long')
        #principia_2_emails.principia_sender_2(df, 'Reversal Trades 1 hr long')
        telegram_sender.send_telegram_message(df, 'Reversal Trades 1 hr long')
        telegram_sender_principia.send_telegram_message(df, 'Reversal Trades 1 hr long')
        telegram_sender_quant.send_telegram_message(df, 'Reversal Trades 1 hr long')
        telegram_sender_bono6m(df, 'Reversal Trades 1 hr long')

    else:
        print('no cryptos were found')