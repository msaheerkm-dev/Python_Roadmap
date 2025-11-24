# pattern program
n=int(input ("how many lines do you want to print the pattern: "))
for i in range(1,n+1):
  for j in range(1,n+1):
    print(" "*j+" *"*n)
    n-=1 