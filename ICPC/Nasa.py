import ee
ee.Initialize()

# Selecciona imágenes Sentinel-2 sobre Santa Cruz
region = ee.Geometry.Point([-63.18, -17.78])
image = ee.ImageCollection("COPERNICUS/S2") \
    .filterBounds(region) \
    .filterDate('2024-01-01', '2024-12-31') \
    .sort('CLOUD_COVER') \
    .first()

# Calcula NDVI
ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')

# Muestra el resultado en consola
print(ndvi.getInfo())
