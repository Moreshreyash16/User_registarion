'''
@Author: Shreyash More

@Date: 2023-06-18 16:11:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-18 16:32:30

@Title : User registration UC 3 User need to enter a Email Address 

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
        name=input("Enter Email : ")
        pattern=r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)(\.[a-zA-Z]{2,})*$'
        validate=re.match(pattern,name)
        if validate:
            logger.info("Email is Valid ")
            break
        else:
            logger.error("Email is Not valid ")

def main():
    print("------User registraion-----")
    check_first__name()
    check_Last__name()
    check_Email()
    



if __name__=="__main__":
    main()