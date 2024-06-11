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

## Pandas index

### document frequency (df) - the number of documents that appear the word
### inverse document frequency (idf): idf = log(n/df) (base 10)
### penalty - the stick for AI which use if*tdf

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
