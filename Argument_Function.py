# def Average(a=1, b=9):
#     print("The average is: ", (a+b)/2)

# # Average(4, 5)
# # Average()
# Average(a=9)

def Average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average value is: ", sum/len(numbers))

Average(5, 6)