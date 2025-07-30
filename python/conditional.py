# a=22
# b=10
# if a>b:
#     print ('true')
# else:
#     print('false')

# a=220
# b=90
# if a>b:
#     print('ok')
# else:
#     print('no')

# first_Number=int(input('enter first number :'))
# second_Number=int(input('enter second number :'))
# if(first_Number>second_Number):
#     print(first_Number,'is larger')
# else:
#     print(second_Number,'is larger')
# if(first_Number==second_Number):
#     print('both are equal')
# elif(first_Number>second_Number):
#     print(first_Number,'is greater')
# else:
#     print(second_Number,'is greater')


# st_mark=int(input('enter the mark:'))
# if st_mark>=90:
#     print('A grade')
# elif st_mark>=80:
#     print('B grade')
# elif st_mark>=70:
#     print('C grade')
# elif st_mark>=60:
#     print('D grade')
# else:
#     print('failed')
    
f=int(input('enter first number :'))
s=int(input('enter second number :'))
t=int(input('enter third number :'))
if(f>s):
    if(f>t):
        print('first number is larger')
    else:
        print('third number is larger')
else:
    if(s>t):
        print('second number is larger')
    else:
        print('third number is larger')