# 제조 데이터 분석 학습 기록

Python 기초부터 NumPy, Pandas까지 설비 데이터를 다루며 배운 내용을 날짜순으로 정리한 저장소입니다.
파일명은 `YYMMDD_주제.py` 형식이며, 각 파일에 학습 내용과 직접 푼 실습이 들어 있습니다.

**학습 기간:** 2026.10.20 ~ 2026.11.13

## 학습 흐름

```
Python 기초 → 자료구조·함수 → 파일·예외 처리 → NumPy → Pandas
```

---

## 1. Python 기초 (10/20 ~ 10/26)

| 날짜 | 파일 | 학습 내용 |
|---|---|---|
| 10/20 | [261020_print_basics.py](261020_print_basics.py) | print 함수, 숫자·문자 출력, 쉼표 출력, 간단한 연산 |
| 10/20 | [261020_variables_basics.py](261020_variables_basics.py) | 변수 선언, 재할당, 다중 할당 |
| 10/21 | [261021_datatypes_operators_input.py](261021_datatypes_operators_input.py) | 자료형(int/float/str/bool), 산술·비교 연산자, input |
| 10/21 | [261021_escape_string_concat.py](261021_escape_string_concat.py) | 이스케이프 문자, 여러 줄 문자열, 문자열 연결 |
| 10/22 | [261022_string_indexing_methods.py](261022_string_indexing_methods.py) | 문자열 인덱싱·슬라이싱, strip/split/replace 등 메서드 |
| 10/23 | [261023_join_fstring_list_methods.py](261023_join_fstring_list_methods.py) | join, f-string 서식, 리스트 추가·삭제·정렬 |
| 10/26 | [261026_if_for_while.py](261026_if_for_while.py) | if/elif/else, for, 구구단, while |

## 2. 자료구조와 함수 (10/27 ~ 10/30)

| 날짜 | 파일 | 학습 내용 |
|---|---|---|
| 10/27 | [261027_for_loop_tuple.py](261027_for_loop_tuple.py) | 리스트 순회, 조건 필터링, 튜플 언패킹 |
| 10/28 | [261028_set_dictionary.py](261028_set_dictionary.py) | 집합 연산, 딕셔너리, 중첩 딕셔너리 |
| 10/29 | [261029_functions.py](261029_functions.py) | 함수 정의, 매개변수, return, 기본값 |
| 10/30 | [261030_modules_os_file_csv_io.py](261030_modules_os_file_csv_io.py) | 모듈·import, os 경로, 파일 읽기/쓰기, csv 모듈 |

## 3. 예외 처리 (11/02 ~ 11/03)

| 날짜 | 파일 | 학습 내용 |
|---|---|---|
| 11/02 | [261102_exception_handling.py](261102_exception_handling.py) | try/except, 예외 종류, 지저분한 데이터 정제 |
| 11/03 | [261103_raise_check_value.py](261103_raise_check_value.py) | raise로 값 범위 검증 |

## 4. NumPy (11/04 ~ 11/09)

| 날짜 | 파일 | 학습 내용 |
|---|---|---|
| 11/04 | [261104_numpy_array_basics.py](261104_numpy_array_basics.py) | 배열 생성, shape/dtype, reshape, 인덱싱·슬라이싱 |
| 11/05 | [261105_numpy_stats_masking_csv.py](261105_numpy_stats_masking_csv.py) | 정규화, 불리언 마스크, 통계, CSV 불러오기, argsort/clip/where |
| 11/06 | [261106_numpy_outlier_missing_corr.py](261106_numpy_outlier_missing_corr.py) | 결측(nan) 처리, IQR·z-score 이상치, 상관계수 |
| 11/09 | [261109_numpy_zscore_cumsum_score.py](261109_numpy_zscore_cumsum_score.py) | 3시그마, axis별 통계, cumsum 변화 시점, z-score 합산 |

## 5. Pandas (11/09 ~ 11/13)

| 날짜 | 파일 | 학습 내용 |
|---|---|---|
| 11/09 | [261109_pandas_read_csv_basics.py](261109_pandas_read_csv_basics.py) | DataFrame/Series, read_csv, usecols, nrows, sep |
| 11/10 | [261110_pandas_head_info_describe.py](261110_pandas_head_info_describe.py) | head/tail, info, describe, 결측 확인 |
| 11/10 | [261110_pandas_loc_iloc_sort.py](261110_pandas_loc_iloc_sort.py) | 열 선택, loc vs iloc, sort_values, 인덱스 |
| 11/11 | [261111_pandas_filter_sort_merge.py](261111_pandas_filter_sort_merge.py) | 조건 필터, str 메서드, 새 열 추가, merge(inner/left/outer) |
| 11/12 | [261112_pandas_value_counts_cut_groupby.py](261112_pandas_value_counts_cut_groupby.py) | value_counts, cut 구간화, groupby, crosstab |
| 11/12 | [261112_pandas_concat_merge.py](261112_pandas_concat_merge.py) | concat, merge, dropna |
| 11/13 | [261113_pandas_agg_transform_corr.py](261113_pandas_agg_transform_corr.py) | groupby agg, transform, pivot_table, 상관계수 행렬 |

---

## 배운 핵심 기술

- **Python:** 변수·자료형, 문자열, 리스트/튜플/집합/딕셔너리, 조건문·반복문, 함수, 파일 입출력, 예외 처리
- **NumPy:** 배열 연산, 마스킹, 정렬, 결측 처리, 이상치 탐지(IQR, z-score), 상관분석
- **Pandas:** CSV 로드, 필터링, 정렬, 병합, 그룹 집계, 구간화, 교차표

## 사용 데이터

설비 센서 데이터(유압 냉각기, 다이캐스팅, 압축기, 공구 등)를 `data/` 폴더의 CSV로 실습했습니다.
데이터 파일은 저장소에 포함하지 않았습니다.
