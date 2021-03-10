import pandas as pd


all_states = pd.read_excel('data/state_M2019_dl.xlsx')
louisiana = all_states[all_states['area_title'] == 'Louisiana']

louisiana_employment_by_sector = louisiana[['occ_code', 'occ_title', 'tot_emp']][louisiana['occ_code'].str.contains('0000')]

louisiana_employment_by_sector.sort_values(by='tot_emp', ascending=False).to_csv('la_emp_by_sec.csv', index=False)

louisiana_oil_employment_breakdown = louisiana[louisiana['occ_title'].str.contains(', Oil ')][['occ_code', 'occ_title', 'tot_emp']]

print(louisiana_oil_employment_breakdown)
