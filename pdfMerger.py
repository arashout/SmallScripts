import PyPDF2
import os


dirPath = input("Enter folder path:\n")
merger = PyPDF2.PdfFileMerger()

files = list(os.scandir(dirPath))

def getCreationDate(dirObj):
    return os.path.getctime(dirObj.path)

for file in files:
    if file.name.endswith(".pdf"):
        print(file.name)
        merger.append(open(file.path, "rb"))

outPath = os.path.join(dirPath, "merged.pdf")
with open(outPath, "wb") as fout:
    merger.write(fout)