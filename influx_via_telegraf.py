
import datetime
import time
from numpy.core.function_base import linspace
import pandas as pd

linlength = 399000 #size of block to test write
rdata=linspace(0,1,linlength)   #create some dummy analog data
now = datetime.datetime.now()   #start at now for easy grafana/chronograf viewing
now = now + datetime.timedelta(hours=4) # utc adjust im too lazy to do the datetime version
then = now + datetime.timedelta(seconds=1)  #end time 1 second later
t = pd.date_range(now, then, periods=linlength).to_pydatetime() #create time index based on now, with linspace entries
df = pd.DataFrame({'time':t, 'analog':rdata})   #make the df
df = df.set_index('time')                       #make it time indexed
print(df)
