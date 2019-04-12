import requests
import pickle
import numpy as np
import pandas as pd
import time
import os.path

NAME = 'bitcoin'
SUFFIX = 'btc'
SLEEP = 5

idx = pd.to_datetime(pd.date_range('2010-07-16', periods=3182, freq='D'))
s = pd.Series(range(len(idx)), index=idx).reset_index()['index'].dt.strftime('%m/%d/%Y').values

for _ in s[::-1]:


    file_name = '/home/babybear68/sources_' + SUFFIX + '/source_' + _[6:] + _[:2] + _[3:5] + '.pkl'

    if os.path.isfile(file_name):
        continue

    source = requests.get('https://www.google.com/search?q=' + NAME + '&tbs=cdr:1,cd_min:' + _ + ',cd_max:' + _ + '&source=lnms&tbm=nws', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})

    if source.ok:
        with open(file_name, 'wb') as f:
            pickle.dump(source, f)
    else:
        time.sleep(120)
        source = requests.get('https://www.google.com/search?q=' + NAME + '&tbs=cdr:1,cd_min:' + _ + ',cd_max:' + _ + '&source=lnms&tbm=nws', headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
        if source.ok:
            with open(file_name, 'wb') as f:
                pickle.dump(source, f)
        else:
            break

    while np.random.rand() < 0.8:
        time.sleep(SLEEP)