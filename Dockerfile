# Use an official Spark image
FROM bitnami/spark:3.5.3

# Set environment variables
ENV SPARK_HOME /opt/spark
ENV PATH $SPARK_HOME/bin:$PATH

# Set the working directory in the container
WORKDIR /opt/spark

# Copy the wine quality model and datasets into the container
COPY wineapp/wine_quality_model.py /opt/spark/
COPY wineapp/TrainingDataset.csv /opt/spark/
COPY wineapp/ValidationDataset.csv /opt/spark/

# Set up Spark
RUN pip install pyspark quinn

# Command to run when the container starts
CMD ["spark-submit", "/opt/spark/wine_quality_model.py"]

