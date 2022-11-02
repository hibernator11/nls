#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:46:41 2022

@author: gustavo
"""

from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE, TURTLE

target_classes = [
    "http://xmlns.com/foaf/0.1/Person",
    "http://xmlns.com/foaf/0.1/Organization",
    "https://schema.org/VideoObject",
    "https://schema.org/Place"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd"
                   }


graph_file_input = "../rdf/datasetEnriched.ttl"

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                graph_file_input = graph_file_input,
                input_format=TURTLE,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_mia.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")
