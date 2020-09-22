import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['january','february','march','april','may','june']

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
    city=input('\nSpecify the name of city you would like to analyse from chicago, new york city or washington\n')
    while city not in CITY_DATA:
        
        print("INVALID INPUT, please enter the right NAME")
        city=input('\nSpecify the name of city you would like to analyse from chicago, new york city or washington\n')     
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month=input('\nWould you like to analyse data based on month. Please enter january, february, march, april, may , june or simply all\n ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input('Would you like to analyse data based on day or simply just all \n')
    print('You entered city as',city,'month  as' ,month, 'day as', day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """ 
    if month!='all':
        month=months.index(month)+1
        df.query(df['months']==month,inplace=1)

    if day!='all':
       df = df[df['day_of_week'] == day.title()]
       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month_no=df['month'].mode()[0]
    popular_month=months[popular_month_no-1]
    print('Most popular month is...',popular_month)
      
    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('Most common day of the week',popular_day)
      
    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print('Most common hour',popular_hour)
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is',popular_start_station)
       
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most commonly used end station is',popular_end_station)
      

    # TO DO: display most frequent combination of start station and end station trip
      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time is...',total_travel_time)
   
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Total travel time is...',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print("Displaying the counts of user types...",user_types)

    # TO DO: Display counts of gender
    gender_count=df['Gender'].value_counts()
    print("Displaying the counts of gender...",gender_count)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year=df['Birth Year'].min()
    recent_year=df['Birth Year'].max()
    common_year=df['Birth Year'].mode()

    print('Displaying earliest year of birth...',earliest_year)
    print('Displaying most reacent year of birth...',recent_year)
    print('Displaying most common year of birth...',common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
