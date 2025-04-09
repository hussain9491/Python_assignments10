# here is assignment 06 count down time 
import time
user = int(input("Enter a time in seconds\n"))

for i in range(user, 0, -1): # in range 1 value for starting point second point is ending point and last is how skip value
    second = i %60
    minute = int(i/60) % 60 
    hour = int(i/3600) % 24
    day = int(i/86400) % 365
    print(f"{day:02}: { hour:02} :{ minute:02} :{ second:02}")
    time.sleep(1);


print("Time up!")