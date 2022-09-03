def triple(num):
    return num*3
list1=[int(x) for x in input().split()]
print("list before any number",list1)
result=map(triple,list1)
print("list after triple of number",list(result))
