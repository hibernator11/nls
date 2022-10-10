# nls

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/hibernator11/nls/HEAD)


### Moving Image Archive

These examples of [Jupyter Notebooks](http://jupyter.org/) are based on the descriptive metadata from the [Moving Image Archive](https://data.nls.uk/data/metadata-collections/moving-image-archive/) catalogue, which is Scotland’s national collection of moving images.

- [MARCXML extraction to CSV](https://nbviewer.org/github/hibernator11/nls/blob/master/notebooks/MovingImageArchive-DataExtraction.ipynb)
- [Data analysis with pandas](https://nbviewer.org/github/hibernator11/nls/blob/master/notebooks/MovingImageArchive-Analysis.ipynb) 
- [Word cloud based on the summary metadata](https://nbviewer.org/github/hibernator11/nls/blob/master/notebooks/MovingImageArchive-WordcloudSummary.ipynb)
- [Enrichment with Wikidata and Geonames](https://nbviewer.org/github/hibernator11/nls/blob/master/notebooks/MovingImageArchive-Enrichment.ipynb)
- [Map visualisation](https://nbviewer.org/github/hibernator11/nls/blob/master/notebooks/MovingImageArchive-GeographicLocations.ipynb)

<img src="images/wordcloud.png">

The transformation is based on the vocabulary [schema.org](https://schema.org/), using the entity [VideoObject](https://schema.org/VideoObject).

<img src="images/transformationMovingImageArchive.png">


### Map visualisation
Several approaches have been followed to create a map visualisation to show the locations named in the metadata provided in the dataset. First, the Python library folium has been used to create a map. 

<img width="50%" src="images/map-visualisation.png">

A second approach, is based on Wikidata and uses the links to create a map as a result of a SPARQL query. Please, click the following link to see the visualisation <a href="https://w.wiki/5o94">Wikidata</a>.

The SPARQL uses the instruction ```VALUES``` to use the links provided by the RDF data:

```
#defaultView:Map
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT ?t (SAMPLE(?location) as ?l)
WHERE {   
  VALUES ?t {wd:Q793283 wd:Q207257 wd:Q211091 wd:Q980084 wd:Q17582129 wd:Q1247435 wd:Q652539 wd:Q2421 wd:Q23436 wd:Q1061313 wd:Q189912 wd:Q530296 wd:Q81052 wd:Q202177 wd:Q54809 wd:Q786649 wd:Q664892 wd:Q1247396 wd:Q1147435 wd:Q9177476 wd:Q47134 wd:Q3643362 wd:Q4093 wd:Q206934 wd:Q550606 wd:Q864668 wd:Q100166 wd:Q123709 wd:Q203000 wd:Q80967 wd:Q978599 wd:Q204940 wd:Q182923 wd:Q207268 wd:Q1229763 wd:Q376914 wd:Q106652 wd:Q36405 wd:Q201149 wd:Q1247384  }.
    ?t wdt:P625 ?location. # coordinates     
          
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
} GROUP BY ?t
```

### Transformation to RDF

The transformation to RDF has been performed using the tool Open Refine (version 3.6.2) and including the RDF transform extension.

- https://openrefine.org/download.html
- https://github.com/AtesComp/rdf-transform/releases


### Datasets 





### References

- https://www.loc.gov/marc/bibliographic/bd040.html
- https://movingimage.nls.uk/
