
#Json           Python
######################
#object         dict
#array          list
#string         str
#number(int)    int
#number(real)   float
#true           True
#false          False
#null           None

#Read & Write JSON Python:
#
#Methods:
#json.load(f) --> Load json data from a file
#json.loads(s) --> Load json data from a string
#json.dump(f) --> Write json data to a file
#json.dumps(s) --> Write json object as string

#1. load
import json
json_file=open('./data/untold_story.json')
movie = json.load(json_file)
print("movie->", movie)
print("type movie ->", type(movie))
json_file.close()

#2. loads -> str to json
json_str = """
{
"title":"The Untold Story",
"release_year":2016,
"is_awesome":"true",
"won_oscal":"false",
"actors":["Sushant Singh Rajput","Kiara Advani","Disha Patani","MS Dhoni"],
"budget":null}
"""
strData = json.loads(json_str)
print("type of strData -> " ,type(strData))
print("strData -> " ,strData)

#3. dump to a file
movieWrite = {}
movieWrite["title"]="The U\u0144told Story"
movieWrite["relase_year"]=2016
movieWrite["actors"]=["Sushant Singh Rajput","Kiara Advani","Disha Patani","MS Dhoni"]
movieWrite["is_awesome"]="true"
movieWrite["won_oscar"]="false"
movieDataFile = open("./data/movie.json", 'w', encoding="utf-8")
json.dump(movieWrite, movieDataFile, ensure_ascii=True)

#4. json to string with ASCII Text:

import json
data = {'item': 'Mobile', 'cost':'£150.00'}
jstr = json.dumps(data)
print("type jstr ->" , jstr)
print(jstr)

import json
data = {'item': 'Mobile', 'cost':'£150.00'}
jstr = json.dumps(data, ensure_ascii=False)
print(jstr)



