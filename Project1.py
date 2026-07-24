name = input("Please ENTER your name: ")
print("Hello "+name+", Welcome to the GAME !!!")

should_we_play = input("Do you want to PLAY ?: ").lower()
# play = should_we_play == "yes"
if should_we_play == "y" or should_we_play == "yes":
    print("Yeah we are PLAYING !!!")
    direction = input("Where do you want to GO ?: ").lower()
    if direction == "left":
        print("We went LEFT !!#DEAD")
    elif direction == "right":
        print("We went RIGHT !!")
        choice = input("Saw a BRIDGE, Cross it or Swim Under ? ").lower()
        if choice == "swim":
            print("Alligator Found & Gulped YOU !!#DEAD")
        elif choice == "cross":
            print("GOLD FOUND !!! GAME WON")
        else:
            print("#DEAD")
    else:
        print("YOU DIE -_-")
else:
    print("No we aren't playing -_-") 
