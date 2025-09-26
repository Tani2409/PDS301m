#list
emptyList = [] 
aList = [5, 7.83, "Fred"] 
print(aList)

x = 5
msg = "Hello"
path = "c:/py/data"
anotherList = [x, msg, path, 2.7, aList]
print(anotherList)

a = 2
b = a + 3
wspath = "c:/py/data1"
thirdList = [a, b, wspath]
print(thirdList)

#subsetting List
lyr = ["geology", "landuse", "publands", "streams", "cities"]
print(lyr[1])
print(lyr[1:2])
print(lyr[1:4])
print(lyr[-2:])
print(lyr[-1])
print(lyr[1][0])
print(lyr[1]==lyr[1:2][0])

a1 = [1212, "First St", "SF", "CA"]
a2 = [2323, "Second St", "Seattle", "WA"]
a3 = [3434, "Third St", "Denver", "CO"]
Addresses = [] #Address is a list of lists
Addresses.append(a1)
Addresses.append(a2)
Addresses.append(a3)
print(Addresses[0])
print(Addresses[1][1])
print(Addresses[2][3])

#append vs extend
Pacific = ['AK','CA','OR','WA']
Desert = ['AZ','NV','UT']
Mountain = ['ID','MT','WY','CO','NM']
WestStates = Pacific + Desert + Mountain
print(WestStates)

States = Pacific
States.append(Desert)
print(States)

#sorting lists
from random import random as rnd
mylist = []
for i in range(10):
 mylist.append(int(rnd()*10))
print(mylist)
mylist.sort()
print(mylist)
print(sorted(mylist))

#counting list
mylist = []
for i in range(10):
 mylist.append(int(rnd()*10))
print(sorted(mylist))
for i in range(10):
 print(f"frequency of {i}: {mylist.count(i)}")

#tuple
mytuple1 = 5, 7, "name", 8
mytuple2 = (5, 7, "name", 8)
print(mytuple1)
print(mytuple2)

a1 = (1212, "First St", "SF", "CA")
a2 = (2323, "Second St", "Seattle", "WA")
a3 = (3434, "Third St", "Denver", "CO")
Addresses = []
Addresses.append(a1)
Addresses.append(a2)
Addresses.append(a3)
print(Addresses)
print(Addresses[1][1])

#dictionaries
CA = {
 "name":"California",
 "capital":"Sacramento",
 "areakm2":423970,
 "population":39538223
}
print(CA)
print(len(CA))

GROVELAND = {"ELEVATION":853,
 "LATITUDE":37.8444,
 "LONGITUDE":-120.2258,
 "PRECIPITATION":176.02
}
print(GROVELAND)

PRECIPITATION = {"GROVELAND":176.02,
 "LEE VINING":71.88,
 "PLACERVILLE":170.69}
print(PRECIPITATION["PLACERVILLE"]) #print value of key PLACERVILLE

PRECIPITATION["BRIDGEPORT"] = 41.4
print(PRECIPITATION)

PRECIPITATION.keys()
for station in PRECIPITATION.keys():
 print(PRECIPITATION[station])

print(GROVELAND.keys())


