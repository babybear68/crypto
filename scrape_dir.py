import pickle
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
from os import listdir
from os.path import isfile, join
from goose3 import Goose

def valid(href):
    if href == None:
        return False
    if 'http' not in href:
        return False
    if 'google' in href:
        return False
    if 'youtube' in href:
        return False
    if 'blogger' in href:
        return False
    return True

PATH = 'sources_btc/'
OUTPUT_PATH = 'texts_btc'
files = [f for f in listdir(PATH) if isfile(join(PATH, f))]

for file in files:
    print(file)
    source_file = None

    if isfile(join(OUTPUT_PATH, 'text' + file[6:-3] + 'txt')):
        continue

    try:
        with open(join(PATH, file), 'rb') as f:
            source_file = pickle.load(f)
    except:
        continue

    soup = BeautifulSoup(source_file.content, features='html.parser')

    urls = []
    for link in soup.find_all('a'):
        if valid(link.get('href')):
            urls.append(link.get('href'))

    urls = set(urls)

    sources = []
    texts = []
    for url in urls:
        # sources.append(requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}))
        try:
            g = Goose({'http_timeout': 5.0, 'strict': False, 'browser_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
            article = g.extract(url=url)
            texts.append(re.sub(r'\n', ' ', article.cleaned_text))
        except:
            continue

    # texts = []
    # for source in sources:
    #     new_soup = BeautifulSoup(source.content, features='html.parser')
    #     text = []
    #     for p in new_soup.find_all('p'):
    #         text.extend(p.findAll(text=True))
    #     text_joined = ' '.join(text)
    #     text_joined = re.sub(r'\n', ' ', text_joined)
    #     texts.append(text_joined)
    try:
        with open(join(OUTPUT_PATH, 'text' + file[6:-3] + 'txt'), 'w') as f:
            f.write('\n'.join(texts))
    except:
        continue