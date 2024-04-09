from scraping import scrap_tags
from cloud import make_cloud

# 상의/아우터/하의/스니커즈 (월별 랭킹)
top = 'https://www.musinsa.com/ranking/best?period=month&age=ALL&mainCategory=001'
outer = 'https://www.musinsa.com/ranking/best?period=month&age=ALL&mainCategory=002'
pants = 'https://www.musinsa.com/ranking/best?period=month&age=ALL&mainCategory=003'
shoes = 'https://www.musinsa.com/ranking/best?period=month&age=ALL&mainCategory=018'

# 워드 클라우드 생성
make_cloud(scrap_tags(top))
make_cloud(scrap_tags(outer))
make_cloud(scrap_tags(pants))
make_cloud(scrap_tags(shoes))