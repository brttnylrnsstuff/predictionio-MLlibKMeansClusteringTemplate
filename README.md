# predictionio-MLlibKMeansClusteringTemplate
PredictionIO clustering engine template (Scala-based parallelized engine) 

## Overview

This is an application which demonstrates the use of K-Means clustering algorithm which can be deployed on
a spark-cluster using prediction.io. Let's go over the whole procedure to get the app running step-wise. Note
that it's assumed that the python SDK for prediction io has been installed and works seemlessly with 
python2.7. It has also been assumed that the preiction.io binaries have been added to PATH environment
variable. If it hasn't been it can be done by editing '~/.bashrc'

## Clustering

![Clustering](http://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Linear-svm-scatterplot.svg/720px-Linear-svm-scatterplot.svg.png)

Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters). It is a main task of exploratory data mining, and a common technique for statistical data analysis, used in many fields, including machine learning, pattern recognition, image analysis, information retrieval, and bioinformatics.

In centroid-based clustering, clusters are represented by a central vector, which may not necessarily be a member of the data set. When the number of clusters is fixed to k, k-means clustering gives a formal definition as an optimization problem: find the k cluster centers and assign the objects to the nearest cluster center, such that the squared distances from the cluster are minimized.

## Data Required

The set of datasets used is a public one. It resides at the link (search for *Shape sets*):

    http://cs.joensuu.fi/sipu/datasets/

The dataset which is used by default is the *jain.txt* dataset and if a different data set is to be used then the number of features has to be changed correspondingly in all the source files. This data reside in the ./data directory.

## Events Required

Typically a prediction-io Engine requires *events*, which is the defaut entity_type of a data point in the template. This is the entity_type to be used while storing the data on the prediction-io event server. This entity_type has been changed to *point* in this template since the data is indeed in the form of points which we want to cluster. Each such data point has a unique *entity_id* which the prediction io server uses to address the data point.The *properties* filed of this *point* captures it's coordinates in a *k*-dimentional space, where *k* is the number of features of the data point. Additionally any relevant information about the data point can also be passed onto the prediction-io event server, for example the true label of the point. Such information would be useful in evaluating the performance of the clustering engine.

The sample point can be found in the python script file which uploads the data for this template to the prediction-io event server. This file resides in ./ScriptsAndInfo/submitData.py and can be unvoked as 

    python ScriptsAndInfo/submitData.py


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
      
4)  We need a corresponding app with which the engine has to communicate. Create a new app using the commandand        also note down the details regarding the app in a text file called say 'ScriptsAndInfo/info.txt'. These will be 
    required for the engine and app to communicate: 
      
      pio app new MyApp

    
5)  Modify 'engine.json' to reflect the AppID of the app you just created. By default it has the id of the app
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
    
10) Modify the python script 'ScriptsAndInfo/submitData.py' to reflect the appID of your app which you had saved in 
    'info.txt'. Execute it to convey the various points to be clustered by the K-Means algorithm as follows:
    
      python2.7 ScriptsAndInfo/submitData.py
      
11) Run the following in the directory where the code resides to build the model: 
      
      pio build
      
    
12) Run the following to train the model:

      pio train
      
    
    
13) Run the following to deploy the model:

      pio deploy
    
    
  
14) Having deployed the engine, we can check that it's up and running using a standard web browser at the URL

      http://localhost:8000
      
15) Finally, we can run a python script such as 'ScriptsAndInfo/getPredictions.py' to get predictions for new data-Points.
    Run:
    
      python2.7 ScriptsAndInfo/getPredictions.py
      
    
## Usage of the Engine

### Input For training:
Any input to the Engine for the sake of training is a data point and has the following fields:

1. entity_type : This is always set to 'point' in this case since there is just a single type of entity which this engine works with a data point.
2. entity_id : This is the unique id which each data point has, and which the engine can use internally to                        distinguish various data points.
3. properties  : The attributes of the data point. Can include the true label too, to evaluate the clustering     algorithm being used. The example included includes:

    "attr0" : First attribute,
    
    "attr1" : Second attribute,
    
    "plan"  : The true label for the data point
    
A sample input for the training phase looks as follows(Using Python SDK):
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
### Query
The input query to the trained clustering engine is a simple JSON object with field **dataPoint**. A typical query looks as given below when we use the Python SDK for prediction-io:
```python
engine_client.send_query({"dataPoint": [12.1, 15.1]})
```
The sample code which sends this query to the prediction-io event server and gets back the PredictedResult resides in ./ScriptsAndInfo/getPredictions.py and can be invoked as

    python ScriptsAndInfo/getPredictions.py
    
This returns a PredictedResult object described in next section.

### Predicted Result

The output is an object of this class and has a single field, the predicted label, of type Double. This field is called *cluster* for obvious reasons.

It is returned as a JSON object by the engine and looks like this:
```javascript
{u'cluster': 0.0}
```
