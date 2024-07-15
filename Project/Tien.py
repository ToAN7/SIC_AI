from newspaper import build
from newspaper import Article
import csv
# Define the URL of the news website
cnn_paper = build('https://thanhnien.vn/', memoize_articles=False)
num = 0
# Iterate through the articles
for articles in cnn_paper.articles:
    num = num + 1
    article = Article(articles.url, request_timeout=100, memoize_articles=False)
    article.download()
    try:
        article.parse()
        print(article.meta_data["description"])
        print(num)
    except Exception as e:
        pass



