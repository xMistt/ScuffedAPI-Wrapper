"""
“Commons Clause” License Condition v1.0

Copyright Oli 2019
The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.

Software: ScuffedAPI
License: Apache 2.0
"""

__version__ = '1.0.3'

from .http import HTTPClient

http = HTTPClient()

class Playlists:
    def __init__(self, data):
        self.name = data['displayName']
        self.description = data['description']
        self.id = data['id']
        self.image = data['image']
        self.sub_game = data['subGame']
        self.affect_profile_stats = data['affect_profile_stats']
        self.max_players = data['max_players']
        self.max_team_size = data['max_team_size']
        self.file_path = data['file_path']

class Banners:
    def __init__(self, data):
        self.name = data['name']
        self.id = data['id']
        self.file_path = data['file_path']['small_image']
        self.type = data['type']

async def get_all_playlists(raw=False):
    playlists = []

    response = await http.scuffedapi_request(url='https://scuffedapi.herokuapp.com/api/playlists')

    if raw == True:
        return response

    for individual_response in response:
        playlist_object = Playlists(individual_response)
        playlists.append(playlist_object)

    return playlists

async def get_playlist(name=None, description=None, playlist_id=None, subGame=None, affect_profile_stats=None, max_players=None, max_team_size=None, file_path=None, raw=False):
    if name is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?displayName={0}'.format(name)
    elif description is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?description={0}'.format(description)
    elif playlist_id is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?id={0}'.format(playlist_id)
    elif subGame is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?subGame={0}'.format(subGame)
    elif affect_profile_stats is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?affect_profile_stats={0}'.format(affect_profile_stats)
    elif max_players is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?max_players={0}'.format(max_players)
    elif max_team_size is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search?max_team_size={0}'.format(max_team_size)
    elif file_path is not None:
       url = 'https://scuffedapi.herokuapp.com/api/playlists/search?file_path={0}'.format(file_path)

    response = await http.scuffedapi_request(url=url)

    if raw == True:
        return response
    else:
        return Playlists(response)

async def get_playlists(name=None, description=None, playlist_id=None, subGame=None, affect_profile_stats=None, max_players=None, max_team_size=None, file_path=None, raw=False):
    playlists = []

    if name is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?displayName={0}'.format(name)
    elif description is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?description={0}'.format(description)
    elif playlist_id is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?id={0}'.format(playlist_id)
    elif subGame is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?subGame={0}'.format(subGame)
    elif affect_profile_stats is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?affect_profile_stats={0}'.format(affect_profile_stats)
    elif max_players is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?max_players={0}'.format(max_players)
    elif max_team_size is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?max_team_size={0}'.format(max_team_size)
    elif file_path is not None:
        url = 'https://scuffedapi.herokuapp.com/api/playlists/search/multiple?file_path={0}'.format(file_path)

    response = await http.scuffedapi_request(url=url)

    if raw == True:
        return response
    
    for individual_response in response:
        playlist_object = Playlists(individual_response)
        playlists.append(playlist_object)

    return playlists

async def get_all_banners(raw=False):
    banners = []

    response = await http.scuffedapi_request(url='https://scuffedapi.herokuapp.com/api/banners')

    if raw == True:
        return response

    for individual_response in response:
        banner_object = Banners(individual_response)
        banners.append(banner_object)

    return banners

async def get_banner(name=None, banner_id=None, banner_type=None, raw=False):
    if name is not None:
        url = 'https://scuffedapi.herokuapp.com/api/banners/search?name={0}'.format(name)
    elif banner_id is not None:
        url = 'https://scuffedapi.herokuapp.com/api/banners/search?id={0}'.format(banner_id)
    elif banner_type is not None:
        url = 'https://scuffedapi.herokuapp.com/api/banners/search?name={0}'.format(banner_type)

    response = await http.scuffedapi_request(url=url)

    if raw == True:
        return response
    else:
        return Banners(response)

async def get_banners(name=None, banner_id=None, banner_type=None, raw=False):
    banners = []

    if name is not None:
        url = 'https://scuffedapi.herokuapp.com/api/banners/search/multiple?name={0}'.format(name)
    elif banner_id is not None:
        url = 'https://scuffedapi.herokuapp.com/api/banners/search/multiple?id={0}'.format(banner_id)
    elif banner_type is not None:
        url = 'https://scuffedapi.herokuapp.com/api/banners/search/multiple?name={0}'.format(banner_type)

    response = await http.scuffedapi_request(url=url)

    if raw == True:
        return response
    
    for individual_response in response:
        banner_object = Banners(individual_response)
        banners.append(banner_object)

    return get_banners

async def get_status():
    response = await http.scuffedapi_request(url='https://scuffedapi.herokuapp.com/api/docs')

    if response != None:
        return 'UP'
    else:
        return 'DOWN'
