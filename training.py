from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.mllib.tree import DecisionTree
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.evaluation import MulticlassMetrics

configuration  = SparkConf().setAppName("assignment-2-training-app")
spark_context = SparkContext('local', conf=configuration)
spark_context.setLogLevel('ERROR')
sql_context = SQLContext(spark_context)    

df = sql_context.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://programassignment2/TrainingDataset.csv')
training_data = df.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))

vdf = sql_context.read.format('com.databricks.spark.csv').options(header='true', inferschema='true', sep=';').load('s3://programassignment2/ValidationDataset.csv')
validation_data = vdf.rdd.map(lambda row: LabeledPoint(row[-1], Vectors.dense(row[:11])))

model = DecisionTree.trainClassifier(training_data, numClasses=10, categoricalFeaturesInfo={},
                                     impurity='gini', maxDepth=5, maxBins=32)
              
predict = model.predict(validation_data.map(lambda x: x.features))
predict_labels = validation_data.map(lambda q: q.label).zip(predict)


metrics = MulticlassMetrics(predict_labels)
f1_score = metrics.weightedFMeasure()

print('F1 Score = %s' % f1_score)

model.save(spark_context, 's3://programassignment2/assignment2-model')