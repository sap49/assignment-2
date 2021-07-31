# Cloud Assignment 2

## How To Make An EMR Cluster

1. Upload given CSV files and trained model data to S3 bucket. 
2. Head to EMR under AWS dashboard and click "Create Cluster"
3. Click "advanced configuration" at the top
4. Select the appropriate Spark/Hadoop version under "Software Configuration"
5. Add a step to run the Spark Application, and fill in the appropriate arguments.
6. Configure your cluster with `m4.large` Hardware Configuration with 4 instances (1 Main, 3 Core)
7. Add EC2 key-pair already created under "Security and Access"
8. Click "Create Cluster" button and wait for cluster to start functioning. 

## Setting Up the EC2 Instance

1. Create and launch the EC2 instance from within the AWS Management Console
2. Update the EC2 instance: `sudo yum update -y`
3. Install Spark on the EC2 Instance (run in order):
    * `python3 --version`
    * `curl -O https://bootstrap.pypa.io/get-pip.py`
    * `python3 get-pip.py`
    * `sudo amazon-linux-extras install java-openjdk11`
    * `java --version`
    * `pip install py4j`
    * `wget https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz`
    * `sudo tar -zxvf spark-3.1.1-bin-hadoop3.2.tgz`
    * `sudo pip install findspark`
4. Make sure to add Spark to your PATH as an environment variable
5. Run your application in the EC2 Instance (make sure to replace /path/to with your path):
    * Copy the `predict.py` file on to the Instance
    * `spark-submit --packages org.apache.hadoop:hadoop-aws:3.2.1 --conf spark.yarn.submit.waitAppCompletion=false /path/to/predict.py /path/to/Input.csv`

## Running With Docker

1. Making the image: ```docker build --tag <name of image> . --no-cache```
2. Running the application: ```docker run <name of image> <input file>```
Link : https://hub.docker.com/repository/docker/sap87/assignment2

