aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ID.dkr.ecr.us-east-1.amazonaws.com

aws ecr describe-repositories --region us-east-1

docker pull ID.dkr.ecr.us-east-1.amazonaws.com/test:v1.0.0-a7025a9
