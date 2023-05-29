#SCALE IT MORE
#TASK 1
#Email Slicer


email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print("Your Username is {0} and Domain is {1}".format(username,domain))