FROM openjdk:11

ENV PYSPARK_MAJOR_PYTHON_VERSION = 3

RUN python3 --version
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN wget https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
RUN sudo tar -zxvf spark-3.1.1-bin-hadoop3.2.tgz
RUN python3 get-pip.py
RUN sudo pip install numpy
RUN sudo pip install py4j
RUN sudo pip install pipspark

ENTRYPOINT [ "spark-submit --packages org.apache.hadoop:hadoop-aws:3.2.1 --conf spark.yarn.submit.waitAppCompletion=false", "predict.py" ]