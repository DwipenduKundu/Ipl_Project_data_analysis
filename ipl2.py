import matplotlib.pyplot as plt
import csv
def start2():
    #here I take the csv file as f file name
    with open('/home/dwipendu/Desktop/Project/deliveries.csv',mode='r') as file:

        #use reader which read the file and r take it as a dictionary
        reader=csv.DictReader(file)
        
        #I convert that dictionary into list for easy access
        Ipl_List=list(reader)
        
        #its for the Batsman dictionary. Here key=batsman and value=runs
        batsman_dict={}

        #Here I am checking for batting team is Royal Challengers Bnagalore or not. If its satisfied then I check for the batsman name is present in the batsman_dict or not if not then initialize that and if yes then simmply added with previous run.
        for row in Ipl_List:
            if row['batting_team']=='Royal Challengers Bangalore':
                if row['batsman'] not in batsman_dict:
                    batsman_dict[row['batsman']]=int(row['total_runs'])
                else:
                    batsman_dict[row['batsman']]+=int(row['total_runs'])
        
        #Taking batsman list where I convert the batsman_dict into list format for better accessing.
        batsman_list=[]
        for keys,values in batsman_dict.items():
            temp=[keys,values]
            batsman_list.append(temp)
        
        #Here sort the baatsman according to there score and take the list from last 10 i.e top 10 so that -1 index to -11 index.
        Top_10_Batsman=sorted(batsman_list,key=lambda x:x[1])[:-11:-1]
        
        #Here taking the names and runs in differet list for easy plotting.
        Top_names=[]
        Top_runs=[]
        for i in Top_10_Batsman:
            Top_names.append(i[0])
            Top_runs.append(i[1])
        graph2(Top_names,Top_runs)

def graph2(names,runs):
    
    #taking the axises
    Batsman=names
    Run=runs

    #Plotting
    plt.bar(Batsman,Run,color='lightblue')


    #giving the title and axis names
    plt.title('Top 10 RCB Batsman')
    plt.xlabel('Batsman')
    plt.ylabel('Runs')
    
    #For better view I rotate the X-axis names.
    plt.xticks(rotation=30) 

    #For better view of that graph I used that.
    plt.tight_layout()
    plt.show()
start2()