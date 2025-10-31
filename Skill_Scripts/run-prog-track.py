
goal = int(input("I am going to show you the goals you need to hit in \n" \
"order to qualify for a certain number of points. Enter the point goal \n" \
"below!\n\n"))
print(f"\nAlright so {goal} points is what your going for.. Below is your breakdown.\n\n")
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

print(f"Run Reqs for {goal} points.\n{miles} miles.\n{speed} mph.\n")
