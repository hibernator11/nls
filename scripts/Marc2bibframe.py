#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:58:01 2022

@author: gustavo
"""

import lxml.etree as lxml
import xml.etree.cElementTree as ET
from xml.etree import ElementTree

ET.register_namespace('marc',"http://www.loc.gov/MARC21/slim") #some name

# add the path to the dataset 
#filename = "../data/nls-nbs-v2/NBS_v2_validated_marcxml.xml"
filename = "../data/boslit/BOSLIT_dataset.xml"
#filename = 'test.xml'

# path to RDF file output
#output = "../rdf/nbs/nbs_output_"
output = "../rdf/boslit/boslit_output_"

# add the path to the XSLT file in the marc2bibframe2 project
xsl_filename = "../tools/marc2bibframe2/xsl/marc2bibframe2.xsl"

count = 0;

for event, elem in ET.iterparse(filename, events=("start", "end")):
    
    if event == 'end':
        # process the tag
        if elem.tag == '{http://www.loc.gov/MARC21/slim}record':
            
            xml_str = ElementTree.tostring(elem).decode()
            marc_record = lxml.XML(xml_str)
            xslt = lxml.parse(xsl_filename)
            transform = lxml.XSLT(xslt)
            result = transform(marc_record)
            
            result.write_output(output + str(count) +".rdf.gz", compression=9)
            count +=1;
            print(count)
            elem.clear()

