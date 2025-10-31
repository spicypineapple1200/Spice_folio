import random

skill = int(input("Hello! Tell me what skill level you are at.\n\n"))
practice = int(input("Now tell me what kind of workout you did...\n" \
"Enter '1' if it was a gym visit, or '0' if it was a home " \
"reflex bar workout.\n\n"))

percentage = 100-skill
chance = random.randint(0, 100)
print(f"\nYour chance roll is...{chance}.")
if chance > percentage and practice == 1:
    chance = random.randint(0, 100)
    print("\nSecond try, just cuz you got that ass up and went to the gym...")
    print(f"Your chance roll is...{chance}.\n")

if chance <= percentage:
    ruling = f"Skill up by one. Congrats! Your skill in boxing is now {skill+1}.\n"
else:
    ruling = f"No skill up this time. Keep training though. Your skill level remains at {skill}.\n"

print(ruling)
