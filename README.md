# GAIA Greenhouse

## Getting started

* install dependencies using `pip install -r requirements.txt `
* start app using: `python app.py`

## get polygon by GeoJSON

```
$ curl -X POST -d "@example-geojson.json" http://0.0.0.0:8080/image/ndvi > image.tif
```

You can also crop image by using rasterio command line tool:

```
# make sure rasterio is installed via pip install rasterio
$ rio mask  --geojson-mask example-geojson.json data/T35MRU_20190915T080611_AOT_10m_ndvi-colored-compressed-wgs84.tif output.tif --overwrite --crop
```
