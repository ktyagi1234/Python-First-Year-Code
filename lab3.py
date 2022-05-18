
#function to determine whether a year is a leap year or not

def leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
    else:
        return False

#function that tells the number of days in any given month

def daysInMonth(month,year): 
    if leap(year) == True:
        if(month == 2):
            day = 29
        elif(month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
            day = 31
        elif(month == 2 or 4 or 6 or 9 or 11):
            day = 30
    elif leap(year) == False:
        if(month == 2):
            day = 28
        elif(month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
            day = 31
        elif(month == 2 or 4 or 6 or 9 or 11):
            day = 30

    print(day)
    return day

#daysInMonth(1,2021)

#function that determines whether a point is in a rectangle or not with (rx,ry) being the coordinates of the leftmost point in the rectangle

def pointInRect(x,y,rx,ry,rw,rh):
    if (x >= rx and x <= rx + rw) and (y <= ry and y >= ry - rh):
        return True
    else:
        return False

#function that determines whether a rectangle is inside another rectangle or not with (x1,y1) being the coordinates of the rectangle in the other rectangle

def rectInRect(x1,y1,w1,h1,x2,y2,w2,h2):
    if(x1 >= x2 and x1 <= x2+w2) and (y1 <= y2 and y1 >= y2 - h2) and (x1 + w1 <= x2 + w2) and (y1 - h1 >= y2-h2):
       # print("good")
        return True
    else:
      #  print("bad")
        return False
#rectInRect(1,4,5,2,2,3,2,0.5)

#function that determines whether two rectangles overlap or not

def overlap(x1,y1,w1,h1,x2,y2,w2,h2):
    if(pointInRect(x1,y1,x2,y2,w2,h2) == True) or (pointInRect(x2,y2,x1,y1,w1,h1) == True):
        return True
    else:
        return False

