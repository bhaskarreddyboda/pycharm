#factors of given number
num=int(input("enter a number"))
for i in range (1,num+1):
    if num % i == 0:
        print(i)
#alpha sorting
def sortString(str):
    return ''.join(sorted(set(str)))

str = 'bhaskar'
print(sortString(str))
i=1000
myset = set ()

for i in range (1000,3001) :
    if i % 2== 0 :
       myset.add(i)
print(sorted(myset))

# length of string
print('enter the string')
a=input()
print('thelength of string')
print(len(a))
#palindrome
print('enter a string')
def isPalindrome(str):
    if str == str[: : -1] :
        print("True")
    else :
        print('false')
isPalindrome(input())


