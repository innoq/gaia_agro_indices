import web
import json
import rasterio
from rasterio import mask

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/image/ndvi', 'image'

)

class index:
    def GET(self):
        name = 'GAIA!'
        return render.index(name)

    def POST(self, x):
        data = json.loads(web.data())
        value = data["name"]
        return "Hello " + value + "!\n"

class image:
    def POST(self):
        print ("payload", web.data())
        geoJSON = json.loads(web.data())
        shapes = [feature["geometry"] for feature in geoJSON["features"]]

        with rasterio.open("data/T35MRU_20190915T080611_AOT_10m_ndvi-colored-compressed-wgs84.tif") as src:
            out_image, out_transform = mask.mask(src, shapes, crop=True)
            out_meta = src.meta

            web.header('Content-Type', 'image/jpeg')

            out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

            # FIXME: fix saving and new reading for serving file
            with rasterio.open("cache/output.tif", "w", **out_meta) as dest:
                dest.write(out_image)

            imageBinary = open("cache/output.tif", 'rb').read()
            return imageBinary

        return "error"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

