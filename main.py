import random


keep_going = True

while keep_going:
    number_picked = random.randrange(0, 15)
    guessed = input("Trouver un nombre entre 1 et 10 : ")
    if guessed != number_picked:
        print(f"Perdu ! C'était {number_picked}")
        keep_going = True if input("On rejoue ? Oui : Non ").lower() == "oui" else False
    else:
        print("C'est gagné !")
        keep_going = True if input("On rejoue ? Oui : Non ").lower() == "oui" else False
print("Bye !")
