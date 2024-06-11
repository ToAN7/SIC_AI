import numpy as np

# Bring data into list - Corpus
lists = []
with open("Test Data\SIC_AI_3\SIC_AI_3_2_data.txt", encoding="utf8") as f:
    for line in f:
        line = line.replace("\n","")
        line.strip()
        lists.append(line)
f.close()

# Tokenize
import underthesea as udts

def preprocess(lists):
    # Profesional
    #return [udts.word_tokenize(line.lower()) for line in lists]
    # Newbie
    tokenized_list = []
    for l in lists:
        tokenized_list.append(udts.word_tokenize(l.lower()))
    return tokenized_list

# Create vector of each words:

def get_vocab(tokenized_lists):
    vocabs = set()
    for line in tokenized_lists:
        vocabs.update(line)
    return vocabs

# Get vector on each lines:
from collections import Counter

def create_vector(one_line, vocabs):
    word_count = Counter(one_line)
    return np.array([word_count[w] for w in vocabs])

# Heuristic - way people find out when will one word in document become important

## Use term frequency to find similarity by measuring the angle of 2 vector
### term frequency (tf) - the important of a word that appear in one document

def cosine_similarity(x_vector, y_vector):
    dot_product = np.dot(x_vector,y_vector)
    norm_vec1 = np.linalg.norm(x_vector)
    norm_vec2 = np.linalg.norm(y_vector)
    return dot_product/(norm_vec1*norm_vec2)

### document frequency (df) - the number of documents that appear the word
### inverse document frequency (idf): idf = log(n/df) (base 10)
### penalty - the reward for AI which use if*tdf
# import os, os.path
import math

def idf_cal(tokenized_docs, vocabs):
    # docs = os.listdir("Test Data\SIC_AI_3")
    # for doc in docs:
    #     with open("Test Data\SIC_AI_3" + doc) as d: # read each file to search for the word
    #         for line in d:
    #         line = line.replace("\n","")
    #         line.strip()
    #         lists.append(line)
    #     d.close()
    n = len(lists)
    idf = {}
    for word in vocabs:
        df = sum([1 for doc in tokenized_docs if word in doc])
        idf[word] = math.log(n/df)
    return idf

def idf_vector(one_doc, idf, vocabs):
    vector = np.zeros(len(vocabs))
    for idx, word in enumerate(vocabs):
        if word in one_doc:
            vector[idx] = idf[word]
    return vector

# Act like main in C++
if __name__ == '__main__':
    tokenized_lists = preprocess(lists)
    print(tokenized_lists)
    print("========================================================")
    
    vocabs = get_vocab(tokenized_lists)
    print(len(vocabs))
    print(vocabs) 
    print("========================================================")

    vec = [create_vector(line, vocabs) for line in tokenized_lists]
    print(vec)
    print("========================================================")
    
    for i in range(len(tokenized_lists)):
        print(cosine_similarity(vec[0],vec[i]))
    print("========================================================")

    idf = idf_cal(tokenized_lists,vocabs)
    vec1 = [create_vector(line, vocabs) * idf_vector(line,idf,vocabs) for line in tokenized_lists]
    print(vec1)

    for i in range(len(tokenized_lists)):
        print(cosine_similarity(vec1[1],vec1[i]))
    print("========================================================")