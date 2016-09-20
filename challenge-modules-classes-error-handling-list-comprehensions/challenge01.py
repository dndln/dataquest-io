import csv

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
# {'2000': 1, '2001': 3, '2007': 17, '1997': 3, '1986': 1, '1946': 1, '1989': 17, '2005': 8, '1998': 2, '2014': 29, '2012': 45, '1983': 1, '1994': 1, '1999': 5, '2013': 40, '   ': 1, '2009': 10, '2011': 13, '1995': 1, '1963': 1, '2003': 9, '2004': 6, '2002': 7, '1947': 1, '2006': 11, '2008': 10, '2010': 21, '1990': 3, '1993': 1}

# use list comprehensions and 'set' to get a set of the unique values in the team column.
unique_teams = [x[1] for x in nfl_suspensions]
unique_teams = set(unique_teams)
print(unique_teams)
