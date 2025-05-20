import csv
from collections import defaultdict
import matplotlib.pyplot as plt


SEASON = 'season'
TEAM1 = 'team1'
TEAM2 = 'team2'


def start4(file_path):
    dict_match = defaultdict(lambda: defaultdict(int))

    # import files as Match
    with open(file_path, mode='r') as match_file:
        # convert it into dictionary
        matche_Reader = csv.DictReader(match_file)

        # create the dictionary as this format: {year:{winner:count}} here
        for delivery in matche_Reader:
            year = delivery[SEASON]
            team1 = delivery[TEAM2]
            team2 = delivery[TEAM2]
            dict_match[year][team1] += 1
            dict_match[year][team2] += 1
    return dict_match


def graph4(dictionary):

    # got all the years list
    all_years = sorted(dictionary.keys())

    # got all team names also
    all_teams = sorted({team for year_data in dictionary.values()
                       for team in year_data})

    # create team and there count of played matches as per there year like {team:[counts....]}
    matches_by_team = {team: [] for team in all_teams}
    for year in all_years:
        year_data = dictionary[year]
        for team in all_teams:
            matches_by_team[team].append(year_data.get(team, 0))

    # plotting
    x_pos = list(range(len(all_years)))
    bottom = [0] * len(all_years)
    plt.figure(figsize=(12, 6))
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


def execute4():
    file_path = '/home/dwipendu/Desktop/Ipl_Project_data_analysis-main/data/matches.csv'
    dict_match = start4(file_path)
    graph4(dict_match)


if __name__ == "__main__":
    execute4()
