# predictionio-template-scala-parallel-vanilla-modified
PredictionIO vanilla engine template (Scala-based parallelized engine) 

This is an application which demonstrates the use of K-Means clustering algorithm which can be deployed on
a spark-cluster using prediction.io. Let's go over the whole procedure to get the app running step-wise. Note
that it's assumed that the python SDK for prediction io has been installed and works seemlessly with 
python2.7.

First, some pre-conditions which must be met.

1)  The directory where this code is to reside must have write permissions. This can be tested by 
    executing a 'mkdir a' command. If the permissions do not exist they can be granted by executing:
    
        'sudo chmod -R 777  .'
        
2)  Prediction.io must be installed. The most recommended way to get prediction.io is to clone the 
    repository and build from source. It also has several dependencies which can be looked up here:
      http://docs.prediction.io/install/
      
Actual installation procedure(Linux-type Systems):

3)  Clone the current repository by executing the following command in the directory where you want 
    the code to reside:
    
      'git clone https://github.com/sahiliitm/predictionio-template-scala-parallel-vanilla-modified.git'
      
4)  We need a corresponding app with which the engine has to communicate. Create a new app using the command: 
      
      'pio app new MyApp'

    ans also note down the details regarding the app in a text file called say 'info.txt'. These will be 
    required for the engine and app to communicate.

5)  Mofidy 'engine.json' to reflect the AppID of the app you just created. By default it has the id of the app
    which I last created.
    
6)  We're now good to go and can put all the pieces together and make sure that the engine and app talk together.
    Towards that end, start HBase by executing 'start-hbase.sh'. The following command does so:
    
      './HBASE_HOME/bin/start-hbase.sh'
      
7)  Start elastic search.

      './ELASTIC_SEARCH_HOME/bin/elasticsearch'
      
8)  Check that both the components are working well by running:
    
      'pio status'
      
9)  Having confirmed that all components work well, run the eventserver which will capture all the relevant
    events and which the Engine would later query to build it's model.
    
      'pio eventserver'
10) Modify the python script 'submitData.py' to reflect the appID of your app which you had saved in 
    'info.txt'. Execute it to convey the various points to be clustered by the K-Means algorithm as follows:
    
      'python2.7 submitData.py'
      
11) Run: 
      
      'pio build'
      
    in the directory where the code resides to build the model. 
    
12) Run:

      'pio train'
      
    to train the model.
    
13) Run:

      'pio deploy'
    
    to deploy the model.
  
14) Having deployed the engine, we can check that it's up and running using a standard web browser at the URL
      'http://localhost:8000'
      
15) Finally, we can run a python script such as 'getPredictions.py' to get predictions for new data-Points.
    Run:
    
      'python2.7 getPredictions.py'
      
    
    
