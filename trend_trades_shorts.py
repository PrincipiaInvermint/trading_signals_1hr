from df_calculators import trend_calculator_shorts

#Empty lists for trend trades
trend_cryptos_shorts = []

#Entry prices list
trend_entry_prices_shorts = []
#Stochs 4hr
trend_stoch_4hrk_shorts = []
trend_stoch_4hrd_shorts = []

#stochs 1d
trend_stoch_1dk_shorts = []
trend_stoch_1dd_shorts = []

#Parametros de Compra Reversal y Trend Trade
RSI_shorts = 55
MFI_shorts = 65
STOCH_shorts = 88



#Alerta cruce del stoch
a = 2.5
b = 7
c = -2.5
d = -7

def trend_trade_detector_shorts(dict1, dict2, dict3, dict4,dict5,dict6,dict7,dict8,dict9,dict10,dict11,dict12,dict13):

    for (k, v), (k2, v2), (k3, v3), (k4, v4),(k5, v5),(k6, v6), (k7,v7),(k8,v8),(k9,v9),(k10,v10),(k11,v11),(k12,v12),(k13,v13) in zip(dict1.items(), dict2.items(), dict3.items(), dict4.items(), dict5.items(),dict6.items(),
                                                                                                                        dict7.items(),dict8.items(),dict9.items(),dict10.items(),dict11.items(),dict12.items(),dict13.items()):

        if ((v > RSI_shorts) and (v2 > MFI_shorts) and (v3 > STOCH_shorts) and (v4 > STOCH_shorts) and ((v3 - v4) <= c) and ((v3 - v4) >= d)  and (v8 <= v6) and (v8 <= v7) and (v5<v6) and (v6<v7)):

            trend_cryptos_shorts.append(k)
            trend_entry_prices_shorts.append(v8)
            trend_stoch_4hrk_shorts.append(v9)
            trend_stoch_4hrd_shorts.append(v10)
            trend_stoch_1dk_shorts.append(v11)
            trend_stoch_1dd_shorts.append(v12)


    #
    trend_list = list(zip(trend_cryptos_shorts, trend_entry_prices_shorts))
    trend_list_macro4hr = list(zip(trend_cryptos_shorts, trend_stoch_4hrk_shorts, trend_stoch_4hrd_shorts))
    trend_list_macro1d = list(zip(trend_cryptos_shorts, trend_stoch_1dk_shorts, trend_stoch_1dd_shorts))

    trend_calculator_shorts.df_trend_calc_shorts(trend_list, trend_list_macro4hr, trend_list_macro1d)

    trend_cryptos_shorts.clear()
    trend_entry_prices_shorts.clear()
    trend_stoch_4hrk_shorts.clear()
    trend_stoch_4hrd_shorts.clear()
    trend_stoch_1dk_shorts.clear()
    trend_stoch_1dd_shorts.clear()