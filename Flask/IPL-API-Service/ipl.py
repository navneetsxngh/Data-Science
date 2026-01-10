import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\singh\OneDrive\Desktop\Data-Science\Flask\IPL-API-Service\matches.csv')

def teamsAPI():
    teams = list(set(list(df['team1']) + list(df['team2'])))
    team_dict = {
        'teams' : teams
    }
    return team_dict

def teamVteamAPI(team1, team2):
    try:
        valid_teams = list(set(df['team1']).union(set(df['team2'])))

        if team1 not in valid_teams or team2 not in valid_teams:
            return {"Message": "Invalid Team name"}

        filtered_df = df[
            ((df['team1'] == team1) & (df['team2'] == team2)) |
            ((df['team1'] == team2) & (df['team2'] == team1))
        ]

        total_matches = filtered_df.shape[0]

        wins = filtered_df['winner'].value_counts()

        matches_won_team1 = wins.get(team1, 0)
        matches_won_team2 = wins.get(team2, 0)

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
            'Total Matches': str(total_matches),
            'Team 1 Wins': str(matches_won_team1),
            'Team 2 Wins': str(matches_won_team2),
            'Draws': str(draws)
        }

        return response

    except Exception as e:
        return {
            "Error": "Something went wrong",
            "Details": str(e)
        }
