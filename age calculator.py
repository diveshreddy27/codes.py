from datetime import date

def age(yn,mn,dn):
    y = 0       #years
    m = 0       #months
    d = 0       #days
    flag = 0

    yb = int(input("enter the birth year : "))
    mb = int(input("enter the birth month : "))
    db = int(input("enter the birth date : "))

    x = mb

    while (flag == 0):
        if (yn > yb):
            yb = yb + 1
            y = y + 1

        if (yn == yb):
            flag = 1

    flag = 0
    while (flag == 0):
        if (mn > mb):
            mb = mb + 1
            m = m + 1
        elif (mb == mn):
            if (dn > db):
                d = dn - db
            elif (dn < db):
                if (x > 0 and x >= 7):
                    if (x % 2 == 0):
                        if (x == 2):
                            if (yn % 4 == 0):
                                d = dn + (29 - db)
                                flag = 1
                            else:
                                d = dn + (28 - db)
                                flag = 1
                        else:
                            d = dn + (30 - db)
                            flag = 1
                    else:
                        d = dn + (31 - db)
                        flag = 1
                elif (x <= 12 and x > 7):
                    if (x % 2 == 0):
                        d = dn + (31 - db)
                        flag = 1
                    else:
                        d = dn + (30 - db)
                        flag = 1
        else:
            y = y - 1
            m = mn + (12 - mb)
            if (dn > db):
                d = dn - db
            elif (dn < db):
                m = m - 1
                if (x > 0 and x <= 7):
                    if (x % 2 == 0):
                        if (x == 2):
                            if (yn % 4 == 0):
                                d = dn + (29 - db)
                                flag = 1
                            else:
                                d = dn + (28 - db)
                                flag = 1
                        else:
                            d = dn + (30 - db)
                            flag = 1
                    else:
                        d = dn + (31 - db)
                        flag = 1
                elif (x <= 12 and x > 7):
                    if (x % 2 == 0):
                        d = dn + (31 - db)
                        flag = 1
                    else:
                        d = dn + (30 - db)
                        flag = 1

    print(y, m, d)
    print(x)

c=date.today()
yn=c.year        #yt=presentyear
mn=c.month       #mt=presentmonth
dn=c.day         #dt=presentdate
age(yn,mn,dn)


