# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials

fetch("https://api.spotify.com/v1/audio-analysis/6EJiVf7U0p1BBfs0qqeb1f", {
  method: "GET",
  headers: {
    Authorization: `Bearer ${userAccessToken}`     
  }
})
.then(response => response.json())
.then(({beats})) => {
  beats.forEach((beat, index) => {
    console.log(`Beat ${index} starts at ${beat.start}`);
  })
}

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = False

""" la playlist de donde necesito informacion
    col_playlist_uri = spotify:playlist:37i9dQZEVXbOa2lmxNORXQ
    playlist_id = 37i9dQZEVXbOa2lmxNORXQ
    
    
    Code	Country name (using title case)	Year	ccTLD	ISO 3166-2	
    CO	     Colombia	                    1974	.co	    ISO 3166-2:CO

    """	
def playlist_tracks(self, playlist_id, fields=None,
                        limit=100, offset=0, market=None):
        """ Get full details of the tracks of a playlist.
        Parameters:
                - playlist_id - the id of the playlist
                - fields - which fields to return
                - limit - the maximum number of tracks to return
                - offset - the index of the first track to return
                - market - an ISO 3166-1 alpha-2 country code.
        """
        plid = self._get_id('playlist', playlist_id)
        return self._get("playlists/%s/tracks" % (plid),
                         limit=limit, offset=offset, fields=fields,
                         market=market)
        playlist_tracks();
        
playlist_1 = pd.read_fwf(dict({
  "items": [
    {
      "track": {
        "duration_ms": 200960,
        "id": "7k4t7uLgtOxPwTpFmtJNTY",
        "name": "Tusa",
        "popularity": 99,
        "uri": "spotify:track:7k4t7uLgtOxPwTpFmtJNTY"
      }
    },
    {
      "track": {
        "duration_ms": 226532,
        "id": "7sQKy5vlPQllr0k9IjYJv3",
        "name": "Sigues Con El",
        "popularity": 91,
        "uri": "spotify:track:7sQKy5vlPQllr0k9IjYJv3"
      }
    },
    {
      "track": {
        "duration_ms": 209754,
        "id": "1rgnBhdG2JDFTbYkYRZAku",
        "name": "Dance Monkey",
        "popularity": 78,
        "uri": "spotify:track:1rgnBhdG2JDFTbYkYRZAku"
      }
    },
    {
      "track": {
        "duration_ms": 200666,
        "id": "3mQ6SLdxxaL52Yte7KF2Ks",
        "name": "Morado",
        "popularity": 87,
        "uri": "spotify:track:3mQ6SLdxxaL52Yte7KF2Ks"
      }
    },
    {
      "track": {
        "duration_ms": 249520,
        "id": "5stPVcRqb4qixbafP9e8lt",
        "name": "Hola - Remix",
        "popularity": 91,
        "uri": "spotify:track:5stPVcRqb4qixbafP9e8lt"
      }
    },
    {
      "track": {
        "duration_ms": 199711,
        "id": "6mAN61JH0dzyZpWslS11jy",
        "name": "Fantasias",
        "popularity": 92,
        "uri": "spotify:track:6mAN61JH0dzyZpWslS11jy"
      }
    },
    {
      "track": {
        "duration_ms": 192024,
        "id": "5DxXgozhkPLgrbKFY91w0c",
        "name": "Vete",
        "popularity": 93,
        "uri": "spotify:track:5DxXgozhkPLgrbKFY91w0c"
      }
    },
    {
      "track": {
        "duration_ms": 145800,
        "id": "2rc7BkzO8qepMFAxHtOrXc",
        "name": "Blanco",
        "popularity": 88,
        "uri": "spotify:track:2rc7BkzO8qepMFAxHtOrXc"
      }
    },
    {
      "track": {
        "duration_ms": 221714,
        "id": "6cy3ki60hLwimwIje7tALf",
        "name": "RITMO (Bad Boys For Life)",
        "popularity": 96,
        "uri": "spotify:track:6cy3ki60hLwimwIje7tALf"
      }
    },
    {
      "track": {
        "duration_ms": 242573,
        "id": "0fea68AdmYNygeTGI4RC18",
        "name": "LA CANCIÓN",
        "popularity": 90,
        "uri": "spotify:track:0fea68AdmYNygeTGI4RC18"
      }
    },
    {
      "track": {
        "duration_ms": 216066,
        "id": "5Id5B3dxJZhPcV9GzgYZZe",
        "name": "Quizas",
        "popularity": 88,
        "uri": "spotify:track:5Id5B3dxJZhPcV9GzgYZZe"
      }
    },
    {
      "track": {
        "duration_ms": 301714,
        "id": "2ksOAxtIxY8yElEWw8RhgK",
        "name": "China",
        "popularity": 92,
        "uri": "spotify:track:2ksOAxtIxY8yElEWw8RhgK"
      }
    },
    {
      "track": {
        "duration_ms": 270740,
        "id": "3jbT1Y5MoPwEIpZndDDwVq",
        "name": "Adicto (with Anuel AA & Ozuna)",
        "popularity": 89,
        "uri": "spotify:track:3jbT1Y5MoPwEIpZndDDwVq"
      }
    },
    {
      "track": {
        "duration_ms": 309120,
        "id": "4R8BJggjosTswLxtkw8V7P",
        "name": "No Me Conoce - Remix",
        "popularity": 86,
        "uri": "spotify:track:4R8BJggjosTswLxtkw8V7P"
      }
    },
    {
      "track": {
        "duration_ms": 304733,
        "id": "1Xnn1TPyr5h0hpRAT4B4EA",
        "name": "Bellaquita - Remix",
        "popularity": 87,
        "uri": "spotify:track:1Xnn1TPyr5h0hpRAT4B4EA"
      }
    },
    {
      "track": {
        "duration_ms": 204000,
        "id": "2J9B63FawlTaPdg4eH5X03",
        "name": "Loco",
        "popularity": 80,
        "uri": "spotify:track:2J9B63FawlTaPdg4eH5X03"
      }
    },
    {
      "track": {
        "duration_ms": 190570,
        "id": "5Xhqh4lwJPtMUTsdBztN1a",
        "name": "Me Gusta",
        "popularity": 86,
        "uri": "spotify:track:5Xhqh4lwJPtMUTsdBztN1a"
      }
    },
    {
      "track": {
        "duration_ms": 186426,
        "id": "43NqTeL8pgBxKHPMiJKUP5",
        "name": "Girl",
        "popularity": 73,
        "uri": "spotify:track:43NqTeL8pgBxKHPMiJKUP5"
      }
    },
    {
      "track": {
        "duration_ms": 221103,
        "id": "4z6wo6PJG4Fve45OXK6D9m",
        "name": "Infeliz",
        "popularity": 85,
        "uri": "spotify:track:4z6wo6PJG4Fve45OXK6D9m"
      }
    },
    {
      "track": {
        "duration_ms": 215459,
        "id": "2pWOMNQJW3g2zmGjP0Vkb0",
        "name": "Whine Up",
        "popularity": 90,
        "uri": "spotify:track:2pWOMNQJW3g2zmGjP0Vkb0"
      }
    },
    {
      "track": {
        "duration_ms": 250533,
        "id": "2TH65lNHgvLxCKXM3apjxI",
        "name": "Callaita",
        "popularity": 90,
        "uri": "spotify:track:2TH65lNHgvLxCKXM3apjxI"
      }
    },
    {
      "track": {
        "duration_ms": 194892,
        "id": "4VgYtXCVJ7IbWAZ5ryfvEQ",
        "name": "Muévelo",
        "popularity": 87,
        "uri": "spotify:track:4VgYtXCVJ7IbWAZ5ryfvEQ"
      }
    },
    {
      "track": {
        "duration_ms": 181845,
        "id": "0x1k6gSTSxaLxe0F2IThaX",
        "name": "Detente",
        "popularity": 79,
        "uri": "spotify:track:0x1k6gSTSxaLxe0F2IThaX"
      }
    },
    {
      "track": {
        "duration_ms": 217253,
        "id": "59s0s39NFWScuHDbHytI14",
        "name": "Indeciso",
        "popularity": 88,
        "uri": "spotify:track:59s0s39NFWScuHDbHytI14"
      }
    },
    {
      "track": {
        "duration_ms": 204906,
        "id": "6Y4PDQv4XjYjHLeLmvyOt0",
        "name": "Si Te Vas",
        "popularity": 87,
        "uri": "spotify:track:6Y4PDQv4XjYjHLeLmvyOt0"
      }
    },
    {
      "track": {
        "duration_ms": 194087,
        "id": "2Fxmhks0bxGSBdJ92vM42m",
        "name": "bad guy",
        "popularity": 95,
        "uri": "spotify:track:2Fxmhks0bxGSBdJ92vM42m"
      }
    },
    {
      "track": {
        "duration_ms": 217129,
        "id": "37zdqI4r1gswIzczSBkRon",
        "name": "Aventura",
        "popularity": 88,
        "uri": "spotify:track:37zdqI4r1gswIzczSBkRon"
      }
    },
    {
      "track": {
        "duration_ms": 222346,
        "id": "25ZAibhr3bdlMCLmubZDVt",
        "name": "QUE PRETENDES",
        "popularity": 86,
        "uri": "spotify:track:25ZAibhr3bdlMCLmubZDVt"
      }
    },
    {
      "track": {
        "duration_ms": 183290,
        "id": "6WrI0LAC5M1Rw2MnX2ZvEg",
        "name": "Don't Start Now",
        "popularity": 97,
        "uri": "spotify:track:6WrI0LAC5M1Rw2MnX2ZvEg"
      }
    },
    {
      "track": {
        "duration_ms": 168533,
        "id": "4iFTIshL0xDCw8JJUl5AJ3",
        "name": "Alguien Me Gusta",
        "popularity": 70,
        "uri": "spotify:track:4iFTIshL0xDCw8JJUl5AJ3"
      }
    },
    {
      "track": {
        "duration_ms": 227233,
        "id": "1cVlW9WQiGlFdWUXFdFZGh",
        "name": "Pa' Olvidarme De Ella",
        "popularity": 86,
        "uri": "spotify:track:1cVlW9WQiGlFdWUXFdFZGh"
      }
    },
    {
      "track": {
        "duration_ms": 190799,
        "id": "6v3KW9xbzN5yKLt9YKDYA2",
        "name": "Señorita",
        "popularity": 88,
        "uri": "spotify:track:6v3KW9xbzN5yKLt9YKDYA2"
      }
    },
    {
      "track": {
        "duration_ms": 178613,
        "id": "1nocRtwyNPVtGcIJqfgdzZ",
        "name": "Tutu",
        "popularity": 87,
        "uri": "spotify:track:1nocRtwyNPVtGcIJqfgdzZ"
      }
    },
    {
      "track": {
        "duration_ms": 258600,
        "id": "1ndyl3wJCFs872XZ3ztPk6",
        "name": "DJ No Pare (feat. Zion, Dalex, Lenny Tavárez) - Remix",
        "popularity": 86,
        "uri": "spotify:track:1ndyl3wJCFs872XZ3ztPk6"
      }
    },
    {
      "track": {
        "duration_ms": 266773,
        "id": "0UfVfRSmy4xMyi67LKH5zZ",
        "name": "La Isla (with Sech & Dalex feat. Justin Quiles, La Exce, Feid, Zion)",
        "popularity": 75,
        "uri": "spotify:track:0UfVfRSmy4xMyi67LKH5zZ"
      }
    },
    {
      "track": {
        "duration_ms": 210426,
        "id": "41L3O37CECZt3N7ziG2z7l",
        "name": "Yummy",
        "popularity": 97,
        "uri": "spotify:track:41L3O37CECZt3N7ziG2z7l"
      }
    },
    {
      "track": {
        "duration_ms": 210520,
        "id": "6RyaV7owmVU6fzEPE17sF1",
        "name": "Que Tire Pa Lante",
        "popularity": 89,
        "uri": "spotify:track:6RyaV7owmVU6fzEPE17sF1"
      }
    },
    {
      "track": {
        "duration_ms": 212711,
        "id": "5099x34vBakWpGkHourFxP",
        "name": "Qué Pena",
        "popularity": 84,
        "uri": "spotify:track:5099x34vBakWpGkHourFxP"
      }
    },
    {
      "track": {
        "duration_ms": 266086,
        "id": "4t9a07PAghtQMRAIP9FQ7Z",
        "name": "Soltera - Remix",
        "popularity": 78,
        "uri": "spotify:track:4t9a07PAghtQMRAIP9FQ7Z"
      }
    },
    {
      "track": {
        "duration_ms": 175733,
        "id": "7KbF6AdprOXEEHlsq11Z6d",
        "name": "11 PM",
        "popularity": 86,
        "uri": "spotify:track:7KbF6AdprOXEEHlsq11Z6d"
      }
    },
    {
      "track": {
        "duration_ms": 233112,
        "id": "684EjRHwNsZQ9hCQxL4NYL",
        "name": "El Favor (with Nicky Jam & Sech, feat. Farruko, Zion & Lunay)",
        "popularity": 83,
        "uri": "spotify:track:684EjRHwNsZQ9hCQxL4NYL"
      }
    },
    {
      "track": {
        "duration_ms": 231848,
        "id": "059bcIhyc2SBwm6sw2AZzd",
        "name": "Te Vi",
        "popularity": 83,
        "uri": "spotify:track:059bcIhyc2SBwm6sw2AZzd"
      }
    },
    {
      "track": {
        "duration_ms": 245425,
        "id": "3ZCTVFBt2Brf31RLEnCkWJ",
        "name": "everything i wanted",
        "popularity": 97,
        "uri": "spotify:track:3ZCTVFBt2Brf31RLEnCkWJ"
      }
    },
    {
      "track": {
        "duration_ms": 250333,
        "id": "70zg99pT51vB4wlMS7e4q7",
        "name": "La Playa - Remix",
        "popularity": 81,
        "uri": "spotify:track:70zg99pT51vB4wlMS7e4q7"
      }
    },
    {
      "track": {
        "duration_ms": 360960,
        "id": "7g8YaUQABMal0zWe7a2ijz",
        "name": "Pa Mí - Remix",
        "popularity": 84,
        "uri": "spotify:track:7g8YaUQABMal0zWe7a2ijz"
      }
    },
    {
      "track": {
        "duration_ms": 161626,
        "id": "2qG5sZ7Si6sdK74qLxedYM",
        "name": "Con Altura",
        "popularity": 86,
        "uri": "spotify:track:2qG5sZ7Si6sdK74qLxedYM"
      }
    },
    {
      "track": {
        "duration_ms": 204563,
        "id": "56f5qnyAlZdlz8wrUDA50h",
        "name": "Desconocidos",
        "popularity": 78,
        "uri": "spotify:track:56f5qnyAlZdlz8wrUDA50h"
      }
    },
    {
      "track": {
        "duration_ms": 201040,
        "id": "7BlBVFwvbWvcwNcUarQmjk",
        "name": "Yo x Ti, Tu x Mi",
        "popularity": 87,
        "uri": "spotify:track:7BlBVFwvbWvcwNcUarQmjk"
      }
    },
    {
      "track": {
        "duration_ms": 305962,
        "id": "7fODjB7BrQTGqh0hogW6XD",
        "name": "Que Mas Pues - Remix",
        "popularity": 83,
        "uri": "spotify:track:7fODjB7BrQTGqh0hogW6XD"
      }
    },
    {
      "track": {
        "duration_ms": 332240,
        "id": "6K5BsR04ijf3FHNzjbaagD",
        "name": "Si Se Da - Remix",
        "popularity": 83,
        "uri": "spotify:track:6K5BsR04ijf3FHNzjbaagD"
      }
    }
  ]
}))

col_top_50 = pd.DataFrame({playlist_1})

for track in col_top_50['Genre'].unique():
    file_name = 'genre_{0}.csv'.format(track) 
    col_top_50[col_top_50['Genre'] == track].to_csv(file_name, sep=',') 

for track, group in col_top_50.groupby('Genre'):
    group.to_csv(f'genre_{track}.csv', sep=',')
 


----------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------

        
""" playlist(playlist_id, fields=None, market=None)
Gets playlist by id.

Parameters:
playlist - the id of the playlist
fields - which fields to return
market - An ISO 3166-1 alpha-2 country code or the
string from_token.


playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None)
Get full details of the tracks of a playlist.

Parameters:
playlist_id - the id of the playlist
fields - which fields to return
limit - the maximum number of tracks to return
offset - the index of the first track to return
market - an ISO 3166-1 alpha-2 country code.
""" 

