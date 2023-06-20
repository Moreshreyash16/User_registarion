'''
@Author: Shreyash More

@Date: 2023-06-18 15:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-18 15:10:30

@Title : User registration UC 8 User need to enter a email address
'''

import re 
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
handlers=[
        logging.StreamHandler(),  # Stream logs to the console
        logging.FileHandler('User_reg.log')  # Store logs in a file
    ])
    # Create a logger
logger = logging.getLogger('my_logger')

def check_first__name(first_name):
    """
        Description:
            It Validates first name 
        Parameter:
            None
        Return:
            None
        """

    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    validate=re.match(pattern,first_name)
    if validate:
        logger.info("First Name is Valid ")
        return True
    else:
        logger.error("First Name is Not valid \n")
        return False

def check_last__name(last_name):
    """
    Description:
        It Validates Last name 
    Parameter:
        None
    Return:
        None
    """

    pattern=r'^[A-Z][a-zA-Z]{2,}$'
    validate=re.match(pattern,last_name)
    if validate:
        logger.info("Last Name is Valid ")
        return True
    else:
        logger.error("Last Name is Not valid \n")
        return False
    
def check_Email(email):
    """
    Description:
        It Validates Email Address
    Parameter:
        None
    Return:
        None
    """
    pattern=r'^[a-zA-Z0-9\+-]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,})$'
    validate=re.match(pattern,email)
    if validate:
        logger.info(f"{email} is Valid ")
        return True
    else:
        logger.error(f"{email} is Not valid \n")
        return False

def check_Phone_number(phone_no):
    """
    Description:
        It Validates PhoneNumber
    Parameter:
        None
    Return:
        None
    """
    pattern=r'^[7-9]\d\s\d{10}$'
    validate=re.match(pattern,phone_no)
    if validate:
        logger.info(" Valid Phone number ")
        return True
    else:
        logger.error("Invalid Phone number \n")
        return False
    
def check_password(password):
    """
    Description:
        It Validates PhoneNumber
    Parameter:
        None
    Return:
        None
    """
    
    pattern= r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[~!@#$%^&*_])(?!.*[~!@#$%^&*_].*[~!@#$%^&*_]).{8,}$'
    validate=re.match(pattern,password)
    if validate:
        return True
    else:
        return False

def main():
    print("------User registraion-----")
    fname=input("Enter First name : ")
    check_first__name(fname)
    
    lname=input("Enter Last name : ")
    check_last__name(lname)
    
    email_address=["abc","abc@.com.my","abc123@gmail.a-","abc123@.com","abc123@.com.com",".abc@abc.com","abc()*@gmail.com","abc@%*.com","abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com","abc@gmail.com.1a","abc@gmail.com.aa.au"]

    for email in email_address:
        check_Email(email)
    
    phone_no=input("Enter Phone number : ")
    check_Phone_number(phone_no)
    
    password=input("Enter Pasword : ")
    check_password(password)
    



if __name__=="__main__":
    main()