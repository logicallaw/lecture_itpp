def is_palindrome(s): #5
    for i in range(len(s)//2): #0,1,2, 3,4
        if s[i] is not s[len(s) - i - 1]: #(0,4)(1,3)(2,2)
            return False
    return True

if is_palindrome("abb2a"):
    print("abba")