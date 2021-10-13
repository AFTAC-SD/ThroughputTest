# -*- coding: utf-8 -*-
"""Tutorial how to use the class helper `SeriesHelper`."""

from influxdb import InfluxDBClient
from influxdb import SeriesHelper
from influxdb import DataFrameClient
import random
import time
from numpy.core.function_base import linspace
import numpy as np
from twisted.internet import task
from twisted.internet import reactor
import pandas as pd
import datetime

linlength = 399000 #size of block to test write


def df_toInflux(data,data_type,host,port,username,password,database,measurement):
    try:
        client = DataFrameClient(
						host=host,
						port=port,
						username=username,
						password=password)

		# client.create_database(database)
        t=time.time()
        r = client.write_points(
						data,
						measurement=measurement,
						database=database,
						time_precision="n",
						protocol='line')
        # print(f'r response {r}')
        print(f'write time is: {time.time()-t} seconds')
        if r == True:
            print("[!] INFO: IQ data was successfully transferred to OSNDS.")
        else:
            print("\n[!] ERROR: The IQ data failed to be transferred to OSNDS.\n")

    except TypeError as e:
        print("\n[!] ERROR:",e,"\n")

df_toInflux(data= df,
			data_type="iq",
			host='localhost',
			port=8086,
			username='',
			password='',
			database='telegraf',
			measurement='speedtest')




rdata=linspace(0,1,linlength)   #create some dummy analog data
now = datetime.datetime.now()   #start at now for easy grafana/chronograf viewing
now = now + datetime.timedelta(hours=4) # utc adjust im too lazy to do the datetime version
then = now + datetime.timedelta(seconds=1)  #end time 1 second later
t = pd.date_range(now, then, periods=linlength).to_pydatetime() #create time index based on now, with linspace entries
df = pd.DataFrame({'time':t, 'analog':rdata})   #make the df
df = df.set_index('time')                       #make it time indexed
print(df)























# def reportInfluxdb():
# while True:
    # t = time.time()
    # if vars.packet_id < vars.sps:
    #     vars.packet_id+=1 
    # else:
    #     vars.packet_id = 0
    # MySeriesHelper(server_name='us.east-1', analog=random.randrange(10), id = vars.packet_id)
    # elapsed = time.time() - t
    # print(elapsed)
    # time.sleep(vars.sample_rate)

# task.LoopingCall(reportInfluxdb).start(vars.sample_rate)    #sets the sample rate (200 sps = 1/200 = 0.005 seconds)
# reactor.run()   #runs the function called in the argument of the LoopingCall



# To manually submit data points which are not yet written, call commit:
# MySeriesHelper.commit()

# To inspect the JSON which will be written, call _json_body_():
# MySeriesHelper._json_body_()