import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
'''
confirmed = pd.read_csv('Dataset/time_series_covid19_confirmed_global.csv')
death = pd.read_csv('Dataset/time_series_covid19_deaths_global.csv')
recover = pd.read_csv('Dataset/time_series_covid19_recovered_global.csv')

dates = confirmed.columns[4:]
confirmed_df = confirmed.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Confirmed')
deaths_df = death.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Deaths')
recovered_df = recover.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Recovered')

recovered_df = recovered_df[recovered_df['Country/Region']!='Canada']

full_table = confirmed_df.merge(right=deaths_df, how='left', on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long'])
full_table = full_table.merge(right=recovered_df, how='left', on=['Province/State', 'Country/Region', 'Date', 'Lat', 'Long'])

full_table['Date'] = pd.to_datetime(full_table['Date'])
'''
def difference(datasets, intervals=1):
    difference = list()
    for i in range(intervals, len(datasets)):
        values = datasets[i] - datasets[i - intervals]
        difference.append(values)
    return pd.Series(difference)

def convertDataToTimeseries(dataset, lagvalue=1):
    dframe = pd.DataFrame(dataset)
    cols = [dframe.shift(i) for i in range(1, lagvalue+1)]
    cols.append(dframe)
    dframe = pd.concat(cols, axis=1)
    dframe.fillna(0, inplace=True)
    return dframe


def scaleDataset(trainX, testX):
    scalerValue = MinMaxScaler(feature_range=(-1, 1))
    scalerValue = scalerValue.fit(trainX)
    trainX = trainX.reshape(trainX.shape[0], trainX.shape[1])
    trainX = scalerValue.transform(trainX)
    testX = testX.reshape(testX.shape[0], testX.shape[1])
    testX = scalerValue.transform(testX)
    return scalerValue, trainX, testX

def forecastRNN(model, batchSize, testX):
    testX = testX.reshape(1, len(testX))
    forecast = model.predict(testX, batch_size=batchSize)
    return forecast[0]
    
def inverseDifference(history_data, yhat_data, intervals=1):
    return yhat_data + history_data[-intervals]

def inverseScale(scalerValue, Xdata, Xvalue):
    newRow = [x for x in Xdata] + [Xvalue]
    array = np.array(newRow)
    array = array.reshape(1, len(array))
    inverse = scalerValue.inverse_transform(array)
    return inverse[0, -1]

'''
df = pd.DataFrame({'Date':full_table['Date'], 'Confirmed':full_table['Confirmed']})
df.to_csv('Confirmed.csv',index=False)

df = pd.DataFrame({'Date':full_table['Date'], 'Deaths':full_table['Deaths']})
df.to_csv('Deaths.csv',index=False)


df = pd.DataFrame({'Date':full_table['Date'], 'Recovered':full_table['Recovered']})
df.to_csv('Recovered.csv',index=False)
'''
confirmed = pd.read_csv('Confirmed.csv')
death = pd.read_csv('Deaths.csv')
recover = pd.read_csv('Recovered.csv')

