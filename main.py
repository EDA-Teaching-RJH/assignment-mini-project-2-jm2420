from processingdata import checkname
from processingdata import checkdob
class User:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
def main():
    name = input("Please enter your surname ")
    dob = input("Please enter your date of birth in the form DD/MM/YYYY ")
    try:        
        assert checkdob(dob) == "3"
        print(checkdob(dob))
    except AssertionError:
        print("Date of Birth not valid")
        main()
    try:
        assert checkusersname == "True"
    except:
        print("Name not valid")
        main()






if __name__ == "__main__":
    main()