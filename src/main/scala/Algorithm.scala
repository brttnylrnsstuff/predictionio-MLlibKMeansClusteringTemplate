package org.template.vanilla

import io.prediction.controller.P2LAlgorithm
import io.prediction.controller.Params
import org.apache.spark.mllib.clustering.KMeans
import org.apache.spark.mllib.clustering.KMeansModel
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.linalg.Vector
import grizzled.slf4j.Logger

case class AlgorithmParams(
	val numCenters: Int,
	val numIterations: Int
) extends Params

class Algorithm(val ap: AlgorithmParams)
  // extends PAlgorithm if Model contains RDD[]
  extends P2LAlgorithm[PreparedData, KMeansModel, Query, PredictedResult] {

  @transient lazy val logger = Logger[this.type]

  def train(data: PreparedData): KMeansModel = {
    // Simply count number of events
    // and multiple it by the algorithm parameter
    // and store the number as model
    val kMeansI = new KMeans()
 	kMeansI.setK(ap.numCenters)
	kMeansI.setMaxIterations(ap.numIterations)
    kMeansI.run(data.events)
  }

  def predict(model: KMeansModel, query: Query): PredictedResult = {
    // Prefix the query with the model data
    val result = model.predict(query.dataPoint)
    PredictedResult(label = result)
  }
}

class Model(val mc: Int) extends Serializable {
  override def toString = s"mc=${mc}"
}
