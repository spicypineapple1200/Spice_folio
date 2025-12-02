import random

print("\n")
level = int(input("Hello! Tell me what skill level you are at: "))

levels = [number for number in range(101)]
while level not in levels:
    print("Only inputs of 0 to 100 are accepted. Let's try this again. *sigh*\n")
    level = int(input("So, what skill level are you at?: "))
    if level in levels:
        break
skill = int(level)

practice = input("Did you put out at the gym today? Be honest.\n" \
"Enter 'y' if so, or 'n' if not: ")
checks = ['y', 'n']
while practice not in checks:
    print("Bad input.\n")
    practice = input("Enter 'y' or 'n', no other input is valid: ")
    print("\n")
    if practice in checks:
        break

percentage = 100-skill
chance = random.randint(0, 100)
print(f"\nYour chance roll is...{chance}.")
if chance > percentage and practice == 'y':
    chance = random.randint(0, 100)
    print("\nSecond try, just cuz you put out while at the gym today...")
    print(f"Your chance roll is...{chance}.\n")

if chance <= percentage:
    ruling = f"Skill up by one. Congrats! Your skill level is now {skill+1}.\n"
else:
    ruling = f"No skill up this time. Keep training though. Your skill level remains at {skill}.\n"

print(ruling)
