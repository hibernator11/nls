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



### Transformation to RDF

The transformation to RDF has been performed using the tool Open Refine (version 3.6.2) and including the RDF transform extension.

- https://openrefine.org/download.html
- https://github.com/AtesComp/rdf-transform/releases


### Datasets 





### References

- https://www.loc.gov/marc/bibliographic/bd040.html
- https://movingimage.nls.uk/
