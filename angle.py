time = int(input("Enter the time (in hhmm): "))
minutes = (time%100)
hour = time//100

def angle_calc(h,m):
    angles_hour_hand = 30*(h+(m/60))  
    angles_minute_hand = 6*m
    diff =abs(angles_hour_hand-angles_minute_hand)
    angle = min(diff,360-diff)
    print(f"The angle between the minute hand and the hour hand is {angle}°.")

if hour<0 or hour>24 or minutes<0 or minutes>60:
    print("Please enter a valid time.")
elif hour>=12 and hour<24:
    hour = 24-hour
    print(f"The time is {hour}:{minutes}PM.")
    angle_calc(hour,minutes)
elif hour<12 :
    print(f"The time is {hour}:{minutes}AM.")
    angle_calc(hour,minutes)
elif hour==24 and minutes==0:
    hour=24-hour
    print(f"The time is {hour}:{minutes}AM.")
    angle_calc(hour,minutes)
    


