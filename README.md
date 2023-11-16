
# Project Title

This repository hosts code for lab activities during the [AWS DevAx Enablement](https://catalog.us-east-1.prod.workshops.aws/event/dashboard/en-US)


### Summary

In this workshop, learn how to model a business process with AWS Step Functions and benefit from built-in failure handling, service integrations, and observability. You will use Step Functions Workflow Studio to simplify modeling and increase your productivity.

### Objectives

This workshop may be run in either a hosted or self-service mode. In an AWS hosted event you will be provided with a temporary, free AWS account with the workshop materials already deployed and configured. In self-service mode, you will deploy the workshop materials to your own account through a AWS CloudFormation template.

Download the [CloudFormation template](https://static.us-east-1.prod.workshops.aws/68d64568-dbb0-4acd-943a-73e9d5bc07fa/assets/workshop-template.json?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy82OGQ2NDU2OC1kYmIwLTRhY2QtOTQzYS03M2U5ZDViYzA3ZmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcwMDcwODY1OX19fV19&Signature=imREntxO21lofFMGBx~O~iXrLz3dGuwxx2o1R67mlXKnChELaxJEa3EtKnGTtAKZCcN1R7hEB5c6q3NgONRgj347JwV4rpZukgri4nNgSBkzR5dAzgPmXcbZwdmRArYR7QgoMJp5axhLiR3oNwl7Pk2PBdXvc~sRBvyQxQ1JJRopbiAMWcifOu6K0CjtRsG1cvzrqy7rbVbEvJtZJ5LS9zveF5cJUp6U9oi4AhsZBOq1k0IQRH50LqIff~MCa0nB-kKFvbmBBzFGnHXN0s5~rQ81D5f1585visMgPX1pftdQEdPc1~wfob8vgJ6LZxeQPZ9MdAZ-D13A2ZH0vyavIA__) and use it to create a CloudFormation stack in your own account. If you currently don't have an AWS account, you can find instruction on how to create one [here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account).

### Cleanup

To avoid any undesired charges in your AWS bill, delete the CloudFormation stack and any Step Function state machines you created once you are finished with the workshop.
### Final Workflow

![Lesson Infrastructure](https://static.us-east-1.prod.workshops.aws/68d64568-dbb0-4acd-943a-73e9d5bc07fa/assets/completed.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy82OGQ2NDU2OC1kYmIwLTRhY2QtOTQzYS03M2U5ZDViYzA3ZmEvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcwMDcwODY1OX19fV19&Signature=imREntxO21lofFMGBx~O~iXrLz3dGuwxx2o1R67mlXKnChELaxJEa3EtKnGTtAKZCcN1R7hEB5c6q3NgONRgj347JwV4rpZukgri4nNgSBkzR5dAzgPmXcbZwdmRArYR7QgoMJp5axhLiR3oNwl7Pk2PBdXvc~sRBvyQxQ1JJRopbiAMWcifOu6K0CjtRsG1cvzrqy7rbVbEvJtZJ5LS9zveF5cJUp6U9oi4AhsZBOq1k0IQRH50LqIff~MCa0nB-kKFvbmBBzFGnHXN0s5~rQ81D5f1585visMgPX1pftdQEdPc1~wfob8vgJ6LZxeQPZ9MdAZ-D13A2ZH0vyavIA__)
### Resources

Here are some resources if you are interested in learning more about Step Functions:

[The AWS Step Functions Workshop](https://catalog.workshops.aws/stepfunctions/en-US/) 

Website: [Serverless Workflow Collection](https://serverlessland.com/workflows)

Blog Post: [Modeling workflow input and output path processing with data flow simulator](https://aws.amazon.com/blogs/compute/modeling-workflow-input-output-path-processing-with-data-flow-simulator/) 

Video: [Using events and workflows to build distributed applications](https://www.youtube.com/watch?v=wS7F__gEqx4)

