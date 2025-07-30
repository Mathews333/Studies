# for i in range(1,11):
#     print(i)

# -----------------------------

# a=int(input('enter a:'))
# b=int(input('enter b:'))
# for i in range(a,b):
#     print(i)

# ----------------------------

# a=int(input('enter starting number:'))
# b=int(input('enter ending number:'))
# for i in range(a,b):
#     if i % 2 != 0:
#         print(i)

# -------------------------------

# a=int(input('enter first number :'))
# b=int(input('enter second number :'))
# sum=0
# for i in range(a,b+1):
#     sum=sum+i
# print('sum =',sum)

# -------------------------------

a=int(input('enter first number :'))
b=int(input('enter second number :'))
sum = 0
for i in range(a,b+1):
    if i % 2 == 0:
     sum += i
print('sum =',sum)