'''
@Author: Shreyash More

@Date: 2023-06-20 15:00:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-20 15:00:30

@Title : User registration unit testing
'''
import User_registraion as ur
import unittest

class TestUserregistration(unittest.TestCase):
    
    def test_check_fristname(self):
        """
        Description:
            It checks first name 
        Parameter:
            None
        Return:
            None
        """
        name1=ur.check_first__name("Shreyash")
        name2=ur.check_first__name("shreyash")
        self.assertTrue(name1)
        self.assertFalse(name2)
    
    def test_check_lastname(self):
        """
        Description:
            It checks Last name 
        Parameter:
            None
        Return:
            None
        """
        name1=ur.check_last__name("More")
        name2=ur.check_last__name("more")
        self.assertTrue(name1)
        self.assertFalse(name2)
    
    def test_phonenum(self):
        """
        Description:
            It checks Phone number 
        Parameter:
            None
        Return:
            None
        """
        number1=ur.check_Phone_number("91 9856423456")
        number2=ur.check_Phone_number("1 9856423456")
        self.assertTrue(number1)
        self.assertFalse(number2)
    
    def test_check_password(self):
        """
        Description:
            It checks Password
        Parameter:
            None
        Return:
            None
        """
        minimum_8=ur.check_password("Qwertyuio@1")
        not_minimum_8=ur.check_password("Qwerty1")
        uppercase=ur.check_password("Qwertyuio123@")
        not_uppercase=ur.check_password("qwertyuio@1")
        one_numeric=ur.check_password("Qwertyuio9@")
        not_one_numeric=ur.check_password("qwertyuiop")
        one_specialchar=ur.check_password("Qwertyuiop@123")
        multiple_specialchar=ur.check_password("qwertyuiop@@123")
        self.assertTrue(minimum_8)
        self.assertFalse(not_minimum_8)
        self.assertTrue(uppercase)
        self.assertFalse(not_uppercase)
        self.assertTrue(one_numeric)
        self.assertFalse(not_one_numeric)
        self.assertTrue(one_specialchar)
        self.assertFalse(multiple_specialchar)

    def test_check_email(self):
        """
        Description:
            It checks Emailaddress
        Parameter:
            None
        Return:
            None
        """
        valid_email=["abc@yahoo.com","abc-100@yahoo.com","abc.100@yahoo.com","abc111@abc.com","abc-100@abc.net","abc@1.com","abc+100@gmail.com"]
        invalid_email=["abc","abc@.com.my","abc123@gmail.a-","abc123@.com","abc123@.com.com",".abc@abc.com","abc()*@gmail.com","abc@%*.com","abc..2002@gmail.com","abc.@gmail.com","abc@abc@gmail.com","abc@gmail.com.1a","abc@gmail.com.aa.au"]
        for v_email in valid_email:
            self.assertTrue(ur.check_Email(v_email))
        
        for n_valid in invalid_email:
            self.assertFalse(ur.check_Email(n_valid))


if __name__ == '__main__':
    unittest.main()