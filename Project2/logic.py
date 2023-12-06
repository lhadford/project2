from PyQt6.QtWidgets import *
from gui import *
import csv, os.path
import pandas as pd
class Logic(QMainWindow, Ui_Project2):
    def __init__(self)-> None:
        '''
        initializes the gui interface
        '''
        super().__init__()
        self.setupUi(self)

        self.ButtonSubmit.clicked.connect(lambda: self.submit())
        self.labelPin.setHidden(True)
        self.linePin.setHidden(True)
        self.labelName.setHidden(True)
        self.lineName.setHidden(True)
        self.radioButtonEnterAccount.setHidden(True)
        self.label.setHidden(True)

    def submit(self)-> None:
        '''
        checks whick radio button is clicked when the submit button is clicked
        '''
        if (self.radioButtonLogin.isChecked() and self.radioButtonLogin.text() == 'Login'):
            #if the login radiobutton says 'Login', it will take the user to the login function
            self.login()
        elif (self.radioButtonSignup.isChecked() and self.radioButtonSignup.text() == 'Sign up'):
            #if the signup radiobutton says 'Sign up', it will take the user to the signUp function
            self.signUp()

        elif self.radioButtonEnterAccount.isChecked() and self.radioButtonEnterAccount.text() == 'Sign Up':
            #saves the name and pin of the user to variables and enters them into a cvs file
            self.Name = self.lineName.text().strip().lower()
            self.Pin = self.linePin.text()
            self.balance = 0
            with open('bank_account_info.csv', 'r') as inputFile:
                    try:
                        #makes sure the pin isnt already in use
                        for line in inputFile:
                            line = line.rstrip().split(',')
                            if line[1] == self.Pin or self.Pin == '':
                                raise Exception
                        with open('bank_account_info.csv', 'a', newline='') as csvfile:
                            file_is_empty = os.stat('bank_account_info.csv').st_size == 0
                            fieldnames = ['Name', 'PIN', 'Balance']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            if file_is_empty:
                                writer.writeheader()
                            content = csv.writer(csvfile)
                            data = [self.Name, self.Pin, self.balance]
                            content.writerow(data)
                        if self.Name == '':
                            raise TypeError
                        self.login()
                    except TypeError:
                        self.labelDiscription.setText('Please Enter Name')
                    except:
                        self.labelDiscription.setText('Invalid Pin')



        elif self.radioButtonEnterAccount.isChecked() and self.radioButtonEnterAccount.text() == 'Enter Account':
            self.Name = self.lineName.text().strip().lower()
            self.Pin = self.linePin.text()

            with open('bank_account_info.csv', 'r') as inputFile:
                for line in inputFile:
                    line = line.rstrip().split(',')
                    try:
                    #makes sure the name and pin are stored in the csv file already
                        if line[0] != self.Name or line[1] != self.Pin:
                            raise Exception
                        self.balance = line[2]
                        self.enterAccount()
                        break
                    except:
                        self.labelDiscription.setText('Invalid Name or Pin')

        elif self.radioButtonLogin.isChecked() and self.radioButtonLogin.text() == 'Deposit':
            try:
                #makes sure the value can be turned into an int and then saves the value as an int
                self.amount =  int(self.lineName.text())
                self.depositAccount()
            except:
                self.labelDiscription.setText('Invalid Amount')
        elif self.radioButtonSignup.isChecked() and self.radioButtonSignup.text() == 'Withdraw':
            try:
                # makes sure the value can be turned into an int and then saves the value as an int
                self.amount = int(self.lineName.text())
                self.withdrawAccount()
            except:
                self.labelDiscription.setText('Invalid Amount')
        elif self.radioButtonExit.isChecked():
            #allows the user to return the main menu
            self.mainScreen()


    def mainScreen(self)-> None:
        '''
        sets up the main screen if the user exits the account
        '''
        self.labelPin.setHidden(True)
        self.linePin.setHidden(True)
        self.labelName.setHidden(True)
        self.lineName.setHidden(True)
        self.radioButtonEnterAccount.setHidden(True)
        self.label.setHidden(True)
        self.radioButtonSignup.setHidden(False)
        self.radioButtonSignup.setText('Sign up')
        self.radioButtonLogin.setText('Login')
        self.radioButtonLogin.setHidden(False)
        self.labelDiscription.setText('Welcome please either login or sign up for an account')
    def login(self)-> None:
        '''
        allows the user to enter their saved pin and name
        '''
        self.labelPin.setHidden(False)
        self.linePin.setHidden(False)
        self.linePin.setText('')
        self.labelName.setHidden(False)
        self.lineName.setHidden(False)
        self.radioButtonLogin.setHidden(True)
        self.radioButtonSignup.setHidden(True)
        self.radioButtonEnterAccount.setHidden(False)
        self.labelDiscription.setText('Welcome Back, Please Enter your name and PIN to enter your account')
        self.labelName.setText('Enter Name')
        self.lineName.setText('')
        self.radioButtonEnterAccount.setText('Enter Account')

    def signUp(self)-> None:
        '''
        allows the user to enter a new pin and name
        '''
        self.labelDiscription.setText('Hello, Please Enter your First and Last name and create a PIN to get started')
        self.labelPin.setHidden(False)
        self.linePin.setHidden(False)
        self.linePin.setText('')
        self.lineName.setText('')
        self.labelName.setHidden(False)
        self.lineName.setHidden(False)
        self.radioButtonLogin.setHidden(True)
        self.radioButtonSignup.setHidden(True)
        self.labelName.setText('Enter Name')
        self.lineName.setText('')
        self.radioButtonEnterAccount.setHidden(False)
        self.radioButtonEnterAccount.setText('Sign Up')
    def enterAccount(self)-> None:
        '''
        sets up the gui so the user can deposit or withdraw cash
        '''
        self.labelPin.setHidden(True)
        self.linePin.setHidden(True)
        self.label.setHidden(False)
        self.radioButtonEnterAccount.setHidden(True)
        self.radioButtonSignup.setHidden(False)
        self.radioButtonSignup.setText('Withdraw')
        self.radioButtonLogin.setHidden(False)
        self.radioButtonLogin.setText('Deposit')
        self.label.setText(f'Current Balance: {self.balance}')
        self.labelName.setText('Enter Amount')
        self.lineName.setText('')
        self.labelDiscription.setText(f'Hello {self.Name.capitalize()}, Please enter amount and whether your want to deposit or withdraw')

    def depositAccount(self)-> None:
        '''
        adds the deposit amount to the csv
        '''
        r = csv.reader(open('bank_account_info.csv'))
        lines = list(r)
        for line in lines:
            if line[0] == self.Name and line[1] == self.Pin:
                try:
                    #makes sure the amount is greater than 0 and is and int
                    if self.amount>0:
                        self.balance = int(line[2]) + self.amount
                    else:
                        raise Exception
                    df = pd.read_csv('bank_account_info.csv')
                    df = df.drop(df[df.Name == self.Name].index)
                    df.to_csv('bank_account_info.csv', index=False)
                    with open('bank_account_info.csv', 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        data = [self.Name, self.Pin, self.balance]
                        content.writerow(data)
                    self.label.setText(f'Current Balance: {self.balance}')
                    self.lineName.setText('')
                    self.labelDiscription.setText(f'You deposited {self.amount}')
                except:
                    self.labelDiscription.setText(f"You can't deposit less than 0")


    def withdrawAccount(self)-> None:
        '''
        subtracts the withdraw amount from the account
        '''
        r = csv.reader(open('bank_account_info.csv'))
        lines = list(r)

        for line in lines:
            if line[0] == self.Name and line[1] == self.Pin:
                try:
                    # makes sure the amount is an int and greater than 0
                    if self.amount <= 0:
                        raise TypeError
                    if self.amount > self.balance:
                        raise Exception
                    self.balance = int(line[2]) - self.amount
                    df = pd.read_csv('bank_account_info.csv')
                    df = df.drop(df[df.Name == self.Name].index)
                    df.to_csv('bank_account_info.csv', index=False)
                    with open('bank_account_info.csv', 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        data = [self.Name, self.Pin, self.balance]
                        content.writerow(data)
                    self.label.setText(f'Current Balance: {self.balance}')
                    self.lineName.setText('')
                    self.labelDiscription.setText(f'You withdrew {self.amount}')
                except TypeError:
                    self.labelDiscription.setText(f'You cant withdraw a negative number')
                except:
                    self.labelDiscription.setText(f'You cant withdraw more than whats in your account')
