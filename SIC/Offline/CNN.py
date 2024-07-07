import newspaper

vnex_paper =  newspaper.build('https://vnexpress.net', language = 'vi', memoize_articles = False, follow_meta_refresh = True, keep_article_html=True)

for atc in vnex_paper.article_urls():
    print(atc)