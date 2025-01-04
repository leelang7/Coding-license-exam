# 파일 읽기
with open('abc.txt', 'r') as file:
    lines = file.readlines()

# 내용 역순 정렬
reversed_lines = lines[::-1]

# 파일에 쓰기
with open('result_abc.txt', 'w') as file:
    file.writelines(reversed_lines)