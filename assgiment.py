#1
# import math
# num=[2,3,4,5,6]
# def listTripler(item):
#  return math.floor(math.pow(item,3))

# resultList=list(map(listTripler,num))
# print(resultList)
#2
# nums=[0,1,2,3,4,5,6,7,8,9,10]
# def evenList(i):
#     if(i%2==0):
#         return i
# def oddList(i):
#     if(i%2!=0):
#         return i

# evenNumbers=list(filter(lambda x:x,map(evenList,nums)))
# oddNumbers=list(filter(lambda x:x,map(oddList,nums)))
# print("Odd numbers : {0}".format(oddNumbers))
# print("Even numbers : {0}".format(evenNumbers))

#3
# courses=("SOFTWARE","ITITMS","DD","ANIMATION")

# output=tuple(map(lambda x:x.lower(),courses))
# print(output)

#4
# import math
# l3=[24,36,64,25]
# output=list(map(lambda x:math.sqrt(x),l3))
# print(output)

#5
# import re #regular expression
# string = ""
# str = "hello world hello"
# def findDuplicate(i):
#   global string
#   if re.search(i,string) == None:
#       string += i

# ans=map(findDuplicate,str)
# print(list(ans)) # you need to print this list formap function as it is mandatory
# print("String with unique characters:",string)



# #6
# number=int(input("Enter number for multiplicationtable :"))
# l=int(input("Enter limit till you want to printtable:"))
# def multiples(i):
#  return number*i

# limitList=[]
# for i in range(1,l+1):
#  limitList.append(i)

# res =list(map(multiples,limitList))
# print("Multiplication Table : ",res)


#7
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# result = map(lambda x, y: x + y, nums1, nums2)
# print("Result: after adding two list")
# print(list(result))

#8
# l= [2.5, 2.4, 3.8]
# newlist = list(map(lambda i:int(i), l))
# print(newlist)

# print(num1, num2, sep = '\n')

#9
#wrong question
# seqtuple = ('A', 'B', 'C', 'D', 'E')
# print(list(reversed(seqtuple)))

# seqrange = range(1, 5)
# print(list(reversed(seqrange)))

# #10
# names ={'a':'anna','b':'bharat','c':'carlo','d':'dim'}
# gmail = dict(map(lambda
# x:(x[0],x[1]+'@gmail.com'),names.items()))
# print(gmail)









