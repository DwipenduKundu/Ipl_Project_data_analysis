import matplotlib.pylab as plt
import csv

def start():
    #here I take the csv file as f file name
    with open('/home/dwipendu/Desktop/Project/deliveries.csv',mode='r') as file:
        
        #use reader which read the file and r take it as a dictionary
        reader=csv.DictReader(file)

        #I convert that dictionary into list for easy access
        Ipl_List=list(reader)

        #its for the required dictionary where we take the colloms which I required. Here key=batting_team and value= total_runs
        req_dict={}

        #simply checking the key is present int the required dictionary or not if it ts present then I add the run with previous run else simply initialize the run.
        for row in Ipl_List:
            if row['batting_team'] not in req_dict:
                req_dict[row['batting_team']]=int(row['total_runs'])
            else:
                req_dict[row['batting_team']]+=int(row['total_runs'])    
        req_dict['Rising Pune Supergiants']+=req_dict['Rising Pune Supergiant']
        del req_dict['Rising Pune Supergiant']
        graph(req_dict)
def graph(required_dict):
    
    #taking the axises
    Team=list(required_dict.keys())
    Score=list(required_dict.values())

    #Plotting
    plt.bar(Team,Score,color='limegreen')

    #giving the title and axis names
    plt.title('Total Runs Scored By Each Team')
    plt.xlabel('Batting Team')
    plt.ylabel('Total Runs')

    #For better view I rotate the X-axis names.
    plt.xticks(rotation=30) 

    #For better view of that graph I used that.
    plt.tight_layout()
    plt.show()
start()