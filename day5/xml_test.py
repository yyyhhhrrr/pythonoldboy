#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import xml.etree.ElementTree as ET

tree=ET.parse("test.xml")
root=tree.getroot()
print(root.tag)

for child in root:
    print(child.tag,child.text)
    for i in child:
        print(i.tag,i.text)

for node in root.iter('from'):
    print(node.tag,node.text)