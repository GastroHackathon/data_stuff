#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:42:48 2019

@author: drx
"""

import json

users = []


user = {'name': 'Florian Krempl',
        'allergies': [],
        'veggie': False,
        'vegan' : False,
        'wealth': 'medium'} #high medium low

users.append(user)
users


with open('data/users.json', 'w') as f:
    json.dump(users, f)



