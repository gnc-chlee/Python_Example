numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        # 짝수인 경우 출력하지 않고 다음 순회로 넘어감
        continue
    
    print(num)

count = 0

while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
    