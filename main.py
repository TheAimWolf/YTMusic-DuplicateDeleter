from ytmusicapi import YTMusic
import time
import os.path


def getAllPlaylists():
    playlists = ytmusic.get_library_playlists()
    print(playlists)


def getDuplicates(_playlist):
    seen = []
    double = []
    for i in _playlist['tracks']:
        if i['title'] in seen:
            double.append(i)
        else:
            seen.append(i['title'])
    if not double:
        print('There is currently no duplicate song in this playlist. If any bug occurred please consider writing an '
              'issue on github (TODO: INSERT GITHUB LINK :P)')
        exit(0)
    print('=======\n')
    for j in double:
        print(j['title'], 'by', j['artists'][0]['name'])
    print('\n=======')
    answer = input('This is the list of duplicate songs in you playlist. Are you sure you want to delete all '
                   'duplicates of each song (can\'t be undone) [y or n]: ')
    if answer == 'y':
        ytmusic.remove_playlist_items(_playlist['id'], double)
        print('All done. Hope everything worked fine. See you next time.')
    else:
        print('OK, just come back if you need my help. If any bug occurred please consider writing an issue on '
              'github (TODO: INSERT GITHUB LINK :P)')
        exit(0)


def getPlaylist(_name):
    id = 0
    playlistsdata = ytmusic.get_library_playlists()
    for i in playlistsdata:
        if _name == i['title']:
            id = (i['playlistId'])
    if id == 0:
        print('Oops. I couldn\'t find that playlist in your library. Please enter a valid playlist name.')
        userInput()
    else:
        print('Warning! Because of limitations of YouTube Music you can\'t edit more than 1000 songs at once. So only '
              'the first 1000 items in your playlist will be processed.')
        playlist = ytmusic.get_playlist(id, limit=1000)
        print('Your playlist was successfully loaded into the cache. Please read the above line before you continue.')
        for i in range(20):
            print('.', end='')
            time.sleep(0.5)
        print('\n')
        return playlist


def userInput():
    name = input('Which playlist I have to fix today? If you don\'t know which playlist you have, just leave empty: ')

    if name == '':
        print('You have entered nothing. I show you all available playlists you have in you libary: ')
        getAllPlaylists()
        userInput()
        exit(0)
    else:
        playlist = getPlaylist(name)
        getDuplicates(playlist)


if os.path.isfile('headers_auth.json'):
    ytmusic = YTMusic('headers_auth.json')
    userInput()
else:
    print("You are not logged in. You need a headers_auth.json in the same directory as the python file. Please see "
          "the github for more informations.")
