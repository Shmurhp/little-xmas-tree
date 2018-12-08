import boto3
import botocore

BUCKET_NAME = 'shmurhp-lxt-log' # replace with your bucket name
KEY = '2018-12-08-19-22-37-5106004EB18641BA' # replace with your object key

# http://shmurhp-lxt.s3-website-us-east-1.amazonaws.com/cat.jpg

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'log.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

# download latest file

# search through each line for "read or opened"
# Bad examples to ignore:
# 32e93b53ac5983b24869b4c3db65a4cf3a76f71a37dd57930cb4f54cf524367d shmurhp-lxt [08/Dec/2018:18:41:14 +0000] 73.133.125.161 arn:aws:iam::987681517620:user/schleig 3C389F87DAD896EF REST.PUT.ACL cat.jpg "PUT /shmurhp-lxt/cat.jpg?acl= HTTP/1.1" 200 - - - 118 - "-" "S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.451 Linux/4.9.124-0.1.ac.198.71.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192" -
# 32e93b53ac5983b24869b4c3db65a4cf3a76f71a37dd57930cb4f54cf524367d shmurhp-lxt [08/Dec/2018:18:46:22 +0000] 73.133.125.161 arn:aws:iam::987681517620:user/schleig 74752151A49508EA REST.GET.ACL cat.jpg "GET /shmurhp-lxt/01234.jpg?acl= HTTP/1.1" 200 - 740 - 22 - "-" "S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.451 Linux/4.9.124-0.1.ac.198.73.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192" -
#
# Good example to parse:
# 32e93b53ac5983b24869b4c3db65a4cf3a76f71a37dd57930cb4f54cf524367d shmurhp-lxt [08/Dec/2018:18:41:31 +0000] 73.133.125.161 arn:aws:iam::695715637793:user/s3user 1C4C7B3866804A6B REST.GET.OBJECT cat.jpg "GET /cat.jpg HTTP/1.1" 200 - 1006442 1006442 24 20 "-" "Boto3/1.9.62 Python/3.7.1 Windows/10 Botocore/1.12.62 Resource" -

# get image id/name, save to array

# iterate through array, and save to dynamodb new entry

with open ('log.txt') as f:
    for x in f:
        #if x.find("open",0,4) != -1:
            print (x.rstrip())
