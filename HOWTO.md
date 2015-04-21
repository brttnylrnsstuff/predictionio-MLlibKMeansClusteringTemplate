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
Original:
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
Changed to:
```Scala
 def readTraining(sc: SparkContext): TrainingData = {
    val pointsDb = Storage.getPEvents()
      // read all events involving "point" type (the only type in our case)
    println("Gathering data from event server.")
	val pointsRDD: RDD[Vector] = pointsDb.aggregateProperties(
      appId = dsp.appId,
      entityType = "point",
      required = Some(List("plan","attr0","attr1")))(sc)
	  .map { case (entityId, properties) =>
        try {
          
        // Convert the data from an Array to a RDD[vector] which is what KMeans 
				// expects as input  
			Vectors.dense(Array(
              properties.get[Double]("attr0"),
              properties.get[Double]("attr1")
        ))
          
        } catch {
          case e: Exception => {
            logger.error(s"Failed to get properties ${properties} of" +
              s" ${entityId}. Exception: ${e}.")
            throw e
          }
        }
      }
		
    new TrainingData(pointsRDD)
  }
  ```
The main changes are:

..* Instead of creating an RDD of Event we create an RDD of Vector, which is the kind of input which KMeans algorithm exp[ects.

..* The *entity_type* and *properties* of the data points should be made in sync with the type which was inputted to the prediction-io event server.

..* The original cluster of the data point represented by the attribute *plan* is dropped since clustering is an unsupervised learning algorithm.
