from zipfile import ZipFile
import os
import time
import datetime

fn = '../../data/fortnite-rawdata.zip'
extract_dir = '../../gen/data-preparation/temp'

os.makedirs(extract_dir, exist_ok=True)

# Create a ZipFile Object and load sample.zip in it
with ZipFile(fn, 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(extract_dir)


f = open('../../gen/data-preparation/temp/unzipping.log','w')
ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
f.write('done at ' + sttime + '\n')
f.close()