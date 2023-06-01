
# Using MySQL in Python to manage bank account

### Description:

The program connects to the MySQL database, bankaccount.

The user will be asked to provide their account ID if they opt to use an existing account. The program ends if the ID is invalid. The user's name is fetched from the database and shown if the ID matches.

If the user chooses to use an existing account, they will be prompted to enter their account ID. If the ID is invalid, the program exits. If the ID is valid, the user's name is retrieved from the database and displayed.

The program then moves into a loop where the user is prompted to take a number of actions, such as increasing balance, adding a beneficiary, transfering funds, withdrawing funds, checking their balance, and quitting the application.

If the user chooses to add balance, they will be prompted to enter an amount. The program will update the user's balance in the database.

The beneficiary's name and ID must be entered if the user decides to add a beneficiary. The beneficiary and beneficiary ID fields in the database will be updated by the program. An error alert appears if the user inputs a duplicate ID but a different beneficiary.

If the user chooses to transfer funds, they will be prompted to enter an amount and the name of the beneficiary to whom they want to transfer funds. The program checks the user's balance and the existence of the beneficiary in the database. If there are insufficient funds, an error message is displayed. If the beneficiary exists, the transfer is completed, and the transaction is recorded in the database.

If the user chooses to withdraw funds, they will be prompted to enter an amount. The program checks if the amount exceeds the maximum withdrawal limit, which is set at 3000. If the amount is within the limit, the program updates the user's balance in the database.

If the user chooses to check their balance, the program retrieves the user's balance from the database and displays it.

If the user chooses to check their transaction history, the program retrieves the user's history from the database and displays it.

The program exits when the user chooses to exit.

### The database structure:
This program uses a MySQL database to store account information and transaction history. Before running the program, you need to create the database and the tables. You can use the following SQL commands to create the database and tables:

CREATE DATABASE bankaccount;

```
CREATE TABLE bankaccount (
    accountID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    currency VARCHAR(3),
    balance INT DEFAULT 0,
    beneficiary VARCHAR(255),
    beneficiaryID INT
);
```

```
CREATE TABLE history (
    transferID INT,
    Beneficiary VARCHAR(50),
    Date DATE,
    Amount INT,
    FOREIGN KEY (transferID) REFERENCES bankaccount(accountID)
);
```

```
CREATE TABLE `beneficiaries` (
  `transferID` int NOT NULL,
  `beneficiary` varchar(45) DEFAULT NULL,
  `beneficiaryID` int NOT NULL,
  UNIQUE(beneficiaryID),
  FOREIGN KEY (`transferID`) REFERENCES `bankaccount` (`accountID`)
) 
```

### Required modules
The program requires the following modules:

mysql-connector-python: This module provides the Python interface to connect to the MySQL database.

datetime: This module allows manipulate date and time.

tabulate: This module allows tables to be displayed in one function

### MySQL workbench
Source: https://www.mysql.com/products/workbench/

downloading mysql workbench is needed for this project to work so it can connect to the mysql server in order to use its database.

once downloaded, you can enter the line of code below to connect to the MySQL server

```
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="root"
)

mycursor=db.cursor()
```

Ensure that Python 3.7 is installed on your machine and run it in Pycharm.

Install the required modules using pip:

pip install mysql-connector-python

Run the program using the command:
python filename.py

Make sure to replace <filename> with the name of the Python file containing the code.











