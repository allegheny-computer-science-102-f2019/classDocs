class User:
    def __init__(self, full_last_name, birthday):
        self.name = full_last_name
        self.birthday = birthday #yyyymmdd
        # Extract the first and last names
        name_pieces = full_last_name.split(" ") #ret a list
        self.first_name = name_pieces[0] # first element
        self.last_name = name_pieces[1] # second element
    #end of __init__()
#end of class
user = User("Frank Wright","18670608")#June 8, 1867
print("\t Name: ",user.name)
print("\t First: ",user.first_name)
print("\t Last: ",user.last_name)
print("\t Birthday: ",user.birthday)
