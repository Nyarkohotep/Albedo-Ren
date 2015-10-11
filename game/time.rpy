  # Запитонить не удалось, придется вызывать этот ивент после любой смены времени
label time_change:
    
    if minute >= 60:
        $ hour = hour + 1
        $ minute = minute - 60
        
    if hour >=24:
        $ day = day + 1
        $ hour = hour - 24
    
    if real_word == "True":
    
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 and day > 31:
           $ day = day - 31
           $ month = month + 1
                      
        elif month == 4 or month == 6 or month == 9 or month == 11 and day > 30:
           $ day = day - 30
           $  month = month + 1
        
        elif month == 2 and year % 4 > 0 and day > 28:
           $ day = day - 28
           $ month = month + 1
            
        elif month == 2 and year % 4 == 0 and day > 29:
           $ day = day - 29
           $ month = month + 1