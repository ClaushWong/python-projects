import os
import random

day = 1
condition = ["AM","PM"]
timing = condition[0]
maxFatigueBar = 80
fatigueBar = maxFatigueBar

timeInt = 8
timeStr = str(timeInt).zfill(2) + ":00" + " " + timing

print "Day" , day
print "Time :" , timeStr
print "Fatigue :" , fatigueBar ,"/" , maxFatigueBar

def action3hr():
    global timeInt, timing, day, fatigueBar, maxFatigueBar
    if fatigueBar >= 17:
        timeInt += 3
        fatigueBar -= random.randint(15,17)
    else :
        print "You're tired. You can't do this."
    
    if timeInt > 12 and timing == "AM":
        timeInt -= 12
        timing = condition[1]
    if timeInt > 12 and timing == "PM":
        timeInt -= 12
        timing = condition[0]
        day += 1

    timeStr = str(timeInt).zfill(2) + ":00" + " " + timing
    print "Day" , day
    print "Time :" , timeStr
    print "Fatigue :" , fatigueBar ,"/" , maxFatigueBar

def action5hr():
    global timeInt, timing, day, fatigueBar, maxFatigueBar
    if fatigueBar >= 23 :
        fatigueBar -= random.randint(20,23)
        timeInt += 5
    else :
        print "You're tired. You can't do this."
    
    if timeInt >= 12 and timing == "AM":
        timeInt -= 12
        timing = condition[1]
    if timeInt >= 12 and timing == "PM":
        timeInt -= 12
        timing = condition[0]
        day += 1

    timeStr = str(timeInt).zfill(2) + ":00" + " " + timing
    print "Day" , day
    print "Time :" , timeStr
    print "Fatigue :" , fatigueBar ,"/" , maxFatigueBar

def sleep():
    global timeInt, timing, day, fatigueBar, maxFatigueBar

    fatigueBar = maxFatigueBar
    if timeInt > 0 and timeInt < 8 and timing == "AM" :
        timeInt = 8
        timing = condition[0]
    if (timeInt > 8 and timing == "AM") or (timeInt > 0 and timing == "PM"):
        day += 1
        timeInt = 8
        timing = condition[0]
    
    timeStr = str(timeInt).zfill(2) + ":00" + " " + timing
    print "Day" , day
    print "Time :" , timeStr
    print "Fatigue :" , fatigueBar ,"/" , maxFatigueBar
