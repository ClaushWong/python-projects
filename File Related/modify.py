info = {}
resource = {}

#Read the file
File = open("resource.txt","r")
FileRead = File.readlines()

for x in range(len(FileRead)):
    info[str(x+1)] = FileRead[x]
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

#Add Data ( if resource length = 30 )
File = open("resource.txt","a")

if len(resource) == 30:
    File.write("c1=0\n")
    File.write("c2=0\n")
    File.write("al-1=0\n")
    print "update done."
elif len(resource) == 33:
    print "no need to update."
else :
    print "contact creator right now."

File.close()
raw_input("")