#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 20:19:05 2022

@author: gustavo
"""

import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling

df=pd.read_csv('data/movingImageArchive/MovingImageArchiveGeoNames.csv',sep=",",quotechar='"',dtype={'geonames': str})
print(df)

locationPattern = "http://example.org/location/"

g = Graph()
owl = Namespace('http://www.w3.org/2002/07/owl#')

wgs84_pos="http://www.w3.org/2003/01/geo/wgs84_pos#"
schema="http://schema.org/"
edm="http://www.europeana.eu/schemas/edm/"
rdfs="http://www.w3.org/2000/01/rdf-schema#"
rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
dcterms="http://purl.org/dc/terms/"
skos="http://www.w3.org/2004/02/skos/core#"

for index, row in df.iterrows():

    # add types
    g.add((URIRef(locationPattern + (row['Location'].lower().replace(" ", ""))), URIRef(rdf+"type"), URIRef(edm + "Place") ))
    g.add((URIRef(locationPattern + row['Location'].lower().replace(" ", "")), URIRef(rdf+'type'), URIRef(schema + "Place") ))
    
    ## add preflabel
    g.add((URIRef(locationPattern + row['Location'].lower().replace(" ", "")), URIRef(skos+'prefLabel'), Literal(row["Location"], "en") ))
    
    ## add lat and long
    g.add((URIRef(locationPattern + row['Location'].lower().replace(" ", "")), URIRef(wgs84_pos+'lat'), Literal(str(row["lat"])) ))
    g.add((URIRef(locationPattern + row['Location'].lower().replace(" ", "")), URIRef(wgs84_pos+'long'), Literal(str(row["long"]))))
    
    if not pd.isnull(row['wikidata']):
        g.add((URIRef(locationPattern + row['Location'].lower().replace(" ", "")), URIRef(owl+'sameAs'), URIRef('https://www.wikidata.org/wiki/' + str(row['wikidata']))))
    if not pd.isnull(row['geonames']):   
        g.add((URIRef(locationPattern + row['Location'].lower().replace(" ", "")), URIRef(owl+'sameAs'), URIRef('https://www.geonames.org/' + str(row['geonames']))))
   
    
print(g.serialize(format='turtle'))

g.serialize('locations.xml',format='xml')