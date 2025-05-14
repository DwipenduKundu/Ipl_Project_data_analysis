import csv
import matplotlib.pyplot as plt
def start5():
    #here I take the csv file as f file name
    with open('/home/dwipendu/Desktop/Project/matches.csv', mode='r') as file:

        #i read the file and take it as a dictionary
        reader=csv.DictReader(file)
        
        #convert that dictionary into list here
        matches_list=list(reader)

        #taking the empty dictionary for the year and there count
        sesson_disc={}

        #here i count the matches played per year
        for row in matches_list:
            if row['season'] not in sesson_disc:
                sesson_disc[row['season']]=1
            else:
                sesson_disc[row['season']]+=1
        
        #here i do the sort of year so it will be proper to see in graph
        sorted_sesson=[]        #make one empty list
        for years,numbers in sesson_disc.items():
            sorted_sesson.append([years,numbers])       #appending the keys and values of the sesson_disc i.e year and numbers
        sorted_sesson=dict(sorted(sorted_sesson,key=lambda x:x[0])) # sorted according to the year
 
        #get year and the number of matches played per year
        year=list(sorted_sesson.keys())
        number=list(sorted_sesson.values())
        graph5(year,number)

def graph5(year,number):
    
    #taking the axises
    Year=year
    Number_of_matches= number

    #Plotting
    plt.bar(Year,Number_of_matches,color='cyan')

    #giving the title and axis names
    plt.title('Number of matches played per year')
    plt.xlabel('Year')
    plt.ylabel('Number of matches')

    #For better view I rotate the X-axis names.
    plt.xticks(rotation=30) 

    #For better view of that graph I used that.
    plt.tight_layout()
    plt.show()
start5()