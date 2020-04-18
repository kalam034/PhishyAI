## PhishyAI

PhishyAI trains ML models for [Phishy](https://github.com/morch028/phishy), a Gmail extension which leverages ML to detect phishing attempts in all incoming emails. Phishy scans all incoming emails for URLs and classify them as malicious or benign.

The models are trained with data set consisting of 456,577 (URLs) records in total with 35% of records labeled as malicious and 65% benign. 51 new features are calculated for each URL based on its properties of domain, path, query, file extension and fragment. The trained models are then tested with unseen data and scores for Accuracy, F1, Precision and Recall are collected. The models are then deployed on [GCP AI Platform](https://cloud.google.com/ai-platform) to predict URLs in real time for [Phishy](https://github.com/morch028/phishy) via API calls. 

### Installation
* Run the following commands:
	```
	git clone https://github.com/kalam034/phishy
	cd PhishyML
	python setup.py install
	```
  * Installs the project and downloads the needed dependencies:
    * pandas
    * numpy
    * scikit-learn 0.20.4 (GCP AI Platform only accepts version SciKit version 0.20.4)

### Usage

* Run `python run_pipeline.py`
	 * Reads the raw data files from different formats and merges them into one uniform dataframe
	 * Calculates 51 new features for each URL based its properties
	 * Trains and evaluates the following ML models
	   * Random Forest 
	   * Gradient Boosting Trees
	   * Logistic Regression
	 * Serializes and saves the models as `joblib` files in `PhishyAI/models`
	 * Saves a copy of the dataframe after each step in `PhishyAI/data/interim`


### Deployment
* Run `python run_pipeline.py` 
* Upload the directory `PhishyAI/models` to a [GCP Storage Bucket](https://cloud.google.com/storage/docs/creating-buckets)
* Log on to [GCP AI Platform](https://cloud.google.com/ai-platform)  and create a model version by selecting one of the uploaded `.joblib` files in GCP Storage Bucket. 

#### Custom Classifier
 As GCP's AI Platform does not return the probability of predictions by default, a custom classifier called `predictor.py` is used to gain this functionality. 
  * `cd ai-platform/predictor/`
  * Run `python setup.py sdist --format=gztar` 
	  * The resulting `.tar` can be uploaded to a GCP storage bucket, then selected when creating a new version of a model in the GCP AI Platform's UI.

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
