#Made by Samin Q
# @blitzwolfz

def Add_Per(number):
    first_step = 0
    for x in range(len(number)):
        first_step += int(number[x])

    second_step = int(str(first_step)[0]) + int(str(first_step)[1])
    return second_step

def Multi_Per(number):
    first_step = 1
    for x in range(len(number)):
        first_step *= int(number[x])

    second_step = int(str(first_step)[0]) * int(str(first_step)[1])
    return second_step

x = str(input("Please enter a number: "))

print("The addition persistence is", Add_Per(x))
print("The multipication persistence is", Multi_Per(x))
