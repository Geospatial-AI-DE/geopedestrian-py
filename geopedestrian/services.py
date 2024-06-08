# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from georapid.client import GeoRapidClient
import requests



def solve_walking(client: GeoRapidClient, latitude: float, longitude: float):
    """
    Solves walking areas representing areas which are accessible by a pedestrian.

    :param client: The client instance to use for this query.
    :type client: :class:`georapid.client.GeoRapidClient`
    :param latitude: The latitude representing the current pedestrian location.
    :type latitude: float
    :param longitude: The longitude representing the current pedestrian location.
    :type longitude: float

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
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()    
