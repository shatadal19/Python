sum = []
size = 5;
print("Enter 5 number: ")

for i in range(0, size):
    number = int(input())
    sum.append(number)

summ = 0
for j in sum:
    summ = summ + j

print("Sum of the element is: ", summ)