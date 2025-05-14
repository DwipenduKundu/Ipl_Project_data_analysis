import csv
import matplotlib.pyplot as plt
from collections import defaultdict
def start7():
    #here I am taking the match csv file
    with open('/home/dwipendu/Desktop/Project/matches.csv', mode='r') as Match_file:
        Match_reader=csv.DictReader(Match_file)
        id_list=[]       #taking empty list for taking input of all ids of 2016

       #checking for the 2016 season and appended those id's to the list
        for row in Match_reader:
            if row['season']=='2016':
                id_list.append(row['id'])
        
        #here removing the duplicates from the list
        id_list=list(set(id_list))

    #here taking the deliveries csv file    
    with open('/home/dwipendu/Desktop/Project/deliveries.csv', mode='r') as Ipl_file:
        Ipl_reader=csv.DictReader(Ipl_file)
        Ipl_list=list(Ipl_reader)               #convert that into list
        Ipl_dict={}                 #taking empty dictionary for the bowling team and there extra runs
        
        #checking rows for the bowling team and there extra runs
        for row in Ipl_list:
            if row['match_id'] in id_list:
                if row['bowling_team'] not in Ipl_dict:
                    Ipl_dict[row['bowling_team']]=int(row['extra_runs'])
                else:
                    Ipl_dict[row['bowling_team']]+=int(row['extra_runs'])
        #the list of keys and values are stored into variable and call the graph function to plot the graph
        Team=Ipl_dict.keys()
        run=Ipl_dict.values()
        graph7(Team,run)


def graph7(Team,run):
    
    #taking the axises
    Team_name=Team
    Extra_runs= run

    #Plotting
    plt.bar(Team_name,Extra_runs,color='darkblue')

    #giving the title and axis names
    plt.title('Extra runs conceded per team in the year 2016')
    plt.xlabel('Team Names')
    plt.ylabel('Extra Runs conceded')

    #For better view I rotate the X-axis names.
    plt.xticks(rotation=45,ha='right') 

    #For better view of that graph I used that.
    plt.tight_layout()
    plt.show()
start7()