import predictionio
import numpy as np
client = predictionio.EventClient(
    access_key='O0xmqC95BAOGLVjagy6YG2ifr1wzPE4PDoMfPdFPGhHO0uMvVv562q2ZbiUqQBoj',
    url='http://localhost:7070',
    threads=5,
    qsize=500
)

data = np.genfromtxt("../data/jain.txt", delimiter = "\t")
num = data.shape[0]
# Set the 4 properties for a user
for i in range(0,num):
	client.create_event(
    	event="$set",
    	entity_type="point",
    	entity_id=i,
    	properties= {
      	"attr0" : data[i][0],
      	"attr1" : data[i][1],
      	"plan" : data[i][2]
    	}
	)
	print(i)
