name = input(" Enter your Character's name: ")
print("Welcome"  ,name, "to the World of Vardheim")

answer = input("You have the option to go left or right, which way do you travel? ").lower()

if answer == "left":
    answer = input('You have entered Elwynn Forest. Do you want to take down the Defias Brotherhood?')

    if answer == "yes":
        print("Congratulations, you are victorious!")

    elif answer == "no":
        print("Congratulations, you accidentally stumble into BlackRock Mountain and were consumed by Ragnaros the Firelord. ")
    else: 
        print("You've made a grave miscalculation. The Defias Brotherhood sought you out and ended you")
elif answer == "right":
    print("You make a right turn from Elwynn Forest and make your way into the Redridge Mountains")