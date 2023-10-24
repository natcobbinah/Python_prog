import json

import plotly.graph_objects as go
from plotly import offline

filename = 'data/readable_eq_data.json'

with open(filename, encoding='utf-8') as file_object:
    all_eq_data = json.load(file_object)

all_eq_dicts = all_eq_data['features']
data_title = all_eq_data['metadata']['title']

mags, lons, lats, hover_texts = [], [],[], []
for eq_dicts in all_eq_dicts:
    mag = eq_dicts['properties']['mag']
    lon = eq_dicts['geometry']['coordinates'][0]
    lat = eq_dicts['geometry']['coordinates'][1]
    title = eq_dicts['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes
# data = [go.Scattergeo(lon=lons, lat = lats)]
data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'marker':{
            'size': [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {
                'title': 'Magnitude'
            }
        }
    }
]
my_layout = go.Layout(title = data_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')