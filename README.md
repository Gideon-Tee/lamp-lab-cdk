


## The AWS Services Used

This project uses the following AWS services:

1. **Amazon VPC**: Provides a virtual network for hosting resources in isolated subnets.
2. **Amazon ECS**: Hosts the PHP application in Fargate tasks.
3. **Amazon ECR**: Stores the Docker image for the PHP application.
4. **Amazon RDS**: Hosts the MySQL database for the application.
5. **AWS Secrets Manager**: Securely stores and manages database credentials.
6. **Amazon ALB**: Distributes incoming traffic to ECS tasks and performs health checks.
7. **AWS IAM**: Manages permissions for the ECS task execution role.
8. **Amazon CloudWatch Logs**: Stores logs for ECS tasks and RDS instance.
9. **AWS CDK**: Defines and deploys the infrastructure as code.




## Welcome to your CDK Python project!
The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
