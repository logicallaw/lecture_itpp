def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
        else:
            return True

print(is_palindrome("abcdcba"))