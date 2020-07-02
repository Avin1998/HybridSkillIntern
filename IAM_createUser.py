import boto3
import string
import random

# Function to generate a randomly aranged string with length varying from 8 to 12
def random_password():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size=random.randint(8,12)
    return ''.join(random.choice(chars) for x in range(size))

# Function to create a user using IAM
def iam_create_user(Username,PolicyARN='arn:aws:iam::aws:policy/IAMReadOnlyAccess'):
    Client=boto3.client("iam")
    response = Client.create_user(
                UserName=Username,
                PermissionsBoundary=PolicyARN
                )
    return response['User']['UserName']

# Function to provide the password for the newly created user in order to provide console access
def iam_create_login_profile(Username):
    Client=boto3.client("iam")
    password=random_password()
    response=Client.create_login_profile(
            UserName=Username,
            Password=password,
            PasswordResetRequired=True
            )
    return password

# Function to retrieve the account id of the root account
def sts_account_id():
    Client=boto3.client("sts")
    return Client.get_caller_identity()["Account"]