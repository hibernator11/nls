#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:03:31 2022

@author: gustavo
"""
from shexer.shaper import Shaper
from shexer.consts import NT, SHEXC, SHACL_TURTLE, TURTLE

target_classes = [
    "http://id.loc.gov/ontologies/bibframe/Agent",
    "http://id.loc.gov/ontologies/bibframe/Work"
]

namespaces_dict = {"http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                   "http://example.org/": "ex",
                   "http://weso.es/shapes/": "",
                   "http://www.w3.org/2001/XMLSchema#": "xsd",
                   "http://id.loc.gov/ontologies/bibframe/":"bibframe",
                   "http://id.loc.gov/ontologies/bflc/":"bflc"
                   }

shaper = Shaper(target_classes=target_classes,
                #raw_graph=raw_graph,
                url_endpoint="http://localhost:3330/rdf/sparql",
                limit_remote_instances=500,
                #graph_file_input = graph_file_input,
                #input_format=TURTLE,
                namespaces_dict=namespaces_dict,  # Default: no prefixes
                instantiation_property="http://www.w3.org/1999/02/22-rdf-syntax-ns#type")  # Default rdf:type

output_file = "shaper_bibframe.shex"

shaper.shex_graph(output_file=output_file,
                  acceptance_threshold=0.8)

print("Done!")

