



import pandas as pd

cdataset = pd.read_csv('Dataset/covid_19_data.csv',usecols=['ObservationDate', 'Confirmed'])
ddataset = pd.read_csv('Dataset/covid_19_data.csv',usecols=['ObservationDate', 'Deaths'])
rdataset = pd.read_csv('Dataset/covid_19_data.csv',usecols=['ObservationDate', 'Recovered'])

cdataset['ObservationDate'] = pd.to_datetime(cdataset['ObservationDate'])
ddataset['ObservationDate'] = pd.to_datetime(ddataset['ObservationDate'])
rdataset['ObservationDate'] = pd.to_datetime(rdataset['ObservationDate'])

print(cdataset.info())
print(cdataset.head())
