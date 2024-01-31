numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)
    
    if num == 5:
        print("5를 찾았습니다!")
        break




while True:
    user_input = input("Type 'exit' to break the loop: ")
    
    if user_input.lower() == "exit":
        break
    else:
        print("Looping...")
