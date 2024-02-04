num = int(input("enter the value to reverse"))

def reverseNumber(num):
    reverse = 0
    while num != 0:
        reverse = (reverse*10) + (num % 10)
        num = int(num / 10)
    return reverse

print("ulatalakadi", reverseNumber(num))
