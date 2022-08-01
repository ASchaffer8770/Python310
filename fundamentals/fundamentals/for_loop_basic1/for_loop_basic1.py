# Prints Numbers 0 -150
for i in range(151):
    print(i)

#Prints all numbers that are multples of 5
for i in range(5, 1000, 5):
    print(i)

#Prints all numbers 1 - 100 if divisable by 5 or 10 prints related message
for i in range(1, 101, 1):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

# Add odds from 0 -500,000 and print final sum

min = 0
max = 500000
oddsum = 0

for i in range(min, max +1):
    if(i % 2 != 0):
        print("{0}".format(i))
        oddsum = oddsum + i
print(oddsum)

# countdown by 4s and print positive numbers during countdown

def count_down():
    x = 2018
    while x > 0:
        print(x)
        x = x - 4
count_down()

#flexible counter

def countdown(low_num, high_num, mult):
    for i in range (low_num, high_num):
        if i % mult == 0:
            print(i)

countdown(2, 9, 3)