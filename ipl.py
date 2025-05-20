import csv
import matplotlib.pylab as plt


BATTING_TEAM = 'batting_team'
TOTAL_RUNS = 'total_runs'


def start(file_path):
    # here I take the csv file as f file name
    with open(file_path, mode='r') as file:

        # use reader which read the file and r take it as a dictionary
        reader = csv.DictReader(file)

        # I convert that dictionary into list for easy access
        ipl_List = list(reader)

        # its for the required dictionary where we take the colloms which I required. Here key=batting_team and value= total_runs
        req_dict = {}

        # simply checking the key is present int the required dictionary or not if it ts present then I add the run with previous run else simply initialize the run.
        for row in ipl_List:
            if row[BATTING_TEAM] not in req_dict:
                req_dict[row[BATTING_TEAM]] = int(row[TOTAL_RUNS])
            else:
                req_dict[row[BATTING_TEAM]] += int(row[TOTAL_RUNS])
        req_dict['Rising Pune Supergiants'] += req_dict['Rising Pune Supergiant']
        del req_dict['Rising Pune Supergiant']
        return req_dict


def graph(required_dict):

    # taking the axises
    team = list(required_dict.keys())
    score = list(required_dict.values())

    # Plotting
    plt.bar(team, score, color='limegreen')

    # giving the title and axis names
    plt.title('Total Runs Scored By Each Team')
    plt.xlabel('Batting Team')
    plt.ylabel('Total Runs')

    # For better view I rotate the X-axis names.
    plt.xticks(rotation=30)

    # For better view of that graph I used that.
    plt.tight_layout()
    plt.show()


def execute():
    file_path = '/home/dwipendu/Desktop/Ipl_Project_data_analysis-main/data/deliveries.csv'
    team_run_dict = start(file_path)
    graph(team_run_dict)


if __name__ == "__main__":
    execute()
