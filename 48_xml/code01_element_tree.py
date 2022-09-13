#Element tree

"""
Parsing XML
 1) ElementTree -> reading xml
 2) Minidom  -> parsing HTML

Read & Write XML:
a) XML stands for Extensible Markup Language.
b) It is similar to HTML in its appearance.
c) XML is used for data presentation while HTML is used to define presentation of data in browser.
d) XML is exclusively designed to send & receive data back and forth between client & servers.
"""

"""
# Element Tree
1. Tag - String rep type of data beign stored
2. Attributes - Consist of number of attributes stored as dict
3. Text String - A text string info 
4. Tail String - Can also have tail string if necessary (Optional)
5. Child Elements - Consist of number of child elements stored as sequence
"""

import xml.etree.ElementTree as ET

#1a. Parsing
mytree = ET.parse('./input/food.xml')
myroot = mytree.getroot()
print("myroot object: " ,myroot)
print("myroot tag: " ,myroot.tag)

#1b. Parsing using from string
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
myroot_from_string = ET.fromstring(data)

print("myroot_from_string tag: " ,myroot_from_string.tag)

#2. Element
print("First Element : " , myroot[0])
print("No of Elements : ", len(myroot))



#Print all attr and elements
print("#################################")
print("All Tag and Attr of First Element : ")
for x in myroot[0]:
    print(x.tag, x.attrib)
print("All Tag and Text of First Element : ")
for x in myroot[0]:
    print(x.tag, str(x.text).strip())
print("Create dictionary of item/price tags of all food items: ")

foodItems = {}
for x in myroot.findall("food") :
    item = x.find("item").text
    price = x.find("price").text
    #print(item, ":", price)
    foodItems[item] = price

print("Food Items as Dict : " ,foodItems)
print("#################################")

#3. Modify
mytree = ET.parse('./input/food.xml')
myroot = mytree.getroot()
print("update discription and push to a new file, add new tag")
for x in myroot.iter('description'):
    new_desc = str(x.text) + "description updated!"
    x.text = str(new_desc)
    x.set("updated", 'yes')
mytree.write("./input/new1.xml")

#4. Add new Element - SubElement
mytree = ET.parse('./input/food.xml')
myroot = mytree.getroot()
ET.SubElement(myroot[0], 'speciality')
for x in myroot.iter('speciality'):
    new_desc = "South Indian Dishes"
    x.text = str(new_desc)
    mytree.write('./input/new2.xml')

#5. Remove Attribute (remove name attribute from item tag for element 0)
mytree = ET.parse('./input/food.xml')
myroot = mytree.getroot()
myroot[0][0].attrib.pop('name')
mytree.write('./input/new3.xml')

#6. Remove First Element
mytree = ET.parse('./input/food.xml')
myroot = mytree.getroot()
myroot[0].clear()
mytree.write('./input/new4.xml')

