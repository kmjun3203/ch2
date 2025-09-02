# 형변환의 종류
# 강제 형변환 : str(100) int("100")
# 자동 형변환 (묵시적 형변환)
# 컴퓨터가 계산 중에 자동으로 자료형을 바꾸는 것

print(type(4.5), type(2))
# 컴퓨터가 계산을 위해 2를 2.0으로 변환한 것
print(4.5 / 2) # float/int => 가능? ㄴㄴ float/float인거임

# 타입을 확인하는 함수들
# type
print(type(4.5))
# isinstance
print(isinstance(4.5, float))
print(isinstance(4.5,(int, float)))

