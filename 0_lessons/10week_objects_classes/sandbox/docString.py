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
#end of class User

help(User) #get information about class.
