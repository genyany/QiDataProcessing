import time

import pandas as pd

from QiDataProcessing.Core.EnumMarket import EnumMarket
from QiDataProcessing.Core.TradingDayHelper import TradingDayHelper
from QiDataProcessing.Instrument.InstrumentManager import InstrumentManager
from QiDataProcessing.QiDataController import QiDataController
import datetime
from QiDataProcessing.Core.EnumBarType import EnumBarType
from QiDataProcessing.QiDataDirectory import QiDataDirectory
from QiDataProcessing.TradingFrame.YfTimeHelper import YfTimeHelper

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

trading_day = datetime.datetime(2019, 10, 13)
tick_path = "\\\\192.168.1.200\\MqData\\futuretick\\Future"
min_path = "\\\\192.168.1.200\\MqData\\futuremin"
day_path = "\\\\192.168.1.200\\MqData\\futureday"

qi_data_directory = QiDataDirectory()
qi_data_directory.trading_day = trading_day
qi_data_directory.future_tick = tick_path
qi_data_directory.future_tick_cache = tick_path
qi_data_directory.future_min = min_path
qi_data_directory.future_day = day_path

qi_data_controller = QiDataController(qi_data_directory)

interval = 5
bar_type = EnumBarType.day
instrument_id_a = "IF9999"
instrument_id_b = "rb9999"
begin_time = datetime.datetime(2019, 7, 10)
end_time = datetime.datetime(trading_day.year, trading_day.month, trading_day.day)
#
# bar_series = qi_data_controller.get_bar_series_by_time(EnumMarket.期货, instrument_id_a, interval, bar_type, begin_time, end_time)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id_a+"]"+str(index)+":"+bar.to_string())
#     index += 1
#
# length = 20
# bar_series = qi_data_controller.get_bar_series_by_length(EnumMarket.期货, instrument_id_b, interval, bar_type, length, end_time)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id_b+"]"+str(index)+":"+bar.to_string())
#     index += 1


# begin_trading_date = datetime.datetime(2017, 7, 5)
# end_trading_date = datetime.datetime(2017, 7, 5)
# instrument_id = "rb9999"
# interval = 1
# bar_type = EnumBarType.hour
# bar_series = qi_data_controller.load_bar_series_by_date(EnumMarket.期货, instrument_id, interval, bar_type, begin_trading_date, end_trading_date)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id+"]"+str(index)+":"+bar.to_string()+','+str(bar.pre_close))
#     index += 1

# begin_trading_date = datetime.datetime(2018, 12, 28, 21, 1, 0)
# end_trading_date = datetime.datetime(2019, 1, 2, 21, 1, 0)
# instrument_id = "rb9999"
# interval = 1
# bar_type = EnumBarType.minute
# bar_series = qi_data_controller.load_bar_series_by_date_time(EnumMarket.期货, instrument_id, interval, bar_type, begin_trading_date, end_trading_date)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id+"]"+str(index)+":"+bar.to_string()+','+str(bar.pre_close))
#     index += 1


# end_trading_date = datetime.datetime(2019, 10, 9)
# instrument_id = "rb9999"
# bar_series = qi_data_controller.load_tick_series(EnumMarket.期货, instrument_id, end_trading_date)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id+"]"+str(index)+":"+bar.to_string())
#     index += 1

qi_data_controller.trading_day = datetime.datetime(2016, 1, 4, 0, 0, 0)
end_time = datetime.datetime(2016, 1, 4, 8, 59, 0)
instrument_id = "ni9999"
bar_series = qi_data_controller.get_bar_series_by_length(EnumMarket.期货, instrument_id, 1, EnumBarType.day, 200, end_time)
index = 1
for bar in bar_series:
    print("["+instrument_id+"]"+str(index)+":"+bar.to_string())
    index += 1

# length = 20
# end_trading_date = datetime.datetime(2019, 1, 2)
# instrument_id = "rb9999"
# interval = 1
# bar_type = EnumBarType.hour
# bar_series = qi_data_controller.load_bar_series_by_length(EnumMarket.期货, instrument_id, interval, bar_type, length, end_trading_date)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id+"]"+str(index)+":"+bar.to_string())
#     index += 1


# length = 4
# end_trading_date = datetime.datetime(2019, 1, 2, 9, 0, 0)
# instrument_id = "rb9999"
# interval = 1
# bar_type = EnumBarType.hour
# bar_series = qi_data_controller.load_bar_series_by_length_limit_end_time(EnumMarket.期货, instrument_id, interval, bar_type, length, end_trading_date)
# index = 1
# for bar in bar_series:
#     print("["+instrument_id+"]"+str(index)+":"+bar.to_string())
#     index += 1

# begin_trading_date = datetime.datetime(2019, 1, 2)
# end_trading_date = datetime.datetime(2019, 11, 12)
# begin_trading_date = TradingDayHelper.get_first_trading_day(begin_trading_date)
# end_trading_date = TradingDayHelper.get_last_trading_day(end_trading_date)
# instrument_id = 'IF9999'
# t0 = time.time()
# while begin_trading_date <= end_trading_date:
#     pre_close = qi_data_controller.load_pre_close_by_tick(EnumMarket.期货, instrument_id, begin_trading_date)
#     print('{0}:{1}'.format(begin_trading_date.strftime('%Y%m%d'), pre_close))
#     begin_trading_date = TradingDayHelper.get_next_trading_day(begin_trading_date)
#
# print('耗时:{0}'.format(time.time()-t0))


date_time = datetime.datetime(2019, 9, 30, 14, 0, 1)
trading_date = YfTimeHelper.get_trading_day(date_time)
print('{0}'.format(trading_date.strftime('%Y%m%d')))

# lst_a = []
# for bar in bar_series:
#     lst_a.append([bar.trading_date, bar.begin_time, bar.end_time, bar.open, bar.high, bar.low, bar.close, bar.pre_close, bar.volume])
# dfA = pd.DataFrame(lst_a, columns=['trading_date', 'begin_time', 'end_time', 'open', 'high', 'low', 'close', 'pre_close', 'volume'])
#
# print(dfA)
#
# tickSeriesA = qi_data_controller.get_tick_series(instrument_id_a, begin_date, end_date)
# lst_a = []
# for tick in tickSeriesA:
#     lst_a.append([tick.date_time, tick.local_time, tick.last_price, tick.ask_price1, tick.bid_price1, tick.ask_volume1, tick.bid_volume1])
# dfA = pd.DataFrame(lst_a, columns=['date_time', 'local_time', 'last_price', 'ask_price1', 'bid_price1', 'ask_volume1', 'bid_volume1'])
#
# print(dfA)
