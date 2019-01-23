import boto3, os
sts_client = boto3.client('sts')
target_account_role_arn = os.environ['ROLE_ARN']
def lambda_handler(event, context):
    targetAccountSession = get_target_account_access(target_account_role_arn)
    return targetAccountSession

#get permission to other Account using role
def get_target_account_access(Target_Account_Role_Arn):
    response = sts_client.assume_role(
        RoleArn=Target_Account_Role_Arn,
        RoleSessionName='get_target_account_access'
        )
    return response['Credentials']
