import requests
from bs4 import BeautifulSoup
import re
import json

def scrap_tags(url):
    session = requests.Session()

    # 403 방지용 헤더
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.musinsa.com/'
    }

    # HTTP GET
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    tag_scores = {}

    products = soup.find_all('li', class_='li_box')

    for index, product in enumerate(products):  
        rank = index + 1
        score = 10 - (rank - 1) // 10

        # 상세 페이지 링크 추출
        product_link = product.find('a', class_='img-block')['href']

        # 상세 페이지 HTTP GET
        product_response = requests.get(product_link, headers=headers)
        product_soup = BeautifulSoup(product_response.text, 'html.parser')

        # 태그 추출
        script_text = product_soup.find('script', text=re.compile('goodsTags'))
        
        json_data = re.search(r'"goodsTags":\s*(\[[^\]]*\])', script_text.text)
        if json_data:
            tags = json.loads(json_data.group(1))
            for tag in tags:
                if tag in tag_scores:
                    tag_scores[tag] += score
                else:
                    tag_scores[tag] = score

    session.close()

    return tag_scores