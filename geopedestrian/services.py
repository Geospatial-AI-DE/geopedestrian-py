# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from georapid.client import GeoRapidClient
import requests
from typing import List



def drive_from(client: GeoRapidClient, latitude: float, longitude: float, category_id: str):
    """
    Drive from categorized places which are accessible by car to the pedestrian location.

    :param client: The client instance to use for this query.
    :type client: :class:`georapid.client.GeoRapidClient`
    :param latitude: The latitude representing the current pedestrian location.
    :type latitude: float
    :param longitude: The longitude representing the current pedestrian location.
    :type longitude: float
    :param category_id: The defined category.
    :type category_id: str

    :return: The places which can reach the pedestrian with driving areas as GeoJSON.
    """

    if latitude < -90.0 or 90.0 < latitude:
        raise ValueError(f'Invalid latitude value! {latitude} is not in the range of [-90.0, 90.0].')
    
    if longitude < -180.0 or 180.0 < longitude:
        raise ValueError(f'Invalid longitude value! {longitude} is not in the range of [-180.0, 180.0].')
    
    endpoint = '{0}/drive_from'.format(client.url)
    params = {
        'lat': latitude,
        'lon': longitude,
        'category': category_id
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()

def analyze_walking(client: GeoRapidClient, latitude: float, longitude: float, category_id: str):
    """
    Analyzes walking to categorized places which are accessible by a pedestrian in 15 minutes.
    The analysis result is a 150 meter spatial grid where each cell contains at least one place.

    :param client: The client instance to use for this query.
    :type client: :class:`georapid.client.GeoRapidClient`
    :param latitude: The latitude representing the current pedestrian location.
    :type latitude: float
    :param longitude: The longitude representing the current pedestrian location.
    :type longitude: float
    :param category_id: The defined category.
    :type category_id: str

    :return: The walking analysis spatial grid cells as GeoJSON.
    """

    if latitude < -90.0 or 90.0 < latitude:
        raise ValueError(f'Invalid latitude value! {latitude} is not in the range of [-90.0, 90.0].')
    
    if longitude < -180.0 or 180.0 < longitude:
        raise ValueError(f'Invalid longitude value! {longitude} is not in the range of [-180.0, 180.0].')
    
    endpoint = '{0}/analyze_walking'.format(client.url)
    params = {
        'lat': latitude,
        'lon': longitude,
        'category': category_id
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()  

def solve_walking(client: GeoRapidClient, latitude: float, longitude: float, break_values: List[int]=[5, 10, 15]):
    """
    Solves walking areas representing areas which are accessible by a pedestrian.

    :param client: The client instance to use for this query.
    :type client: :class:`georapid.client.GeoRapidClient`
    :param latitude: The latitude representing the current pedestrian location.
    :type latitude: float
    :param longitude: The longitude representing the current pedestrian location.
    :type longitude: float
    :param break_values: The break values for each walking area in minutes.
    :type break_values: List[int]

    :return: The calculated walking areas as GeoJSON.
    """

    if latitude < -90.0 or 90.0 < latitude:
        raise ValueError(f'Invalid latitude value! {latitude} is not in the range of [-90.0, 90.0].')
    
    if longitude < -180.0 or 180.0 < longitude:
        raise ValueError(f'Invalid longitude value! {longitude} is not in the range of [-180.0, 180.0].')
    
    endpoint = '{0}/solve_walking'.format(client.url)
    params = {
        'lat': latitude,
        'lon': longitude
    }
    if break_values:
        if 50 < len(break_values):
            raise ValueError(f'Invalid break values! Not more than 50 break values are supported.')

        for break_value in break_values:
            if not isinstance(break_value, int):
                raise ValueError(f'Invalid break value! {break_value} is not a valid integer.')
            elif break_value < 1 or 300 < break_value:
                raise ValueError(f'Invalid break value! {break_value} is not in the range of [1, 300].')
        
        if 0 < len(break_values):
            break_values.sort()
            params['breaks'] = ','.join([str(break_value) for break_value in break_values])

    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()

def walk_from(client: GeoRapidClient, latitude: float, longitude: float, category_id: str):
    """
    Walk from categorized places which are accessible to the pedestrian location.

    :param client: The client instance to use for this query.
    :type client: :class:`georapid.client.GeoRapidClient`
    :param latitude: The latitude representing the current pedestrian location.
    :type latitude: float
    :param longitude: The longitude representing the current pedestrian location.
    :type longitude: float
    :param category_id: The defined category.
    :type category_id: str

    :return: The places which can reach the pedestrian with walking routes as GeoJSON.
    """

    if latitude < -90.0 or 90.0 < latitude:
        raise ValueError(f'Invalid latitude value! {latitude} is not in the range of [-90.0, 90.0].')
    
    if longitude < -180.0 or 180.0 < longitude:
        raise ValueError(f'Invalid longitude value! {longitude} is not in the range of [-180.0, 180.0].')
    
    endpoint = '{0}/walk_from'.format(client.url)
    params = {
        'lat': latitude,
        'lon': longitude,
        'category': category_id
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()

def walk_to(client: GeoRapidClient, latitude: float, longitude: float, category_id: str):
    """
    Walk to categorized places which are accessible by a pedestrian.

    :param client: The client instance to use for this query.
    :type client: :class:`georapid.client.GeoRapidClient`
    :param latitude: The latitude representing the current pedestrian location.
    :type latitude: float
    :param longitude: The longitude representing the current pedestrian location.
    :type longitude: float
    :param category_id: The defined category.
    :type category_id: str

    :return: The accessible places with walking routes as GeoJSON.
    """

    if latitude < -90.0 or 90.0 < latitude:
        raise ValueError(f'Invalid latitude value! {latitude} is not in the range of [-90.0, 90.0].')
    
    if longitude < -180.0 or 180.0 < longitude:
        raise ValueError(f'Invalid longitude value! {longitude} is not in the range of [-180.0, 180.0].')
    
    endpoint = '{0}/walk_to'.format(client.url)
    params = {
        'lat': latitude,
        'lon': longitude,
        'category': category_id
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()  
