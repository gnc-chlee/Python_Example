import math

def quadratic_formula(a, b, c):
    # 판별식 계산
    discriminant = b**2 - 4*a*c

    # 판별식이 음수인 경우 예외 처리
    if discriminant < 0:
        print("이차방정식의 해는 실수가 아닌 복소수입니다.")
        return None

    # 근의 공식 적용
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return root1, root2

# 예제: x^2 - 5x + 6 = 0
a = 1
b = 3
c = 6

roots = quadratic_formula(a, b, c)
if roots is not None:
    print(f"해: {roots}")
