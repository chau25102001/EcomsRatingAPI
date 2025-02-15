from server.config.db import insert_many_products
from server.crawler.Shopee import Shopee
from server.crawler.Tiki import Tiki


def crawl_by_keyword(keyword: str):
    shopee = Shopee('https://shopee.vn')
    tiki = Tiki('https://tiki.vn/')
    r1 = shopee.find_reviews_by_keyword(keyword)
    insert_many_products(r1)
    r2 = tiki.find_reviews_by_keyword(keyword)
    insert_many_products(r2)


def crawl_by_url(url: str):
    if 'shopee' in url:
        shopee = Shopee('https://shopee.vn')
        results = shopee.find_reviews_by_url(url)
        print(results)
        # for res in results:
        insert_many_products(results)
    elif 'tiki' in url:
        tiki = Tiki('https://tiki.vn/')
        results = tiki.find_reviews_by_url(url)
        print(results)
        insert_many_products(results)
    else:
        print("Nothing happen!!!")


def crawl_by(data: str, by: str):
    if by == 'keyword':
        crawl_by_keyword(data)
    elif by == 'url':
        crawl_by_url(data)
