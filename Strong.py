# Compulsory Task

# Declaring all variables as false

haveLength = False
upCase = False
lowCase = False
haveNum = False
numReq = 0

# Declaring a variable to determine whether the user's password has atleast 6 characters.

checkLength = input ("Does your password have atleast 6 characters (Yes or No)?\n")
checkLength = checkLength.lower() # Used to make the answer lowercase so that it can be entered by the user using upper and/or lowercase letters.

# If statement to determine if the user has used a long enough password and therefore changing the haveLength value to true.

if checkLength == "yes":
    haveLength = True
    numReq += 1 # Adds one to the number of good password requirements.

# Declaring a variable to determine whether the user's password has atleast one uppercase letter.

checkUpCase = input ("Does your password contain atleast one uppercase letter (Yes or No?)\n")
checkUpCase = checkUpCase.lower() # Used to make the answer lowercase so that it can be entered by the user using upper and/or lowercase letters.

# If statement to determine if he user has an uppercase letter in his/her password and therefore changing upCase's value to true.

if checkUpCase =="yes":
    upCase = True
    numReq += 1 # Adds one to the number of good password requirements.

# Declaring a variable to determine whether the user's password has atleast one lowercase letter.

checkLowCase = input ("Does your password have atleast one lowercase letter (Yes or No)?\n")
checkLowCase = checkLowCase.lower() # Used to make the answer lowercase so that it can be entered by the user using upper and/or lowercase letters.

# If statement to determine if he user has a lowercase letter in his/her password and therefore changing lowCase's value to true.

if checkLowCase == "yes":
    lowCase = True
    numReq += 1 # Adds one to the number of good password requirements.

# Declaring a variable to determine whether the user's password contains atleast one number.

checkNum = input ("Does your password contain atleast one number (Yes or No?)\n")
checkNum = checkNum.lower() # Used to make the answer lowercase so that it can be entered by the user using upper and/or lowercase letters.

# If statement to determine if he user's password contains a number and therefore changing haveNum's value to true.

if checkNum =="yes":
    haveNum = True
    numReq += 1 # Adds one to the number of good password requirements.

# The check number of requirements variable increases by one for every variable that changes to true and if it reaches three then the following string is printed.

if numReq == 3:
    print("This is a suitable password.")
    

    

