#Armstrong Check script
#Written by https://github.com/snmzcm
def main():
    numberz = input("Enter a number for Armstrong Number Check: ")
    numberCheck = int(numberz)
    digits = len(numberz)
    totalsum = 0
    #print(digits)
    for i in numberz:
        i = int(i)
        sum = i ** digits
        totalsum += sum
        print(f"Digit: {i} ^ {digits} equals to {sum}")
    if totalsum == numberCheck:
        print(f"{numberCheck} is an Armstrong Number ")
    else:
        print(f"{numberCheck} is not an Armstrong Number")






main()
