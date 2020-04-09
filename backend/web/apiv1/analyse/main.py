# -*- encoding= utf-8 -*-
from wordcloud import WordCloud
import os
from datasource.datasource import MongoDataSource
from segmenter.jieba_segmenter import JieBaSegmenter


def main():
    datasource = MongoDataSource()
    res = datasource.get_recent_data(1)
    path = os.path.abspath('.')
    wc = WordCloud(font_path=path + r'/res/font/FangZhengKaiTiJianTi.ttf',
                   background_color='black',
                   width=1920,
                   height=1080,
                   max_words=100)

    sentences = list()
    word_count = dict()

    for item in res:
        data = item['data']
        for d in data:
            sentences.append(d['key'])

    jb_seg = JieBaSegmenter(sentences)
    word_count = jb_seg.get_result()
    print(sorted(word_count.items(), key=lambda d: d[1]))
    wc.generate_from_frequencies(word_count)
    wc.to_file('test.png')


if __name__ == '__main__':
    main()
