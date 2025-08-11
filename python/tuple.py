# my_tuple=(1,2,3)
# print(my_tuple)
# tuple1=11,22,33
# print(tuple1)

# ------------------------

# tuple2=(1,2,3,3,3)
# print(tuple2)
# c=tuple2.count(3)
# print(c)
# i=tuple2.index(2)
# print(i)

# ------------------------

# tuple3=(1,2,3,4,1,4)
# print(tuple3)
# il=tuple3.index(4,4)
# print(il)

# ------------------------

# tuple4=(1,2,3,4)
# for i in 1,2,3,4:
#     print(i)

# ------------------------

# tuple5=(1,2,3,5,7,9,99,57,127)
# l=[]
# for i in tuple5:
#      if i % 2 !=0:
#          l.append(i)
# print(l)

# ------------------------

# tuple6=(1,2,3,4,5,6,7)
# l=[]
# for i in tuple6:

# ------------------------

l = []
for i in range(2, 100):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        l.append(i)

print(l)