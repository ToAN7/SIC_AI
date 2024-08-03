import pandas as pd
import numpy as np
import re
import string
import csv

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]','',text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+','',text)
    text = re.sub('<.*?>+',b'',text)
    text = re.sub('[%s]' % re.escape(string.punctuation),'',text)
    text = re.sub('\w*\d\w*','',text)
    text = re.sub(' +', ' ',text)
    text = np.array(['Date', 'Content', 'Source'],np.string_)
    return text

def clean(filename, outputname):
    raw_data = pd.read_csv(filename, delimiter="|").astype(str)
    raw_data['Content'] = raw_data["Content"].apply(wordopt)

    for x in range(len(raw_data)):
        if raw_data['Content'][x] != 'nan' and raw_data['Date'][x] != '{}':
            row = [raw_data["Date"][x],raw_data["Content"][x],raw_data["Source"][x]]
            text = np.append(text, row, axis = 0)

    text = np.reshape(text, (text.size//3,3))
    with open(outputname, 't+w') as csvFile:
        csvWriter = csv.writer(csvFile, lineterminator = '\n', delimiter='|', quoting= csv.QUOTE_ALL)
        csvWriter = csvWriter.writerows(text)
    
    return "Success"