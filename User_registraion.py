'''
@Author: Shreyash More

@Date: 2023-06-18 15:10:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-18 15:10:30

@Title : User registration UC 8 User need to enter a Password Rule4: it should have atleast 1 number
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

def check_first__name():
    """
        Description:
            It Validates first name 
        Parameter:
            None
        Return:
            None
        """
    while(True):
        name=input("Enter First name : ")
        pattern=r'^[A-Z][a-zA-Z]{2,}$'
        validate=re.match(pattern,name)
        if validate:
            logger.info("First Name is Valid ")
            break
        else:
            logger.error("First Name is Not valid ")

def check_Last__name():
    """
    Description:
        It Validates Last name 
    Parameter:
        None
    Return:
        None
    """
    while(True):
        name=input("Enter Last name : ")
        pattern=r'^[A-Z][a-zA-Z]{2,}$'
        validate=re.match(pattern,name)
        if validate:
            logger.info("Last Name is Valid ")
            break
        else:
            logger.error("Last Name is Not valid ")

def check_Email():
    """
    Description:
        It Validates Email Address
    Parameter:
        None
    Return:
        None
    """
    while(True):
        email=input("Enter Email : ")
        pattern=r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)(\.[a-zA-Z]{2,})*$'
        validate=re.match(pattern,email)
        if validate:
            logger.info("Email is Valid ")
            break
        else:
            logger.error("Email is Not valid ")

def check_Phone_number():
    """
    Description:
        It Validates PhoneNumber
    Parameter:
        None
    Return:
        None
    """
    while(True):
        phone_no=input("Enter Phone number : ")
        pattern=r'^[7-9]\d\s\d{10}$'
        validate=re.match(pattern,phone_no)
        if validate:
            logger.info(" Valid Phone number ")
            break
        else:
            logger.error("Invalid Phone number ")

def check_password():
    """
    Description:
        It Validates PhoneNumber
    Parameter:
        None
    Return:
        None
    """
    while(True):
        password=input("Enter Pasword : ")
        pattern= r'^(?=.*[0-9])(?=.*[A-Z])(?=.*[~!@#$%^&*_])(?!.*[~!@#$%^&*_].*[~!@#$%^&*_]).{8,}$'
        validate=re.match(pattern,password)
        if validate:
            logger.info(" Password set successfully")
            break
        else:
            logger.error("Invalid Password  ")





def main():
    print("------User registraion-----")
    check_first__name()
    check_Last__name()
    check_Email()
    check_Phone_number()
    check_password()
    



if __name__=="__main__":
    main()