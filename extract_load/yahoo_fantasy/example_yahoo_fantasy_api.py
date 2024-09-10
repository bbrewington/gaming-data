from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import pandas as pd

# TODO (user): Make file 'oauth2.json' with contents: {"consumer_key": "YOUR_VALUE", "consumer_secret": "YOUR_VALUE"}
oauth = OAuth2(None, None, from_file='oauth2.json')

AIMPOINT_FB_2024_ID = "449.l.1096319"

league = yfa.League(oauth, AIMPOINT_FB_2024_ID)

# TODO: Generalize this code to work for all weeks.  Currently have to change "week=1" & Ctrl+F "wk1" for current week
matchups_wk1_raw = league.matchups(week=1)
matchups_wk1 = {k: v for k, v in matchups_wk1_raw['fantasy_content']['league'][1]['scoreboard']['0']['matchups'].items() if k != 'count'}
points_wk1 = []
for matchup in matchups_wk1.values():
    teams = {k: v for k, v in matchup['matchup']['0']['teams'].items() if k != 'count'}
    points_wk1.extend(
        {
            'team_name': value['team'][0][2]['name'],
            'manager_nickname': teams[team]['team'][0][-1]['managers'][0]['manager']['nickname'],
            'projected_pts': teams[team]['team'][1]['team_projected_points']['total'],
            'actual_pts': teams[team]['team'][1]['team_points']['total'],
        }
        for team, value in teams.items()
    )

pd.DataFrame(points_wk1).to_csv('points_wk1.csv')
