str = input("여러 개의 숫자를 콤마로 구분해 입력해주세요 :")
numbers = str.split(',')
sum = 0

for i in numbers:
    sum += int(i)

print(sum)