number = input("입력 :")
nums = list(map(int, number)) # 숫자문자열 -> 숫자 리스트
result = []

for i, num in enumerate(nums):
    result.append(str(num)) 
    if i < len(nums) -1: # 현재 요소가 다음 요소를 가질 떄
        if(num %2 ==1) & (nums[i+1] %2==1): # 현재 요소와 다음 요소가 홀수이면
            result.append('-')
        elif (num%2==0) & (nums[i+1] %2==0): # 현재 요소와 다음 요소가 짝수이면
            result.append('*')

print("".join(result))
