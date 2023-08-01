from binance.client import Client
import configparser
import pandas as pd
import talib
import time
import incredible_trades
import reversal_trades
import trend_trades
import incredible_trades_shorts
import trend_trades_shorts

# Cargar contraseñas API binanc
config = configparser.ConfigParser()
config.read_file(open('conexion_API.cfg'))
api = config.get('BINANCE', 'API')
key = config.get('BINANCE', 'KEY')
# este es moha
#Conexion con binance para extraer datos
client = Client(api, key)

#Crypto List
symbols = ('BTC','ETH','BNB','ADA','SOL','MATIC','DOT','TRX','AVAX','UNI','ATOM','LTC','LINK','XMR','ALGO','NEAR','AAVE',
            'FET','OCEAN','EGLD','FIL','SAND','MANA','FTM')




#Parametros para las señales 1 hora
run_interval_seconds = 60 * 30

#Ciclo While que se ejecuta cada 1 hora buscando las condiciones para los 3 tipos de trades

while True:

    RSI_list_1hr = []
    RSI_list_4hr = []
    RSI_list_1d = []

    STOCH_RSI_list_1hr_fastd = []
    STOCH_RSI_list_1hr_fastk = []

    STOCH_RSI_list_4hr_fastd = []
    STOCH_RSI_list_4hr_fastk = []

    STOCH_RSI_list_1d_fastd = []
    STOCH_RSI_list_1d_fastk = []

    MFI_list_1hr = []
    MFI_list_4hr = []
    MFI_list_1d = []

    MA_50_list_1hr = []
    MA_100_list_1hr = []
    MA_200_list_1hr = []

    MA_100_list_4hr = []
    MA_200_list_4hr = []

    closing_list = []


    for symbol in symbols:
        candles_1hr = client.get_klines(symbol=symbol + 'USDT', interval=Client.KLINE_INTERVAL_1HOUR)
        candles_4hr = client.get_klines(symbol=symbol + 'USDT', interval=Client.KLINE_INTERVAL_4HOUR)
        candles_1d = client.get_klines(symbol=symbol + 'USDT', interval=Client.KLINE_INTERVAL_1DAY)

        df_1hr = pd.DataFrame(candles_1hr)
        df_4hr = pd.DataFrame(candles_4hr)
        df_1d = pd.DataFrame(candles_1d)

        # 1 hour chart data
        closings_1hr = df_1hr.iloc[:, 4]
        high_1hr = df_1hr.iloc[:, 2]
        low_1hr = df_1hr.iloc[:, 3]
        volume_1hr = df_1hr.iloc[:, 5]

        #last clossing prices
        close = (closings_1hr.iloc[-1])


        #Moving averages
        MA_50 = talib.SMA(closings_1hr, timeperiod=50)
        MA_100 = talib.SMA(closings_1hr, timeperiod=100)
        MA_200 = talib.SMA(closings_1hr, timeperiod=200)

        last_MA50 = MA_50.iloc[-1]
        last_MA100 = MA_100.iloc[-1]
        last_MA200 = MA_200.iloc[-1]


        # RSI and STOCH RSI 1 hour
        rsi_1hr = talib.RSI(closings_1hr, timeperiod=14)
        fastk_1hr, fastd_1hr = talib.STOCH(rsi_1hr, rsi_1hr, rsi_1hr, fastk_period=14, slowk_period=3, slowd_period=4,
                                           slowd_matype=0)

        last_fastk_1hr = fastk_1hr.iloc[-1]
        last_fastd_1hr = fastd_1hr.iloc[-1]

        last_RSI_1hr = rsi_1hr.iloc[-1]

        # MFI 1 hour
        MFI_1hr = talib.MFI(high_1hr, low_1hr, closings_1hr, volume_1hr, timeperiod=12)
        last_MFI_1hr = MFI_1hr.iloc[-1]

        # 4 hours chart
        closings_4hr = df_4hr.iloc[:, 4]

        # RSI and STOCH RSI 4 hour
        rsi_4hr = talib.RSI(closings_4hr, timeperiod=14)
        fastk_4hr, fastd_4hr = talib.STOCH(rsi_4hr, rsi_4hr, rsi_4hr, fastk_period=14, slowk_period=3, slowd_period=4,
                                           slowd_matype=0)

        last_fastk_4hr = fastk_4hr.iloc[-1]
        last_fastd_4hr = fastd_4hr.iloc[-1]

        last_RSI_4hr = rsi_4hr.iloc[-1]

        # 1 day chart
        closings_1d = df_1d.iloc[:, 4]
        high_1d = df_1d.iloc[:, 2]
        low_1d = df_1d.iloc[:, 3]
        volume_1d = df_1d.iloc[:, 5]

        # RSI and STOCH RSI 1 day
        rsi_1d = talib.RSI(closings_1d, timeperiod=14)
        fastk_1d, fastd_1d = talib.STOCH(rsi_1d, rsi_1d, rsi_1d, fastk_period=14, slowk_period=3, slowd_period=4,
                                         slowd_matype=0)

        last_fastk_1d = fastk_1d.iloc[-1]
        last_fastd_1d = fastd_1d.iloc[-1]

        last_RSI_1d = rsi_1d.iloc[-1]

        # MFI 1 day
        MFI_1d = talib.MFI(high_1d, low_1d, closings_1d, volume_1d, timeperiod=12)
        last_MFI_1d = MFI_1d.iloc[-1]

        #Append last MA values in a dedicates list
        MA_50_list_1hr.append(last_MA50)
        MA_100_list_1hr.append(last_MA100)
        MA_200_list_1hr.append(last_MA200)


        # Append last RSI values for each chart in a dedicated list
        RSI_list_1hr.append(last_RSI_1hr)
        RSI_list_4hr.append(last_RSI_4hr)
        RSI_list_1d.append(last_RSI_1d)

        # Append last STOCH RSI Values for each chart in a dedicated list
        STOCH_RSI_list_1hr_fastk.append(last_fastk_1hr)
        STOCH_RSI_list_1hr_fastd.append(last_fastd_1hr)
        STOCH_RSI_list_4hr_fastk.append(last_fastk_4hr)
        STOCH_RSI_list_4hr_fastd.append(last_fastd_4hr)
        STOCH_RSI_list_1d_fastk.append(last_fastk_1d)
        STOCH_RSI_list_1d_fastd.append(last_fastd_1d)

        # Append last MFI values for each chart in a dedicated list
        MFI_list_1hr.append(last_MFI_1hr)
        MFI_list_1d.append(last_MFI_1d)

        #Append last closing values
        closing_list.append(float(close))

        # Dictionary for better visualization
        dict_1hr = dict(zip(symbols, RSI_list_1hr))
        dict_4hr = dict(zip(symbols, RSI_list_4hr))
        dict_1d = dict(zip(symbols, RSI_list_1d))

        dict_1hr_closes = dict(zip(symbols,closing_list))

        dict_1hr_STOCHRSI_k = dict(zip(symbols, STOCH_RSI_list_1hr_fastk))
        dict_1hr_STOCHRSI_d = dict(zip(symbols, STOCH_RSI_list_1hr_fastd))
        dict_4hr_STOCHRSI_k = dict(zip(symbols, STOCH_RSI_list_4hr_fastk))
        dict_4hr_STOCHRSI_d = dict(zip(symbols, STOCH_RSI_list_4hr_fastd))
        dict_1d_STOCHRSI_k = dict(zip(symbols, STOCH_RSI_list_1d_fastk))
        dict_1d_STOCHRSI_d = dict(zip(symbols, STOCH_RSI_list_1d_fastd))

        dict_1hr_MFI = dict(zip(symbols, MFI_list_1hr))
        dict_1d_MFI = dict(zip(symbols, MFI_list_1d))

        dict_1hr_50MA = dict(zip(symbols,MA_50_list_1hr))
        dict_1hr_100MA = dict(zip(symbols, MA_100_list_1hr))
        dict_1hr_200MA = dict(zip(symbols, MA_200_list_1hr))


    print('Incredible trades longs:')
    incredible_trades.incredible_trade_detector(dict_1hr, dict_1hr_MFI, dict_1hr_STOCHRSI_k, dict_1hr_STOCHRSI_d, dict_1hr_closes,
                              dict_4hr_STOCHRSI_k,dict_4hr_STOCHRSI_d,dict_1d_STOCHRSI_k,dict_1d_STOCHRSI_d,dict_4hr)

    print('-------------------------------------------------------------------')

    print('Reversal trades longs:')
    reversal_trades.reversal_trade_detector(dict_1hr, dict_1hr_MFI, dict_1hr_STOCHRSI_k, dict_1hr_STOCHRSI_d,dict_1hr_50MA,dict_1hr_100MA,dict_1hr_200MA,dict_1hr_closes,
                         dict_4hr_STOCHRSI_k,dict_4hr_STOCHRSI_d,dict_1d_STOCHRSI_k,dict_1d_STOCHRSI_d,dict_4hr,dict_1d)
    print('-------------------------------------------------------------------')

    print('Trend trades longs:')
    #trend_trades.trend_trade_detector(dict_1hr, dict_1hr_MFI, dict_1hr_STOCHRSI_k, dict_1hr_STOCHRSI_d, dict_1hr_50MA,dict_1hr_100MA, dict_1hr_200MA, dict_1hr_closes,
                         #dict_4hr_STOCHRSI_k, dict_4hr_STOCHRSI_d, dict_1d_STOCHRSI_k, dict_1d_STOCHRSI_d,dict_4hr)

    print('-------------------------------------------------------------------')

    print('Incredible trades shorts:')
    incredible_trades_shorts.incredible_trade_detector_shorts(dict_1hr, dict_1hr_MFI, dict_1hr_STOCHRSI_k, dict_1hr_STOCHRSI_d, dict_1hr_closes,
                                                              dict_4hr_STOCHRSI_k,dict_4hr_STOCHRSI_d,dict_1d_STOCHRSI_k,dict_1d_STOCHRSI_d,dict_4hr)

    print('-------------------------------------------------------------------')

    print('Trend trades shorts:')
    #trend_trades_shorts.trend_trade_detector_shorts(dict_1hr, dict_1hr_MFI, dict_1hr_STOCHRSI_k, dict_1hr_STOCHRSI_d, dict_1hr_50MA,dict_1hr_100MA, dict_1hr_200MA, dict_1hr_closes,dict_4hr_STOCHRSI_k,
                                      #dict_4hr_STOCHRSI_d, dict_1d_STOCHRSI_k, dict_1d_STOCHRSI_d,dict_4hr)

    time.sleep(run_interval_seconds)
