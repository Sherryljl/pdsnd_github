import time
import pandas as pd
import numpy as np
import datetime
from itertools import islice

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('\nType a city of interest(chicago, new york city, washington):')
    cities=['chicago','new york city','washington']
    while city not in cities:
        print('\nThe city name is not valid!')
        city=input('\nPlease enter a valid city name(chicago,new york city, washington):')

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('\nType a month of interest(all,january,february,...,june):')
    months=['all','january','february','march','april','may','june']
    while month not in months:
        print('\nThe month name is not valid!')
        month=input('\nPlease enter a valid month name(all,january,february,...,june):')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('\nType a day of week of interest(all,monday,tuesday,wednesday,thursday,friday,saturday,sunday)')
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while day not in days:
        print('\nThe dat of week name is not valid!')
        day=input('\nPlease enter a valid day of week name(all,monday,tuesday,wednesday,thursday,friday,saturday,sunday):')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.strftime('%A')
    if month!='all':
        months_list=['january','february','march','april','may','june']
        df=df[df['month']==months_list.index(month)+1]
    if day!='all':
        df=df[df['day']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('\nThe most popular month is {}'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day_of_week=df['day'].mode()[0]
    print('\nThe most popular day of week is {}'.format(popular_day_of_week))


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('\nThe most popular hour is {}'.format(popular_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is {}'.format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('\nThe most commonly used end station is {}'.format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station']=df['Start Station']+'--'+df['End Station']
    popular_station=df['Combined Station'].mode()[0]
    print('\nThe most frequent combination of start station and end station trip is {}'.format(popular_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print('\nTotal travel time is {} seconds'.format(total_time))

    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('\nMean travel time is {} seconds'.format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types:\n')
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('\nThe Gender column does not exist.')
    else:
        print('\nCounts of gender:\n')
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('\nThe Birth Year column does not exist.')
    else:
        min_birthyear=df['Birth Year'].min()
        print('\nThe earliest year of birth is {}'.format(int(min_birthyear)))
        max_birthyear=df['Birth Year'].max()
        print('\nThe most recent year of birth is {}'.format(int(max_birthyear)))
        mode_birthyear=df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is {}'.format(int(mode_birthyear)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def next_n_lines(file_opened, N):
    """return a list of N lines chunk from a opened file
    Args:
        file_opened - opened file for chosen ciry
        N - number of records will be return at a time
    """
    return [x.strip() for x in islice(file_opened, N)]

def view_raw(city):
    """Displace 5 rows of raw data every time"""
    seeraw=input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n')
    if seeraw=='yes':
        with open(CITY_DATA[city]) as cityfile:
            seemore='yes'
            while seemore=='yes':
                print (next_n_lines(cityfile,5))
                seemore=input('\nWould you like to see five more records? Enter yes or no.\n')




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw(city)

        restart = input('\nWould you like to restart to see another city? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
