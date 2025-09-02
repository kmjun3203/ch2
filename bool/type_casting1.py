# 형번환
# 자료형을 다른 자료형으로 바꾸는 것

print(3.23, type(3.23))

# float -> int
print(int(3.23))

# 문자열 "323"
print("323", type("323"))
# str -> int   
print(int("323"))

# int -> float
print(float(323))

# str -> float
print(float("3.23"))

# int -> bool
print(bool(0)) #False
print(bool(1)) #True
print(bool(2)) #True

# int -> str
print(str(123))
# float -> str
print(str(3.14))

# 형변환이 필요한 이유?
# int float bool str 
# 서로 다른 데이터 타입 간의 호환성과 오류 방지, 정확한 연산 처리 때문