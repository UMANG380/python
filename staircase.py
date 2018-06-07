n=int(input())
def staircase(n):

    if(n<=2):
      return n
    elif n==3:
      return 4
    else:
      return staircase(n-1)+staircase(n-2)+staircase(n-3)

print(staircase(n))
