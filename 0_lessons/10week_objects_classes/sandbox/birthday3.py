
class User:
    """MY COOL CLASS!! This is a class to create a user object. Used to store name and birthday."""

    def __init__(self, fullast_name, birthday):
        self.name = fullast_name
        self.birthday = birthday #yyyymmdd
        # Extract the first and last names
        name_pieces = fullast_name.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1] # second element
    #end of __init__()


    def ageMethod1(self):
      """Return the age of the person in years. Convert birthday to get these years."""
      today = datetime.date(2019, 1, 1) # 1 Jan 2019
      yyyy = int(self.birthday[0:4])
      mm = int(self.birthday[4:6])
      dd = int(self.birthday[6:8])
      dob = datetime.date(yyyy,mm,dd) #date of birth
      age_in_days = (today - dob).days
      age_in_years = age_in_days/365
      return int(age_in_years)
      #end of ageMethod1()

    def getToday(self):
      """returns today's date in yyyy-mm-dd format"""
      import datetime #library
      today = datetime.datetime.today().strftime('%Y-%m-%d') # On one line. Is a string
      yyyy = int(today[0:4])
      mm = int(today[5:7])
      dd = int(today[8:10])
      today = datetime.date(yyyy,mm,dd) #date of birth
      # print(" + today's date:", today)
      return today
      #end of getToday()
    def ageMethod2(self):
      """Return the age of the person in years. Convert birthday to get these years."""
      yyyy_b = int(self.birthday[0:4])
      mm_b = int(self.birthday[4:6])
      dd_b = int(self.birthday[6:8])
      #date of birth
      dob = datetime.date(yyyy_b,mm_b,dd_b)
      today = self.getToday()
      age_in_days = (today - dob).days
      age_in_years = age_in_days/365
      return int(age_in_years)
      #end of ageMethod2()

#end of class User

#help(User) #get information about class.


import datetime
user = User("Frank Wright","18670608") #June 8, 1867
print("\t FullName: ",user.name)
print("\t First: ",user.first_name)
print("\t Last: ",user.last_name)
print("\t Birthday: ",user.birthday)
print("\t AgeMethod1: ",user.ageMethod1())
print("\t Today's date:", user.getToday())
print("\t AgeMethod2: age from today is ",user.ageMethod2()) #dynamic
#help(User) # see the docstrings! yey!
