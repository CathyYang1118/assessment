# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:33:39 2019

@author: Think
"""

# -*- conding:utf-8 -*-

import numpy as np
import pandas as pd
import jieba.posseg as pseg
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open('19.txt', 'r')
content = text.read()
text.close()

stat = []
stop_words = set(['我们', '以', '把', '了', '到', '上', '有','中国','国家','全面','党',
                  '问题','世界','时代','领导','战略','力量','特色','关系','全党'])

segs = pseg.cut(content)

for seg in segs:
    if str(seg.flag)[0] == 'n':
        if str(seg.word) not in stop_words:
            stat.append({'from':'19','word': seg.word})
            #print(seg.flag)
    
print(stat)

stat_df = pd.DataFrame(stat)
pt_stat = stat_df.pivot_table(index='word', columns='from', fill_value=0, aggfunc=np.size)
print(pt_stat.sort_index(by='19'))

cloud = WordCloud(font_path='C:\\simhei.ttf', background_color='white')
words = pt_stat['19'].to_dict()
cloud.fit_words(words)
plt.imshow(cloud)
plt.axis('off')
plt.show()