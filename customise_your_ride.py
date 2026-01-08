print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice:"))

if(choice == 1):
    print("What type of Bike?")
    print("1. Scooty")
    print("2. Scooter")
    choice = int(input("Enter your choice: "))
    if (choice == 1): 
        print("You have chosen Scooty!")
    else:
        print("You have chosen Scooter!")
elif (choice == 2):
    print("What type of Car?")
    print("1. Sedan")
    print("2. XUV")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("You have chosen Sedan!")
    else:
        print("You have chosen XUV!")
else:
    print("Wrong Choice!, Pick again...")
