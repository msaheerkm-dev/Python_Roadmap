

num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is NOT a prime number")
#             break
#     else:
#         print(num, "is a PRIME number")
# else:
#     print("Number must be greater than 1")

divisor=[i for i in range(2,num) if num % i==0]
print('prime' if len(divisor)==0 and num>1 else 'not prime')



