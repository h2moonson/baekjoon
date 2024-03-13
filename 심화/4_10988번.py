# 소문자로만 단어 주어짐, 팰린드롬인가 아닌가?
# 거꾸로 읽어도 같은 단어말함 level, noon
word = input()
n = len(word)
# def is_palindrome(n, word):
#     if n%2 == 0: #짝수일때
#         for i in range(n//2):
#             if word[i] != word[n-1-i]:
#                 return 0
#             else: 
#                 pass
        
#     else:  #홀수일때 
#         for i in range (n-1//2):
#             if word[i] != word[n-1-i]:
#                 return 0
#             else:
#                 pass
#     return 1
def is_palindrome2(word):
    return word == word[::-1]
print(is_palindrome2(word))
#print(is_palindrome2(word.lower())) 엄밀하게는 소문자만 받아야되기에