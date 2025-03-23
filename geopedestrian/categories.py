# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

import json
import os



class CategoryRegistry(object):
    """
    Represents all available place categories.
    A category describes a type of place, such as "movie theater" or "zoo". 
    The categories fall into ten general groups: 
    - Arts and Entertainment
    - Business and Professional Services
    - Community and Government
    - Dining and Drinking
    - Events
    - Health and Medicine
    - Landmarks and Outdoors
    - Retail
    - Sports and Recreation
    - Travel and Transportation
    """

    def __init__(self) -> None:
        with open(os.path.join(os.path.dirname(__file__), 'data', 'places-categories-2025.json'), mode='r', encoding='utf-8') as in_stream:
            self._categories = json.load(in_stream)

    def find_id(self, name: str) -> str:
        """
        Finds the corresponding category ID.

        :param name: The category name e.g. Beer Garden.
        :type name: str

        :return: The category ID or None if no such category was found.
        """

        if not 'categories' in self._categories:
            return None
        
        for category in self._categories['categories']:
            full_labels = category['fullLabel']
            category_id = category['categoryId']
            for full_label in full_labels:
                if name == full_label:
                    return category_id
                
        return None