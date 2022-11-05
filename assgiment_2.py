# 1.using filter() function filter the list so that only negative numbers are left.

# l=[10,-20,-5,6,-8,55,-4]

# def negative(i):
#  if(i<0):
#   return i

# output=list(filter(negative,l))
# print(output)

# 2.using filter function filter the even numbers so that only odd numbers are passed to the new list

# numbers = (1,2,3,4,5,6,7,8)

# def oddNumFilter(i):
#  if i%2==0:
#   return True
#  return False
# check_odd = list(filter(oddNumFilter,numbers))
# print("Odd Numbers : ",check_odd)

# 3.using filter() and list() functions and .lower() method filter all the vowels in a given string

# string = "Hello World"
# lowerCharacters = list(filter(lambda x: True if x.lower() in "aeiou" else False, string))
# print(lowerCharacters)

# 4.This time using filter() and list() functions filter all the positive integers in the string.

# str="Winter Olympics in 2022 will take place inBeijing China"
# lst = list(filter(lambda x: True if x in"0123456789" else False, str))
# print(lst)

# 5.Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.
lst=[-1000, 500, -600, 700, 5000, -90000, -17500]
num = list(filter(lambda x: True if x>0 else False,
map(lambda x: x*-1, lst)))
print(num)