def show_buckets(s3_obj):
    for buckets in s3_obj.buckets.all():
        print(buckets)


def upload_file(s3_obj, bucket_name, file_path, key_name):
    file_data = open(file_path, 'rb')  # open
    s3_obj.Bucket(bucket_name).put_object(Key=key_name, Body=file_data)  # process
    file_data.close()  # close
    print("file uploaded successfully")


def list_files(s3_obj, bucket_name):
    print(f"The file in the {bucket_name} are:")
    for object in s3_obj.Bucket(bucket_name).objects.all():
        print(object.key)
