num = 10000000
count = 0
while len(str(num)) != 9:
    if num % 18 == 0:
        if "0" in str(num) or "4" in str(num) or "5" in str(num) or "6" in str(num)or "7" in str(num) or "8" in str(num) or "9" in str(num):
            num = num + 1
        else:
            count = count + 1
            print(num)
            num = num + 1
    else:
        num = num + 1
print(count)

# prints all the numbers and the total amount of numbers from 0 to num which are divisible by 18 and do not contain a 0, 4, 5, 6, 7, 8, or 9 in them
