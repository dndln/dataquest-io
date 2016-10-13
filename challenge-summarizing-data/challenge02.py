import pandas as pd
import ipdb

all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')

print(all_ages.head())
print(recent_grads.head())

# Unique values in Major_category column.
print(all_ages.loc[:, 'Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

# aa_major_categories = all_ages.loc[:, 'Major_category'].unique()
# rg_major_categories = recent_grads.loc[:, 'Major_category'].unique()
#
# for x in aa_major_categories:
#     rows = (all_ages.loc[:, 'Major_category'] == x)
#     returned_rows = all_ages.loc[rows, :]
#     num_people = returned_rows.loc[:, 'Total'].sum()
#     aa_cat_counts[x] = num_people
#
# for x in rg_major_categories:
#     rows = (recent_grads.loc[:, 'Major_category'] == x)
#     returned_rows = recent_grads_.loc[rows, :]
#     num_people = returned_rows.loc[:, 'Total'].sum()
#     rg_cat_counts[x] = num_people

def calculate_num_people(df):
    list_of_cats = df.loc[:, 'Major_category'].unique()
    count_dictionary = dict()

    for x in list_of_cats:
        rows = (df.loc[:, 'Major_category'] == x)
        returned_rows = df.loc[rows, :]
        num_people = returned_rows.loc[:, 'Total'].sum()
        count_dictionary[x] = num_people
    return count_dictionary

aa_cat_counts = calculate_num_people(all_ages)
rg_cat_counts = calculate_num_people(recent_grads)


low_wage_percent = 0.0

num_low_wage_jobs = recent_grads.loc[:, 'Low_wage_jobs'].sum()
num_students = recent_grads.loc[:, 'Total'].sum()

low_wage_percent_temp = num_low_wage_jobs / num_students
low_wage_percent = float(low_wage_percent_temp)
print(low_wage_percent)

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()

rg_lower_count = 0

for x in majors:
    rg_rows = (recent_grads.loc[:, 'Major'] == x)
    aa_rows = (all_ages.loc[:, 'Major'] == x) 
    # .sum() is actually unnecessary, as there is only one row per Major
    rg_unemp_rate = recent_grads.loc[rg_rows, 'Unemployment_rate'].sum()
    aa_unemp_rate = all_ages.loc[aa_rows, 'Unemployment_rate'].sum()

    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1

print(rg_lower_count)

#test_row = recent_grads[recent_grads['Major'] == 'PETROLEUM ENGINEERING']
