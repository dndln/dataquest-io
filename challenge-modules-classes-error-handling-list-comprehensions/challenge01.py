import csv
import ipdb

# assumes 'nfl_suspensions_data.csv' is in current working directory
f = open('nfl-suspensions-data.csv' , 'r')
# read file into a list
nfl_suspensions = list(csv.reader(f))
# remove the header row
nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]

# count up the frequency for each value in the 'year' columns
years = {}
for element in nfl_suspensions:
    current_year = element[5]
    if current_year in years:
        years[current_year] += 1
    else:
        years[current_year] = 1

# print(years)
# a dictionary of key = year, and value = no. of suspensions in that year
# {'2000': 1, '2001': 3, '2007': 17, '1997': 3, '1986': 1, '1946': 1, ... }

# use list comprehensions and 'set' to get a set of the unique values in the team column.
unique_teams = [x[1] for x in nfl_suspensions]
unique_teams = set(unique_teams)
# print(unique_teams)
# {'ATL', 'SEA', 'CHI', 'SD', 'CIN', 'GB', 'CLE', 'JAX', 'MIN', 'NO', ... }

# likewise for 'games' column
unique_games = [x[2] for x in nfl_suspensions]
unique_games = set(unique_games)
# print(unique_games)
# {'6', '20', '4', 'Indef.', '2', '16', '10', '3', '5', '1', '32', '8', '14', '36'}

# create a 'Suspension' class to represent each NFL suspension in the dataset.
class Suspension:

    # def __init__(self, list): # don't shadow python default names like 'list'!
    def __init__(self, arglist):
        self.name = arglist[0]
        self.team = arglist[1]
        self.games = arglist[2]
        # self.year = arglist[5] # deprecated
        # use a try except block instead
        try:
            self.year = int(arglist[5])
        except Exception as exc:
            self.year = 0

    # def get_year(): # need to pass in the instance of the class!
    def get_year(self):
        return self.year

# create a Suspension instance of the third row
third_suspension = Suspension(nfl_suspensions[2])

# create a Suspension instance of the 23rd row
missing_year = Suspension(nfl_suspensions[22])
# get the year
twenty_third_year = missing_year.get_year()
# 0, because it was 'Indef.' which caused an Exception and got self.year set to 0
print(twenty_third_year)
