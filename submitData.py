import predictionio

client = predictionio.EventClient(
    access_key='7tBkEmybaJ2xnY0y3r3aiDIyMfqABbXBj03VnZenWHXQJfBwEewlhnriDbwc6Elh',
    url='http://localhost:7070',
    threads=5,
    qsize=500
)

# Set the 4 properties for a user
client.create_event(
    event="$set",
    entity_type="user",
    entity_id=2,
    properties= {
      "attr0" : 12.1,
      "attr1" : 2.3,
      "plan" : int(2)
    }
)
