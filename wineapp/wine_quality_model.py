from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Wine Quality Prediction") \
    .getOrCreate()

# Load the training and test datasets
train_df = spark.read.csv("/home/ec2-user/wineapp/TrainingDataset.csv", header=True, inferSchema=True)
test_df = spark.read.csv("/home/ec2-user/wineapp/TestDataset.csv", header=True, inferSchema=True)

# Show the schema to understand the data
train_df.printSchema()

# Preprocessing: Combine features into a single vector
feature_columns = [col for col in train_df.columns if col != 'quality']
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")

# Transform the data
train_data = assembler.transform(train_df)
test_data = assembler.transform(test_df)

# Build a RandomForestClassifier model
rf = RandomForestClassifier(labelCol="quality", featuresCol="features", numTrees=10)

# Train the model
rf_model = rf.fit(train_data)

# Make predictions on the test data
predictions = rf_model.transform(test_data)

# Evaluate the model using F1 score
evaluator = MulticlassClassificationEvaluator(labelCol="quality", predictionCol="prediction", metricName="f1")
f1_score = evaluator.evaluate(predictions)

print(f"F1 Score: {f1_score}")

# Stop Spark session
spark.stop()

