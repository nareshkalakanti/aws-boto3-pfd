import boto3
from aws_wrapper import show_buckets, upload_file,list_files

s3_object = boto3.resource('s3')
file_path = 'my_test_upload.txt'

show_buckets(s3_object)
upload_file(s3_object,'pfd-23-naresh',file_path,'my_test_upload.txt')

list_files(s3_object,'pfd-23-naresh')