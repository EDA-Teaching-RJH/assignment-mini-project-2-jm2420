import re
import datetime
def checkname(usersname): 
    if re.search(r"+\w", usersname.strip): #checks whether name is made from one or more word characters and is not a decimal
        return True
    else:
        return False
    
def checkdob(dob):
    currentdate = datetime.datetime.now()
    if re.search(r"^\d{2}[/]{1}\d{2}[/]{1}\d{2}", dob):
        return True
        print("length valid")
        splitnums = dob.split("/", 2)
        day = int(splitnums[0])
        print("day", day)
        mon = int(splitnums[1])
        print("mon", mon)
        yea = int(splitnums[2])
        print("Yea", Yea)
        #if mon == 1,3,
        valuesvalid = 0
        if day <= 31:
            valuesvalid = valuesvalid + 1
            print(valuesvalid)
        else:
            print("day invalid")
        if month <= 12:
            valuesvalid = valuesvalid + 1
            print(valuesvalid)
        else:
            print("Month invalid")
        if year <= currentdate.year:
            valuesvalid = valuesvalid + 1
            print(valuesvalid)
        else:
            print("Year invalid")
        return valuesvalid
            

