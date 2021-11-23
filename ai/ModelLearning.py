import json
import os
import nltk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from pprint import pprint
from konlpy.tag import Okt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics


#############
# File Open #
#############

# ~.txt 파일에서 데이터를 불러오는 method
def read_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]  # 제목열 제외
    return data

# nsmc 데이터를 불러와서 python 변수에 담기
train_data = read_data('./dataset/ratings_train.txt')  # 트레이닝 데이터 Open
test_data = read_data('./dataset/ratings_test.txt')    # 테스트 데이터 Open

print(len(train_data))
print(train_data[0])

print(len(test_data))
print(test_data[0])



