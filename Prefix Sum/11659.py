"""
https://www.acmicpc.net/problem/11659 (구간 합 구하기 4)

Prefix Sum
"""

import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(M):
    left, right = map(int, sys.stdin.readline().split())
    print(prefix_sum[right] - prefix_sum[left - 1])
