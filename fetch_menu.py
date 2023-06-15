from google_images_search import GoogleImagesSearch
import json

f = open('placesAPI.json')
data = json.load(f)
api_key = data['key']
cx = data['cx']
f.close()

gis = GoogleImagesSearch(api_key, cx)

_search_params = {
    'q': 'Bismillah menu',
    'num': 10,
    'fileType': 'jpg|gif|png',
    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    # 'safe': 'active|high|medium|off|safeUndefined', ##
    # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined', ##
    # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined', ##
    # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined', ##
    # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined' ##
}


gis.search(search_params=_search_params, path_to_dir='/downloaded/')