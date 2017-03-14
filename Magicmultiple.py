#Program to print multiples of a number entered

x = int(input("Enter a number here: "))

for i in range(20):
    print(x, "x", i+1, "=", x*(i+1))
    i+=1

input("\n\nPress<Enter> to exit here")