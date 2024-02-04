num = int(input("enter the value to count"))

def countDigit(num):
    count = 0
    while num != 0:
        count += 1
        num = int(num / 10)
    return count

print("ithana number iruku", countDigit(num))