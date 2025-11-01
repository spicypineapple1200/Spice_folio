import textwrap

def current(goal):
    points = 0
    miles = 1.0
    speed = 5.0
    switch = True
    while points < goal:
        points+=1
        if switch:
            miles+=0.1
            miles = round(miles, 1)
        elif not switch:
            speed+=0.1
            speed = round(speed, 1)
        else:pass
        if points%20 == 0: switch = not switch
        else: pass
    return miles, speed

def rank_up(goal):
    goal+=1
    points = 0
    miles = 1.0
    speed = 5.0
    switch = True
    while points < goal:
        points+=1
        if switch:
            miles+=0.1
            miles = round(miles, 1)
        elif not switch:
            speed+=0.1
            speed = round(speed, 1)
        else:pass
        if points%20 == 0: switch = not switch
        else: pass
    return miles, speed

def swim_time(miles, speed):
    swim_time = int(round(((miles/speed)*60), 0))
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
else:
    statement = False

if statement:
    print("\n")
    text = "Welcome to run-track-prog, a script designed to help you keep track of your running and alternative cardio training progress. The program begins at 0 points where the minimum requirement is to run....\n"
    print(textwrap.fill(text, width=60))
    print("\n1.0 miles\n5.0 miles per hour\n1.0 incline\n")
    
    text = "When you can complete the above, the program begins! The program is designed for you to complete anywhere from 1 to 2 runs a week. After each run the parameters, either the distance or the speed, will be incrementally increased. You can of course remain at a certain difficulty level if you wish. ALWAYS remember to listen to your body.\n"
    print(textwrap.fill(text, width=60))
    
    print("\n"+("-"*60)+"\n")
    
    level = ("What skill level are you at currently? I will let you know what your parameters are, what parameters you need to get to the next level, and what your alternative cardio options are. The program is designed for you to rank up ONLY from your runs, with the alternative cardio options used as fill ins so you are not running too much.")
    print(textwrap.fill(text, width=60))

# WORKING version of the script, to be commenting out while testing
print("\n")
level = int(input("Anyways, what skill level are you at?: "))
print("\n")
# ---------------------

# TESTING portion of the script, to be commenting out in the working version
# text = "Anyways, what skill level are you at?: "
# print("\n")

# level = 99

# print(textwrap.fill(text, width=60))
# print("\n")
# ---------------------

print("---------RANKING UP---------\n")

print(f"You are currently at level {level}, meaning you currently run...\n")
miles, speed = current(level)
print(f"{miles} miles.\n{speed} miles per hour.\n1.0 incline.\n\n")

print(f"To reach level {level+1} you need to run...\n")
r_miles, r_speed = rank_up(level)
print(f"{r_miles} miles.\n{r_speed} miles per hour.\n1.0 incline.\n")

if statement:
    text = "Now for alternative cardio! When you need a break from your running journey, these workout parameters can be followed to give you a workout on par with your current training level. Your options are...swimming and biking! These are optional and can be ignored if you dislike either of those activities."
    print(textwrap.fill(text, width=60))

# ---------------------

print("\n")
print("---------ALTERNATIVE CARDIO---------\n")

print("---Swim Requirements---\n")
swim_time = swim_time(miles, speed)
print(f"Complete a {swim_time} minute swim.\n\n")

print("----BIKING REQUIREMENTS----\n")
text = "For biking you have two options. Either outdoor biking or stationary biking."
print(textwrap.fill(text, width=60))

print("\n--OUTDOOR BIKING--\n")
bike_distance, bike_level = bike_reqs(miles, speed)
print(f"Complete a {bike_distance} mile bike ride.\n")
print("\n--STATIONARY BIKING--\n")
print(f"Bike for {bike_distance} miles, with a level of {bike_level}.\n")

print("Get out there and TRAIN!")
