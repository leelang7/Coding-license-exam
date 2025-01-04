fib_list = [0, 1]

def fibo(n):
    i = 0
    while fib_list[i] + fib_list[i+1] <= int(n):
        fib_list.append(fib_list[i] + fib_list[i+1])
        i += 1

num = input("정수를 입력하세요 :")
fibo(num)
print(fib_list)