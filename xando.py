import random

one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"
sep = " | "
nl = "\n"

print (nl)
print (one + sep + two + sep + three)
print (four + sep + five + sep + six)
print (seven + sep + eight + sep + nine)

corner = [one, three, seven, nine]
middle = [two, four, six, eight]
centre = five


print ("You are crosses: ")
choice = input ("Where will you go? ")
if choice == "1":
    one = "X"
    pick = [three, seven, nine]
    (random.choice(pick)) 
    # need to set the output of the random to a value


    print (rng)

elif choice == "2":
    two = "X"
