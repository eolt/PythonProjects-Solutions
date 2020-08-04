def changeD(day):
    
    if day == "monday":
        return "tuesday"
    
    if day == "tuesday":
        return "wednesday"
    
    if day == "wednesday":
        return "thursday"
    
    if day == "thursday":
        return "friday"
    
    if day == "friday":
        return "saturday"
    
    if day == "saturday":
        return "sunday"
    
    if day == "sunday":
        return "monday"
    
    return ""


def changeM(end):
    if end == "AM":
        return "PM"
    else:
        return "AM"
    
def isNextDay(hr, time):
    if time == "AM":
        return True
    else:
        return False
    

def add_time(start, duration, day=""):
    
    rotations = 0
    days_ltr = 0
    
    time = start.split(":")
    hr_1 = int(time[0])
    min_1 = int(time[1].strip("APM"))
    end = time[1].strip("0123456789 ")
    
    time_2 = duration.split(":")
    hr_2 = int(time_2[0])
    min_2 = int(time_2[1].strip("APM"))

    new_hr = int(hr_1) + int(hr_2)
    new_min = int(min_1) + int(min_2)
    
    while new_min >= 60:
        new_min -= 60
        new_hr += 1

    while new_hr > 12:
        new_hr -= 12
        rotations += 1
        end = changeM(end)
        if isNextDay(new_hr, end):
            day = changeD(day.lower())
            days_ltr += 1        
            
    if new_hr == 12:
        rotations += 1
        end = changeM(end)
        if isNextDay(new_hr, end):
            day = changeD(day.lower())
            days_ltr += 1   
                
    if len(str(new_min)) < 2:
        new_min = "0" + str(new_min)
    
    new_time = str(new_hr) + ":" + str(new_min) + " " + end 
    
    if len(day) > 1:
        new_time += ", " + day.capitalize()
        
    if days_ltr >= 1:
        if days_ltr > 1:
            new_time += " (" + str(days_ltr) + " days later)"
        else:
            new_time += " (next day)"
    
    
    return new_time
