#ex6 :
def is_palindrome(mot):
    return mot == mot[::-1]                                                                                                                                                                                      == mot.lower()[::-1]

print(is_palindrome("adieu"))  
print(is_palindrome("non"))