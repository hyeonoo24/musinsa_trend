import matplotlib.pyplot as plt
from wordcloud import WordCloud

def make_cloud(tags):
    font_path = 'c:/Windows/Fonts/NanumGothic.ttf'  #한글 표시를 위한 글꼴 지정

    wordcloud = WordCloud(font_path=font_path, width = 800, height = 400, background_color ='white').generate_from_frequencies(tags)

    # 워드 클라우드 표시
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()