import pandas as pd
import numpy as np
import re
import string
import csv

def clean(filename, outputname):
    raw_data = pd.read_csv(filename, delimiter="|").astype(str)

    raw_data['Content'] = raw_data['Content'].lower()
    raw_data['Content'] = re.sub('\[.*?\]','',raw_data['Content'])
    raw_data['Content'] = re.sub("\\W"," ",raw_data['Content'])
    raw_data['Content'] = re.sub('https?://\S+|www\.\S+','',raw_data['Content'])
    raw_data['Content'] = re.sub('<.*?>+',b'',raw_data['Content'])
    raw_data['Content'] = re.sub('[%s]' % re.escape(string.punctuation),'',raw_data['Content'])
    raw_data['Content'] = re.sub('\w*\d\w*','',raw_data['Content'])
    raw_data['Content'] = re.sub(' +', ' ',raw_data['Content'])
    raw_data['Content'] = np.array(['Date', 'Content', 'Source'],np.string_)

    for x in range(len(raw_data)):
        if raw_data['Content'][x] != 'nan' and raw_data['Date'][x] != '{}':
            row = [raw_data["Date"][x],raw_data["Content"][x],raw_data["Source"][x]]
            text = np.append(text, row, axis = 0)

    text = np.reshape(text, (text.size//3,3))
    with open(outputname, 't+w') as csvFile:
        csvWriter = csv.writer(csvFile, lineterminator = '\n', delimiter='|', quoting= csv.QUOTE_ALL)
        csvWriter = csvWriter.writerows(text)
    
    return "Success"