curl -X "GET" "https://api.spotify.com/v1/playlists/37i9dQZEVXbOa2lmxNORXQ/tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQDwjHpMO57lP9qLPGIJY_3Cq2TXwES2q1u-bwvRYb3UWLmkzAwNT1xC8IVjxJML58C-Lxa--_hzWd4TZoSExEkkkRo4K0PbItWyuH26M3Y4_tgwfoiBnDamENP-9QbyzNyMGrbuustYWyglNjrx"

curl -X "GET" "https://api.spotify.com/v1/playlists/37i9dQZEVXbOa2lmxNORXQ/tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQDwjHpMO57lP9qLPGIJY_3Cq2TXwES2q1u-bwvRYb3UWLmkzAwNT1xC8IVjxJML58C-Lxa--_hzWd4TZoSExEkkkRo4K0PbItWyuH26M3Y4_tgwfoiBnDamENP-9QbyzNyMGrbuustYWyglNjrx"

curl -X "GET" "https://api.spotify.com/v1/playlists/37i9dQZEVXbOa2lmxNORXQ/tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQDwjHpMO57lP9qLPGIJY_3Cq2TXwES2q1u-bwvRYb3UWLmkzAwNT1xC8IVjxJML58C-Lxa--_hzWd4TZoSExEkkkRo4K0PbItWyuH26M3Y4_tgwfoiBnDamENP-9QbyzNyMGrbuustYWyglNjrx"
{
  "href": "https://api.spotify.com/v1/playlists/37i9dQZEVXbOa2lmxNORXQ/tracks?offset=0&limit=100",
  "items": [
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/790FomKkXshlbRYZFtlgla"
              },
              "href": "https://api.spotify.com/v1/artists/790FomKkXshlbRYZFtlgla",
              "id": "790FomKkXshlbRYZFtlgla",
              "name": "KAROL G",
              "type": "artist",
              "uri": "spotify:artist:790FomKkXshlbRYZFtlgla"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh"
              },
              "href": "https://api.spotify.com/v1/artists/0hCNtLu0JehylgoiP8L4Gh",
              "id": "0hCNtLu0JehylgoiP8L4Gh",
              "name": "Nicki Minaj",
              "type": "artist",
              "uri": "spotify:artist:0hCNtLu0JehylgoiP8L4Gh"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7mKevNHhVnZER3BLgI8O4F"
          },
          "href": "https://api.spotify.com/v1/albums/7mKevNHhVnZER3BLgI8O4F",
          "id": "7mKevNHhVnZER3BLgI8O4F",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ffb4bf313f7604378ae9dec5381696b613914261",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/f94cbc0d16fded80c38c2f685356cf4275f885de",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/5e9efcf683ce6206768847c4be20cb17a2eecda2",
              "width": 64
            }
          ],
          "name": "Tusa",
          "release_date": "2019-11-07",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:7mKevNHhVnZER3BLgI8O4F"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/790FomKkXshlbRYZFtlgla"
            },
            "href": "https://api.spotify.com/v1/artists/790FomKkXshlbRYZFtlgla",
            "id": "790FomKkXshlbRYZFtlgla",
            "name": "KAROL G",
            "type": "artist",
            "uri": "spotify:artist:790FomKkXshlbRYZFtlgla"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh"
            },
            "href": "https://api.spotify.com/v1/artists/0hCNtLu0JehylgoiP8L4Gh",
            "id": "0hCNtLu0JehylgoiP8L4Gh",
            "name": "Nicki Minaj",
            "type": "artist",
            "uri": "spotify:artist:0hCNtLu0JehylgoiP8L4Gh"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 200960,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71921183"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7k4t7uLgtOxPwTpFmtJNTY"
        },
        "href": "https://api.spotify.com/v1/tracks/7k4t7uLgtOxPwTpFmtJNTY",
        "id": "7k4t7uLgtOxPwTpFmtJNTY",
        "is_local": false,
        "name": "Tusa",
        "popularity": 99,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:7k4t7uLgtOxPwTpFmtJNTY"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
              },
              "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
              "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
              "name": "Dimelo Flow",
              "type": "artist",
              "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
              },
              "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
              "id": "4SsVbpTthjScTS7U2hmr1X",
              "name": "Arcangel",
              "type": "artist",
              "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
              },
              "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
              "id": "77ziqFxp5gaInVrF2lj4ht",
              "name": "Sech",
              "type": "artist",
              "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1y0pdsLO6cixGzAv7Sf8rf"
          },
          "href": "https://api.spotify.com/v1/albums/1y0pdsLO6cixGzAv7Sf8rf",
          "id": "1y0pdsLO6cixGzAv7Sf8rf",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/6e72909c0fd703211340b86b4d52bca2669f04dc",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/49a8712a6136a6ddc6b86ff21d0e30d9652ae3af",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/d165dcc0596549a7e0022de29de51aa94763ea57",
              "width": 64
            }
          ],
          "name": "Sigues Con El",
          "release_date": "2019-12-13",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1y0pdsLO6cixGzAv7Sf8rf"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
            "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
            "name": "Dimelo Flow",
            "type": "artist",
            "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
            },
            "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
            "id": "4SsVbpTthjScTS7U2hmr1X",
            "name": "Arcangel",
            "type": "artist",
            "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 226532,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QMFME1942300"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7sQKy5vlPQllr0k9IjYJv3"
        },
        "href": "https://api.spotify.com/v1/tracks/7sQKy5vlPQllr0k9IjYJv3",
        "id": "7sQKy5vlPQllr0k9IjYJv3",
        "is_local": false,
        "name": "Sigues Con El",
        "popularity": 91,
        "preview_url": "https://p.scdn.co/mp3-preview/f56625fc4cc304a59ef6b705b1fa24db296f293a?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:7sQKy5vlPQllr0k9IjYJv3"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2NjfBq1NflQcKSeiDooVjY"
              },
              "href": "https://api.spotify.com/v1/artists/2NjfBq1NflQcKSeiDooVjY",
              "id": "2NjfBq1NflQcKSeiDooVjY",
              "name": "Tones and I",
              "type": "artist",
              "uri": "spotify:artist:2NjfBq1NflQcKSeiDooVjY"
            }
          ],
          "available_markets": [
            "AU",
            "NZ"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/31IDBea3eEs57a0joX6TjN"
          },
          "href": "https://api.spotify.com/v1/albums/31IDBea3eEs57a0joX6TjN",
          "id": "31IDBea3eEs57a0joX6TjN",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b27338802659d156935ada63c9e3",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e0238802659d156935ada63c9e3",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d0000485138802659d156935ada63c9e3",
              "width": 64
            }
          ],
          "name": "Dance Monkey",
          "release_date": "2019-05-10",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:31IDBea3eEs57a0joX6TjN"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2NjfBq1NflQcKSeiDooVjY"
            },
            "href": "https://api.spotify.com/v1/artists/2NjfBq1NflQcKSeiDooVjY",
            "id": "2NjfBq1NflQcKSeiDooVjY",
            "name": "Tones and I",
            "type": "artist",
            "uri": "spotify:artist:2NjfBq1NflQcKSeiDooVjY"
          }
        ],
        "available_markets": [
          "AU",
          "NZ"
        ],
        "disc_number": 1,
        "duration_ms": 209754,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QZES71982312"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1rgnBhdG2JDFTbYkYRZAku"
        },
        "href": "https://api.spotify.com/v1/tracks/1rgnBhdG2JDFTbYkYRZAku",
        "id": "1rgnBhdG2JDFTbYkYRZAku",
        "is_local": false,
        "name": "Dance Monkey",
        "popularity": 78,
        "preview_url": "https://p.scdn.co/mp3-preview/7e70b1eb012b7589a6487169bcd6135889ce89aa?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:1rgnBhdG2JDFTbYkYRZAku"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7ynTaSXD9esXkgY0GG8UFd"
          },
          "href": "https://api.spotify.com/v1/albums/7ynTaSXD9esXkgY0GG8UFd",
          "id": "7ynTaSXD9esXkgY0GG8UFd",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/6f4824f010aba5a9af09f363877b3f8a7032ede6",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/84d04256c17e95dcfd0ab597d7e03bf3942b36ad",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/9cc10bb11fd4785723c17451469b87c5512a5cea",
              "width": 64
            }
          ],
          "name": "Morado",
          "release_date": "2020-01-09",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:7ynTaSXD9esXkgY0GG8UFd"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 200666,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71924691"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3mQ6SLdxxaL52Yte7KF2Ks"
        },
        "href": "https://api.spotify.com/v1/tracks/3mQ6SLdxxaL52Yte7KF2Ks",
        "id": "3mQ6SLdxxaL52Yte7KF2Ks",
        "is_local": false,
        "name": "Morado",
        "popularity": 87,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:3mQ6SLdxxaL52Yte7KF2Ks"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
              },
              "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
              "id": "0KPX4Ucy9dk82uj4GpKesn",
              "name": "Dalex",
              "type": "artist",
              "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
              },
              "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
              "id": "1pQWsZQehhS4wavwh7Fnxd",
              "name": "Lenny Tavárez",
              "type": "artist",
              "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/37230BxxYs9ksS7OkZw3IU"
              },
              "href": "https://api.spotify.com/v1/artists/37230BxxYs9ksS7OkZw3IU",
              "id": "37230BxxYs9ksS7OkZw3IU",
              "name": "Chencho Corleone",
              "type": "artist",
              "uri": "spotify:artist:37230BxxYs9ksS7OkZw3IU"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/65Pp2tO1Ul66KcCmmkRGWZ"
          },
          "href": "https://api.spotify.com/v1/albums/65Pp2tO1Ul66KcCmmkRGWZ",
          "id": "65Pp2tO1Ul66KcCmmkRGWZ",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab5a9b7adec162e6162eecacbfea204829ed2776",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/990d38773a6c66762a2d6cd3d4d95aee237c1e3d",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/e8203ddf9674e918802bd60a1fdce5b78ad56be5",
              "width": 64
            }
          ],
          "name": "Hola (Remix)",
          "release_date": "2019-11-01",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:65Pp2tO1Ul66KcCmmkRGWZ"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
            },
            "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
            "id": "1pQWsZQehhS4wavwh7Fnxd",
            "name": "Lenny Tavárez",
            "type": "artist",
            "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/37230BxxYs9ksS7OkZw3IU"
            },
            "href": "https://api.spotify.com/v1/artists/37230BxxYs9ksS7OkZw3IU",
            "id": "37230BxxYs9ksS7OkZw3IU",
            "name": "Chencho Corleone",
            "type": "artist",
            "uri": "spotify:artist:37230BxxYs9ksS7OkZw3IU"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2LmcxBak1alK1bf7d1beTr"
            },
            "href": "https://api.spotify.com/v1/artists/2LmcxBak1alK1bf7d1beTr",
            "id": "2LmcxBak1alK1bf7d1beTr",
            "name": "Juhn",
            "type": "artist",
            "uri": "spotify:artist:2LmcxBak1alK1bf7d1beTr"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
            "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
            "name": "Dimelo Flow",
            "type": "artist",
            "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 249520,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QM9WM1900166"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5stPVcRqb4qixbafP9e8lt"
        },
        "href": "https://api.spotify.com/v1/tracks/5stPVcRqb4qixbafP9e8lt",
        "id": "5stPVcRqb4qixbafP9e8lt",
        "is_local": false,
        "name": "Hola - Remix",
        "popularity": 91,
        "preview_url": "https://p.scdn.co/mp3-preview/52045e21f1d7a4a23558a41d7adfa27183c435a6?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5stPVcRqb4qixbafP9e8lt"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1mcTU81TzQhprhouKaTkpq"
              },
              "href": "https://api.spotify.com/v1/artists/1mcTU81TzQhprhouKaTkpq",
              "id": "1mcTU81TzQhprhouKaTkpq",
              "name": "Rauw Alejandro",
              "type": "artist",
              "uri": "spotify:artist:1mcTU81TzQhprhouKaTkpq"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
              },
              "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
              "id": "329e4yvIujISKGKz1BZZbO",
              "name": "Farruko",
              "type": "artist",
              "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1Flcx9eDuv7pTGM9nJBmGL"
          },
          "href": "https://api.spotify.com/v1/albums/1Flcx9eDuv7pTGM9nJBmGL",
          "id": "1Flcx9eDuv7pTGM9nJBmGL",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273ca6183e9d0bfb66f996eefce",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02ca6183e9d0bfb66f996eefce",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851ca6183e9d0bfb66f996eefce",
              "width": 64
            }
          ],
          "name": "Fantasias",
          "release_date": "2019-08-29",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1Flcx9eDuv7pTGM9nJBmGL"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1mcTU81TzQhprhouKaTkpq"
            },
            "href": "https://api.spotify.com/v1/artists/1mcTU81TzQhprhouKaTkpq",
            "id": "1mcTU81TzQhprhouKaTkpq",
            "name": "Rauw Alejandro",
            "type": "artist",
            "uri": "spotify:artist:1mcTU81TzQhprhouKaTkpq"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 199711,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QM6P41989279"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6mAN61JH0dzyZpWslS11jy"
        },
        "href": "https://api.spotify.com/v1/tracks/6mAN61JH0dzyZpWslS11jy",
        "id": "6mAN61JH0dzyZpWslS11jy",
        "is_local": false,
        "name": "Fantasias",
        "popularity": 92,
        "preview_url": "https://p.scdn.co/mp3-preview/930d66f49d44245621349c6b495e61c7eedff9b5?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6mAN61JH0dzyZpWslS11jy"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
              },
              "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
              "id": "4q3ewBCX7sLwd24euuV69X",
              "name": "Bad Bunny",
              "type": "artist",
              "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3fxzSn0ObgCjLadyR53ohN"
          },
          "href": "https://api.spotify.com/v1/albums/3fxzSn0ObgCjLadyR53ohN",
          "id": "3fxzSn0ObgCjLadyR53ohN",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/bd91c863f1a7c435295426722a8eee2b83891c70",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/82db26a0981303f39b8d8133a989321e32efb535",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/585fbe78b6317259f864deccdb928808e3753c2b",
              "width": 64
            }
          ],
          "name": "Vete",
          "release_date": "2019-11-21",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:3fxzSn0ObgCjLadyR53ohN"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 192024,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QMFME1914637"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5DxXgozhkPLgrbKFY91w0c"
        },
        "href": "https://api.spotify.com/v1/tracks/5DxXgozhkPLgrbKFY91w0c",
        "id": "5DxXgozhkPLgrbKFY91w0c",
        "is_local": false,
        "name": "Vete",
        "popularity": 93,
        "preview_url": "https://p.scdn.co/mp3-preview/2803e299f302d099cd11449e450d5bf21749fec5?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5DxXgozhkPLgrbKFY91w0c"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/5mcUbpuVL0i5q4cECQ6cV4"
          },
          "href": "https://api.spotify.com/v1/albums/5mcUbpuVL0i5q4cECQ6cV4",
          "id": "5mcUbpuVL0i5q4cECQ6cV4",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5355c438531755ff42144c9dc7d2f9c88598fb9b",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/cede4723ed2b2fc4d2efa18f199b74b9091f4a5b",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/f000f4becd556847f2f510fbbadffb79aa545b7d",
              "width": 64
            }
          ],
          "name": "Blanco",
          "release_date": "2019-11-15",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:5mcUbpuVL0i5q4cECQ6cV4"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 145800,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71922372"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2rc7BkzO8qepMFAxHtOrXc"
        },
        "href": "https://api.spotify.com/v1/tracks/2rc7BkzO8qepMFAxHtOrXc",
        "id": "2rc7BkzO8qepMFAxHtOrXc",
        "is_local": false,
        "name": "Blanco",
        "popularity": 88,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2rc7BkzO8qepMFAxHtOrXc"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1yxSLGMDHlW21z4YXirZDS"
              },
              "href": "https://api.spotify.com/v1/artists/1yxSLGMDHlW21z4YXirZDS",
              "id": "1yxSLGMDHlW21z4YXirZDS",
              "name": "The Black Eyed Peas",
              "type": "artist",
              "uri": "spotify:artist:1yxSLGMDHlW21z4YXirZDS"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6EobpC5SDFy5DF50dWNVGF"
          },
          "href": "https://api.spotify.com/v1/albums/6EobpC5SDFy5DF50dWNVGF",
          "id": "6EobpC5SDFy5DF50dWNVGF",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/924d09e38cbae5d1f55dd026e00c05df1c87625b",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/890e795473ec65f1ae35f7463a824dc1bc530f7f",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/90f3c09c37f82d3e2dab670a64882a70735e43fc",
              "width": 64
            }
          ],
          "name": "RITMO (Bad Boys For Life)",
          "release_date": "2019-10-12",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:6EobpC5SDFy5DF50dWNVGF"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1yxSLGMDHlW21z4YXirZDS"
            },
            "href": "https://api.spotify.com/v1/artists/1yxSLGMDHlW21z4YXirZDS",
            "id": "1yxSLGMDHlW21z4YXirZDS",
            "name": "The Black Eyed Peas",
            "type": "artist",
            "uri": "spotify:artist:1yxSLGMDHlW21z4YXirZDS"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 221714,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "USSM11912430"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6cy3ki60hLwimwIje7tALf"
        },
        "href": "https://api.spotify.com/v1/tracks/6cy3ki60hLwimwIje7tALf",
        "id": "6cy3ki60hLwimwIje7tALf",
        "is_local": false,
        "name": "RITMO (Bad Boys For Life)",
        "popularity": 96,
        "preview_url": "https://p.scdn.co/mp3-preview/60e9246623919cb164490957ba79af46ceabe237?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6cy3ki60hLwimwIje7tALf"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
              },
              "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
              "id": "4q3ewBCX7sLwd24euuV69X",
              "name": "Bad Bunny",
              "type": "artist",
              "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6ylFfzx32ICw4L1A7YWNLN"
          },
          "href": "https://api.spotify.com/v1/albums/6ylFfzx32ICw4L1A7YWNLN",
          "id": "6ylFfzx32ICw4L1A7YWNLN",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b2734891d9b25d8919448388f3bb",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e024891d9b25d8919448388f3bb",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d000048514891d9b25d8919448388f3bb",
              "width": 64
            }
          ],
          "name": "OASIS",
          "release_date": "2019-06-28",
          "release_date_precision": "day",
          "total_tracks": 8,
          "type": "album",
          "uri": "spotify:album:6ylFfzx32ICw4L1A7YWNLN"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 242573,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71911618"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0fea68AdmYNygeTGI4RC18"
        },
        "href": "https://api.spotify.com/v1/tracks/0fea68AdmYNygeTGI4RC18",
        "id": "0fea68AdmYNygeTGI4RC18",
        "is_local": false,
        "name": "LA CANCIÓN",
        "popularity": 90,
        "preview_url": null,
        "track": true,
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:0fea68AdmYNygeTGI4RC18"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2kqUKsTuEj1lPbm6BSn1AU"
              },
              "href": "https://api.spotify.com/v1/artists/2kqUKsTuEj1lPbm6BSn1AU",
              "id": "2kqUKsTuEj1lPbm6BSn1AU",
              "name": "Rich Music LTD",
              "type": "artist",
              "uri": "spotify:artist:2kqUKsTuEj1lPbm6BSn1AU"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
              },
              "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
              "id": "77ziqFxp5gaInVrF2lj4ht",
              "name": "Sech",
              "type": "artist",
              "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
              },
              "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
              "id": "0KPX4Ucy9dk82uj4GpKesn",
              "name": "Dalex",
              "type": "artist",
              "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1faqBAWocW4ZOe0OFjudGw"
          },
          "href": "https://api.spotify.com/v1/albums/1faqBAWocW4ZOe0OFjudGw",
          "id": "1faqBAWocW4ZOe0OFjudGw",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/921605d27fe1da77d1cbd3808c630c3f4e2f8425",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/79fb18e3b8a089dd7035cbb7311f2c67f509970f",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/927099a6fbdca56eccc9b2cf1e836885855b5e2c",
              "width": 64
            }
          ],
          "name": "The Academy",
          "release_date": "2019-10-11",
          "release_date_precision": "day",
          "total_tracks": 7,
          "type": "album",
          "uri": "spotify:album:1faqBAWocW4ZOe0OFjudGw"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2kqUKsTuEj1lPbm6BSn1AU"
            },
            "href": "https://api.spotify.com/v1/artists/2kqUKsTuEj1lPbm6BSn1AU",
            "id": "2kqUKsTuEj1lPbm6BSn1AU",
            "name": "Rich Music LTD",
            "type": "artist",
            "uri": "spotify:artist:2kqUKsTuEj1lPbm6BSn1AU"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/14zUHaJZo1mnYtn6IBRaRP"
            },
            "href": "https://api.spotify.com/v1/artists/14zUHaJZo1mnYtn6IBRaRP",
            "id": "14zUHaJZo1mnYtn6IBRaRP",
            "name": "Justin Quiles",
            "type": "artist",
            "uri": "spotify:artist:14zUHaJZo1mnYtn6IBRaRP"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
            },
            "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
            "id": "1pQWsZQehhS4wavwh7Fnxd",
            "name": "Lenny Tavárez",
            "type": "artist",
            "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2LRoIwlKmHjgvigdNGBHNo"
            },
            "href": "https://api.spotify.com/v1/artists/2LRoIwlKmHjgvigdNGBHNo",
            "id": "2LRoIwlKmHjgvigdNGBHNo",
            "name": "Feid",
            "type": "artist",
            "uri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3E6xrwgnVfYCrCs0ePERDz"
            },
            "href": "https://api.spotify.com/v1/artists/3E6xrwgnVfYCrCs0ePERDz",
            "id": "3E6xrwgnVfYCrCs0ePERDz",
            "name": "Wisin",
            "type": "artist",
            "uri": "spotify:artist:3E6xrwgnVfYCrCs0ePERDz"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pgDilWYDWLoOgGjf1iHNu"
            },
            "href": "https://api.spotify.com/v1/artists/1pgDilWYDWLoOgGjf1iHNu",
            "id": "1pgDilWYDWLoOgGjf1iHNu",
            "name": "Zion",
            "type": "artist",
            "uri": "spotify:artist:1pgDilWYDWLoOgGjf1iHNu"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 216066,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM9WM1900145"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5Id5B3dxJZhPcV9GzgYZZe"
        },
        "href": "https://api.spotify.com/v1/tracks/5Id5B3dxJZhPcV9GzgYZZe",
        "id": "5Id5B3dxJZhPcV9GzgYZZe",
        "is_local": false,
        "name": "Quizas",
        "popularity": 88,
        "preview_url": "https://p.scdn.co/mp3-preview/6981a658d2beb2cadfb7b361169a9e36b60441d9?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5Id5B3dxJZhPcV9GzgYZZe"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
              },
              "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
              "id": "2R21vXR83lH98kGeO99Y66",
              "name": "Anuel AA",
              "type": "artist",
              "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
              },
              "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
              "id": "4VMYDCV2IEDYJArk749S6m",
              "name": "Daddy Yankee",
              "type": "artist",
              "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/790FomKkXshlbRYZFtlgla"
              },
              "href": "https://api.spotify.com/v1/artists/790FomKkXshlbRYZFtlgla",
              "id": "790FomKkXshlbRYZFtlgla",
              "name": "KAROL G",
              "type": "artist",
              "uri": "spotify:artist:790FomKkXshlbRYZFtlgla"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1PTTAq0OxggVgqP5WTYWDh"
          },
          "href": "https://api.spotify.com/v1/albums/1PTTAq0OxggVgqP5WTYWDh",
          "id": "1PTTAq0OxggVgqP5WTYWDh",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b2735fa6dc9fc261344044c301a9",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e025fa6dc9fc261344044c301a9",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d000048515fa6dc9fc261344044c301a9",
              "width": 64
            }
          ],
          "name": "China",
          "release_date": "2019-07-19",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1PTTAq0OxggVgqP5WTYWDh"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
            },
            "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
            "id": "2R21vXR83lH98kGeO99Y66",
            "name": "Anuel AA",
            "type": "artist",
            "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
            },
            "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
            "id": "4VMYDCV2IEDYJArk749S6m",
            "name": "Daddy Yankee",
            "type": "artist",
            "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/790FomKkXshlbRYZFtlgla"
            },
            "href": "https://api.spotify.com/v1/artists/790FomKkXshlbRYZFtlgla",
            "id": "790FomKkXshlbRYZFtlgla",
            "name": "KAROL G",
            "type": "artist",
            "uri": "spotify:artist:790FomKkXshlbRYZFtlgla"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
            },
            "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
            "id": "1i8SpTcr7yvPOmcqrbnVXY",
            "name": "Ozuna",
            "type": "artist",
            "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 301714,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QM6P41952433"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2ksOAxtIxY8yElEWw8RhgK"
        },
        "href": "https://api.spotify.com/v1/tracks/2ksOAxtIxY8yElEWw8RhgK",
        "id": "2ksOAxtIxY8yElEWw8RhgK",
        "is_local": false,
        "name": "China",
        "popularity": 92,
        "preview_url": "https://p.scdn.co/mp3-preview/a2486b829160d65e2bf30038bb3a5f76df3393b1?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2ksOAxtIxY8yElEWw8RhgK"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0GM7qgcRCORpGnfcN2tCiB"
              },
              "href": "https://api.spotify.com/v1/artists/0GM7qgcRCORpGnfcN2tCiB",
              "id": "0GM7qgcRCORpGnfcN2tCiB",
              "name": "Tainy",
              "type": "artist",
              "uri": "spotify:artist:0GM7qgcRCORpGnfcN2tCiB"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
              },
              "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
              "id": "2R21vXR83lH98kGeO99Y66",
              "name": "Anuel AA",
              "type": "artist",
              "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
              },
              "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
              "id": "1i8SpTcr7yvPOmcqrbnVXY",
              "name": "Ozuna",
              "type": "artist",
              "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7nqA49hzXJWPH4cnM8nk6x"
          },
          "href": "https://api.spotify.com/v1/albums/7nqA49hzXJWPH4cnM8nk6x",
          "id": "7nqA49hzXJWPH4cnM8nk6x",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/0742e68c4eb73c4f523dc15092f0039160699959",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/73ad426477aca8a1e3dc2e208ce14506e0c2f7d5",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/cf7a68db70735b2ce74dfedbf2c2792acc63a6a8",
              "width": 64
            }
          ],
          "name": "Adicto (with Anuel AA & Ozuna)",
          "release_date": "2019-08-22",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:7nqA49hzXJWPH4cnM8nk6x"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0GM7qgcRCORpGnfcN2tCiB"
            },
            "href": "https://api.spotify.com/v1/artists/0GM7qgcRCORpGnfcN2tCiB",
            "id": "0GM7qgcRCORpGnfcN2tCiB",
            "name": "Tainy",
            "type": "artist",
            "uri": "spotify:artist:0GM7qgcRCORpGnfcN2tCiB"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
            },
            "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
            "id": "2R21vXR83lH98kGeO99Y66",
            "name": "Anuel AA",
            "type": "artist",
            "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
            },
            "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
            "id": "1i8SpTcr7yvPOmcqrbnVXY",
            "name": "Ozuna",
            "type": "artist",
            "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 270740,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71912751"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3jbT1Y5MoPwEIpZndDDwVq"
        },
        "href": "https://api.spotify.com/v1/tracks/3jbT1Y5MoPwEIpZndDDwVq",
        "id": "3jbT1Y5MoPwEIpZndDDwVq",
        "is_local": false,
        "name": "Adicto (with Anuel AA & Ozuna)",
        "popularity": 89,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:3jbT1Y5MoPwEIpZndDDwVq"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0EFisYRi20PTADoJrifHrz"
              },
              "href": "https://api.spotify.com/v1/artists/0EFisYRi20PTADoJrifHrz",
              "id": "0EFisYRi20PTADoJrifHrz",
              "name": "Jhay Cortez",
              "type": "artist",
              "uri": "spotify:artist:0EFisYRi20PTADoJrifHrz"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1V9QpD8kjA2iHCElhFGvlo"
          },
          "href": "https://api.spotify.com/v1/albums/1V9QpD8kjA2iHCElhFGvlo",
          "id": "1V9QpD8kjA2iHCElhFGvlo",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/b00042ed446d0d8e12d402bef5a27f5f9a89cdb2",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/1da6cb9545d4e9e0d69c3f1459fcce0b8be81758",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/7c1abc03d7ec0746cea67364305bb40587b542ab",
              "width": 64
            }
          ],
          "name": "Famouz",
          "release_date": "2019-05-24",
          "release_date_precision": "day",
          "total_tracks": 13,
          "type": "album",
          "uri": "spotify:album:1V9QpD8kjA2iHCElhFGvlo"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0EFisYRi20PTADoJrifHrz"
            },
            "href": "https://api.spotify.com/v1/artists/0EFisYRi20PTADoJrifHrz",
            "id": "0EFisYRi20PTADoJrifHrz",
            "name": "Jhay Cortez",
            "type": "artist",
            "uri": "spotify:artist:0EFisYRi20PTADoJrifHrz"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 309120,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71908293"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4R8BJggjosTswLxtkw8V7P"
        },
        "href": "https://api.spotify.com/v1/tracks/4R8BJggjosTswLxtkw8V7P",
        "id": "4R8BJggjosTswLxtkw8V7P",
        "is_local": false,
        "name": "No Me Conoce - Remix",
        "popularity": 86,
        "preview_url": null,
        "track": true,
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:4R8BJggjosTswLxtkw8V7P"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
              },
              "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
              "id": "0KPX4Ucy9dk82uj4GpKesn",
              "name": "Dalex",
              "type": "artist",
              "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
              },
              "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
              "id": "1pQWsZQehhS4wavwh7Fnxd",
              "name": "Lenny Tavárez",
              "type": "artist",
              "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7FNnA9vBm6EKceENgCGRMb"
              },
              "href": "https://api.spotify.com/v1/artists/7FNnA9vBm6EKceENgCGRMb",
              "id": "7FNnA9vBm6EKceENgCGRMb",
              "name": "Anitta",
              "type": "artist",
              "uri": "spotify:artist:7FNnA9vBm6EKceENgCGRMb"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/5dXeJdc2hib8JB3Vqon2zB"
          },
          "href": "https://api.spotify.com/v1/albums/5dXeJdc2hib8JB3Vqon2zB",
          "id": "5dXeJdc2hib8JB3Vqon2zB",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/e3557652c105d966e98028f7cfdfe659e340e23f",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/67c80cf1a6d538437a4826ca2fd4f4ccb8ab5b1b",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/3e52f332f1dc6813f188bf34148402bf17f56197",
              "width": 64
            }
          ],
          "name": "Bellaquita (Remix)",
          "release_date": "2019-11-22",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:5dXeJdc2hib8JB3Vqon2zB"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
            },
            "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
            "id": "1pQWsZQehhS4wavwh7Fnxd",
            "name": "Lenny Tavárez",
            "type": "artist",
            "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7FNnA9vBm6EKceENgCGRMb"
            },
            "href": "https://api.spotify.com/v1/artists/7FNnA9vBm6EKceENgCGRMb",
            "id": "7FNnA9vBm6EKceENgCGRMb",
            "name": "Anitta",
            "type": "artist",
            "uri": "spotify:artist:7FNnA9vBm6EKceENgCGRMb"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1GDbiv3spRmZ1XdM1jQbT7"
            },
            "href": "https://api.spotify.com/v1/artists/1GDbiv3spRmZ1XdM1jQbT7",
            "id": "1GDbiv3spRmZ1XdM1jQbT7",
            "name": "Natti Natasha",
            "type": "artist",
            "uri": "spotify:artist:1GDbiv3spRmZ1XdM1jQbT7"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/14zUHaJZo1mnYtn6IBRaRP"
            },
            "href": "https://api.spotify.com/v1/artists/14zUHaJZo1mnYtn6IBRaRP",
            "id": "14zUHaJZo1mnYtn6IBRaRP",
            "name": "Justin Quiles",
            "type": "artist",
            "uri": "spotify:artist:14zUHaJZo1mnYtn6IBRaRP"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 304733,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM9WM1900167"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1Xnn1TPyr5h0hpRAT4B4EA"
        },
        "href": "https://api.spotify.com/v1/tracks/1Xnn1TPyr5h0hpRAT4B4EA",
        "id": "1Xnn1TPyr5h0hpRAT4B4EA",
        "is_local": false,
        "name": "Bellaquita - Remix",
        "popularity": 87,
        "preview_url": "https://p.scdn.co/mp3-preview/f778ddbb1ad3a932f35d23b62150690c1baa5bd7?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:1Xnn1TPyr5h0hpRAT4B4EA"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7a0XAaPaK2aDSqa8p3QnC7"
              },
              "href": "https://api.spotify.com/v1/artists/7a0XAaPaK2aDSqa8p3QnC7",
              "id": "7a0XAaPaK2aDSqa8p3QnC7",
              "name": "Beéle",
              "type": "artist",
              "uri": "spotify:artist:7a0XAaPaK2aDSqa8p3QnC7"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1uFr2PCsnDVZ71AiJnZYrb"
          },
          "href": "https://api.spotify.com/v1/albums/1uFr2PCsnDVZ71AiJnZYrb",
          "id": "1uFr2PCsnDVZ71AiJnZYrb",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/94b173c3581f177cd3f22397b2eac69263a56aa2",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/52d7a3a4f5719ae77bc26597e0f93f5c5c1fc6e7",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/0a4e7980abde2cde89d7db2962af97a70ab9b06d",
              "width": 64
            }
          ],
          "name": "Loco",
          "release_date": "2019-08-08",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1uFr2PCsnDVZ71AiJnZYrb"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7a0XAaPaK2aDSqa8p3QnC7"
            },
            "href": "https://api.spotify.com/v1/artists/7a0XAaPaK2aDSqa8p3QnC7",
            "id": "7a0XAaPaK2aDSqa8p3QnC7",
            "name": "Beéle",
            "type": "artist",
            "uri": "spotify:artist:7a0XAaPaK2aDSqa8p3QnC7"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 204000,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "TCAEJ1943714"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2J9B63FawlTaPdg4eH5X03"
        },
        "href": "https://api.spotify.com/v1/tracks/2J9B63FawlTaPdg4eH5X03",
        "id": "2J9B63FawlTaPdg4eH5X03",
        "is_local": false,
        "name": "Loco",
        "popularity": 80,
        "preview_url": "https://p.scdn.co/mp3-preview/8f0e0583206ca11a381f0d6ce38a528f62289ddb?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2J9B63FawlTaPdg4eH5X03"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0EmeFodog0BfCgMzAIvKQp"
              },
              "href": "https://api.spotify.com/v1/artists/0EmeFodog0BfCgMzAIvKQp",
              "id": "0EmeFodog0BfCgMzAIvKQp",
              "name": "Shakira",
              "type": "artist",
              "uri": "spotify:artist:0EmeFodog0BfCgMzAIvKQp"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
              },
              "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
              "id": "2R21vXR83lH98kGeO99Y66",
              "name": "Anuel AA",
              "type": "artist",
              "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/4IcQ1ni07PmlOenqwf6MgG"
          },
          "href": "https://api.spotify.com/v1/albums/4IcQ1ni07PmlOenqwf6MgG",
          "id": "4IcQ1ni07PmlOenqwf6MgG",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/923c415e082d033a2fcc51bcb5759d4fd667257c",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/f937488d8ac19c86944858b5aaf635ce6b7d43b6",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/7496c43041ea85528ab4cbf32537c6ddaa1d7258",
              "width": 64
            }
          ],
          "name": "Me Gusta",
          "release_date": "2020-01-13",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:4IcQ1ni07PmlOenqwf6MgG"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0EmeFodog0BfCgMzAIvKQp"
            },
            "href": "https://api.spotify.com/v1/artists/0EmeFodog0BfCgMzAIvKQp",
            "id": "0EmeFodog0BfCgMzAIvKQp",
            "name": "Shakira",
            "type": "artist",
            "uri": "spotify:artist:0EmeFodog0BfCgMzAIvKQp"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
            },
            "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
            "id": "2R21vXR83lH98kGeO99Y66",
            "name": "Anuel AA",
            "type": "artist",
            "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 190570,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USQX92000112"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5Xhqh4lwJPtMUTsdBztN1a"
        },
        "href": "https://api.spotify.com/v1/tracks/5Xhqh4lwJPtMUTsdBztN1a",
        "id": "5Xhqh4lwJPtMUTsdBztN1a",
        "is_local": false,
        "name": "Me Gusta",
        "popularity": 86,
        "preview_url": "https://p.scdn.co/mp3-preview/5192e13f69683dae143271829cede1ab62724078?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5Xhqh4lwJPtMUTsdBztN1a"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7iK8PXO48WeuP03g8YR51W"
              },
              "href": "https://api.spotify.com/v1/artists/7iK8PXO48WeuP03g8YR51W",
              "id": "7iK8PXO48WeuP03g8YR51W",
              "name": "Myke Towers",
              "type": "artist",
              "uri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3dM5WCvdXdNqLE14d16GmJ"
          },
          "href": "https://api.spotify.com/v1/albums/3dM5WCvdXdNqLE14d16GmJ",
          "id": "3dM5WCvdXdNqLE14d16GmJ",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/bec001cd97e20e2440207f6cd59439e2b19c9485",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/0b85f230d2a3fae5640836b922d0dad6dcfbf14f",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/5c89591139cc0188742f305e0122a4b7ff2bf8f3",
              "width": 64
            }
          ],
          "name": "Easy Money Baby",
          "release_date": "2020-01-24",
          "release_date_precision": "day",
          "total_tracks": 18,
          "type": "album",
          "uri": "spotify:album:3dM5WCvdXdNqLE14d16GmJ"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7iK8PXO48WeuP03g8YR51W"
            },
            "href": "https://api.spotify.com/v1/artists/7iK8PXO48WeuP03g8YR51W",
            "id": "7iK8PXO48WeuP03g8YR51W",
            "name": "Myke Towers",
            "type": "artist",
            "uri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 186426,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM4TW2040254"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/43NqTeL8pgBxKHPMiJKUP5"
        },
        "href": "https://api.spotify.com/v1/tracks/43NqTeL8pgBxKHPMiJKUP5",
        "id": "43NqTeL8pgBxKHPMiJKUP5",
        "is_local": false,
        "name": "Girl",
        "popularity": 73,
        "preview_url": "https://p.scdn.co/mp3-preview/4ae37e956c60463cd52d3251c3ecca93dad4120e?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 10,
        "type": "track",
        "uri": "spotify:track:43NqTeL8pgBxKHPMiJKUP5"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
              },
              "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
              "id": "4SsVbpTthjScTS7U2hmr1X",
              "name": "Arcangel",
              "type": "artist",
              "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0CPLMVp7rMi3BkzAMve96K"
          },
          "href": "https://api.spotify.com/v1/albums/0CPLMVp7rMi3BkzAMve96K",
          "id": "0CPLMVp7rMi3BkzAMve96K",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/2603cc5bad6175fc4c5418f3f6000571d817115e",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/e2b9297466a8178e1683495f7ca711e673d45dfe",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/e5bd8b2563984faccf82381cabea23a02630d4bc",
              "width": 64
            }
          ],
          "name": "Historias de un Capricornio",
          "release_date": "2019-12-20",
          "release_date_precision": "day",
          "total_tracks": 15,
          "type": "album",
          "uri": "spotify:album:0CPLMVp7rMi3BkzAMve96K"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
            },
            "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
            "id": "4SsVbpTthjScTS7U2hmr1X",
            "name": "Arcangel",
            "type": "artist",
            "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 221103,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QMFME1989811"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4z6wo6PJG4Fve45OXK6D9m"
        },
        "href": "https://api.spotify.com/v1/tracks/4z6wo6PJG4Fve45OXK6D9m",
        "id": "4z6wo6PJG4Fve45OXK6D9m",
        "is_local": false,
        "name": "Infeliz",
        "popularity": 85,
        "preview_url": "https://p.scdn.co/mp3-preview/0b2ecaf8a9bb1cae2fe805eed0b1ef96ffc70541?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:4z6wo6PJG4Fve45OXK6D9m"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
              },
              "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
              "id": "1SupJlEpv7RS2tPNRaHViT",
              "name": "Nicky Jam",
              "type": "artist",
              "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1CYQlkKE5Q0khU6eMwVAVt"
          },
          "href": "https://api.spotify.com/v1/albums/1CYQlkKE5Q0khU6eMwVAVt",
          "id": "1CYQlkKE5Q0khU6eMwVAVt",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/90b05a542c028a68c0b08f9f2ae88b36b61a5bf3",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/a804785c4706218dea64e3cc7d928db08d52c0d1",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/5a3e430528c2bc1ac0a2c0a1a54ee980f6213391",
              "width": 64
            }
          ],
          "name": "Intimo",
          "release_date": "2019-11-01",
          "release_date_precision": "day",
          "total_tracks": 15,
          "type": "album",
          "uri": "spotify:album:1CYQlkKE5Q0khU6eMwVAVt"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
            },
            "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
            "id": "1SupJlEpv7RS2tPNRaHViT",
            "name": "Nicky Jam",
            "type": "artist",
            "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
            },
            "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
            "id": "2R21vXR83lH98kGeO99Y66",
            "name": "Anuel AA",
            "type": "artist",
            "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 215459,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSD11900378"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2pWOMNQJW3g2zmGjP0Vkb0"
        },
        "href": "https://api.spotify.com/v1/tracks/2pWOMNQJW3g2zmGjP0Vkb0",
        "id": "2pWOMNQJW3g2zmGjP0Vkb0",
        "is_local": false,
        "name": "Whine Up",
        "popularity": 90,
        "preview_url": "https://p.scdn.co/mp3-preview/c455bf2ed715a49c3904091ec005d8001ad8ec30?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 3,
        "type": "track",
        "uri": "spotify:track:2pWOMNQJW3g2zmGjP0Vkb0"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
              },
              "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
              "id": "4q3ewBCX7sLwd24euuV69X",
              "name": "Bad Bunny",
              "type": "artist",
              "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0GM7qgcRCORpGnfcN2tCiB"
              },
              "href": "https://api.spotify.com/v1/artists/0GM7qgcRCORpGnfcN2tCiB",
              "id": "0GM7qgcRCORpGnfcN2tCiB",
              "name": "Tainy",
              "type": "artist",
              "uri": "spotify:artist:0GM7qgcRCORpGnfcN2tCiB"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/06S3Qjh4QWLtn6c7CVhYh7"
          },
          "href": "https://api.spotify.com/v1/albums/06S3Qjh4QWLtn6c7CVhYh7",
          "id": "06S3Qjh4QWLtn6c7CVhYh7",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/182e289afc639f69fbbe33448c97e749d48894a6",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/4923d440991830ab3a9fec7b2345df16a642287b",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/25c85118c4a9a96f160407d4ef9c82bfe175c58f",
              "width": 64
            }
          ],
          "name": "Callaita",
          "release_date": "2019-05-31",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:06S3Qjh4QWLtn6c7CVhYh7"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0GM7qgcRCORpGnfcN2tCiB"
            },
            "href": "https://api.spotify.com/v1/artists/0GM7qgcRCORpGnfcN2tCiB",
            "id": "0GM7qgcRCORpGnfcN2tCiB",
            "name": "Tainy",
            "type": "artist",
            "uri": "spotify:artist:0GM7qgcRCORpGnfcN2tCiB"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 250533,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM6N21919851"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2TH65lNHgvLxCKXM3apjxI"
        },
        "href": "https://api.spotify.com/v1/tracks/2TH65lNHgvLxCKXM3apjxI",
        "id": "2TH65lNHgvLxCKXM3apjxI",
        "is_local": false,
        "name": "Callaita",
        "popularity": 90,
        "preview_url": "https://p.scdn.co/mp3-preview/23c0b25cf824c1bfd7a814fe7cd1264c31a5a9dc?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2TH65lNHgvLxCKXM3apjxI"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
              },
              "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
              "id": "1SupJlEpv7RS2tPNRaHViT",
              "name": "Nicky Jam",
              "type": "artist",
              "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
              },
              "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
              "id": "4VMYDCV2IEDYJArk749S6m",
              "name": "Daddy Yankee",
              "type": "artist",
              "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6sTdi5hrN3uFhARaqbikjG"
          },
          "href": "https://api.spotify.com/v1/albums/6sTdi5hrN3uFhARaqbikjG",
          "id": "6sTdi5hrN3uFhARaqbikjG",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/c4a63733a1ae8322a71144cc9c49145320d1b98e",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/6e50fce786ab67b73b290e21e35fb101688642c4",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/2a8377ecd2435175be94926c6ee4abb8d74dfa3b",
              "width": 64
            }
          ],
          "name": "Muévelo",
          "release_date": "2020-01-08",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:6sTdi5hrN3uFhARaqbikjG"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
            },
            "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
            "id": "1SupJlEpv7RS2tPNRaHViT",
            "name": "Nicky Jam",
            "type": "artist",
            "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
            },
            "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
            "id": "4VMYDCV2IEDYJArk749S6m",
            "name": "Daddy Yankee",
            "type": "artist",
            "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 194892,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSD11900363"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4VgYtXCVJ7IbWAZ5ryfvEQ"
        },
        "href": "https://api.spotify.com/v1/tracks/4VgYtXCVJ7IbWAZ5ryfvEQ",
        "id": "4VgYtXCVJ7IbWAZ5ryfvEQ",
        "is_local": false,
        "name": "Muévelo",
        "popularity": 87,
        "preview_url": "https://p.scdn.co/mp3-preview/a288f3bb79069c08738c470fe22bc5f6a6ae1d39?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:4VgYtXCVJ7IbWAZ5ryfvEQ"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1phfTBIocBW3UwqcYjaEN6"
              },
              "href": "https://api.spotify.com/v1/artists/1phfTBIocBW3UwqcYjaEN6",
              "id": "1phfTBIocBW3UwqcYjaEN6",
              "name": "Mike Bahía",
              "type": "artist",
              "uri": "spotify:artist:1phfTBIocBW3UwqcYjaEN6"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3UbZvsLswQE2L5mBiGlzO0"
          },
          "href": "https://api.spotify.com/v1/albums/3UbZvsLswQE2L5mBiGlzO0",
          "id": "3UbZvsLswQE2L5mBiGlzO0",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/190999a55ca05d7b196bf066bf978d797dffe389",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/459c647abff90e759b2f39fee58be25a20c43ecd",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/d60169a4f398517acfc96e1d8b7c1ac1638612d6",
              "width": 64
            }
          ],
          "name": "Navegando",
          "release_date": "2019-11-15",
          "release_date_precision": "day",
          "total_tracks": 11,
          "type": "album",
          "uri": "spotify:album:3UbZvsLswQE2L5mBiGlzO0"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1phfTBIocBW3UwqcYjaEN6"
            },
            "href": "https://api.spotify.com/v1/artists/1phfTBIocBW3UwqcYjaEN6",
            "id": "1phfTBIocBW3UwqcYjaEN6",
            "name": "Mike Bahía",
            "type": "artist",
            "uri": "spotify:artist:1phfTBIocBW3UwqcYjaEN6"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5H1nN1SzW0qNeUEZvuXjAj"
            },
            "href": "https://api.spotify.com/v1/artists/5H1nN1SzW0qNeUEZvuXjAj",
            "id": "5H1nN1SzW0qNeUEZvuXjAj",
            "name": "Danny Ocean",
            "type": "artist",
            "uri": "spotify:artist:5H1nN1SzW0qNeUEZvuXjAj"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 181845,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "MXF151900373"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0x1k6gSTSxaLxe0F2IThaX"
        },
        "href": "https://api.spotify.com/v1/tracks/0x1k6gSTSxaLxe0F2IThaX",
        "id": "0x1k6gSTSxaLxe0F2IThaX",
        "is_local": false,
        "name": "Detente",
        "popularity": 79,
        "preview_url": "https://p.scdn.co/mp3-preview/dc295bfc5402d73631af4b53437008d743319e4f?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 3,
        "type": "track",
        "uri": "spotify:track:0x1k6gSTSxaLxe0F2IThaX"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0vR2qb8m9WHeZ5ByCbimq2"
              },
              "href": "https://api.spotify.com/v1/artists/0vR2qb8m9WHeZ5ByCbimq2",
              "id": "0vR2qb8m9WHeZ5ByCbimq2",
              "name": "Reik",
              "type": "artist",
              "uri": "spotify:artist:0vR2qb8m9WHeZ5ByCbimq2"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1GAymyGBvB4gQy5Z5LZ1Wj"
              },
              "href": "https://api.spotify.com/v1/artists/1GAymyGBvB4gQy5Z5LZ1Wj",
              "id": "1GAymyGBvB4gQy5Z5LZ1Wj",
              "name": "Lalo Ebratt",
              "type": "artist",
              "uri": "spotify:artist:1GAymyGBvB4gQy5Z5LZ1Wj"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/4qecT0ZJrf35thz2WaEm6P"
          },
          "href": "https://api.spotify.com/v1/albums/4qecT0ZJrf35thz2WaEm6P",
          "id": "4qecT0ZJrf35thz2WaEm6P",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5666bdf4a07cefa612997de9f20b1342502a1c6b",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/4d5609be0d960b2d8277158456f6250abc47e0a5",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/8d57376c9b0d836393a695bd6ed950769d8a6bf9",
              "width": 64
            }
          ],
          "name": "Indeciso",
          "release_date": "2019-08-23",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:4qecT0ZJrf35thz2WaEm6P"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0vR2qb8m9WHeZ5ByCbimq2"
            },
            "href": "https://api.spotify.com/v1/artists/0vR2qb8m9WHeZ5ByCbimq2",
            "id": "0vR2qb8m9WHeZ5ByCbimq2",
            "name": "Reik",
            "type": "artist",
            "uri": "spotify:artist:0vR2qb8m9WHeZ5ByCbimq2"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1GAymyGBvB4gQy5Z5LZ1Wj"
            },
            "href": "https://api.spotify.com/v1/artists/1GAymyGBvB4gQy5Z5LZ1Wj",
            "id": "1GAymyGBvB4gQy5Z5LZ1Wj",
            "name": "Lalo Ebratt",
            "type": "artist",
            "uri": "spotify:artist:1GAymyGBvB4gQy5Z5LZ1Wj"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 217253,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71915898"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/59s0s39NFWScuHDbHytI14"
        },
        "href": "https://api.spotify.com/v1/tracks/59s0s39NFWScuHDbHytI14",
        "id": "59s0s39NFWScuHDbHytI14",
        "is_local": false,
        "name": "Indeciso",
        "popularity": 88,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:59s0s39NFWScuHDbHytI14"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
              },
              "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
              "id": "77ziqFxp5gaInVrF2lj4ht",
              "name": "Sech",
              "type": "artist",
              "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
              },
              "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
              "id": "1i8SpTcr7yvPOmcqrbnVXY",
              "name": "Ozuna",
              "type": "artist",
              "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/2S6p0g6YzG3609Ty45i5Cq"
          },
          "href": "https://api.spotify.com/v1/albums/2S6p0g6YzG3609Ty45i5Cq",
          "id": "2S6p0g6YzG3609Ty45i5Cq",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/611dca931644449e5d131d8fbba514f88c8c36f1",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/0f2ba1bae9a9afb487e0012b8083151b637d615d",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/b73b2bf30cd28ac5fb9f6dd728c1467e235edc77",
              "width": 64
            }
          ],
          "name": "Si Te Vas",
          "release_date": "2019-09-26",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:2S6p0g6YzG3609Ty45i5Cq"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
            },
            "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
            "id": "1i8SpTcr7yvPOmcqrbnVXY",
            "name": "Ozuna",
            "type": "artist",
            "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 204906,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "QM9WM1900143"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6Y4PDQv4XjYjHLeLmvyOt0"
        },
        "href": "https://api.spotify.com/v1/tracks/6Y4PDQv4XjYjHLeLmvyOt0",
        "id": "6Y4PDQv4XjYjHLeLmvyOt0",
        "is_local": false,
        "name": "Si Te Vas",
        "popularity": 87,
        "preview_url": "https://p.scdn.co/mp3-preview/5cb4ad4d3ffe549979c79007dd7437211affb89b?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6Y4PDQv4XjYjHLeLmvyOt0"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
              },
              "href": "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
              "id": "6qqNVTkY8uBg9cP3Jd7DAH",
              "name": "Billie Eilish",
              "type": "artist",
              "uri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0S0KGZnfBGSIssfF54WSJh"
          },
          "href": "https://api.spotify.com/v1/albums/0S0KGZnfBGSIssfF54WSJh",
          "id": "0S0KGZnfBGSIssfF54WSJh",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/cd89c09ece48d687d4b6a894e28300064ade5512",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/e31ade267f31182d0690ee9debefaabfefc29860",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ed409b4be5bdf96fd451d7d1455b0667a3c6999c",
              "width": 64
            }
          ],
          "name": "WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?",
          "release_date": "2019-03-29",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:0S0KGZnfBGSIssfF54WSJh"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
            },
            "href": "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
            "id": "6qqNVTkY8uBg9cP3Jd7DAH",
            "name": "Billie Eilish",
            "type": "artist",
            "uri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 194087,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71900764"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2Fxmhks0bxGSBdJ92vM42m"
        },
        "href": "https://api.spotify.com/v1/tracks/2Fxmhks0bxGSBdJ92vM42m",
        "id": "2Fxmhks0bxGSBdJ92vM42m",
        "is_local": false,
        "name": "bad guy",
        "popularity": 95,
        "preview_url": null,
        "track": true,
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:2Fxmhks0bxGSBdJ92vM42m"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/47MpMsUfWtgyIIBEFOr4FE"
              },
              "href": "https://api.spotify.com/v1/artists/47MpMsUfWtgyIIBEFOr4FE",
              "id": "47MpMsUfWtgyIIBEFOr4FE",
              "name": "Lunay",
              "type": "artist",
              "uri": "spotify:artist:47MpMsUfWtgyIIBEFOr4FE"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/46xbsFOp9g1WqTidQEs7YT"
          },
          "href": "https://api.spotify.com/v1/albums/46xbsFOp9g1WqTidQEs7YT",
          "id": "46xbsFOp9g1WqTidQEs7YT",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/7d8bcb83a8f44da61d358964af9695189807dab6",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/954f83113d09edf0c8115db4beba654b1ef5f2ad",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/d29072867f72417727b467bd2539328e2edeee57",
              "width": 64
            }
          ],
          "name": "Épico",
          "release_date": "2019-10-25",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:46xbsFOp9g1WqTidQEs7YT"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/47MpMsUfWtgyIIBEFOr4FE"
            },
            "href": "https://api.spotify.com/v1/artists/47MpMsUfWtgyIIBEFOr4FE",
            "id": "47MpMsUfWtgyIIBEFOr4FE",
            "name": "Lunay",
            "type": "artist",
            "uri": "spotify:artist:47MpMsUfWtgyIIBEFOr4FE"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
            },
            "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
            "id": "1i8SpTcr7yvPOmcqrbnVXY",
            "name": "Ozuna",
            "type": "artist",
            "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2R21vXR83lH98kGeO99Y66"
            },
            "href": "https://api.spotify.com/v1/artists/2R21vXR83lH98kGeO99Y66",
            "id": "2R21vXR83lH98kGeO99Y66",
            "name": "Anuel AA",
            "type": "artist",
            "uri": "spotify:artist:2R21vXR83lH98kGeO99Y66"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 217129,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USA2P1955936"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/37zdqI4r1gswIzczSBkRon"
        },
        "href": "https://api.spotify.com/v1/tracks/37zdqI4r1gswIzczSBkRon",
        "id": "37zdqI4r1gswIzczSBkRon",
        "is_local": false,
        "name": "Aventura",
        "popularity": 88,
        "preview_url": "https://p.scdn.co/mp3-preview/c8aff04a7560fa6b626882ff4a171995e6e5f19b?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:37zdqI4r1gswIzczSBkRon"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
              },
              "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
              "id": "4q3ewBCX7sLwd24euuV69X",
              "name": "Bad Bunny",
              "type": "artist",
              "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6ylFfzx32ICw4L1A7YWNLN"
          },
          "href": "https://api.spotify.com/v1/albums/6ylFfzx32ICw4L1A7YWNLN",
          "id": "6ylFfzx32ICw4L1A7YWNLN",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b2734891d9b25d8919448388f3bb",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e024891d9b25d8919448388f3bb",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d000048514891d9b25d8919448388f3bb",
              "width": 64
            }
          ],
          "name": "OASIS",
          "release_date": "2019-06-28",
          "release_date_precision": "day",
          "total_tracks": 8,
          "type": "album",
          "uri": "spotify:album:6ylFfzx32ICw4L1A7YWNLN"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 222346,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71912318"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/25ZAibhr3bdlMCLmubZDVt"
        },
        "href": "https://api.spotify.com/v1/tracks/25ZAibhr3bdlMCLmubZDVt",
        "id": "25ZAibhr3bdlMCLmubZDVt",
        "is_local": false,
        "name": "QUE PRETENDES",
        "popularity": 86,
        "preview_url": null,
        "track": true,
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:25ZAibhr3bdlMCLmubZDVt"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6M2wZ9GZgrQXHCFfjv46we"
              },
              "href": "https://api.spotify.com/v1/artists/6M2wZ9GZgrQXHCFfjv46we",
              "id": "6M2wZ9GZgrQXHCFfjv46we",
              "name": "Dua Lipa",
              "type": "artist",
              "uri": "spotify:artist:6M2wZ9GZgrQXHCFfjv46we"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0ix3XtPV1LwmZADsprKxcp"
          },
          "href": "https://api.spotify.com/v1/albums/0ix3XtPV1LwmZADsprKxcp",
          "id": "0ix3XtPV1LwmZADsprKxcp",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/6d61103bd4043701d6cd230a02fa43d916c4f144",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/a8b8d0bd26dc496f5b9ea65994172c5d541aa1b9",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/7e8a124b56cfaf3e0cb1d882f79d47cdd0bccd93",
              "width": 64
            }
          ],
          "name": "Don't Start Now",
          "release_date": "2019-10-31",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:0ix3XtPV1LwmZADsprKxcp"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6M2wZ9GZgrQXHCFfjv46we"
            },
            "href": "https://api.spotify.com/v1/artists/6M2wZ9GZgrQXHCFfjv46we",
            "id": "6M2wZ9GZgrQXHCFfjv46we",
            "name": "Dua Lipa",
            "type": "artist",
            "uri": "spotify:artist:6M2wZ9GZgrQXHCFfjv46we"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 183290,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "GBAHT1901121"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6WrI0LAC5M1Rw2MnX2ZvEg"
        },
        "href": "https://api.spotify.com/v1/tracks/6WrI0LAC5M1Rw2MnX2ZvEg",
        "id": "6WrI0LAC5M1Rw2MnX2ZvEg",
        "is_local": false,
        "name": "Don't Start Now",
        "popularity": 97,
        "preview_url": "https://p.scdn.co/mp3-preview/ed151225213380a41e5c4af00ff558e25b5875d1?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6WrI0LAC5M1Rw2MnX2ZvEg"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7hIqJfRYGBWWT1Qxu6Cpd2"
              },
              "href": "https://api.spotify.com/v1/artists/7hIqJfRYGBWWT1Qxu6Cpd2",
              "id": "7hIqJfRYGBWWT1Qxu6Cpd2",
              "name": "Andy Rivera",
              "type": "artist",
              "uri": "spotify:artist:7hIqJfRYGBWWT1Qxu6Cpd2"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/5TDSNRe3rVLJhxjIhxfcUx"
              },
              "href": "https://api.spotify.com/v1/artists/5TDSNRe3rVLJhxjIhxfcUx",
              "id": "5TDSNRe3rVLJhxjIhxfcUx",
              "name": "Jhonny Rivera",
              "type": "artist",
              "uri": "spotify:artist:5TDSNRe3rVLJhxjIhxfcUx"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/3SN7I8KV2qBwTCZ4aNDcbS"
              },
              "href": "https://api.spotify.com/v1/artists/3SN7I8KV2qBwTCZ4aNDcbS",
              "id": "3SN7I8KV2qBwTCZ4aNDcbS",
              "name": "Jessi Uribe",
              "type": "artist",
              "uri": "spotify:artist:3SN7I8KV2qBwTCZ4aNDcbS"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/79WB96tQV9vPJ920cbneZ9"
          },
          "href": "https://api.spotify.com/v1/albums/79WB96tQV9vPJ920cbneZ9",
          "id": "79WB96tQV9vPJ920cbneZ9",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/8b3d64adb9a3354904632e66f6b1d53ccc13c0c1",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/3453158ab94e0c6feecb8ef61e07fb7331d1e52d",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/8c27e6695077866303e73713bfb17923e6f6daa1",
              "width": 64
            }
          ],
          "name": "Alguien Me Gusta",
          "release_date": "2019-09-19",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:79WB96tQV9vPJ920cbneZ9"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7hIqJfRYGBWWT1Qxu6Cpd2"
            },
            "href": "https://api.spotify.com/v1/artists/7hIqJfRYGBWWT1Qxu6Cpd2",
            "id": "7hIqJfRYGBWWT1Qxu6Cpd2",
            "name": "Andy Rivera",
            "type": "artist",
            "uri": "spotify:artist:7hIqJfRYGBWWT1Qxu6Cpd2"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5TDSNRe3rVLJhxjIhxfcUx"
            },
            "href": "https://api.spotify.com/v1/artists/5TDSNRe3rVLJhxjIhxfcUx",
            "id": "5TDSNRe3rVLJhxjIhxfcUx",
            "name": "Jhonny Rivera",
            "type": "artist",
            "uri": "spotify:artist:5TDSNRe3rVLJhxjIhxfcUx"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3SN7I8KV2qBwTCZ4aNDcbS"
            },
            "href": "https://api.spotify.com/v1/artists/3SN7I8KV2qBwTCZ4aNDcbS",
            "id": "3SN7I8KV2qBwTCZ4aNDcbS",
            "name": "Jessi Uribe",
            "type": "artist",
            "uri": "spotify:artist:3SN7I8KV2qBwTCZ4aNDcbS"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 168533,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "COSO11900298"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4iFTIshL0xDCw8JJUl5AJ3"
        },
        "href": "https://api.spotify.com/v1/tracks/4iFTIshL0xDCw8JJUl5AJ3",
        "id": "4iFTIshL0xDCw8JJUl5AJ3",
        "is_local": false,
        "name": "Alguien Me Gusta",
        "popularity": 70,
        "preview_url": "https://p.scdn.co/mp3-preview/9ff74fd77a6599c56708fcd38d566139e40764f4?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:4iFTIshL0xDCw8JJUl5AJ3"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4bw2Am3p9ji3mYsXNXtQcd"
              },
              "href": "https://api.spotify.com/v1/artists/4bw2Am3p9ji3mYsXNXtQcd",
              "id": "4bw2Am3p9ji3mYsXNXtQcd",
              "name": "Piso 21",
              "type": "artist",
              "uri": "spotify:artist:4bw2Am3p9ji3mYsXNXtQcd"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0XwVARXT135rw8lyw1EeWP"
              },
              "href": "https://api.spotify.com/v1/artists/0XwVARXT135rw8lyw1EeWP",
              "id": "0XwVARXT135rw8lyw1EeWP",
              "name": "Christian Nodal",
              "type": "artist",
              "uri": "spotify:artist:0XwVARXT135rw8lyw1EeWP"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6NSiAkMa61CjJI9AHqOhuZ"
          },
          "href": "https://api.spotify.com/v1/albums/6NSiAkMa61CjJI9AHqOhuZ",
          "id": "6NSiAkMa61CjJI9AHqOhuZ",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5e350b5b4b8323e4c473a8070ef8c7df6ee36788",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/40fd30763826eb5a62b4e00d0fab1cfa923660ef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/7850cf1e9ca78a7b14ad957d393da22365cec97b",
              "width": 64
            }
          ],
          "name": "Pa' Olvidarme De Ella",
          "release_date": "2019-09-06",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:6NSiAkMa61CjJI9AHqOhuZ"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4bw2Am3p9ji3mYsXNXtQcd"
            },
            "href": "https://api.spotify.com/v1/artists/4bw2Am3p9ji3mYsXNXtQcd",
            "id": "4bw2Am3p9ji3mYsXNXtQcd",
            "name": "Piso 21",
            "type": "artist",
            "uri": "spotify:artist:4bw2Am3p9ji3mYsXNXtQcd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0XwVARXT135rw8lyw1EeWP"
            },
            "href": "https://api.spotify.com/v1/artists/0XwVARXT135rw8lyw1EeWP",
            "id": "0XwVARXT135rw8lyw1EeWP",
            "name": "Christian Nodal",
            "type": "artist",
            "uri": "spotify:artist:0XwVARXT135rw8lyw1EeWP"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 227233,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "MXF151900316"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1cVlW9WQiGlFdWUXFdFZGh"
        },
        "href": "https://api.spotify.com/v1/tracks/1cVlW9WQiGlFdWUXFdFZGh",
        "id": "1cVlW9WQiGlFdWUXFdFZGh",
        "is_local": false,
        "name": "Pa' Olvidarme De Ella",
        "popularity": 86,
        "preview_url": "https://p.scdn.co/mp3-preview/616028fe8445d19c25adb9a947947095be9bf0df?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:1cVlW9WQiGlFdWUXFdFZGh"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7n2wHs1TKAczGzO7Dd2rGr"
              },
              "href": "https://api.spotify.com/v1/artists/7n2wHs1TKAczGzO7Dd2rGr",
              "id": "7n2wHs1TKAczGzO7Dd2rGr",
              "name": "Shawn Mendes",
              "type": "artist",
              "uri": "spotify:artist:7n2wHs1TKAczGzO7Dd2rGr"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0xzScN8P3hQAz3BT3YYX5w"
          },
          "href": "https://api.spotify.com/v1/albums/0xzScN8P3hQAz3BT3YYX5w",
          "id": "0xzScN8P3hQAz3BT3YYX5w",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/93de84650354b3a8436a893332b436cf3bb000d0",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/4e75d4d2bc7fbd8d3b48c37f8c2ead1f36774e49",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/b68c52237ed6815023eb6e62ab93e380c04611a6",
              "width": 64
            }
          ],
          "name": "Shawn Mendes (Deluxe)",
          "release_date": "2019-06-19",
          "release_date_precision": "day",
          "total_tracks": 16,
          "type": "album",
          "uri": "spotify:album:0xzScN8P3hQAz3BT3YYX5w"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7n2wHs1TKAczGzO7Dd2rGr"
            },
            "href": "https://api.spotify.com/v1/artists/7n2wHs1TKAczGzO7Dd2rGr",
            "id": "7n2wHs1TKAczGzO7Dd2rGr",
            "name": "Shawn Mendes",
            "type": "artist",
            "uri": "spotify:artist:7n2wHs1TKAczGzO7Dd2rGr"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4nDoRrQiYLoBzwC5BhVJzF"
            },
            "href": "https://api.spotify.com/v1/artists/4nDoRrQiYLoBzwC5BhVJzF",
            "id": "4nDoRrQiYLoBzwC5BhVJzF",
            "name": "Camila Cabello",
            "type": "artist",
            "uri": "spotify:artist:4nDoRrQiYLoBzwC5BhVJzF"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 190799,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71911283"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6v3KW9xbzN5yKLt9YKDYA2"
        },
        "href": "https://api.spotify.com/v1/tracks/6v3KW9xbzN5yKLt9YKDYA2",
        "id": "6v3KW9xbzN5yKLt9YKDYA2",
        "is_local": false,
        "name": "Señorita",
        "popularity": 88,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6v3KW9xbzN5yKLt9YKDYA2"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/28gNT5KBp7IjEOQoevXf9N"
              },
              "href": "https://api.spotify.com/v1/artists/28gNT5KBp7IjEOQoevXf9N",
              "id": "28gNT5KBp7IjEOQoevXf9N",
              "name": "Camilo",
              "type": "artist",
              "uri": "spotify:artist:28gNT5KBp7IjEOQoevXf9N"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4QVBYiagIaa6ZGSPMbybpy"
              },
              "href": "https://api.spotify.com/v1/artists/4QVBYiagIaa6ZGSPMbybpy",
              "id": "4QVBYiagIaa6ZGSPMbybpy",
              "name": "Pedro Capó",
              "type": "artist",
              "uri": "spotify:artist:4QVBYiagIaa6ZGSPMbybpy"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6xu5asYeoMIT5Sa5b1P13q"
          },
          "href": "https://api.spotify.com/v1/albums/6xu5asYeoMIT5Sa5b1P13q",
          "id": "6xu5asYeoMIT5Sa5b1P13q",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273f748b7d038bc70dfba593fdd",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02f748b7d038bc70dfba593fdd",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851f748b7d038bc70dfba593fdd",
              "width": 64
            }
          ],
          "name": "Tutu",
          "release_date": "2019-08-09",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:6xu5asYeoMIT5Sa5b1P13q"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/28gNT5KBp7IjEOQoevXf9N"
            },
            "href": "https://api.spotify.com/v1/artists/28gNT5KBp7IjEOQoevXf9N",
            "id": "28gNT5KBp7IjEOQoevXf9N",
            "name": "Camilo",
            "type": "artist",
            "uri": "spotify:artist:28gNT5KBp7IjEOQoevXf9N"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4QVBYiagIaa6ZGSPMbybpy"
            },
            "href": "https://api.spotify.com/v1/artists/4QVBYiagIaa6ZGSPMbybpy",
            "id": "4QVBYiagIaa6ZGSPMbybpy",
            "name": "Pedro Capó",
            "type": "artist",
            "uri": "spotify:artist:4QVBYiagIaa6ZGSPMbybpy"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 178613,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSD11900263"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1nocRtwyNPVtGcIJqfgdzZ"
        },
        "href": "https://api.spotify.com/v1/tracks/1nocRtwyNPVtGcIJqfgdzZ",
        "id": "1nocRtwyNPVtGcIJqfgdzZ",
        "is_local": false,
        "name": "Tutu",
        "popularity": 87,
        "preview_url": "https://p.scdn.co/mp3-preview/bbb93b30e71d9c18736fb3ba053b876af87cf9e7?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:1nocRtwyNPVtGcIJqfgdzZ"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/14zUHaJZo1mnYtn6IBRaRP"
              },
              "href": "https://api.spotify.com/v1/artists/14zUHaJZo1mnYtn6IBRaRP",
              "id": "14zUHaJZo1mnYtn6IBRaRP",
              "name": "Justin Quiles",
              "type": "artist",
              "uri": "spotify:artist:14zUHaJZo1mnYtn6IBRaRP"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1GDbiv3spRmZ1XdM1jQbT7"
              },
              "href": "https://api.spotify.com/v1/artists/1GDbiv3spRmZ1XdM1jQbT7",
              "id": "1GDbiv3spRmZ1XdM1jQbT7",
              "name": "Natti Natasha",
              "type": "artist",
              "uri": "spotify:artist:1GDbiv3spRmZ1XdM1jQbT7"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
              },
              "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
              "id": "329e4yvIujISKGKz1BZZbO",
              "name": "Farruko",
              "type": "artist",
              "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/71uU1JDWZ61OMDtW8h1Kp8"
          },
          "href": "https://api.spotify.com/v1/albums/71uU1JDWZ61OMDtW8h1Kp8",
          "id": "71uU1JDWZ61OMDtW8h1Kp8",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b27361b418f21b955326dcddd014",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e0261b418f21b955326dcddd014",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d0000485161b418f21b955326dcddd014",
              "width": 64
            }
          ],
          "name": "DJ No Pare (feat. Zion, Dalex, Lenny Tavárez) [Remix]",
          "release_date": "2019-09-06",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:71uU1JDWZ61OMDtW8h1Kp8"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/14zUHaJZo1mnYtn6IBRaRP"
            },
            "href": "https://api.spotify.com/v1/artists/14zUHaJZo1mnYtn6IBRaRP",
            "id": "14zUHaJZo1mnYtn6IBRaRP",
            "name": "Justin Quiles",
            "type": "artist",
            "uri": "spotify:artist:14zUHaJZo1mnYtn6IBRaRP"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1GDbiv3spRmZ1XdM1jQbT7"
            },
            "href": "https://api.spotify.com/v1/artists/1GDbiv3spRmZ1XdM1jQbT7",
            "id": "1GDbiv3spRmZ1XdM1jQbT7",
            "name": "Natti Natasha",
            "type": "artist",
            "uri": "spotify:artist:1GDbiv3spRmZ1XdM1jQbT7"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
            },
            "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
            "id": "1pQWsZQehhS4wavwh7Fnxd",
            "name": "Lenny Tavárez",
            "type": "artist",
            "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pgDilWYDWLoOgGjf1iHNu"
            },
            "href": "https://api.spotify.com/v1/artists/1pgDilWYDWLoOgGjf1iHNu",
            "id": "1pgDilWYDWLoOgGjf1iHNu",
            "name": "Zion",
            "type": "artist",
            "uri": "spotify:artist:1pgDilWYDWLoOgGjf1iHNu"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 258600,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USWL11900240"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1ndyl3wJCFs872XZ3ztPk6"
        },
        "href": "https://api.spotify.com/v1/tracks/1ndyl3wJCFs872XZ3ztPk6",
        "id": "1ndyl3wJCFs872XZ3ztPk6",
        "is_local": false,
        "name": "DJ No Pare (feat. Zion, Dalex, Lenny Tavárez) - Remix",
        "popularity": 86,
        "preview_url": "https://p.scdn.co/mp3-preview/662fa6450a8b90db980d3cdd27c9e3411da2c44e?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:1ndyl3wJCFs872XZ3ztPk6"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
              },
              "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
              "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
              "name": "Dimelo Flow",
              "type": "artist",
              "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
              },
              "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
              "id": "77ziqFxp5gaInVrF2lj4ht",
              "name": "Sech",
              "type": "artist",
              "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
              },
              "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
              "id": "0KPX4Ucy9dk82uj4GpKesn",
              "name": "Dalex",
              "type": "artist",
              "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0qbOBxWyWz3RwoxeiIjdOL"
          },
          "href": "https://api.spotify.com/v1/albums/0qbOBxWyWz3RwoxeiIjdOL",
          "id": "0qbOBxWyWz3RwoxeiIjdOL",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/f552d22c4e010f9479c36b98b632e29f7be37a07",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/39cfadf840153f34d2667336fbd6d8c9782b4b4d",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/235512d6e0d2ce1623ecadb035361cc7d4deba0d",
              "width": 64
            }
          ],
          "name": "La Isla (with Sech & Dalex feat. Justin Quiles, La Exce, Feid, Zion)",
          "release_date": "2019-11-29",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:0qbOBxWyWz3RwoxeiIjdOL"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
            "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
            "name": "Dimelo Flow",
            "type": "artist",
            "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/14zUHaJZo1mnYtn6IBRaRP"
            },
            "href": "https://api.spotify.com/v1/artists/14zUHaJZo1mnYtn6IBRaRP",
            "id": "14zUHaJZo1mnYtn6IBRaRP",
            "name": "Justin Quiles",
            "type": "artist",
            "uri": "spotify:artist:14zUHaJZo1mnYtn6IBRaRP"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2RON3ZWvFVAHpiJA74KNHj"
            },
            "href": "https://api.spotify.com/v1/artists/2RON3ZWvFVAHpiJA74KNHj",
            "id": "2RON3ZWvFVAHpiJA74KNHj",
            "name": "La Exce",
            "type": "artist",
            "uri": "spotify:artist:2RON3ZWvFVAHpiJA74KNHj"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2LRoIwlKmHjgvigdNGBHNo"
            },
            "href": "https://api.spotify.com/v1/artists/2LRoIwlKmHjgvigdNGBHNo",
            "id": "2LRoIwlKmHjgvigdNGBHNo",
            "name": "Feid",
            "type": "artist",
            "uri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pgDilWYDWLoOgGjf1iHNu"
            },
            "href": "https://api.spotify.com/v1/artists/1pgDilWYDWLoOgGjf1iHNu",
            "id": "1pgDilWYDWLoOgGjf1iHNu",
            "name": "Zion",
            "type": "artist",
            "uri": "spotify:artist:1pgDilWYDWLoOgGjf1iHNu"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 266773,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "USA2P1950440"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0UfVfRSmy4xMyi67LKH5zZ"
        },
        "href": "https://api.spotify.com/v1/tracks/0UfVfRSmy4xMyi67LKH5zZ",
        "id": "0UfVfRSmy4xMyi67LKH5zZ",
        "is_local": false,
        "name": "La Isla (with Sech & Dalex feat. Justin Quiles, La Exce, Feid, Zion)",
        "popularity": 75,
        "preview_url": "https://p.scdn.co/mp3-preview/52a5496c2ae3369845309a8823151f733868845f?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:0UfVfRSmy4xMyi67LKH5zZ"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s"
              },
              "href": "https://api.spotify.com/v1/artists/1uNFoZAHBGtllmzznpCI3s",
              "id": "1uNFoZAHBGtllmzznpCI3s",
              "name": "Justin Bieber",
              "type": "artist",
              "uri": "spotify:artist:1uNFoZAHBGtllmzznpCI3s"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1SN6N3fNkZk5oXQ9X46QZ3"
          },
          "href": "https://api.spotify.com/v1/albums/1SN6N3fNkZk5oXQ9X46QZ3",
          "id": "1SN6N3fNkZk5oXQ9X46QZ3",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/fe55e78fd32d3b9a9548b0f5501707ff796b0655",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/c83c4acc6dc6f1a9234d26725cac607e12cea22f",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/2373b3eee73f654a2ba43c4e3e7ffebeb368d9e5",
              "width": 64
            }
          ],
          "name": "Yummy",
          "release_date": "2020-01-03",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1SN6N3fNkZk5oXQ9X46QZ3"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s"
            },
            "href": "https://api.spotify.com/v1/artists/1uNFoZAHBGtllmzznpCI3s",
            "id": "1uNFoZAHBGtllmzznpCI3s",
            "name": "Justin Bieber",
            "type": "artist",
            "uri": "spotify:artist:1uNFoZAHBGtllmzznpCI3s"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 210426,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71923046"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/41L3O37CECZt3N7ziG2z7l"
        },
        "href": "https://api.spotify.com/v1/tracks/41L3O37CECZt3N7ziG2z7l",
        "id": "41L3O37CECZt3N7ziG2z7l",
        "is_local": false,
        "name": "Yummy",
        "popularity": 97,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:41L3O37CECZt3N7ziG2z7l"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
              },
              "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
              "id": "4VMYDCV2IEDYJArk749S6m",
              "name": "Daddy Yankee",
              "type": "artist",
              "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/155yGQqPxsYkhV7zQyL95t"
          },
          "href": "https://api.spotify.com/v1/albums/155yGQqPxsYkhV7zQyL95t",
          "id": "155yGQqPxsYkhV7zQyL95t",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/465bc45bb1ddbd6b2fbe8c16f0ee179e96f58369",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/8295e4f5b7fffbcffe59bb6e7a4ff9cfd8db9a5d",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/34e1a0302fef4fef76ff29993c13ae14170e5158",
              "width": 64
            }
          ],
          "name": "Que Tire Pa Lante",
          "release_date": "2019-10-18",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:155yGQqPxsYkhV7zQyL95t"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
            },
            "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
            "id": "4VMYDCV2IEDYJArk749S6m",
            "name": "Daddy Yankee",
            "type": "artist",
            "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 210520,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "US2BU1901810"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6RyaV7owmVU6fzEPE17sF1"
        },
        "href": "https://api.spotify.com/v1/tracks/6RyaV7owmVU6fzEPE17sF1",
        "id": "6RyaV7owmVU6fzEPE17sF1",
        "is_local": false,
        "name": "Que Tire Pa Lante",
        "popularity": 89,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6RyaV7owmVU6fzEPE17sF1"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
              },
              "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
              "id": "1r4hJ1h58CWwUQe3MxPuau",
              "name": "Maluma",
              "type": "artist",
              "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1Db95k6t4rCPHSmdfsTeDl"
          },
          "href": "https://api.spotify.com/v1/albums/1Db95k6t4rCPHSmdfsTeDl",
          "id": "1Db95k6t4rCPHSmdfsTeDl",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/12df90593df0bf6d6f85fa5a5d19a88c5d696de0",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/d7a46d309f94106418c5570c0691feaf2d6bcb8a",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/5965cd57b9e65f5f4d9900cb2b1352ab666ffed7",
              "width": 64
            }
          ],
          "name": "Qué Pena",
          "release_date": "2019-09-27",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1Db95k6t4rCPHSmdfsTeDl"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
            },
            "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
            "id": "1r4hJ1h58CWwUQe3MxPuau",
            "name": "Maluma",
            "type": "artist",
            "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 212711,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSD11900171"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5099x34vBakWpGkHourFxP"
        },
        "href": "https://api.spotify.com/v1/tracks/5099x34vBakWpGkHourFxP",
        "id": "5099x34vBakWpGkHourFxP",
        "is_local": false,
        "name": "Qué Pena",
        "popularity": 84,
        "preview_url": "https://p.scdn.co/mp3-preview/b82a2d454d23261612a6511904e5498dc064de04?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5099x34vBakWpGkHourFxP"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/47MpMsUfWtgyIIBEFOr4FE"
              },
              "href": "https://api.spotify.com/v1/artists/47MpMsUfWtgyIIBEFOr4FE",
              "id": "47MpMsUfWtgyIIBEFOr4FE",
              "name": "Lunay",
              "type": "artist",
              "uri": "spotify:artist:47MpMsUfWtgyIIBEFOr4FE"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/46xbsFOp9g1WqTidQEs7YT"
          },
          "href": "https://api.spotify.com/v1/albums/46xbsFOp9g1WqTidQEs7YT",
          "id": "46xbsFOp9g1WqTidQEs7YT",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/7d8bcb83a8f44da61d358964af9695189807dab6",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/954f83113d09edf0c8115db4beba654b1ef5f2ad",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/d29072867f72417727b467bd2539328e2edeee57",
              "width": 64
            }
          ],
          "name": "Épico",
          "release_date": "2019-10-25",
          "release_date_precision": "day",
          "total_tracks": 14,
          "type": "album",
          "uri": "spotify:album:46xbsFOp9g1WqTidQEs7YT"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/47MpMsUfWtgyIIBEFOr4FE"
            },
            "href": "https://api.spotify.com/v1/artists/47MpMsUfWtgyIIBEFOr4FE",
            "id": "47MpMsUfWtgyIIBEFOr4FE",
            "name": "Lunay",
            "type": "artist",
            "uri": "spotify:artist:47MpMsUfWtgyIIBEFOr4FE"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m"
            },
            "href": "https://api.spotify.com/v1/artists/4VMYDCV2IEDYJArk749S6m",
            "id": "4VMYDCV2IEDYJArk749S6m",
            "name": "Daddy Yankee",
            "type": "artist",
            "uri": "spotify:artist:4VMYDCV2IEDYJArk749S6m"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X"
            },
            "href": "https://api.spotify.com/v1/artists/4q3ewBCX7sLwd24euuV69X",
            "id": "4q3ewBCX7sLwd24euuV69X",
            "name": "Bad Bunny",
            "type": "artist",
            "uri": "spotify:artist:4q3ewBCX7sLwd24euuV69X"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 266086,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USA2P1927909"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4t9a07PAghtQMRAIP9FQ7Z"
        },
        "href": "https://api.spotify.com/v1/tracks/4t9a07PAghtQMRAIP9FQ7Z",
        "id": "4t9a07PAghtQMRAIP9FQ7Z",
        "is_local": false,
        "name": "Soltera - Remix",
        "popularity": 78,
        "preview_url": "https://p.scdn.co/mp3-preview/dd6fc3e183f2643f0f4a3d650fa4f923c2a46040?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 7,
        "type": "track",
        "uri": "spotify:track:4t9a07PAghtQMRAIP9FQ7Z"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
              },
              "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
              "id": "1r4hJ1h58CWwUQe3MxPuau",
              "name": "Maluma",
              "type": "artist",
              "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3YIUNL7qFE8NP3X3zaYSND"
          },
          "href": "https://api.spotify.com/v1/albums/3YIUNL7qFE8NP3X3zaYSND",
          "id": "3YIUNL7qFE8NP3X3zaYSND",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273073bc2070f7fa02b2a6bda64",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02073bc2070f7fa02b2a6bda64",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851073bc2070f7fa02b2a6bda64",
              "width": 64
            }
          ],
          "name": "11:11",
          "release_date": "2019-05-17",
          "release_date_precision": "day",
          "total_tracks": 16,
          "type": "album",
          "uri": "spotify:album:3YIUNL7qFE8NP3X3zaYSND"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
            },
            "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
            "id": "1r4hJ1h58CWwUQe3MxPuau",
            "name": "Maluma",
            "type": "artist",
            "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 175733,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSD11900166"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7KbF6AdprOXEEHlsq11Z6d"
        },
        "href": "https://api.spotify.com/v1/tracks/7KbF6AdprOXEEHlsq11Z6d",
        "id": "7KbF6AdprOXEEHlsq11Z6d",
        "is_local": false,
        "name": "11 PM",
        "popularity": 86,
        "preview_url": "https://p.scdn.co/mp3-preview/2993254fae01c3abd401c55d9d30937a8b130c9e?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:7KbF6AdprOXEEHlsq11Z6d"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
              },
              "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
              "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
              "name": "Dimelo Flow",
              "type": "artist",
              "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
              },
              "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
              "id": "1SupJlEpv7RS2tPNRaHViT",
              "name": "Nicky Jam",
              "type": "artist",
              "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
              },
              "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
              "id": "77ziqFxp5gaInVrF2lj4ht",
              "name": "Sech",
              "type": "artist",
              "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/28561uZztshyZSVG6ElL62"
          },
          "href": "https://api.spotify.com/v1/albums/28561uZztshyZSVG6ElL62",
          "id": "28561uZztshyZSVG6ElL62",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b2735c11ee5d105def87483ce9da",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e025c11ee5d105def87483ce9da",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d000048515c11ee5d105def87483ce9da",
              "width": 64
            }
          ],
          "name": "El Favor (with Nicky Jam & Sech, feat. Farruko, Zion & Lunay)",
          "release_date": "2019-08-30",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:28561uZztshyZSVG6ElL62"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/3fZk3Gm5dN5v5yfYMQ04Bx"
            },
            "href": "https://api.spotify.com/v1/artists/3fZk3Gm5dN5v5yfYMQ04Bx",
            "id": "3fZk3Gm5dN5v5yfYMQ04Bx",
            "name": "Dimelo Flow",
            "type": "artist",
            "uri": "spotify:artist:3fZk3Gm5dN5v5yfYMQ04Bx"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
            },
            "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
            "id": "1SupJlEpv7RS2tPNRaHViT",
            "name": "Nicky Jam",
            "type": "artist",
            "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pgDilWYDWLoOgGjf1iHNu"
            },
            "href": "https://api.spotify.com/v1/artists/1pgDilWYDWLoOgGjf1iHNu",
            "id": "1pgDilWYDWLoOgGjf1iHNu",
            "name": "Zion",
            "type": "artist",
            "uri": "spotify:artist:1pgDilWYDWLoOgGjf1iHNu"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/47MpMsUfWtgyIIBEFOr4FE"
            },
            "href": "https://api.spotify.com/v1/artists/47MpMsUfWtgyIIBEFOr4FE",
            "id": "47MpMsUfWtgyIIBEFOr4FE",
            "name": "Lunay",
            "type": "artist",
            "uri": "spotify:artist:47MpMsUfWtgyIIBEFOr4FE"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 233112,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USA2P1944692"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/684EjRHwNsZQ9hCQxL4NYL"
        },
        "href": "https://api.spotify.com/v1/tracks/684EjRHwNsZQ9hCQxL4NYL",
        "id": "684EjRHwNsZQ9hCQxL4NYL",
        "is_local": false,
        "name": "El Favor (with Nicky Jam & Sech, feat. Farruko, Zion & Lunay)",
        "popularity": 83,
        "preview_url": "https://p.scdn.co/mp3-preview/5f0536002dc215c10d649a4da83acbd9f1c53d50?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:684EjRHwNsZQ9hCQxL4NYL"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4bw2Am3p9ji3mYsXNXtQcd"
              },
              "href": "https://api.spotify.com/v1/artists/4bw2Am3p9ji3mYsXNXtQcd",
              "id": "4bw2Am3p9ji3mYsXNXtQcd",
              "name": "Piso 21",
              "type": "artist",
              "uri": "spotify:artist:4bw2Am3p9ji3mYsXNXtQcd"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1aWJsBQa67l72j1VT3D6Ow"
              },
              "href": "https://api.spotify.com/v1/artists/1aWJsBQa67l72j1VT3D6Ow",
              "id": "1aWJsBQa67l72j1VT3D6Ow",
              "name": "Micro Tdh",
              "type": "artist",
              "uri": "spotify:artist:1aWJsBQa67l72j1VT3D6Ow"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/02XOoh8XrlCc466QkkjGk5"
          },
          "href": "https://api.spotify.com/v1/albums/02XOoh8XrlCc466QkkjGk5",
          "id": "02XOoh8XrlCc466QkkjGk5",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273244a592f4a0fc01b2446e797",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02244a592f4a0fc01b2446e797",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851244a592f4a0fc01b2446e797",
              "width": 64
            }
          ],
          "name": "Te Vi",
          "release_date": "2018-12-14",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:02XOoh8XrlCc466QkkjGk5"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4bw2Am3p9ji3mYsXNXtQcd"
            },
            "href": "https://api.spotify.com/v1/artists/4bw2Am3p9ji3mYsXNXtQcd",
            "id": "4bw2Am3p9ji3mYsXNXtQcd",
            "name": "Piso 21",
            "type": "artist",
            "uri": "spotify:artist:4bw2Am3p9ji3mYsXNXtQcd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1aWJsBQa67l72j1VT3D6Ow"
            },
            "href": "https://api.spotify.com/v1/artists/1aWJsBQa67l72j1VT3D6Ow",
            "id": "1aWJsBQa67l72j1VT3D6Ow",
            "name": "Micro Tdh",
            "type": "artist",
            "uri": "spotify:artist:1aWJsBQa67l72j1VT3D6Ow"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 231848,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "MXF151800454"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/059bcIhyc2SBwm6sw2AZzd"
        },
        "href": "https://api.spotify.com/v1/tracks/059bcIhyc2SBwm6sw2AZzd",
        "id": "059bcIhyc2SBwm6sw2AZzd",
        "is_local": false,
        "name": "Te Vi",
        "popularity": 83,
        "preview_url": "https://p.scdn.co/mp3-preview/4cec92c7db1831f52f6704f2b104ee28942eef48?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:059bcIhyc2SBwm6sw2AZzd"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
              },
              "href": "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
              "id": "6qqNVTkY8uBg9cP3Jd7DAH",
              "name": "Billie Eilish",
              "type": "artist",
              "uri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/4i3rAwPw7Ln2YrKDusaWyT"
          },
          "href": "https://api.spotify.com/v1/albums/4i3rAwPw7Ln2YrKDusaWyT",
          "id": "4i3rAwPw7Ln2YrKDusaWyT",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/18ad2ce4723468f55c2b9af9d5fe865d39890be3",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/1e3362e292757120dc85c865c15669e5c503cb91",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/c6683baebbc098fb64d3221f2b3f909200cdea6e",
              "width": 64
            }
          ],
          "name": "everything i wanted",
          "release_date": "2019-11-13",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:4i3rAwPw7Ln2YrKDusaWyT"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
            },
            "href": "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
            "id": "6qqNVTkY8uBg9cP3Jd7DAH",
            "name": "Billie Eilish",
            "type": "artist",
            "uri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 245425,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USUM71922577"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3ZCTVFBt2Brf31RLEnCkWJ"
        },
        "href": "https://api.spotify.com/v1/tracks/3ZCTVFBt2Brf31RLEnCkWJ",
        "id": "3ZCTVFBt2Brf31RLEnCkWJ",
        "is_local": false,
        "name": "everything i wanted",
        "popularity": 97,
        "preview_url": null,
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:3ZCTVFBt2Brf31RLEnCkWJ"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7iK8PXO48WeuP03g8YR51W"
              },
              "href": "https://api.spotify.com/v1/artists/7iK8PXO48WeuP03g8YR51W",
              "id": "7iK8PXO48WeuP03g8YR51W",
              "name": "Myke Towers",
              "type": "artist",
              "uri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
              },
              "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
              "id": "1r4hJ1h58CWwUQe3MxPuau",
              "name": "Maluma",
              "type": "artist",
              "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
              },
              "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
              "id": "329e4yvIujISKGKz1BZZbO",
              "name": "Farruko",
              "type": "artist",
              "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3qppmBh6lM8UXGTZF0dyTD"
          },
          "href": "https://api.spotify.com/v1/albums/3qppmBh6lM8UXGTZF0dyTD",
          "id": "3qppmBh6lM8UXGTZF0dyTD",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ef730af92c90660eb7ffa3fc7399921125d7a8ba",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/072a19c14c87e9a0df450fb86ecce746c48782fe",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/7ce69d538cacc9341ac47ec25c11f7607d44ff77",
              "width": 64
            }
          ],
          "name": "La Playa (Remix)",
          "release_date": "2020-01-03",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:3qppmBh6lM8UXGTZF0dyTD"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7iK8PXO48WeuP03g8YR51W"
            },
            "href": "https://api.spotify.com/v1/artists/7iK8PXO48WeuP03g8YR51W",
            "id": "7iK8PXO48WeuP03g8YR51W",
            "name": "Myke Towers",
            "type": "artist",
            "uri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
            },
            "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
            "id": "1r4hJ1h58CWwUQe3MxPuau",
            "name": "Maluma",
            "type": "artist",
            "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 250333,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QMFME1914751"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/70zg99pT51vB4wlMS7e4q7"
        },
        "href": "https://api.spotify.com/v1/tracks/70zg99pT51vB4wlMS7e4q7",
        "id": "70zg99pT51vB4wlMS7e4q7",
        "is_local": false,
        "name": "La Playa - Remix",
        "popularity": 81,
        "preview_url": "https://p.scdn.co/mp3-preview/e59b4cd3f0332587f260348f9f10b18a0783c243?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:70zg99pT51vB4wlMS7e4q7"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
              },
              "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
              "id": "0KPX4Ucy9dk82uj4GpKesn",
              "name": "Dalex",
              "type": "artist",
              "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/6stPNzjz40FWTiwlOR98Lp"
          },
          "href": "https://api.spotify.com/v1/albums/6stPNzjz40FWTiwlOR98Lp",
          "id": "6stPNzjz40FWTiwlOR98Lp",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273b9242ba03ab231608f123e06",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02b9242ba03ab231608f123e06",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851b9242ba03ab231608f123e06",
              "width": 64
            }
          ],
          "name": "Climaxxx",
          "release_date": "2019-05-10",
          "release_date_precision": "day",
          "total_tracks": 15,
          "type": "album",
          "uri": "spotify:album:6stPNzjz40FWTiwlOR98Lp"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/11YLRSsZA3YVuQQtHXKTlz"
            },
            "href": "https://api.spotify.com/v1/artists/11YLRSsZA3YVuQQtHXKTlz",
            "id": "11YLRSsZA3YVuQQtHXKTlz",
            "name": "Rafa Pabön",
            "type": "artist",
            "uri": "spotify:artist:11YLRSsZA3YVuQQtHXKTlz"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
            },
            "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
            "id": "1pQWsZQehhS4wavwh7Fnxd",
            "name": "Lenny Tavárez",
            "type": "artist",
            "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4m6ubhNsdwF4psNf3R8kwR"
            },
            "href": "https://api.spotify.com/v1/artists/4m6ubhNsdwF4psNf3R8kwR",
            "id": "4m6ubhNsdwF4psNf3R8kwR",
            "name": "KHEA",
            "type": "artist",
            "uri": "spotify:artist:4m6ubhNsdwF4psNf3R8kwR"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6w3SkAHYPsQ1bxV7VDlG5y"
            },
            "href": "https://api.spotify.com/v1/artists/6w3SkAHYPsQ1bxV7VDlG5y",
            "id": "6w3SkAHYPsQ1bxV7VDlG5y",
            "name": "Cazzu",
            "type": "artist",
            "uri": "spotify:artist:6w3SkAHYPsQ1bxV7VDlG5y"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2LRoIwlKmHjgvigdNGBHNo"
            },
            "href": "https://api.spotify.com/v1/artists/2LRoIwlKmHjgvigdNGBHNo",
            "id": "2LRoIwlKmHjgvigdNGBHNo",
            "name": "Feid",
            "type": "artist",
            "uri": "spotify:artist:2LRoIwlKmHjgvigdNGBHNo"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 360960,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM9WM1900002"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7g8YaUQABMal0zWe7a2ijz"
        },
        "href": "https://api.spotify.com/v1/tracks/7g8YaUQABMal0zWe7a2ijz",
        "id": "7g8YaUQABMal0zWe7a2ijz",
        "is_local": false,
        "name": "Pa Mí - Remix",
        "popularity": 84,
        "preview_url": "https://p.scdn.co/mp3-preview/99bf02294818b0f72efaa135e1d42cc20584ef6e?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 14,
        "type": "track",
        "uri": "spotify:track:7g8YaUQABMal0zWe7a2ijz"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7ltDVBr6mKbRvohxheJ9h1"
              },
              "href": "https://api.spotify.com/v1/artists/7ltDVBr6mKbRvohxheJ9h1",
              "id": "7ltDVBr6mKbRvohxheJ9h1",
              "name": "ROSALÍA",
              "type": "artist",
              "uri": "spotify:artist:7ltDVBr6mKbRvohxheJ9h1"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
              },
              "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
              "id": "1vyhD5VmyZ7KMfW5gqLgo5",
              "name": "J Balvin",
              "type": "artist",
              "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/4bxHLppgdmaYJk0yfdcP0l"
          },
          "href": "https://api.spotify.com/v1/albums/4bxHLppgdmaYJk0yfdcP0l",
          "id": "4bxHLppgdmaYJk0yfdcP0l",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b27365b0e3e1bd8b5fe2f602c1ea",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e0265b0e3e1bd8b5fe2f602c1ea",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d0000485165b0e3e1bd8b5fe2f602c1ea",
              "width": 64
            }
          ],
          "name": "Con Altura",
          "release_date": "2019-03-28",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:4bxHLppgdmaYJk0yfdcP0l"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7ltDVBr6mKbRvohxheJ9h1"
            },
            "href": "https://api.spotify.com/v1/artists/7ltDVBr6mKbRvohxheJ9h1",
            "id": "7ltDVBr6mKbRvohxheJ9h1",
            "name": "ROSALÍA",
            "type": "artist",
            "uri": "spotify:artist:7ltDVBr6mKbRvohxheJ9h1"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5"
            },
            "href": "https://api.spotify.com/v1/artists/1vyhD5VmyZ7KMfW5gqLgo5",
            "id": "1vyhD5VmyZ7KMfW5gqLgo5",
            "name": "J Balvin",
            "type": "artist",
            "uri": "spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1oMiDFyAgmIzw9ZBQYHOJI"
            },
            "href": "https://api.spotify.com/v1/artists/1oMiDFyAgmIzw9ZBQYHOJI",
            "id": "1oMiDFyAgmIzw9ZBQYHOJI",
            "name": "El Guincho",
            "type": "artist",
            "uri": "spotify:artist:1oMiDFyAgmIzw9ZBQYHOJI"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 161626,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSM11900950"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2qG5sZ7Si6sdK74qLxedYM"
        },
        "href": "https://api.spotify.com/v1/tracks/2qG5sZ7Si6sdK74qLxedYM",
        "id": "2qG5sZ7Si6sdK74qLxedYM",
        "is_local": false,
        "name": "Con Altura",
        "popularity": 86,
        "preview_url": "https://p.scdn.co/mp3-preview/db95e1fba1c9df7e2f6966ba91347df3c36a9630?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2qG5sZ7Si6sdK74qLxedYM"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2wkoKEfS6dXwThbyTnZWFU"
              },
              "href": "https://api.spotify.com/v1/artists/2wkoKEfS6dXwThbyTnZWFU",
              "id": "2wkoKEfS6dXwThbyTnZWFU",
              "name": "Mau y Ricky",
              "type": "artist",
              "uri": "spotify:artist:2wkoKEfS6dXwThbyTnZWFU"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/01yYW0rRRwlEZx1dMmc5ff"
          },
          "href": "https://api.spotify.com/v1/albums/01yYW0rRRwlEZx1dMmc5ff",
          "id": "01yYW0rRRwlEZx1dMmc5ff",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273d2ebc81ef0f59b6144e57daa",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02d2ebc81ef0f59b6144e57daa",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851d2ebc81ef0f59b6144e57daa",
              "width": 64
            }
          ],
          "name": "Para Aventuras y Curiosidades",
          "release_date": "2019-05-03",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:01yYW0rRRwlEZx1dMmc5ff"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2wkoKEfS6dXwThbyTnZWFU"
            },
            "href": "https://api.spotify.com/v1/artists/2wkoKEfS6dXwThbyTnZWFU",
            "id": "2wkoKEfS6dXwThbyTnZWFU",
            "name": "Mau y Ricky",
            "type": "artist",
            "uri": "spotify:artist:2wkoKEfS6dXwThbyTnZWFU"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0tmwSHipWxN12fsoLcFU3B"
            },
            "href": "https://api.spotify.com/v1/artists/0tmwSHipWxN12fsoLcFU3B",
            "id": "0tmwSHipWxN12fsoLcFU3B",
            "name": "Manuel Turizo",
            "type": "artist",
            "uri": "spotify:artist:0tmwSHipWxN12fsoLcFU3B"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/28gNT5KBp7IjEOQoevXf9N"
            },
            "href": "https://api.spotify.com/v1/artists/28gNT5KBp7IjEOQoevXf9N",
            "id": "28gNT5KBp7IjEOQoevXf9N",
            "name": "Camilo",
            "type": "artist",
            "uri": "spotify:artist:28gNT5KBp7IjEOQoevXf9N"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 204563,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "USSD11800344"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/56f5qnyAlZdlz8wrUDA50h"
        },
        "href": "https://api.spotify.com/v1/tracks/56f5qnyAlZdlz8wrUDA50h",
        "id": "56f5qnyAlZdlz8wrUDA50h",
        "is_local": false,
        "name": "Desconocidos",
        "popularity": 78,
        "preview_url": "https://p.scdn.co/mp3-preview/ba457449d5bc6330c44916396269d4e39d85b4a6?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 12,
        "type": "track",
        "uri": "spotify:track:56f5qnyAlZdlz8wrUDA50h"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7ltDVBr6mKbRvohxheJ9h1"
              },
              "href": "https://api.spotify.com/v1/artists/7ltDVBr6mKbRvohxheJ9h1",
              "id": "7ltDVBr6mKbRvohxheJ9h1",
              "name": "ROSALÍA",
              "type": "artist",
              "uri": "spotify:artist:7ltDVBr6mKbRvohxheJ9h1"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
              },
              "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
              "id": "1i8SpTcr7yvPOmcqrbnVXY",
              "name": "Ozuna",
              "type": "artist",
              "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3844bY26oeSkqd06th4EYp"
          },
          "href": "https://api.spotify.com/v1/albums/3844bY26oeSkqd06th4EYp",
          "id": "3844bY26oeSkqd06th4EYp",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273694844fd046ab81e5dc9a4cf",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e02694844fd046ab81e5dc9a4cf",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d00004851694844fd046ab81e5dc9a4cf",
              "width": 64
            }
          ],
          "name": "Yo x Ti, Tu x Mi",
          "release_date": "2019-08-15",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:3844bY26oeSkqd06th4EYp"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7ltDVBr6mKbRvohxheJ9h1"
            },
            "href": "https://api.spotify.com/v1/artists/7ltDVBr6mKbRvohxheJ9h1",
            "id": "7ltDVBr6mKbRvohxheJ9h1",
            "name": "ROSALÍA",
            "type": "artist",
            "uri": "spotify:artist:7ltDVBr6mKbRvohxheJ9h1"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1i8SpTcr7yvPOmcqrbnVXY"
            },
            "href": "https://api.spotify.com/v1/artists/1i8SpTcr7yvPOmcqrbnVXY",
            "id": "1i8SpTcr7yvPOmcqrbnVXY",
            "name": "Ozuna",
            "type": "artist",
            "uri": "spotify:artist:1i8SpTcr7yvPOmcqrbnVXY"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 201040,
        "episode": false,
        "explicit": false,
        "external_ids": {
          "isrc": "USSM11900596"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7BlBVFwvbWvcwNcUarQmjk"
        },
        "href": "https://api.spotify.com/v1/tracks/7BlBVFwvbWvcwNcUarQmjk",
        "id": "7BlBVFwvbWvcwNcUarQmjk",
        "is_local": false,
        "name": "Yo x Ti, Tu x Mi",
        "popularity": 87,
        "preview_url": "https://p.scdn.co/mp3-preview/f8d270e551ebd663edbb22a6f2fb58a3f5d73edd?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:7BlBVFwvbWvcwNcUarQmjk"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
              },
              "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
              "id": "77ziqFxp5gaInVrF2lj4ht",
              "name": "Sech",
              "type": "artist",
              "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/3TgOrQ3p23Af8zSsxK8fdX"
          },
          "href": "https://api.spotify.com/v1/albums/3TgOrQ3p23Af8zSsxK8fdX",
          "id": "3TgOrQ3p23Af8zSsxK8fdX",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b2738643435482956bab8aa6fcfe",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e028643435482956bab8aa6fcfe",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d000048518643435482956bab8aa6fcfe",
              "width": 64
            }
          ],
          "name": "Sueños",
          "release_date": "2019-04-19",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:3TgOrQ3p23Af8zSsxK8fdX"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/14zUHaJZo1mnYtn6IBRaRP"
            },
            "href": "https://api.spotify.com/v1/artists/14zUHaJZo1mnYtn6IBRaRP",
            "id": "14zUHaJZo1mnYtn6IBRaRP",
            "name": "Justin Quiles",
            "type": "artist",
            "uri": "spotify:artist:14zUHaJZo1mnYtn6IBRaRP"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1r4hJ1h58CWwUQe3MxPuau"
            },
            "href": "https://api.spotify.com/v1/artists/1r4hJ1h58CWwUQe3MxPuau",
            "id": "1r4hJ1h58CWwUQe3MxPuau",
            "name": "Maluma",
            "type": "artist",
            "uri": "spotify:artist:1r4hJ1h58CWwUQe3MxPuau"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/0KPX4Ucy9dk82uj4GpKesn"
            },
            "href": "https://api.spotify.com/v1/artists/0KPX4Ucy9dk82uj4GpKesn",
            "id": "0KPX4Ucy9dk82uj4GpKesn",
            "name": "Dalex",
            "type": "artist",
            "uri": "spotify:artist:0KPX4Ucy9dk82uj4GpKesn"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1SupJlEpv7RS2tPNRaHViT"
            },
            "href": "https://api.spotify.com/v1/artists/1SupJlEpv7RS2tPNRaHViT",
            "id": "1SupJlEpv7RS2tPNRaHViT",
            "name": "Nicky Jam",
            "type": "artist",
            "uri": "spotify:artist:1SupJlEpv7RS2tPNRaHViT"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1pQWsZQehhS4wavwh7Fnxd"
            },
            "href": "https://api.spotify.com/v1/artists/1pQWsZQehhS4wavwh7Fnxd",
            "id": "1pQWsZQehhS4wavwh7Fnxd",
            "name": "Lenny Tavárez",
            "type": "artist",
            "uri": "spotify:artist:1pQWsZQehhS4wavwh7Fnxd"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 305962,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM9WM1900123"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7fODjB7BrQTGqh0hogW6XD"
        },
        "href": "https://api.spotify.com/v1/tracks/7fODjB7BrQTGqh0hogW6XD",
        "id": "7fODjB7BrQTGqh0hogW6XD",
        "is_local": false,
        "name": "Que Mas Pues - Remix",
        "popularity": 83,
        "preview_url": "https://p.scdn.co/mp3-preview/d3d3491e11961762ef195a601496ee61d21f2dd3?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 9,
        "type": "track",
        "uri": "spotify:track:7fODjB7BrQTGqh0hogW6XD"
      },
      "video_thumbnail": {
        "url": null
      }
    },
    {
      "added_at": "1970-01-01T00:00:00Z",
      "added_by": {
        "external_urls": {
          "spotify": "https://open.spotify.com/user/"
        },
        "href": "https://api.spotify.com/v1/users/",
        "id": "",
        "type": "user",
        "uri": "spotify:user:"
      },
      "is_local": false,
      "primary_color": null,
      "track": {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7iK8PXO48WeuP03g8YR51W"
              },
              "href": "https://api.spotify.com/v1/artists/7iK8PXO48WeuP03g8YR51W",
              "id": "7iK8PXO48WeuP03g8YR51W",
              "name": "Myke Towers",
              "type": "artist",
              "uri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
              },
              "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
              "id": "329e4yvIujISKGKz1BZZbO",
              "name": "Farruko",
              "type": "artist",
              "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
              },
              "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
              "id": "4SsVbpTthjScTS7U2hmr1X",
              "name": "Arcangel",
              "type": "artist",
              "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/75Y4sJ1vwZfEivbsKPzAx6"
          },
          "href": "https://api.spotify.com/v1/albums/75Y4sJ1vwZfEivbsKPzAx6",
          "id": "75Y4sJ1vwZfEivbsKPzAx6",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b2730e13eee4ec9f7ca9c603baf4",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e020e13eee4ec9f7ca9c603baf4",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d000048510e13eee4ec9f7ca9c603baf4",
              "width": 64
            }
          ],
          "name": "Si Se da Remix",
          "release_date": "2019-08-02",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:75Y4sJ1vwZfEivbsKPzAx6"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7iK8PXO48WeuP03g8YR51W"
            },
            "href": "https://api.spotify.com/v1/artists/7iK8PXO48WeuP03g8YR51W",
            "id": "7iK8PXO48WeuP03g8YR51W",
            "name": "Myke Towers",
            "type": "artist",
            "uri": "spotify:artist:7iK8PXO48WeuP03g8YR51W"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/329e4yvIujISKGKz1BZZbO"
            },
            "href": "https://api.spotify.com/v1/artists/329e4yvIujISKGKz1BZZbO",
            "id": "329e4yvIujISKGKz1BZZbO",
            "name": "Farruko",
            "type": "artist",
            "uri": "spotify:artist:329e4yvIujISKGKz1BZZbO"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4SsVbpTthjScTS7U2hmr1X"
            },
            "href": "https://api.spotify.com/v1/artists/4SsVbpTthjScTS7U2hmr1X",
            "id": "4SsVbpTthjScTS7U2hmr1X",
            "name": "Arcangel",
            "type": "artist",
            "uri": "spotify:artist:4SsVbpTthjScTS7U2hmr1X"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/77ziqFxp5gaInVrF2lj4ht"
            },
            "href": "https://api.spotify.com/v1/artists/77ziqFxp5gaInVrF2lj4ht",
            "id": "77ziqFxp5gaInVrF2lj4ht",
            "name": "Sech",
            "type": "artist",
            "uri": "spotify:artist:77ziqFxp5gaInVrF2lj4ht"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7uS0OYJ72fRQDd8RZEo4J0"
            },
            "href": "https://api.spotify.com/v1/artists/7uS0OYJ72fRQDd8RZEo4J0",
            "id": "7uS0OYJ72fRQDd8RZEo4J0",
            "name": "Zion",
            "type": "artist",
            "uri": "spotify:artist:7uS0OYJ72fRQDd8RZEo4J0"
          }
        ],
        "available_markets": [
          "AD",
          "AE",
          "AR",
          "AT",
          "AU",
          "BE",
          "BG",
          "BH",
          "BO",
          "BR",
          "CA",
          "CH",
          "CL",
          "CO",
          "CR",
          "CY",
          "CZ",
          "DE",
          "DK",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "ES",
          "FI",
          "FR",
          "GB",
          "GR",
          "GT",
          "HK",
          "HN",
          "HU",
          "ID",
          "IE",
          "IL",
          "IN",
          "IS",
          "IT",
          "JO",
          "JP",
          "KW",
          "LB",
          "LI",
          "LT",
          "LU",
          "LV",
          "MA",
          "MC",
          "MT",
          "MX",
          "MY",
          "NI",
          "NL",
          "NO",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PH",
          "PL",
          "PS",
          "PT",
          "PY",
          "QA",
          "RO",
          "SA",
          "SE",
          "SG",
          "SK",
          "SV",
          "TH",
          "TN",
          "TR",
          "TW",
          "US",
          "UY",
          "VN",
          "ZA"
        ],
        "disc_number": 1,
        "duration_ms": 332240,
        "episode": false,
        "explicit": true,
        "external_ids": {
          "isrc": "QM6P41962776"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6K5BsR04ijf3FHNzjbaagD"
        },
        "href": "https://api.spotify.com/v1/tracks/6K5BsR04ijf3FHNzjbaagD",
        "id": "6K5BsR04ijf3FHNzjbaagD",
        "is_local": false,
        "name": "Si Se Da - Remix",
        "popularity": 83,
        "preview_url": "https://p.scdn.co/mp3-preview/7a73a1eb9342fbdb4dcd0e48b5fd92a9b659d246?cid=774b29d4f13844c495f206cafdad9c86",
        "track": true,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:6K5BsR04ijf3FHNzjbaagD"
      },
      "video_thumbnail": {
        "url": null
      }
    }
  ],
  "limit": 100,
  "next": null,
  "offset": 0,
  "previous": null,
  "total": 50
}
        
