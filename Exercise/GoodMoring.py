import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

Hour = int(time.strftime('%H'))
print(Hour)

if Hour < 12:
    print("Good Morning")
elif Hour < 16:
    print("Good Afternoon")
elif Hour < 20:
    print("Good Evening")
else:
    print("Good Night")
