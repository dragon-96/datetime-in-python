import glob2
import datetime
l=glob2.glob("*.txt")
nm=datetime.datetime.now()
f=open(nm.strftime("%d-%B-%Y-%H-%M"+".txt"),"w")
for i in l:
    with open(i,"r") as fi:
        f.write(fi.read()+"\n")
f.close()
