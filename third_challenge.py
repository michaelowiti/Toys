def convert2_24hrs(hour,minute,period):
    if period == "pm" and hour != 12:
        hour +=12 

    elif period=="am" and hour ==12:
        hour = 0    


    return f"{hour:02d}{minute:02d}" 

time1 = convert2_24hrs(12, 0, "pm")  # Output: "1200"
time2 = convert2_24hrs(12, 0, "am")  # Output: "0000"   