import logging
import uuid
# Assigning variables
headmate = 'headmate'
collective = 'collective'
front = 'front'
fronter = 'fronter'
cocon = 'coconsious'
dormant = 'dormant'
front_status =[fronter,cocon,dormant,]
age = int
body_age = 'body age'
maturity_age = 'developmental period'
headmate_id = [uuid.uuid4]
social_id = [uuid.uuid4]
maturity_age = ['little', 'adolescent', 'adult', 'elderly']
headmate_count = input
account_type = ['singlet', 'collective']
status = ['away', 'online', 'invisable', 'busy']
account_name = 'Name'
account_password = 'Account password'
headmate_name = 'headmate name'

# setting account type to singlet or collective
if account_type: 'collective'
else: account_type = 'singlet'
#account types and what is in them
class collective:
    headmate_count
    fronter
    social_id
    body_age
    maturity_age
    status

class headmate:
    headmate_name
    age
    maturity_age
    headmate_id
    social_id
    front_status
class singlet:
    body_age
    social_id
# Setting account privacy based on bodies age    
if body_age < 13:
    set 
    maturity_age = 'little'
elif body_age > 13 <18:
    set 
    maturity_age = 'adolescent'
elif body_age > 17 < 60:
    set
    maturity_age = 'adult'
elif body_age >59:
 set
 maturity_age ='elderly'
    
if body_age <18 or maturity_age ('little', 'adolescent'):
    print( 'User is a minor. Keep youir interactions with this user age appropriate.' )
elif body_age <13 or maturity_age ('little'):
    print('This user requires an adult to give permission before you can interact with them. Contact their guardian to be granted access.')
else: body_age > 17 or maturity_age ('adult', 'elderly')

class account:
    account_type
    social_id
    account_name
    account_password
    
def create_social_id():
 return str(uuid.uuid4())
def create_headmate_id():
    return str(uuid.uuid4())

def create_headmate():
    headmate_count= +1
    Social_id = create_social_id
    headmate_id = create_headmate_id
     # Prompt the user for headmate details
    name = input("Enter the headmate's name: ")

    # Validate age input
    while True:
        try:
            age = int(input("Enter the headmate's age (must be a number): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")
    
    # Prompt for maturity age with choices
    maturity_age_options = ['little', 'adolescent', 'adult', 'elderly']
    print("Select the headmate's maturity age from the options: ", ", ".join(maturity_age_options))
    
    while True:
        maturity_age = input("Enter the headmate's maturity age: ").lower()
        if maturity_age in maturity_age_options:
            break
        else:
            print("Invalid input. Please choose from: ", ", ".join(maturity_age_options))
    
    # Prompt for favorite color
    favorite_color = input("Enter the headmate's favorite color: ")
    