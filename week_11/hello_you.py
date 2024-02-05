while True:
    name = input("what is your name? ")
    if not name.isalpha():  #isalpha method checks if the input is a letter
        print("sorry, letters only babe. please try again.")
    else:
        break

print("hey,", name + "!")

#I know this is so hard, but you gotta keep up. trust.