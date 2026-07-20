# predict the next prime number after a given number n
def nextprime(n):
    n1=n+1
    if n1==1:
        return n1
    while True:
        
        count=0
        for i in range(1,n1+1):
            if n1%i==0 and n1%n1==0:
                count+=1
        if count==2:
            return n1
        
        n1=n1+1
# print(nextprime(12))


# anagram
def anagram(A, B):
    if sorted(A) == sorted(B):
        return True
    else:
        return False

#  A = "while"
#  B = "listen"

# print(anagram(A, B))


#nested list
def listing(nested_list):
    finallist=[]
    for i in nested_list:
        if isinstance(i,int):
            finallist.append(i)
        else:
            finallist.extend(i)
    return finallist
    
# nested_list=[[1,5,2],[5,3],[7,8],9]
# print(listing(nested_list))

# sum of digits of elements in a list
def digit(n):
    total=0
    for i in n:
        for digit in str(i):
            total+=int(digit)
    return total
# n=[1,2,34,55,66,7]
# print(digit(n))

# armstrong number
def armstrong(n):
    if n < 0:
        return False

    total = 0
    digits = len(str(n))

    for i in str(n):
        total += int(i) ** digits

    return total == n


# print(armstrong(153))   
# print(armstrong(-1)) 
# 
# 
# 
#  

# longest substring palindrome
def longest_substring_palindrome(s):
    words = s.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    rev=longest[::-1]
    if longest==rev:
        return "palindrome"
    else:
        return "it is not a palindrome"

# s = "Python programming is awesome"
# print(longest_substring_palindrome(s))


# 3sum of elements in a array
def three_sum(nums):
    result = []

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])

                    if triplet not in result:
                        result.append(triplet)

    return result


# nums = [2, 4, 5, 2, -1, -4]
# print(three_sum(nums))