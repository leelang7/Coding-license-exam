import re

pattern = r'a[.]{3,}b'

strings = ["acccb", "a....b", "aaab", "a.cccb"]

matching_strings = [s for s in strings if re.match(pattern, s)]

print("매치되는 문자열:", matching_strings)