# predictionio-template-scala-parallel-vanilla-modified
PredictionIO clustering engine template (Scala-based parallelized engine) 

## Overview

This is an application which demonstrates the use of K-Means clustering algorithm which can be deployed on
a spark-cluster using prediction.io. Let's go over the whole procedure to get the app running step-wise. Note
that it's assumed that the python SDK for prediction io has been installed and works seemlessly with 
python2.7. It has also been assumed that the preiction.io binaries have been added to PATH environment
variable. If it hasn't been it can be done by editing '~/.bashrc'

## Clustering

Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters). It is a main task of exploratory data mining, and a common technique for statistical data analysis, used in many fields, including machine learning, pattern recognition, image analysis, information retrieval, and bioinformatics.

In centroid-based clustering (the kind we use in this template), clusters are represented by a central vector, which may not necessarily be a member of the data set. When the number of clusters is fixed to k, k-means clustering gives a formal definition as an optimization problem: find the k cluster centers and assign the objects to the nearest cluster center, such that the squared distances from the cluster are minimized.

## Training Data

The training data used is a set of public data sets that can be found at 

    http://cs.joensuu.fi/sipu/datasets/
    
The data set used in the default implementation of this template is *jain.txt*.

## Building the App with Preidiction.io

First, some pre-conditions which must be met.

1)  The directory where this code is to reside must have write permissions. This can be tested by 
    executing a 'mkdir a' command. If the permissions do not exist they can be granted by executing:
    
        sudo chmod -R 777  .
        
2)  Prediction.io must be installed. The most recommended way to get prediction.io is to clone the 
    repository and build from source. It also has several dependencies which can be looked up here:
      http://docs.prediction.io/install/
      
Actual installation procedure(Linux-type Systems):

3)  Clone the current repository by executing the following command in the directory where you want 
    the code to reside:
    
      git clone https://github.com/sahiliitm/predictionio-template-scala-parallel-vanilla-modified.git
      
4)  We need a corresponding app with which the engine has to communicate. Create a new app using the commandand        also note down the details regarding the app in a text file called say 'info.txt'. These will be 
    required for the engine and app to communicate: 
      
      pio app new MyApp

    
5)  Mofidy 'engine.json' to reflect the AppID of the app you just created. By default it has the id of the app
    which I last created.
    
6)  We're now good to go and can put all the pieces together and make sure that the engine and app talk together.
    Towards that end, start HBase by executing 'start-hbase.sh'. The following command does so:
    
      ./HBASE_HOME/bin/start-hbase.sh
      
7)  Start elastic search.

      ./ELASTIC_SEARCH_HOME/bin/elasticsearch
      
8)  Check that both the components are working well by running:
    
      pio status
      
9)  Having confirmed that all components work well, run the eventserver which will capture all the relevant
    events and which the Engine would later query to build it's model.
    
      pio eventserver
    
10) Modify the python script 'submitData.py' to reflect the appID of your app which you had saved in 
    'info.txt'. Execute it to convey the various points to be clustered by the K-Means algorithm as follows:
    
      python2.7 submitData.py
      
11) Run the following in the directory where the code resides to build the model: 
      
      pio build
      
    
12) Run the following to train the model:

      pio train
      
    
    
13) Run the following to deploy the model:

      pio deploy
    
    
  
14) Having deployed the engine, we can check that it's up and running using a standard web browser at the URL

      http://localhost:8000
      
15) Finally, we can run a python script such as 'getPredictions.py' to get predictions for new data-Points.
    Run:
    
      python2.7 getPredictions.py
      
    
## Usage of the Engine

### Input For training:
Any input to the Engine for the sake of training is a data point and has the following fields:

1. entity_type : This is always set to 'point' in this case since there is just a single type of entity which this engine works with a data point.
2. entity_id : This is the unique id which each data point has, and which the engine can use internally to                        distinguish various data points.
3. properties  : The attributes of the data point. Can include the true label too, to evaluate the clustering     algorithm being used. The example included includes:

    "attr0" : First attribute,
    
    "attr1" : Second attribute,
    
    "plan"  : The true label for the data point
    
A sample query looks as follows(Using Python SDK):
```python
client.create_event(
event="$set",
entity_type="point",
entity_id=i,
properties= {
        "attr0" : 12.6,
        "attr1" : 1.5,
        "plan" : 1
        }
    )
```
### Input for Prediction
The input query is a simple JSON object with field **dataPoint**. A typical query looks as follows whem using Python SDK:
```python
engine_client.send_query({"dataPoint": [12.1, 15.1]})
```
This returns a PredictedResult object described in next section.

###Output

It is an object of class **PredictedResult** and has a single field, the predicted label, of type Double.
It is returned as a JSON object by the engine and looks like this:
```javascript
{u'label': 0.0}
```
