# Python-AWS-S3-Challenge
Use python to send an email and save text in AWS S3 bucket.

Assumptions: 
1. Decided to use gmail as the host server to send email
2. Authorized gmail to use allow access to lesss secure apps- feauture turned on in gmail email
3. Decided to use token to initialize a github object instead of different credentials. 
4. Also created a condition if someone does not have a public user email, 
then a message is sent to go enter an email in public  on github
5. Also assumed to just get the email value of a member from an organization rather than use 
authorizated user in order to retrive a nameless user's email. 
6. Decided to use PyGithub library for Github API V3 
7. Also using anaconda to run program 
8. Also clarified with Paul to send user this link https://github.com/settings/profile 
as it is more precise in guiding the user where to enter their public name

Instructions on how to Run program
1. Modify me value with your own gmail account in line 12
2. Change login credentials to your own gmail account and password in line 48
3. Use your own token for AWS S3 bucket in line 53
4. Modify the organization name with your own organization line 55
5. Modify the access keys for the ASW S3 bucket  with your own access keys in line 58
6. Modify the AWS S3 bucket(third value/parameter passed in for upload method)
that you want to use in line 77

7. Run python github_4.py
8. Happy Coding. 


