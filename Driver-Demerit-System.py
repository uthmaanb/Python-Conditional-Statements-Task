avg_speed = int(input("What was your Average speed?: "))
allowed_speed = int(input("what is the allowed speed?: "))

points = (avg_speed - allowed_speed)/5
print("\n")

print("Average speed: ", avg_speed)
print("Allowed speed: ", allowed_speed)
print("Points: ", points)

if points >= 12:
    print("TIME TO GO TO JAIL")
