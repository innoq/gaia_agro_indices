import json
import rasterio
from rasterio import mask

with open('example-geojson.json') as json_file:
  geoJSON = json.load(json_file)
  print("geoJSON: ", geoJSON)
  shapes = [feature["geometry"] for feature in geoJSON["features"]]
  print("shapes", shapes)

with rasterio.open("data/T35MRU_20190915T080611_AOT_10m_ndvi-colored-compressed-wgs84.tif") as src:
    out_image, out_transform = mask.mask(src, shapes, crop=True)
    out_meta = src.meta.copy()

out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open("output.tif", "w", **out_meta) as dest:
    dest.write(out_image)
