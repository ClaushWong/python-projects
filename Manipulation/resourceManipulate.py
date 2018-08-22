#Open File, Retrieve Data and Close File
file_y = open("resource.txt","r")
file_y_read = file_y.readlines()
file_y.close()

#Declare Dictionary
info = {}
resource = {}
#Data use to store the amount of material that user do
data = {}

#Data Storing
for x in range(len(file_y_read)):
    info[str(x+1)] = file_y_read[x]
    splitInfo = info[str(x+1)].split("=")
    resource[str(x+1)] = splitInfo
    #Remove the "\n" from string
    m = list(resource[str(x+1)][1])
    try :
        deleteChar = m.index("\n")
    except :
        pass
    else :
        del(m[deleteChar])
    
    m = "".join(m)
    resource[str(x+1)][1] = m

#print "Before :" , resource["1"][1]

#for x in range(len(resource)):
    #print resource[str(x+1)][0] , ":" ,resource[str(x+1)][1]

#Senario A
#data["1"] = int(resource["1"][1])
#data["1"] += 5
#print data["1"]

#for x in range(0,1):#range(len(resource))
    #resource[str(x+1)][1] = str(data[str(x+1)])

#Open File , Replace Data , Close File
file_x = open("resource.txt","w")
for x in range(len(resource)):
    file_x.write(resource[str(x+1)][0] + "=" + resource[str(x+1)][1] + "\n")
file_x.close()

print resource

#print "After :" , resource["1"][1]

raw_input("Work")