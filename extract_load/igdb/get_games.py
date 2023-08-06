import requests

url = "https://api.igdb.com/v4/games"

games_fields = ['age_ratings','aggregated_rating','aggregated_rating_count','alternative_names',
                'artworks','bundles','category','checksum','collection','cover','created_at','dlcs',
                'expanded_games','expansions','external_games','first_release_date','follows','forks',
                'franchise','franchises','game_engines','game_localizations','game_modes','genres','hypes',
                'involved_companies','keywords','language_supports','multiplayer_modes','name','parent_game',
                'platforms','player_perspectives','ports','rating','rating_count','release_dates','remakes',
                'remasters','screenshots','similar_games','slug','standalone_expansions','status','storyline',
                'summary','tags','themes','total_rating','total_rating_count','updated_at','url','version_parent',
                'version_title','videos','websites']
payload = games_fields.join(',') + ';'

orig_games_fields = "fields age_ratings,aggregated_rating,aggregated_rating_count,alternative_names,artworks,bundles,category,checksum,collection,cover,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;"

assert payload != orig_games_fields, 'Payloads do not match'

# headers = {
#   'Accept': 'application/json',
#   'Client-ID': 'your_client_id_here',
#   'Authorization': 'Bearer your_auth_token_here',
#   'Content-Type': 'text/plain'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
