import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('911.csv')
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


# Checking the info of dataframe
def show_info():
    return df.info()


# Checking the head of the dataframe
def print_head():
    return df.head(10)


# Top five zipcodes for 911 calls
def zipcodes_calls():
    top_five_call = df['zip'].value_counts().head(5)
    return top_five_call


# Top five township for 911 calls
def top_five_township():
    top_five = df['twp'].value_counts().head(5)
    return top_five


# Checking unique title codes in the data frame
def unique_title_codes():
    unique_title = df['title'].nunique()
    return unique_title


# Creating an extra column 'reason' in a dataframe
# Checking the most common reason for 911 calls
def reason_column():
    df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
    return df['Reason'].value_counts()


# Creating a count plot of 911 calls by reason.
def count_plot_reason():
    sns.countplot(x='Reason', data=df, ax=ax1)


# Converting timestamp object to date time.
def date_time():
    df['timeStamp'] = pd.to_datetime(df['timeStamp'])
    # Adding hour, month and day of week columns in the data frame
    df['Month'] = df['timeStamp'].apply(lambda time: time.month)
    df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
    df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)


# Creating count plot based on Day of week and reason.
def reason_dayofweek():
    sns.countplot(x='Day of Week', data=df, hue='Reason', ax=ax2)
    # relocating the legend outside the graph
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)


# Creating linear fit on number of calls per month
def lm_plot():
    sns.lmplot(x='Month', y='twp', data=by_month.reset_index())


# Creating heat map
def heatmap_day_hour():
    sns.heatmap(dayHour)


# Creating heat map
def cluster_map_day():
    sns.clustermap(dayHour)


if __name__ == "__main__":
    print()
    print("Information about the dataframe: ")
    print(show_info())
    print()

    print()
    print("Checking the head of the dataframe: ")
    print(print_head())
    print()

    print("Top five zipcode for 911 calls: ")
    print(zipcodes_calls())
    print()

    print("The unique title codes present in the dataframe: ")
    print(unique_title_codes())
    print()

    print("The top five town for 911 calls are:")
    print(top_five_township())
    print()

    print("Most common reason for 911 calls:")
    print(reason_column())
    print()

    date_time()
    # Mapping day of week to the list of days in the week
    data_map = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    df['Day of Week'] = df['Day of Week'].map(data_map)
    by_month = df.groupby('Month').count()

    # Plotting the data and showing in the graph
    reason_dayofweek()
    count_plot_reason()
    lm_plot()
    # Grouping by multiple column, creating multi level index
    # Using unstack, for unstacking the index for one to be able to use
    # as column and row
    dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()

    # Creating Heatmap
    heatmap_day_hour()
    # Creating Cluster map
    cluster_map_day()
    plt.show()
