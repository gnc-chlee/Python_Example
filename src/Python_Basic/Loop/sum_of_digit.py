# 자릿수 합 구하기
num = 12345
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(digit_sum)  # 출력: 15