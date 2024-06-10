def fun1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter The index: "))
    print(l[1])
    return 1
  except:
    print("Something is error")
    return 0

  finally:
   print("I am alawys exicuted")
# print("I am alawys exicuted")

x = fun1()
print(x)