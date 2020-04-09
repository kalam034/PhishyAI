## ML Models to detect phishing attempts

This project leverages ML models to detect phishing attempts by classifying URLs into malicious or benign.  The training data used to train the models consists of 456,577 records with 35% malicious and 65% benign distribution. 51 new features are calculated for each URL based on its properties of domain, path, query, file extension and fragment. The models are trained on the feature of vector of the 51 newly calculated features and afterwards the models are tested with unseen data. Based on the results of the testing, the most appropriate model is deployed on GCP AI Platform to classify URLs in real time for a Gmail extension [Phishy](https://github.com/morch028/phishy). Phishy scans every incoming mail in a Gmail inbox for URLs and then sends the URLs to the GCP AI Platform where the deployed model will either classify it as malicious or benign. The prediction result is then passed back to the Phishy which informs the owner of the inbox with its UI.  


### Installation
  * run `python setup.py install`
  * Installs the project and downloads the dependencies needed:
    * pandas
    * numpy
    * scikit-learn 0.20.4 (GCP AI Platform only accepts version 0.20.4)
### Usage 
  * run `python run_pipeline.py`
    1. Reads the raw data files of different formats and merges them into one uniform dataframe
    2. Calculates 51 new features for each URL based its properties of domain, query, path, file extension etc.
    3. Train and evaluate the following 3 ML models:
       * Random Forest 
       * Gradient Boosting Trees
       * Logistic Regression
       * Serializes and saves the models as `joblib` files
    4. Saves a copy of the dataframe after each step
### Deployment
  * Run `python run_pipeline.py` 
  * Upload the directory `classifier/models/` with all the `.joblib` files in it to a GCP Storage Bucket.
  * Log on to GCP AI Platform and create a Model Version by selecting one of the uploaded `.joblib` files in GCP Storage Bucket. 
#### Custom Classifier
  * Google's AI Platform does not return the probability of predictions by default, a custom classifier called `CustomClassifier.py` is used
    to gain this functionality. 
  * Go to `classifier/ai-platform/predictor/` directory and run `python setup.py sdist --format=gztar` 
  * Upload the resulting `.tar` to GCP storage bucket and then create a new version of a model in the GCP AI Platform's UI.

[Click Here](https://cloud.google.com/ai-platform/prediction/docs/deploying-models) to find out more information on how to deploy SciKit-Learn models on GCP AI Platform

### Model Metrics
  * Random Forest 
    * Accuracy: 0.810
    * F1: 0.724
    * Recall: 0.709
    * Precision: 0.740
  * Gradient Boosting Trees
    * Accuracy: 0.804
    * F1: 0.705
    * Recall: 0.664
    * Precision: 0.752
  * Logistic Regression
    * Accuracy: 0.734
    * F1: 0.621
    * Recall: 0.619
    * Precision: 0.623
