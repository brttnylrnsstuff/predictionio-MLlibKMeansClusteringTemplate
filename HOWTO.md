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
```Scala
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


