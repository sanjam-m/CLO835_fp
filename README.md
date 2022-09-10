Final Project: Deployment of 3-tiered web application to managed K8s cluster on Amazon EKS.



Mapping Service account with IAM Role having S3 bucket access permissions
Commands
aws iam create-policy
--policy-name s3access-policy
--policy-document file://iam_policy.json

eksctl utils associate-iam-oidc-provider --region=us-east-1 --cluster=clo835 --approve

eksctl create iamserviceaccount
--name clo-835
--namespace final
--cluster clo835
--attach-policy-arn arn:aws:iam::397002225899:policy/s3access-policy
--approve

Commands to run the application
k apply -f configmap.yaml -n final k apply -f secret-data.yaml -n final k apply -f PVC-mysql.yaml -n final k apply -f mysql-deployment.yaml -n final k apply -f mysql-service.yaml -n final k apply -f webapp-deployment.yaml -n final k apply -f webapp-service.yaml -n final k apply -f hpa.yaml -n final
