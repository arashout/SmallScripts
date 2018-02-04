import comtypes.client
import os

def PPTtoPDF(inputFileName, formatType = 32):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    #Remove .ppt extension and add .pdf
    outputFileName = inputFileName[0:-4] + ".pdf"
    deck = powerpoint.Presentations.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType) # formatType = 32 for ppt to pdf
    deck.Close()
    powerpoint.Quit()
    
dirPath = input("Enter directory that contains .PPT files to be convert:\n")
for file in os.scandir(dirPath):
    if("ppt" in file.name[-4:]):
        print(file.path)
        try:
            PPTtoPDF(file.path)
        except:
            print("Couldn't convert")

