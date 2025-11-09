# 1) 데이터 요약 및 집계 (aggregation)
## 평균 (sum/len)
## 증앙값 (sorted 후 중간 인덱스)
## 최빈값 (collections.Counter)
## 조건부 평균 (filter of if)

# 2) 조건별 그룹 통계 (grouping)
## 딕셔너리 (defaultdict(list) or dict.setdefault()) 활용
## 그룹별 평균, 개수, 합 계산


# 3) 정렬 + 순위 (sorting & reranking)
## 점수 상위 N명, 최하위, 특정 조건 만족자 등 찾기
## sorted(key=lambda x:...)
## 슬라이싱 [:n]
## 람다 정렬로 조건 정리

# 4) 데이터 필터링 + 통계 (filter + aggregation)
## 특정 조건 만족하는 데이터만 남기고 통계 계산
## filter() + sum(), len()
## 조건에 맞는 비율 계산

# 5) 간단한 통계 계산 (covariance, correlation 등)
## numpy 없이 수학적 통계식 직접 구현
## 공분산 (covariance), 상관계수 (correlation coefficient)
## 독립 여부
## class 짜기

# 6) 데이터 정제 (data cleaning /outlier)
# 평균 ± 표준편차 기반 필터링
# None/NaN 값 제외
# 중앙값으로 대체


## N명의 학생이 있고, 각 학생은 여러 과목 점수를 가진다.
## 학생별 평균을 구하고, 평균이 전체 평균 이상인 학생의 이름을 알파벳순으로 정렬해서 반환하라.