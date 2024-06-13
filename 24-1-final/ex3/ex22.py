def string_concat(s1, s2):
    return s1 + s2
def string_indexing(s, index):
    if 0 <= index < len(s):
        return s[index]
    else:
        return "Index out of range"

def string_slicing(s, start, end):
    return s[start : end]

def string_to_upper(s):
    return s.upper()

def string_to_lower(s):
    return s.lower()

def string_length(s):
    return len(s)

def string_replace(s, old, new):
    return s.replace(old, new)

# 문자열 길이
length = string_length("Hello, World!")
print(f"Length: {length}")

# 문자열 연결
result = string_concat("Hello", " World")
print(f"Concatenated String: {result}")

# 문자열 인덱싱
char = string_indexing("Hello, World!", 7)
print(f"Character at index 7: {char}")

# 문자열 슬라이싱
substring = string_slicing("Hello, World!", 0, 5)
print(f"Sliced String: {substring}")

# 문자열 대소문자 변환
upper = string_to_upper("Hello, World!")
lower = string_to_lower("Hello, World!")
print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")

# 문자열 치환
replaced = string_replace("Hello, World!", "World", "Python")
print(f"Replaced String: {replaced}")