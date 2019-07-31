from MetaTrader5 import *
from datetime import datetime
import pandas as pd
# Initializing MT5 connection
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# Copying data to pandas data frame
stockdata = pd.DataFrame()
rates = MT5CopyRatesFromPos("DOLQ19", MT5_TIMEFRAME_M1, 0, 5000)
# Deinitializing MT5 connection
MT5Shutdown()

stockdata['Open'] = [y.open for y in rates]
stockdata['Close'] = [y.close for y in rates]
stockdata['High'] = [y.high for y in rates]
stockdata['Low'] = [y.low for y in rates]
stockdata['Date'] = [y.time for y in rates]

print(stockdata)
