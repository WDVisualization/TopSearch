from abc import ABCMeta, abstractclassmethod
import os


# 对分词操作的抽象类
# 方法：数据输入(数据格式为列表，为热搜词条)，数据分词，过滤停用词，计算频率
# 参数：是否计算频率
class BaseSegmenter(metaclass=ABCMeta):
    # 热搜词条
    sentences_list = None

    # 词：计数字典
    word_count_dic = dict()

    # 停用词
    stop_words_dic = None

    # 所有热搜词计数（去除停用词）
    sum_count = 0

    # 是否计算频率
    cal_frq = False

    def __init__(self, sentences_list, **kwargs):
        self.sentences_list = sentences_list
        # print(self.sentences_list)
        for k, v in kwargs.items():
            if k == 'cal_frq':
                if v is True:
                    self.enable_cal_frq(True)
                elif v is False:
                    self.enable_cal_frq(False)
                else:
                    raise ValueError

            if k == 'extra_stop_words_dic' and v is not None:
                self.load_extra_stop_words_dic(v)

        self.laod_default_stop_words_dic()
        self.segment()
        self.remove_stop_words()
        if self.cal_frq:
            self.calculate_frequency()

    def set_hotwords_list(self, sentences_list):
        self.sentences_list = sentences_list

    def enable_cal_frq(self, v):
        self.cal_frq = v
        # if v is True:
        #     print('开启频率计算')
        # else:
        #     print('关闭频率计算')

    @abstractclassmethod
    def segment(cls):
        pass

    def load_extra_stop_words_dic(self, extra_stop_words_list):
        # print('加载额外停用词')
        if self.stop_words_dic is None:
            self.stop_words_dic = list()
        self.stop_words_dic.extend(extra_stop_words_list)
        self.stop_words_dic = list(set(self.stop_words_dic))

    def laod_default_stop_words_dic(self):
        # print('加载默认停用词')
        if self.stop_words_dic is None:
            self.stop_words_dic = list()

        path = os.path.abspath("..")
        print(path)

        temp = open(path + r'/res/stopwords/baidu_stopwords.txt',
                    'rb').read().decode('utf-8').split('\n')

        self.stop_words_dic.extend(temp)

        temp1 = open(path + r'/res/stopwords/cn_stopwords.txt',
                     'rb').read().decode('utf-8').split('\n')

        self.stop_words_dic.extend(temp1)
        self.stop_words_dic = list(set(self.stop_words_dic))

    def remove_stop_words(self):
        # print('去除停用词')
        temp = self.word_count_dic.copy()
        for k in temp:
            if k in self.stop_words_dic:
                del self.word_count_dic[k]

    def calculate_frequency(self):
        self.count()
        for k, v in self.word_count_dic.items():
            self.word_count_dic[k] = v / self.sum_count

    def count(self):
        # print('计算总数')
        self.sum_count = 0
        for k, v in self.word_count_dic.items():
            self.sum_count += v

    def get_result(self):
        return self.word_count_dic
