def square(num):
    return num**2
list1=[int(x) for x in input().split()]
print("list before any operation is",list1)
result=map(square,list1)
print("list after square of number",list(result))