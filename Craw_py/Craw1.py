#tuoitre
import pandas as pd
from newspaper import build
from newspaper import Article
import csv
import requests
from bs4 import BeautifulSoup
# Define the URL of the news website
cnn_paper = build('https://tuoitre.vn/',language='vi',memoize_articles=True)
Source =[]
Date=[]
Content=[]
num = 0
# Iterate through the articles
print("So bai viet")
for articles in cnn_paper.articles:
    article = Article(articles.url, request_timeout=100,language='vi')
    # respone =requests.get(articles.url)
    # soup = BeautifulSoup(respone.content, 'html.parser')
    # meta_tag = soup.find('meta', attrs={'property':'og:description'})
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
df['Date'] = df['Date'].astype(str)
df['Content'] = df['Content'].astype(str)
# df = df[df['Date'].str.contains('2024-07-30')]
df = df[df['Content'].str.len() > 10]
s1 = "Chia sẻ về xu hướng nghề nghiệp mới trong những năm gần đây, giúp các bạn trẻ có cái nhìn toàn cảnh để định hướng bản thân trong tương lai"
s2 = "Chọn lý do vi phạm : Xúc phạm, gây hại người khác Lạc đề Vi phạm pháp luật Vi phạm đạo đức, thuần phong mỹ tục Tố cáo sai sự thật Vi phạm bản quyền Để lộ thông tin cá nhân Spam, rác Lý do khácÝ kiến :"
df=df[~df["Content"].str.contains(s1, na=False)]
df=df[~df["Content"].str.contains(s2, na=False)]
df.to_csv('data_tuoitre11.csv', index=False, mode='w')
