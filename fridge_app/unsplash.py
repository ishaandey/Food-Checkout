import json

def get_food_img(thing='cheese'):
    PARAMS = {
        'key':'AIzaSyC-YOb4s4JRxypbUvFB8Hf5gtMAi1nFi5Y&cx=016878084261136898543:i7sgeakvavd',
        'q':thing+' unsplash',
    }
    r = requests.get(url="https://www.googleapis.com/customsearch/v1", data=json.dumps(PARAMS)).json()
    print(r)
