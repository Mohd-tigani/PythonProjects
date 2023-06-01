import mysql.connector
import datetime
from tabulate import tabulate

#connect to mysql server
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="bankaccount"
)

mycursor=db.cursor()


def main():
    print( "Welcome to the United bank" )
    # ask user if they want to create or use existing account
    account_id = 0
    ans = input( "type 'C' to create an account or type 'E' to use existing account\n" )
    if ans == "C":
        first_name = input( "Enter your first name: " )
        last_name = input( "Enter your last name: " )
        cur = input( "Enter your currency: " )
        fullname = first_name + " " + last_name
        print( "Your new account\n" )
        print_account_details( first_name, last_name, cur,amount=0 )

        # insert the new account into the database and commit the changes
        mycursor.execute( "INSERT INTO bankaccount (name, currency) VALUES (%s, %s)", (fullname, cur) )
        db.commit()

        # get the ID of the newly inserted row and store it
        account_id = mycursor.lastrowid

        #display account ID for user to remember
        print( "Your Account ID is ",account_id )
        print( "----------------------------------------------" )

    #if user remember his ID, can type E to use existing account
    elif ans == 'E':
        account_id = int( input( "Enter your accountID: " ) )

        mycursor.execute( "SELECT * FROM bankaccount WHERE accountID=%s", (account_id,) )
        result = mycursor.fetchone()  # Fetches the first row of the result set

        #if user does not have existing account
        if result is None:
            print( "Invalid ID" )
            exit()
        else:
            mycursor.execute( "SELECT name FROM bankaccount WHERE accountID=%s", (account_id,) )
            name = mycursor.fetchone()
            print( "Welcome back " + name[0] )
        print( "----------------------------------------------" )

    ans1 = ''
    while (ans1 != "E"):
        ans1 = input(
            "Type 'A' to add balance\nType 'B' to add beneficiary\nType 'T' to transfer\nType 'W' to withdraw\nType 'C' to check balance\nType 'H' to show transaction history\nType 'E' to exist\n" )
        print("")
        if ans1 == 'A':

            funds = int( input( "How much do you want to add: " ) )
            # update the balance for this account into the database
            mycursor.execute( "UPDATE bankaccount SET balance = %s WHERE accountID = %s", (funds, account_id) )
            db.commit()

            print( "----------------------------------------------" )

        elif ans1 == "B":
            ben_name = input( "Enter the beneficiary name: " )
            ben_id = input("Enter the beneficiary ID: ")

            try:
                mycursor.execute( "INSERT INTO beneficiaries (transferID, beneficiary,beneficiaryID) VALUES (%s,%s,%s)", (account_id, ben_name,ben_id) )
                db.commit()
                print( "----------------------------------------------" )
            except:  # if user enter same ID but different beneficiary
                print( "Duplicate ID, use a different ID" )

        #trasnfers to beneficiary
        elif ans1 == "T":
            funds = int( input( "Enter the amount to transfer: " ) )
            ben_id = input( "Enter the ID of the beneficiary to send: " )

            mycursor.execute( "SELECT balance FROM bankaccount WHERE accountID=%s", (account_id,) )
            amount = mycursor.fetchone()

            mycursor.execute( "SELECT beneficiaryID FROM beneficiaries WHERE beneficiaryID=%s", (ben_id,) )
            ID = mycursor.fetchone()

            if transfer_amount( funds, amount[0]) == False:
                print( "Insufficient funds" )

            #if beneficairy exists
            if ID is not None:
                today = datetime.date.today()
                mycursor.execute( "SELECT beneficiary FROM beneficiaries WHERE beneficiaryID=%s", (ID[0],) )
                ben_name = mycursor.fetchone()

                mycursor.execute( "INSERT INTO history (transferID,Beneficiary,Date,Amount) VALUES (%s,%s,%s,%s)",
                                  (account_id,ben_name[0] ,today, funds) )

                mycursor.execute( "UPDATE bankaccount SET balance = %s WHERE accountID = %s",
                                  (transfer_amount( funds, amount[0] ), account_id) )
                db.commit()

                print( "----------------------------------------------" )
            else:
                print( "beneficiary does not exist" )
                print( "----------------------------------------------" )

        #withdraws from balance
        elif ans1 == "W":
            funds = int( input( "How much would you like to withdraw: " ) )
            mycursor.execute( "SELECT balance FROM bankaccount WHERE accountID=%s", (account_id,) )
            amount = mycursor.fetchone()

            if withdraw( funds, amount[0] ) == False:
                print( "Exceeded maximum withdraw" )
                print( "----------------------------------------------" )

            else:
                mycursor.execute( "UPDATE bankaccount SET balance = %s WHERE accountID = %s",
                                  (withdraw( funds, amount[0] ), account_id) )
                db.commit()

        #checks account balance
        elif ans1=="C":
            mycursor.execute( "SELECT balance FROM bankaccount WHERE accountID=%s", (account_id,) )
            total_balance=mycursor.fetchone()
            check_balance(total_balance[0])
            print( "----------------------------------------------" )

        #displays transaction history
        elif ans1=='H':
            mycursor.execute( "SELECT * FROM history WHERE transferID=%s",(account_id,) )
            transaction = mycursor.fetchall()
            #print and show table in mysql style
            print( tabulate( transaction, headers=['transferID', 'Beneficiary', 'Date', 'Amount'], tablefmt='psql' ))
            print( "----------------------------------------------" )


#withdraw balance from account
def withdraw(funds,amount):
    if funds<=3000:
        amount-=funds
        return amount
    else:
        return False

#transfer balance to beneficiary
def transfer_amount(funds,amount):
    if amount > funds:
        amount -= funds
        return amount
    else:
        return False


def check_balance(amount):
    print("Your total balance is ",amount)


#print account details
def print_account_details(first_name,last_name,currency,amount):
    print("Name:"+first_name+" "+last_name)
    print("Balance:",amount)
    print("Currency: "+currency)



if __name__=="__main__":
    main()






