#ex1
from os import lstat


def sum_number(*numbers):
    return sum(numbers)

print(sum_number(1,2,3,4,5))

print("____________________")

#ex2
def a(l):
    l2=list(filter(lambda x:x%2==0,l))
    print(l2)
a([1,2,3,4,5])

print("____________________")

#ex3
def A(func,lst):
    return [func(x) for x in lst]

print(A(lambda x:x**3 ,[1,2,3,4,5]))