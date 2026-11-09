rotations = [1200, 1500, 800, 2000, 1100, 1300, 950, 1750, 1400, 1600]
print("1. 원래 회전수 데이터:", rotations)

# 단계 ②: 가장 작은 값과 가장 큰 값 구하기
min_val = min(rotations)
max_val = max(rotations)
print(f"2. 최솟값(min): {min_val}, 최댓값(max): {max_val}")

# 단계 ③ & ④: 모든 값에서 가장 작은 값을 빼고, 최댓값과 최솟값의 차이로 나누기 (정규화)
range_val = max_val - min_val
normalized_list = [(x - min_val) / range_val for x in rotations]

# 단계 ⑤: 소수점 둘째 자리까지 다듬기 및 0과 1 포함 여부 확인
rounded_normalized = [round(val, 2) for val in normalized_list]
print("3. 소수점 둘째 자리까지 정규화된 결과:", rounded_normalized)

# 결과에 0과 1이 각각 잘 포함되었는지 확인
has_zero = 0.0 in rounded_normalized
has_one = 1.0 in rounded_normalized

print(f"4. 확인 결과 -> 가장 작은 값(0) 포함 여부: {has_zero}, 가장 큰 값(1) 포함 여부: {has_one}")

rpm_list = [2200, 1800, 2500, 1900, 2100, 1500, 2300, 1700, 2400, 1950]
current_list = [20, 28, 15, 30, 22, 26, 18, 29, 21, 24]
total_count = len(rpm_list)

print("1. 회전수 데이터:", rpm_list)
print("   전류 데이터:", current_list)

low_rpm_mask = [rpm < 2000 for rpm in rpm_list]

high_current_mask = [cur > 25 for cur in current_list]

combined_mask = [(r < 2000) or (c > 25) for r, c in zip(rpm_list, current_list)]

low_rpm_count = sum(low_rpm_mask)
low_rpm_percent = (low_rpm_count / total_count) * 100

high_current_count = sum(high_current_mask)
high_current_percent = (high_current_count / total_count) * 100

combined_count = sum(combined_mask)
combined_percent = (combined_count / total_count) * 100

print(" 최종 결과 (횟수 및 비율):")
print(f"• 회전수 2000 미만 시점: {low_rpm_count}개 ({low_rpm_percent}%)")
print(f"• 전류 25 초과 시점: {high_current_count}개 ({high_current_percent}%)")
print(f"• 회전수 2000 미만이거나 전류 25 초과 시점: {combined_count}개 ({combined_percent}%)")

torque_list = [8.5, 12.0, 6.2, 14.5, 7.1, 5.0, 9.3, 4.2, 6.8, 3.5]
total_count = len(torque_list)

print("원래 토크 데이터:", torque_list)

torque_mask = [t > 10 for t in torque_list]

print("참거짓 묶음 만들기 (토크 > 10):")
print(torque_mask)

true_count = sum(torque_mask)
ratio = true_count / total_count
print(f"• 조건에 걸린 시점 개수: {true_count}개")
print(f"• 전체 대비 비율: {ratio} (또는 {ratio * 100}%)")

import numpy as np

table_data = [
    [2200, 10.5],
    [1800, 12.0],
    [2500, 8.2],
    [1900, 14.5],
    [2100, 9.1],
    [1500, 13.0],
    [2300, 9.8],
    [1700, 13.5],
    [2400, 8.9],
    [1950, 11.2]
]

arr = np.array(table_data)

means = np.mean(arr, axis=0)
stds = np.std(arr, axis=0, ddof=1)

print(f"• 회전수(RPM) -> 평균: {means[0]:.1f}, 표준편차: {stds[0]:.1f}")
print(f"• 토크(Torque) -> 평균: {means[1]:.1f}, 표준편차: {stds[1]:.1f}")