import arcpy, time, os

#Path for the new blank mxd, you will delete this.
blankmapPath = r"C:\work\haynes_test4.mxd“
#Path for you final resulting mxd
newmapPath = r"C:\work\haynes_hack.mxd"
open(blankmapPath, "w").close()
print "Created new map document"

#Use Python’s OS module to open the file in ArcMap
os.startfile(blankmapPath)
#Make the computer wait .... in seconds
time.sleep(30)
