#Using MLLib for Clustering

This HOWTO describes how the vanilla prediction-io template can be modified to turn it into a clustering template with MLLib-KMeans integration.  You can easily add and use any other MLlib classification algorithms. The following will demonstrate how to add the MLlib KMeans algorithm into the engine.

## Updating Algorithm.scala

Since we have to include and use an algorithm from a library, this is possibly the most important step in the integration. In 'Algorithm.scala'  import the MLlib KMeans algorithm by adding the following lines:
  
```Scala
  import org.apache.spark.mllib.clustering.KMeans
  import org.apache.spark.mllib.clustering.KMeansModel
  import org.apache.spark.mllib.linalg.Vector
  import org.apache.spark.mllib.linalg.Vectors
```
These are the necessary classes in order to use the MLLib's KMeans algporithm.
Modify the AlgorithmParams class for the KMeans algorithm:
```Scala
  case class AlgorithmParams(
    val numberOfCenters: Int,
    val numberOfIterations: Int
  ) extends Params
```
By Default the class includes nothing useful and serves only as a template class. By including these fields in the AlgorithmParams class, we can easily change the meta-parameters of the algorithm by editing the relevant fields in the *engine.json* file which resides in the root directory for the Clustering template code. Below is a code listing which shows how the engine.json file is to be modifed as well as the meta-parameter settings used by default.

Original:
```Javascript
  "algorithms": [
    {
      "name": "algo",
      "params": {
        "mult" : 1
      }
    }
  ]
  ```
  Changed to:
```Javascript
 "algorithms": [
    {
      "name": "algo",
      "params": {
        "numberOfCenters" : 2,
		"numberOfIterations" : 500
      }
    }
  ]
  ```
Now, we must modify the main class *Algorithm* which will implement the KMeans algorithm. The model which this class implements is changed from the original *Model* class to the *KMeansModel* class, which is the model returned by the KMeans algorithm.
Original:
```Scala
class Algorithm(val ap: AlgorithmParams)
  // extends PAlgorithm if Model contains RDD[]
  extends P2LAlgorithm[PreparedData, Model, Query, PredictedResult] {
```
Changed to:
```Scala
class Algorithm(val ap: AlgorithmParams)
  // extends PAlgorithm if Model contains RDD[]
  extends P2LAlgorithm[PreparedData, KMeansModel, Query, PredictedResult] {
 ```
The two main functions implemented by the Algorithm class are the *train* and *predict* functions. The train function is used to build a *KMeansModel* which can then be used by the Engine to *predict* the cluster assignments for new data points using the Predict function.

The code which accomplishes this is:

Train:

```Scala
 def train(data: PreparedData): KMeansModel = {
    
    println("Running the K-Means clustering algorithm.")
	  // Creates a new KMeans class which generates the KMeansModel
    val kMeansI = new KMeans()
 	  // Setting the parameters
    kMeansI.setK(ap.numberOfCenters)
	  kMeansI.setMaxIterations(ap.numberOfIterations)
	  // Return the KMeansModel which we get after running the KMeans
    // algorithm on the data gathered by the DataSource component
    kMeansI.run(data.points)
  }
  ```
  Predict:
  ```Scala
  def predict(model: KMeansModel, query: Query): PredictedResult = {
    // Use the KMeansModel to predict cluster for new dataPoint
    val result = model.predict(Vectors.dense(query.dataPoint))
    PredictedResult(cluster = result)
  }
  ```
## Updating Data]Source.scala
We need to modify the DataSource.scala source file to reflect the format in which data is being given to the event server. The following header files are added since we expect an RDD of *Vector*.   
```Scala
  import org.apache.spark.mllib.linalg.Vector
  import org.apache.spark.mllib.linalg.Vectors
```
The main function in the DataSource class is the readTraining function. It reads the data points from the prediction-io event server and adds it to the RDD of Vector which the KMeans algorithm expects as input.
```Scala
 def readTraining(sc: SparkContext): TrainingData = {

    // read all events of EVENT involving ENTITY_TYPE and TARGET_ENTITY_TYPE
    val eventsRDD: RDD[Event] = PEventStore.find(
      appName = dsp.appName,
      entityType = Some("ENTITY_TYPE"),
      eventNames = Some(List("EVENT")),
      targetEntityType = Some(Some("TARGET_ENTITY_TYPE")))(sc)

    new TrainingData(eventsRDD)
  }
 ```
