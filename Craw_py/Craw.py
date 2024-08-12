#thanhnien
import pandas as pd
from newspaper import build
from newspaper import Article
import string
import csv
# Define the URL of the news website
cnn_paper = build('https://afamily.vn/',language='vi',memoize_articles=True)
Source =[]
Date=[]
Content=[]
num = 0
# Iterate through the articles
print("So bai viet")
for articles in cnn_paper.articles:
    article = Article(articles.url, request_timeout=100,language='vi')
    article.download()
    try:
        article.parse()
        if article.publish_date == None:
            continue
        else:
            num = num + 1
            Source.append(article.url)
            Content.append(article.meta_data["description"])
            Date.append(article.publish_date)
        print(num)
    except Exception as e:
        pass
df = pd.DataFrame({
    'Date': Date,
    'Content': Content,
    'Source': Source
})
# df.to_csv('data_thanhnien6.csv',mode='w',index=False)

# thanhnien = pd.read_csv('data_thanhnien6.csv')
df['Date'] = df['Date'].astype(str)
df['Content'] = df['Content'].astype(str)
# df = df[df['Date'].str.contains('2024-07-30')]
# df = df[df['Content'].str.len() > 20]
df.to_csv('../data_fake.csv', index=False, mode='w')

