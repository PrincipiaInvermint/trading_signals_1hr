from df_calculators import trend_calculator

#Empty lists for trend trades
trend_cryptos = []

#Entry prices list
trend_entry_prices = []
#Stochs 4hr
trend_stoch_4hrk = []
trend_stoch_4hrd = []

#stochs 1d
trend_stoch_1dk = []
trend_stoch_1dd = []

#Parametros de Compra Reversal y Trend Trade
RSI_buy = 45
MFI_buy = 35
STOCH_buy = 12


#Alerta cruce del stoch
a = 2.5
b = 7
c = -2.5
d = -7

def trend_trade_detector(dict1, dict2, dict3, dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13):

    for (k, v), (k2, v2), (k3, v3), (k4, v4),(k5, v5),(k6, v6), (k7,v7),(k8,v8),(k9,v9),(k10,v10),(k11,v11),(k12,v12),(k13,v13) in zip(dict1.items(), dict2.items(), dict3.items(), dict4.items(), dict5.items(),dict6.items(),
                                                                                                                        dict7.items(),dict8.items(),dict9.items(),dict10.items(),dict11.items(),dict12.items(),dict13.items()):

        if ((v < RSI_buy) and (v2 < MFI_buy) and (v3 < STOCH_buy) and (v4 < STOCH_buy)  and ((v3 - v4) >= a) and ((v3 - v4) <= b)  and (v8 >= v6) and (v8 >= v7) and (v5>v6) and (v6>v7)):

            trend_cryptos.append(k)
            trend_entry_prices.append(v8)
            trend_stoch_4hrk.append(v9)
            trend_stoch_4hrd.append(v10)
            trend_stoch_1dk.append(v11)
            trend_stoch_1dd.append(v12)


    #
    trend_list = list(zip(trend_cryptos, trend_entry_prices))
    trend_list_macro4hr = list(zip(trend_cryptos, trend_stoch_4hrk, trend_stoch_4hrd))
    trend_list_macro1d = list(zip(trend_cryptos, trend_stoch_1dk, trend_stoch_1dd))

    trend_calculator.df_trend_calc(trend_list, trend_list_macro4hr, trend_list_macro1d)

    trend_cryptos.clear()
    trend_entry_prices.clear()
    trend_stoch_4hrk.clear()
    trend_stoch_4hrd.clear()
    trend_stoch_1dk.clear()
    trend_stoch_1dd.clear()
