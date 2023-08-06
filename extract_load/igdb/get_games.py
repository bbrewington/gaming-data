import requests

class TwitchClient():
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://id.twitch.tv/oauth2/token"

    def auth(self):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }

        response = requests.request("POST", self.base_url, params=params)
        return response.json()

class IgdbClient():
    def __init__(self, twitch_client, auth_token):
        self.client_id = twitch_client.client_id
        self.auth_token = auth_token
        self.base_url = "https://api.igdb.com/v4/games"

    def api_request(self, request_type, payload=None):
        headers = {
          'Accept': 'application/json',
          'Client-ID': self.client_id,
          'Authorization': 'Bearer ' + self.auth_token,
          'Content-Type': 'text/plain'
        }
              
        response = requests.request(request_type, self.base_url, headers=headers, data=payload)
        return response

    def get_games(self):
        games_fields = ['age_ratings','aggregated_rating','aggregated_rating_count','alternative_names',
                        'artworks','bundles','category','checksum','collection','cover','created_at','dlcs',
                        'expanded_games','expansions','external_games','first_release_date','follows','forks',
                        'franchise','franchises','game_engines','game_localizations','game_modes','genres','hypes',
                        'involved_companies','keywords','language_supports','multiplayer_modes','name','parent_game',
                        'platforms','player_perspectives','ports','rating','rating_count','release_dates','remakes',
                        'remasters','screenshots','similar_games','slug','standalone_expansions','status','storyline',
                        'summary','tags','themes','total_rating','total_rating_count','updated_at','url','version_parent',
                        'version_title','videos','websites']

        payload = 'fields ' + ','.join(games_fields) + ';'

        response = self.api_request(request_type="POST", payload=payload)
        
        return response.json()

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv()

    twitch_client = TwitchClient(client_id=os.getenv('TWITCH_CLIENT_ID'), client_secret=os.getenv('TWITCH_CLIENT_SECRET'))
    auth_token = twitch_client.auth()['access_token']

    igdb_client = IgdbClient(twitch_client=twitch_client, auth_token=auth_token)
    games = igdb_client.get_games()
    print(games)
