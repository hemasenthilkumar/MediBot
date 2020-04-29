import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["restdb"]
mycol = mydb["pdf"]
d=dict()
l=[]
for x in mycol.find():
    l.append(x['profile_image_name'])
    d['text']=l
print(d)    
    
  
