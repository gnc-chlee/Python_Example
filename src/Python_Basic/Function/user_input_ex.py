def process_user_input():
    """사용자로부터 입력을 받아 처리하는 함수"""
    while True:
        user_input = input("종료하려면 'exit'을 입력하세요: ")
        
        if user_input.lower() == "exit":
            print("프로그램을 종료합니다.")
            break
        else:
            print(f"사용자 입력: {user_input}")

# 함수 호출
process_user_input()
