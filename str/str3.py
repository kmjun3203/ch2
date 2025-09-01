print("hello")

# 문자열 자르기
# index란? 문자의 위치
# 무조건 0부터 시작이며 연속적
print("hello"[0])
print("hello"[1])
print("hello"[2])
print("hello"[3])
print("hello"[4])

# 문자 슬라이스
# [index] => 문자 하나만 추출
# [idex시작:index끝] => 범위로 추출
# 슬라이스에서 끝번호는 포함X
print("hello"[0:2])
print("hello"[2:5])
# 2번부터 마지막까지
print("hello"[2:])
# 처음부터 두번째까지
print("hello"[:2])
# 전체
print("hello"[:])

print(len("aaa"))
print(len("hello, world"))
