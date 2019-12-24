#%%Shreyansh
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

trainDF = pd.read_csv("./datasets/Train.csv")
testDF = pd.read_csv("./datasets/Test.csv")
trainDF.shape

#%%Shreyansh
trainDF.columns

#%%Shreyansh
trainDF.head()

#%% Abhishek
trainDF.info()

#%% Shreyansh
trainDF.describe()

#%% Shreyansh
columns = trainDF.columns.values
columns

matplotlib.rcParams['figure.figsize'] = (15, 15)

numericalColumns = np.delete(columns, [0, 1, 12, 13])
numericalColumns
for i in range(1, len(numericalColumns)):
    plt.subplot(5, 4, i)
    sns.distplot(trainDF[numericalColumns[i]])
    plt.xticks([])
    plt.yticks([])

columns = np.delete(columns, [9, 10])
columns
# rain_p_h and sno_p_h are very sparse and can be dropped
# visibility and dew point are perfectly categorical

#%%Ankur Cell
corr = trainDF.corr()
corr.style.background_gradient(cmap='coolwarm')
trainDF['is_holiday_label'] = np.where(trainDF['is_holiday'] == 'None', 0,1)



#%% Abhishek
trainDF.hist()



#%% Amrit
df=trainDF
time=[]
for i in df['date_time']:
    time.append(i[11:])
df_time=pd.DataFrame(time)    
trainDF['time']=df_time
# In[60]:
time=[]
for i in df['date_time']:
    time.append(i[:4])
df_time=pd.DataFrame(time)    
trainDF['year']= df_time
# In[62]:
time=[]
for i in df['date_time']:
    time.append(i[5:7])
df_time=pd.DataFrame(time)    
trainDF['month']= df_time
# In[63]:
time=[]
for i in df['date_time']:
    time.append(i[8:10])
df_time=pd.DataFrame(time)    
trainDF['date']= df_time
# In[72]:
day=[]
for i in range(len(df)):
    temp=datetime.date(int(df['year'][i]),int(df['month'][i]),int(df['date'][i]))
    day.append(datetime.date.weekday(temp))
# In[73]:
day=pd.DataFrame(day)
# In[76]:
trainDF['weekday']=day
# In[77]:
trainDF.head()

trainDF["year"] = trainDF["year"].astype("int64")
trainDF["month"] = trainDF["month"].astype("int64")
trainDF["date"] = trainDF["date"].astype("int64")


#%% Abhishek
dfT = trainDF[trainDF["year"]==2012]
dfT.drop()
# dfT
# plt.scatter(,trainDF["traffic_volume"])

#%%
