def isPalindrome(text):
    text = text.strip().upper()
    start = 0
    end = len(text) - 1
    while start <= end:
        if not text[start].isalpha():
            start += 1
        elif not text[end].isalpha(): 
            end -= 1
        elif text[start] != text[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

print(isPalindrome("hello world")) #False
print(isPalindrome("Go hang a salami - I'm a lasagna hog.")) #True