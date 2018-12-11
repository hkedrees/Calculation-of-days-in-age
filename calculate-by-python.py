
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0:
            if year % 100 != 0:
                return True
        else:
            return False
            
    #if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #    return True
    #return False
    
    #return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    #######################################################
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    #######################################################

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    y = y1
    m = m1
    d = d1
    days = 0
    
    while y < y2:

        while m <= 12:

            while d < daysOfMonths[m-1]:
                d += 1
                days += 1
                
            if m == 2:
                if isLeapYear(y):
                    days += 1
                    
            d = 1
            m += 1

        y += 1
        m = 1

    while m < m2:

        while d < daysOfMonths[m-1]:
                d += 1
                days += 1
        if m == 2:
            if isLeapYear(y):
                days += 1
        d = 1
        m += 1

    while d < d2:
        d += 1
        days += 1
        
 
    return days


# test
print daysBetweenDates(1994,2,26,1995,2,26)
