import predictionio
engine_client = predictionio.EngineClient(url="http://localhost:8000")
print engine_client.send_query({"dataPoint": [12.1, 15.1]})
print engine_client.send_query({"dataPoint": [24.1, 7.0]})
print engine_client.send_query({"dataPoint": [5.25, 14.2]})

