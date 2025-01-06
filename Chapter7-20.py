import re

# 테스트할 이메일 리스트
emails = [
    "park@naver.com",
    "kim@daum.net",
    "lee@myhome.co.kr",
]

# 정규식 패턴
pattern = r".*[@].*[.](?=com$|net$).*$"

# 매치되는 이메일 찾기
matching_emails = [email for email in emails if re.match(pattern, email)]

print("매치되는 이메일:", matching_emails)