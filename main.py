# coding=utf-8
# MovieTomatoes Ver 0.1
# 내용:
#   1) 네이버 영화에서 영화 리뷰 수집
#   2) 수집 된 리뷰 MongoDB에 저장
#   3) MongoDB에서 수집 된 데이터 불러옴
#   4) 인공지능에 사용할 수 있게 전처리
#   5) 전처리 된 데이터를 활용하여 인공지능 분석 시작
#   6) 분석결과를 시각화
# 만든이: jasurbekcnu
# 일자: 2021.11.09

import requests
from bs4 import BeautifulSoup
import webcrawl.WebCrawlService as wcs


#########################
# 1.데이터 수집 및 저장 #
#########################

movie_code = '209496'  # 네이버 영화 code

# 1.제목 수집
title = wcs.get_movie_title(movie_code)
print(title)
