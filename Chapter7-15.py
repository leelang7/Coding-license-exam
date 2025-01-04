def check_unique_digits(number_string):
    # 0부터 9까지의 숫자를 모두 포함하는 문자열
    required_digits = set("0123456789")
    
    # 입력 문자열을 집합으로 변환하여 중복 제거
    input_digits = set(number_string)
    
    # 입력 문자열의 집합이 모든 필요한 숫자를 포함하는지 확인
    return input_digits == required_digits

inputs = ["0123456789", "01234", "01234567890", "6789012345", "012322456789"]

outputs = [check_unique_digits(number) for number in inputs]
print(outputs)  # 결과: [True, False, False, True, False]