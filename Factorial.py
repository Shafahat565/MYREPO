num = int(input("Enter number: "))

def facto(num):
    if num == 0 or num == 1:
        return 1
    return num * facto(num-1)

result = facto(num)
print("Factorial:", result)