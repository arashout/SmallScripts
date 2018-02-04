import json
import sys

anonDict = dict()
dictFilePath = ""
resumePath = ""
anonToNormal = False

if len(sys.argv) != 4:
    print("Exactly two arguments not provide!")
    print("Assuming input files with default paths")
    print("Conversion from normal resume -> anon resume\n")
    dictFilePath = "anonData.json"
    resumePath = "resumeText.txt"
    
elif len(sys.argv) == 4:
    dictFilePath = sys.argv[1]
    resumePath = sys.argv[2]
    anonToNormal = sys.argv[3]

with open(dictFilePath, "r") as fp:
    anonDict = json.load(fp)
    print("Loaded dictionary with: " + fp.name)

print("Reading .txt file located in: " + resumePath)
with open(resumePath, "r") as fp:
    fileContent = fp.read()

print("")
# Reverse dictionary mapping depending on direction of conversion
if anonToNormal:
    anonDict = {y:x for x,y in anonDict.items()}
    print("Go from a anon resume to normal version")
    newResumePath = "normalResume.txt"
else:
    print("Go from a normal resume to anon version")
    newResumePath = "anonResume.txt"

newContent = fileContent
for key, value in anonDict.items():
    newContent = newContent.replace(key, value)

with open(newResumePath, "w") as fp:
    fp.write(newContent)

print("Finished!")