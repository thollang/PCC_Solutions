usernames=[]
if usernames:
    for username in usernames:
        if username=='admin':
            print("Hello "+username+",would you like to see a status report?")
        else:
            print("Hello "+username+",thank you for logging in again")
else:
    print("We need fo tind some users!")
