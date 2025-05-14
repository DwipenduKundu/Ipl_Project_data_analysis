import csv
import matplotlib.pyplot as plt
def start8():
    #here I am taking the match csv file
    with open('/home/dwipendu/Desktop/Project/matches.csv', mode='r') as Match_file:
       
        Match_reader=csv.DictReader(Match_file)  #taking the data into dictionary format
        match_list=list(Match_reader)        #convert that into list for better access
        id_list=[]                           #taking empty list for taking input of all ids of 2015

       #checking for the 2015 season and appended those id's to the list
        for row in match_list:
            if row['season']=='2015':
                id_list.append(row['id'])
    
    #here taking the deliveries csv file    
    with open('/home/dwipendu/Desktop/Project/deliveries.csv', mode='r') as Ipl_file:
        Ipl_reader=csv.DictReader(Ipl_file)     #taking the data into dictionary format
        Ipl_list=list(Ipl_reader)               #convert that into list
        
        #taking the run dictionary and balls dictionary
        Ipl_runs={}
        Ipl_ball={}
        
        #checking rows for the bowling team and there extra runs
        for row in Ipl_list:
            #checking for the match id is present in the list or not i.e 2015 season we are taking
            if row['match_id'] in id_list:
                bowler=row['bowler']
                runs=int(row['total_runs'])

                #If the balls are wide or no balls then we are not counting those as balls
                if row['wide_runs']=='0' and row['noball_runs']=='0':

                    #here adding the balls count per bowler in dictionary format
                    if row['bowler'] not in Ipl_ball:
                        Ipl_ball[bowler]=1
                    else:
                        Ipl_ball[bowler]+=1

                #here adding the runs count per bowler in dictionary format
                if row['bowler'] not in Ipl_runs:
                    Ipl_runs[bowler]=runs
                else:
                    Ipl_runs[bowler]+=runs
                    
        #make one  economic rate dictionary
        economy_rate={}
        
        #here calculating the economy rate per bowler and add that to economy_rate dictionary
        for bowler in Ipl_runs:
            #rate=runs/over
            economy_rate[bowler]=6*(Ipl_runs[bowler]/Ipl_ball[bowler])            #i multiplied that 6 with that beacause we take the ball count but we need the over count of per bowler

        #simply sorted the 10 eliments
        Top_10_economy=sorted(economy_rate.items(),key=lambda x:x[1])[:10:]
        Top_names=[]
        Top_economy=[]

        #take top names and rate for bar plotting
        for i in Top_10_economy:
            Top_names.append(i[0])
            Top_economy.append(i[1])
        graph8(Top_names,Top_economy)
        

def graph8(names,economy):
    
    #taking the axises
    Bowler=names
    Economy=economy

    #Plotting
    plt.bar(Bowler,Economy,color='lightgreen')


    #giving the title and axis names
    plt.title('Top 10 Economical Bowlers in 2015')
    plt.xlabel('Bowlers')
    plt.ylabel('Economy Rate')
    
    #For better view I rotate the X-axis names.
    plt.xticks(rotation=30) 

    #For better view of that graph I used that.
    plt.tight_layout()
    plt.show()
start8()