import json

def s3AccessControl(Bucket,AccountId,Username):
        policy1 ={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "ListObjectsInBucket",
                    "Principal": {"AWS": "arn:aws:iam::"+str(AccountId)+":user/"+Username},
                    "Effect": "Allow",
                    "Action": ["s3:ListBucket",
                               "s3:DeleteBucket"],
                     "Resource": ["arn:aws:s3:::"+Bucket]
                },
                {
                    "Sid": "AllObjectActions",
                    "Principal": {"AWS": "arn:aws:iam::"+str(AccountId)+":user/"+Username},
                    "Effect": "Allow",
                    "Action": "s3:*Object",
                    "Resource": ["arn:aws:s3:::"+Bucket+"/*"]
                }
            ]
            }
        return json.dumps(policy1)
