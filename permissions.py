import os
import subprocess
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
path = "selectedAPKs//selectedAPKs//"

# for file in os.listdir(path):
#     os.system("apktool d -f "+ path+file+" -o decoded//"+file)

decodedPath = "decoded//"
permissionsDict = {}
appDict = {}
for dir in os.listdir(decodedPath):
    tree = ET.parse(decodedPath+dir+"//AndroidManifest.xml")
    root = tree.getroot()
    permissionCount = 0
    for permission in root.iter("uses-permission"):
        permissionCount = permissionCount+1
        permissionName = permission.attrib.get("{http://schemas.android.com/apk/res/android}name")
        if(permissionsDict.get(permissionName) ==None):
            permissionsDict[permissionName] = 1
        else:
            permissionsDict[permissionName] = permissionsDict[permissionName] + 1
    appDict[dir] = permissionCount

permissionsDict = dict(sorted(permissionsDict.items(), key=lambda item: item[1], reverse=True)) 
appDict = dict(sorted(appDict.items(), key=lambda item: item[1], reverse=True)) 
lineGraphData = {}
for item in appDict.items():
    # print(item[1])
    if(lineGraphData.get(item[1])==None):
        lineGraphData[item[1]] = 1
    else:
        lineGraphData[item[1]] =lineGraphData[item[1]]+1

lineGraphDataX = list()
lineGraphDataY = list()

for item in lineGraphData.items():
    print(item[0])
    lineGraphDataX.append(item[0])
    lineGraphDataY.append(item[1])
    
plt.plot(lineGraphDataX, lineGraphDataY)
plt.title('App Permissions')
plt.xlabel('# of permissions requested by the apps')
plt.ylabel('# of apps that request a specific number of permissions')
plt.show()

for x in list(permissionsDict.items())[:10]:
    print (x)
for x in list(appDict.items())[:10]:
    print (x)  



