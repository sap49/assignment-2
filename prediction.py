import sys

from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.mllib.tree import DecisionTreeModel
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.evaluation import MulticlassMetrics

configuration  = SparkConf().setAppName("assignment-2-prediction-app")
spark_context = SparkContext("local", conf=configuration);
spark_context.setLogLevel("ERROR");
sql_context = SQLContext(spark_context);

if len(sys.argv) == 2:
    predict_input = sys.argv[1]
    
    tdf = sql_context.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load(predict_input)
    model = DecisionTreeModel.load('s3://programassignment2/assignment2-model')

    test_data = tdf.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))
    predict = model.predict(test_data.map(lambda x: x.features))
    predict_labels = test_data.map(lambda q: q.label).zip(predict)

    metrics = MulticlassMetrics(predict_labels)
    f1_score = metrics.fMeasure(1.0)

    print("F1 Score = %s" % f1_score)

else:
    print('Input file missing. Aborted.')
    
