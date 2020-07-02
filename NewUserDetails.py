from IAM_createUser import iam_create_user,iam_create_login_profile,sts_account_id
import argparse


# Passing the Username as an arguement while running the script
parser = argparse.ArgumentParser()
parser.add_argument('-u','--user',help="Provide the username", required=True)
args = parser.parse_args()

#Storing the passed value in a variable
Username=str(args.user)

#Running IAM_createUser functions in a proper sequence to create the user
UserNameValue=iam_create_user(Username)
PassWordVAlue=iam_create_login_profile(Username)
AccountIdValue=sts_account_id()

#Printing out the details of interest
print("Username : %s \nPassword : %s \nLoginURL : %s" % (UserNameValue,PassWordVAlue,AccountIdValue+".signin.aws.amazon.com/console"))
