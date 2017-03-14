# create lists - get entries from user

print("Hello and welcome to your one and only SORTAL\nPlease continue to fill out the proper forms:\n")


N = int(input("Enter the size of the list: "))
ArList = []

for x in range(N):
    print("Enter a name here :")
    x = input("")
    ArList.append(x)
    ArList.sort()


for x in ArList:
    print(x)

input("Press<Enter> to exit the program: ")