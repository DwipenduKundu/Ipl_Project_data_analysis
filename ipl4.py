import csv
from collections import defaultdict
import matplotlib.pyplot as plt

def start4():
    Dict_match = defaultdict(lambda: defaultdict(int))

    #import files as Match
    with open('/home/dwipendu/Desktop/Project/matches.csv', mode='r') as Match_file:
        Matche_Reader = csv.DictReader(Match_file)      #convert it into dictionary
        
        #create the dictionary as this format: {year:{winner:count}} here
        for delivery in Matche_Reader:
            year = delivery['season']
            team1 = delivery['team1']
            team2 = delivery['team2']
            Dict_match[year][team1] += 1
            Dict_match[year][team2] += 1
    graph(Dict_match)

def graph(Dictionary):

    #got all the years list
    all_years = sorted(Dictionary.keys())

    #got all team names also
    all_teams = sorted({team for year_data in Dictionary.values() for team in year_data})

    #create team and there count of played matches as per there year like {team:[counts....]}
    matches_by_team = {team: [] for team in all_teams}
    for year in all_years:
        year_data = Dictionary[year]
        for team in all_teams:
            matches_by_team[team].append(year_data.get(team, 0))
    

    #plotting
    x_pos = list(range(len(all_years)))  
    bottom = [0] * len(all_years)
    plt.figure(figsize=(12,6))  
    for team in all_teams:
        team_values = matches_by_team[team]
        plt.bar(x_pos, team_values, bottom=bottom, label=team)
        bottom = [bottom[i] + team_values[i] for i in range(len(all_years))]

    plt.xticks(x_pos, all_years, rotation=0)
    plt.xlabel("Year")
    plt.ylabel("Number of Matches Played")
    plt.title("Matches per Year")
    plt.legend(title="Teams", bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

start4()