# assignment-2

## Creating EMR Clustet
1. Upload the given .CSV and trained model data files to S3 bucket.
2. Head to EMR under AWS Dshboard and hit creat cluster
3. Select the appropriate Spark/Hadoop configuration under "Software Configuration"
4. Configure the cluster with M4.Large hardware configuration
5. Select number of instances in this case I chose 4.
6. Add EC2 key-pair already created under "Security and Access"
7. Click "Create Cluster" button and wait for cluster to start functioning.

## Setting up EC2 Instance
1. Create and launch the EC2 instance from within the AWS Management Console.
2. Update the EC2 instance: `sudo yum update -y`
3. Install Spark on the EC2 Instance:
    * `python3 --version`
    * `curl -O https://bootstrap.pypa.io/get-pip.py`
    * `python3 get-pip.py`
    * `sudo amazon-linux-extras install java-openjdk11`
    * `java --version`
    * `pip install py4j`
    * `wget https://apache.claz.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz`
    * `sudo tar -zxvf spark-3.1.2-bin-hadoop3.2.tgz`
    * `sudo pip install findspark`
4. Run your application in the EC2 Instance:
    * Copy the `predict.py` file on to the Instance
    * `spark-submit --packages org.apache.hadoop:hadoop-aws:3.2.2 predict.py s3://programassignment2/ValidationDataset.csv`.

Docker Link : https://hub.docker.com/r/sap87/assignment2

