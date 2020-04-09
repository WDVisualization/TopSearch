# import hanlp
# from .base_segmenter import BaseSegmenter


# class HanlpSegmenter(BaseSegmenter):
#     def __init__(self, hotwords_list, cal_frq=True, extra_stop_words_dic=None):
#         super().__init__(hotwords_list,
#                          cal_frq=cal_frq,
#                          extra_stop_words_dic=extra_stop_words_dic)

#     def segment(self):
#         tokenizer = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')
#         for s in self.sentences_list:
#             words = tokenizer(s)
#             for word in words:
#                 if word in self.word_count_dic:
#                     self.word_count_dic[word] += 1
#                 else:
#                     self.word_count_dic[word] = 1
