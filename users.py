import json
import getpass
import os

users = {}
database = "users1.json"

def create_user():
    global users
    """ create a new user """
    print("--- Create new user ---")
    user = input("username = ")
    # checking if user is in users list
    if user in users:
        print(f"err - username {user} is already taken")
        return      
    # assigning variables in a dictionary
    passw = input('password = ')
    users[user] = {"passw": passw}
    print(f"User {user} added successfully")

def user_management(username):
    """ let user edit account """
    global users
    record = users.get(username)
    choice = input((
        "Enter \nd - delete your account\nc - change password"
        "\n any other key to continue_ "))
    if choice == 'd':
        passw = getpass.getpass("Enter pasword = ")
        if record["passw"] == passw:
            del users[username]
            print("user deleted")
        else:
            print("invalid password")
    if choice == 'c':
        currentpass = getpass.getpass("Enter current password = ")
        if record['passw'] == currentpass:
            np = input("Create new password = ")
            npch = getpass.getpass("Re-enter password = ")     
            if np == npch:
                record['passw'] = npch
                users[username] = record
                print("password changed")
            else:
                print("Password don't match")
        
def user_sign_in():
    """ sign in user using username and password """
    username = input("Enter username = ")
    passw = getpass.getpass("Enter password = ")
    record = users.get(username)
    if record is None:
        print("err - no such user found")
        return
    
    if record['passw'] == passw:
        print("Login sucsessfull")
        return user_management(username)
    
    print("err - invalid username / password")
    
def security_loop():
    """running loop"""
    while True:
        #input
        qst = input("Are you already signed in?_y/n_q to quit_   ")
        #if/else loops for calling functions
        if qst == 'n':
            #creating user
            create_user()
        elif qst =='y':
            #login
            user_sign_in()
            #breaking loop  
        elif qst == 'q':
            break

    write_users(users)


def read_users():
    """
    Read users from a file
    """
    if os.path.isfile(database): 
        f = open(database)
        return json.load(f)
    return {}

def write_users(users):
    """
    Save users to file
    """
    f = open("users1.json", "w")
    json.dump(users, f)

# call the loop function
users = read_users()
security_loop()
