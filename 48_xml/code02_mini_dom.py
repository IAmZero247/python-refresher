from xml.dom import minidom

#1a Reading First Way
mytree = minidom.parse('./input/food.xml')

#1b Reading Second Way
filedata = open('./input/food.xml')
mytree= minidom.parse(filedata)

#1c Thrird Way
data = '''<?xml version="1.0" encoding="UTF-8"?>
<metadata>
<food>
    <item name="breakfast">Idly</item>
    <price>$2.5</price>
    <description>
   Two idly's with chutney
   </description>
    <calories>553</calories>
</food>
</metadata>
'''
mytree= minidom.parseString(data)

#2 Finding Elements
mytree = minidom.parse('./input/food.xml')
tagname = mytree.getElementsByTagName('item')[0] #first element
print("tagname ->",tagname)
print("attribute of above tagname -> ",tagname.attributes['name'].value)
print("data of above tagname ->", tagname.firstChild.data)
tagname = mytree.getElementsByTagName('item') #first element
print("traversing directly to first element ->",tagname[1].firstChild.data)
print("printing all element below ->")
for x in tagname:
    print(x.firstChild.data)

print("length of tagname")
print(len(tagname))

