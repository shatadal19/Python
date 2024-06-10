a  = input("Enter the number: ")
print(f"Multiply table of {a} is: ")
try:
    for i in range(1, 11):
     print(f"{int(a)}X{i} = {int(a)*i}")
except:
   print("invalid Input")

print("Some importent code line")