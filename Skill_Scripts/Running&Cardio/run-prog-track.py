import textwrap

def rank(goal):
    miles, speed= 1.0, 5.0
    for count in range(goal):
        miles = round(miles+0.04, 2)
        speed = round(speed+0.05, 2)
    speed = round(speed, 1)
    return miles, speed

def swim_time(miles, speed):
    swim_time = int(round((miles*11.5)+speed, 0))
    return swim_time

def bike_reqs(miles, speed):
    bike_distance = round(miles*3, 1)
    bike_level = int(round(speed, 0))
    return bike_distance, bike_level
    

# END OF FUNCTIONS, BEGINNING OF SCRIPT

print("\n")
statement = input("Do you want the intro/long text messages? If so enter \"y\", if not enter \"n\": ")

if statement == "y":
    statement = True
elif statement == "n":
    statement = False
else:
    while statement != True or statement != False:
        print("\nEvidently your struggling. Darling, a \"y\" or an \"n\" only please! Focus now.\n")
        statement = input("Do you want the intro/long text messages? If so enter \"y\", if not enter \"n\": ")
        if statement == "y":
            statement = True
            break
        elif statement == "n":
            statement = False
            break

if statement:
    print("\n")
    text = "Welcome to run-track-prog, a script designed to help you keep track of your endurance training progress. The program begins at 0 points where the minimum requirement is to complete the following..."
    print(textwrap.fill(text, width=60))
    print("\nRun...\n1.0 miles\n5.0 miles per hour\n1.0 incline\n")
    print("Swim...\n16 minutes\n")
    print("Bike...\n3.0 miles\nDifficulty Level 5\n")
    
    text = "The program is designed for you to complete the run, swim, and bike requirements to move to the next level. Ideally, the three events are all done in a week but to each his own. This is at your own pace. ALWAYS remember to listen to your body.\n"
    print(textwrap.fill(text, width=60))
    
    print("\n"+("-"*60)+"\n")
    
    level = ("What skill level are you at currently? I will let you know what your three challenges are in order to get to the next level.")

level = input("So, what skill level are you at?: ")
print("\n")

levels = [str(i) for i in range(101)]
while level not in levels:
    print("Only inputs of 0 to 100 are accepted. Let's try this again. *sigh*\n")
    print("\n")
    level = input("So, what skill level are you at?: ")
    print("\n")
    if level in levels:
        break
level = int(level)

check_up = input(f"You are currently at level {level}, Would you like to see your current stats? Enter a \"y\" or an \"n\": ")

if check_up == "y":
    check_up = True
elif check_up == "n":
    check_up = False
else:
    while check_up != True or check_up != False:
        print("\nCome on now fam. A \"y\" or an \"n\" only please! Focus now.\n")
        check_up = input("Would you like to see your current stats?: ")
        if check_up == "y":
            check_up = True
            break
        elif check_up == "n":
            check_up = False
            break
if check_up:
    print(f"\nLevel {level}. Below are your stats...\n")
    # run
    miles, speed = rank(level)
    print(f"Run...\n{miles} miles.\n{speed} miles per hour.\n1.0 incline.\n")
    # swim
    my_swim_time = swim_time(miles, speed)
    print(f"Swim...\n{my_swim_time} minutes\n")
    # bike
    bike_distance, bike_level = bike_reqs(miles, speed)
    print(f"Bike...\n{bike_distance} miles\nDifficulty Level {bike_level}\n")
else:
    print("\n")

print(("-"*25)+"RANKING UP"+("-"*25)+"\n")

if level == 100:
    text = "Looks like you have completed our program and achieved 100 points. Congratulations!"
    print(textwrap.fill(text, width=60))
    if not check_up:
        print(f"\nCongrats again on {level}. Below are your stats...\n")
        # run
        miles, speed = rank(level)
        print(f"Run...\n{miles} miles.\n{speed} miles per hour.\n1.0 incline.\n")
        # swim
        my_swim_time = swim_time(miles, speed)
        print(f"Swim...\n{my_swim_time} minutes\n")
        # bike
        bike_distance, bike_level = bike_reqs(miles, speed)
        print(f"Bike...\n{bike_distance} miles\nDifficulty Level {bike_level}\n")
else:
    level+=1
    print(f"To get to Level {level}. You must accomplish the following...\n")
    # run
    miles, speed = rank(level)
    print(f"Run...\n{miles} miles.\n{speed} miles per hour.\n1.0 incline.\n")
    # swim
    my_swim_time = swim_time(miles, speed)
    print(f"Swim...\n{my_swim_time} minutes\n")
    # bike
    bike_distance, bike_level = bike_reqs(miles, speed)
    print(f"Bike...\n{bike_distance} miles\nDifficulty Level {bike_level}\n")

print("\nGet out there and TRAIN!")
