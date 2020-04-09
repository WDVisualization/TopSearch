from django.shortcuts import render
from django.http import HttpResponse
from .analyse.segmenter.jieba_segmenter import JieBaSegmenter
from .models import Hotwords
import json
# Create your views here.


def index(request):
    hotwords = list()
    for hotword in Hotwords.objects:
        for word in hotword.data:
            # print(word.key)
            hotwords.append(word.key)
    result = JieBaSegmenter(hotwords).get_result()
    print(result)
    return HttpResponse(json.dumps(result))
