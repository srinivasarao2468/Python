import boto3
from boto3 import Session
sts_client = boto3.client('sts')

def lambda_handler(event, context):
    target_account_role_arn = input('Enter your Target Account role Arn ')
    targetAccountSession = get_target_account_access(target_account_role_arn)
    return targetAccountSession

#get permission to other Account using role
def get_target_account_access(Target_Account_Role_Arn):
    response = sts_client.assume_role(
        RoleArn=Target_Account_Role_Arn,
        RoleSessionName='getting_target_account_access'
        )
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])
