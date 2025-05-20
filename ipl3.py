import csv
import matplotlib.pyplot as plt


# Taking extertal umpire data
umpires_dict = {
    'RB Tiffin': 'Zimbabwe',
    'S Das': 'India',
    'A Nand Kishore': 'India',
    'TH Wijewardene': 'Sri Lanka',
    'PR Reiffel': 'Australia',
    'AL Hill': 'England',
    'RM Deshpande': 'India',
    'SD Fry': 'Australia',
    'C Shamshuddin': 'India',
    'AM Saheba': 'India',
    'IL Howell': 'South Africa',
    'DJ Harper': 'Australia',
    'AY Dandekar': 'India',
    'AK Chaudhary': 'India',
    'K Srinivasan': 'India',
    'BNJ Oxenford': 'Australia',
    'RK Illingworth': 'England',
    'Aleem Dar': 'Pakistan',
    'SJ Davis': 'Australia',
    'S Asnani': 'India',
    'K Srinath': 'India',
    'SL Shastri': 'India',
    'MR Benson': 'England',
    'CB Gaffaney': 'New Zealand',
    'RJ Tucker': 'Australia',
    'GAV Baxter': 'New Zealand',
    'RE Koertzen': 'South Africa',
    'I Shivram': 'India',
    'PG Pathak': 'India',
    'SS Hazare': 'India',
    'CK Nandan': 'India',
    'SJA Taufel': 'Australia',
    'KN Ananthapadmanabhan': 'India',
    'BG Jerling': 'South Africa',
    'Asad Rauf': 'Pakistan',
    'K Bharatan': 'India',
    'A Deshmukh': 'India',
    'BF Bowden': 'New Zealand',
    'GA Pratapkumar': 'India',
    'BR Doctrove': 'West Indies',
    'Nitin Menon': 'India',
    'VA Kulkarni': 'India',
    'K Hariharan': 'India',
    'SK Tarapore': 'India',
    'Subroto Das': 'India',
    'HDPK Dharmasena': 'Sri Lanka',
    'M Erasmus': 'South Africa',
    'AV Jayaprakash': 'India',
    'VK Sharma': 'India',
    'JD Cloete': 'South Africa',
    'YC Barde': 'India',
    'NJ Llong': 'England',
    'SD Ranade': 'India',
    'S Ravi': 'India'
}


def start3(file_dict):
    # convert that dictionary into list for easy access
    umpire_list = []
    for keys, values in file_dict.items():
        temp = [keys, values]
        umpire_list.append(temp)

    # removing the Indian umpires from the list and add that to list of umpires and there origin.
    umpire_origin = []  # create a list of umpires and their origin
    for data in umpire_list:
        if data[1] != 'India':  # exclude the Indian umpires
            # append that to umire_origin
            umpire_origin.append([data[0], data[1]])

    # count the umpires according to there origin
    umpire_count = {}  # creating a umpire counts dictionary
    for data in umpire_origin:
        if data[1] not in umpire_count:
            umpire_count[data[1]] = 1  # assign
        else:
            umpire_count[data[1]] += 1  # add the count

    # get the umpire and counts list
    country = list(umpire_count.keys())
    counts = list(umpire_count.values())
    return country, counts


def graph3(country, num):

    # taking the axises
    origin = country
    number = num

    # plotting
    plt.bar(origin, number, color='lime')

    # giving the title and axis names
    plt.title('Umpires Origin')
    plt.xlabel('Country')
    plt.ylabel('Number of Umpires')

    # For better view I rotate the X-axis names.
    plt.xticks(rotation=30)

    # For better view of that graph I used that.
    plt.tight_layout()
    plt.show()


def execute3():
    country, counts = start3(umpires_dict)
    graph3(country, counts)


if __name__ == "__main__":
    execute3()
