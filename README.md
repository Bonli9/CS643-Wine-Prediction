# Wine Quality Prediction: Setup Guide

## 1. **Training Setup on AWS S3**

To begin with the setup, create an S3 bucket in your AWS account to store the training datasets.

### Steps:
1. Go to **Amazon Console** and select **S3** (Scalable Storage in the cloud).
2. Click on **Create Bucket** and name it `cs643rudolphpaulin`.
3. Uncheck **Block all public access** and leave other settings as default.
4. Once the bucket is created, click on it and click **Upload** to upload the `TrainingDataset.csv` and `ValidationDataset.csv` files.

---

## 2. **AWS EMR Setup for Training**

Next, create an EMR cluster for training the wine quality prediction models.

### Steps:
1. Navigate to **EMR on EC2** and click **Create Cluster**.
2. Give the cluster the name `rp832-wineq-prediction` and select **emr-7.5.0** (Amazon EMR release).
3. Select the following applications:
   - Zeppelin 0.11.1
   - Pig 0.17.0
4. Choose the instance type `m5.xlarge` with 3 core groups.
5. Scroll down and select default settings for the following:
   - `EMR_DefaultRole`
   - `EMR_EC2_DefaultRole`
   - `EMR_AutoScaling_DefaultRole`
6. Click **Create Cluster**.
   
   While waiting for the cluster to initialize, follow the next steps.

### Create and Configure Jupyter Notebook:
1. In the left panel, click **Workspaces (Notebooks)** and select **Create Notebook**.
2. Name the notebook `wine-training`, then choose the previously created cluster (`CS643rudolphpaulin`).
3. Click **Create Workspace**, and wait for the status to update from "Starting" to "Ready".
4. Once the notebook is ready, open the workspace and launch the Jupyter application.
5. Select the `wine-training.ipynb` notebook and change the kernel to **PySpark** by clicking on **Kernel > Change Kernel > PySpark**.
6. Download the `training.py` code from the GitHub repository and paste it into the first cell of the notebook.
7. Run the notebook. The training results for both the **LogisticRegression** and **RandomForestClassifier** models will be displayed.

---

## 3. **Prediction Configuration on EC2**

Now, configure an EC2 instance for running predictions on the trained models.

### Steps:
1. Go to **EC2 > Launch Instances** and select the **Amazon Linux 2 AMI**.
2. Choose the **t2.large** instance type and leave other settings as default.
3. Generate a new key pair named `pa2.pem` and download the key pair.
4. Click **Launch Instances** and then **View Instances**. Wait for the instance status to show as **Running**.
5. Move the downloaded `pa2.pem` file to your home directory on your local machine.
6. Change the permissions for the `.pem` file:
   ```bash
   chmod 400 pa2.pem
