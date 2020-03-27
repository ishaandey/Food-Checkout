#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:49:44 2020

@author: ishaandey
"""

import requests

def get_food_img(thing='cheese'):
    try:
        PARAMS = {
            'client_id':'NPmSc3FjJfHkYFq5idCJn99iao-5yNyViqO8upWtkiw',
            'query':thing,
            'page':1,
            'per_page':1,
        }
        client_id = PARAMS['client_id']
        r = requests.get(url="https://api.unsplash.com/search/photos", params=PARAMS).json()
        df = pd.read_json(r['results'])
        url = r['results'][0]['urls']['full']
    except:
        url = "https://images.unsplash.com/photo-1509440159596-0249088772ff?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80"
    return url

get_food_img('blueberries')