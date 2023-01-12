from df_calculators import incredible_calculator_shorts

#Parametros de venta increible
RSI_inc_shorts = 70
MFI_inc_shorts = 75
STOCH_inc_shorts = 85
stoch_4hr_short = 85

#Empty lists for incredible trades
incredible_cryptos_shorts = []

#Entry prices list
incredible_prices_shorts = []
#Stochs 4hr
incredible_stoch_4hrk_shorts = []
incredible_stoch_4hrd_shorts = []

#stochs 1d
incredible_stoch_1dk_shorts = []
incredible_stoch_1dd_shorts = []

#Alerta cruce del stoch
a = 2.5
b = 7
c = -2.5
d = -7


def incredible_trade_detector_shorts(dict1, dict2, dict3,dict4, dict5, dict6, dict7, dict8, dict9, dict10):

    for (k, v), (k2, v2), (k3, v3), (k4, v4), (k5, v5), (k6, v6), (k7, v7), (k8, v8), (k9, v9), (k10, v10) in zip(dict1.items(), dict2.items(),
                            dict3.items(), dict4.items(), dict5.items(),dict6.items(),dict7.items(),dict8.items(),dict9.items(),dict10.items()):

        if ((v > RSI_inc_shorts) and (v2 > MFI_inc_shorts) and (v3 > STOCH_inc_shorts) and (v4 > STOCH_inc_shorts) and ((v3-v4)<=c) and ((v3-v4) >=d) and (v6 > stoch_4hr_short) and (v7 > stoch_4hr_short) and (v10 >= 65)):

            incredible_cryptos_shorts.append(k)
            incredible_prices_shorts.append(v5)
            incredible_stoch_4hrk_shorts.append(v6)
            incredible_stoch_4hrd_shorts.append(v7)
            incredible_stoch_1dk_shorts.append(v8)
            incredible_stoch_1dd_shorts.append(v9)

    incredible_list = list(zip(incredible_cryptos_shorts, incredible_prices_shorts))
    incredible_list_macro4hr = list(zip(incredible_cryptos_shorts, incredible_stoch_4hrk_shorts, incredible_stoch_4hrd_shorts))
    incredible_list_macro1d = list(zip(incredible_cryptos_shorts, incredible_stoch_1dk_shorts, incredible_stoch_1dd_shorts))

    incredible_calculator_shorts.df_incredible_calc_shorts(incredible_list, incredible_list_macro4hr, incredible_list_macro1d)

    incredible_cryptos_shorts.clear()
    incredible_prices_shorts.clear()
    incredible_stoch_4hrk_shorts.clear()
    incredible_stoch_4hrd_shorts.clear()
    incredible_stoch_1dk_shorts.clear()
    incredible_stoch_1dd_shorts.clear()