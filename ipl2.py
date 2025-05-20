import matplotlib.pyplot as plt
import csv


BATTING_TEAM = 'batting_team'
BATSMAN = 'batsman'
TOTAL_RUNS = 'total_runs'


def start2(file_path):
    # here I take the csv file as f file name
    with open(file_path, mode='r') as file:

        # use reader which read the file and r take it as a dictionary
        reader = csv.DictReader(file)

        # I convert that dictionary into list for easy access
        ipl_List = list(reader)

        # its for the Batsman dictionary. Here key=batsman and value=runs
        batsman_dict = {}

        # Here I am checking for batting team is Royal Challengers Bnagalore or not. If its satisfied then I check for the batsman name is present in the batsman_dict or not if not then initialize that and if yes then simmply added with previous run.
        for row in ipl_List:
            if row[BATTING_TEAM] == 'Royal Challengers Bangalore':
                if row[BATSMAN] not in batsman_dict:
                    batsman_dict[row[BATSMAN]] = int(row[TOTAL_RUNS])
                else:
                    batsman_dict[row[BATSMAN]] += int(row[TOTAL_RUNS])

        # Taking batsman list where I convert the batsman_dict into list format for better accessing.
        batsman_list = []
        for keys, values in batsman_dict.items():
            temp = [keys, values]
            batsman_list.append(temp)

        # Here sort the baatsman according to there score and take the list from last 10 i.e top 10 so that -1 index to -11 index.
        top_10_Batsman = sorted(batsman_list, key=lambda x: x[1])[:-11:-1]

        # Here taking the names and runs in differet list for easy plotting.
        top_names = []
        top_runs = []
        for i in top_10_Batsman:
            top_names.append(i[0])
            top_runs.append(i[1])
        return top_names, top_runs


def graph2(names, runs):

    # taking the axises
    batsman = names
    run = runs

    # Plotting
    plt.bar(batsman, run, color='lightblue')

    # giving the title and axis names
    plt.title('Top 10 RCB Batsman')
    plt.xlabel('Batsman')
    plt.ylabel('Runs')

    # For better view I rotate the X-axis names.
    plt.xticks(rotation=30)

    # For better view of that graph I used that.
    plt.tight_layout()
    plt.show()


def execute2():
    file_path = '/home/dwipendu/Desktop/Ipl_Project_data_analysis-main/data/deliveries.csv'
    batsman, runs = start2(file_path)
    graph2(batsman, runs)


if __name__ == "__main__":
    execute2()
