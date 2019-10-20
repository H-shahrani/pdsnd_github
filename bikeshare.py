import time
import pandas as pd
import numpy as np

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
    while True:
        city=input('\nWould you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('Invalid input')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('\nWhich month - January, February, March, April, May or June?\n').lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print('Invalid input')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
        if day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
            break
        else:
            print('Invalid input')

    #df.head()
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
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # Convert the "Start Time" column to datetime and extract the month number and weekday name
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month :
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filter by day of week :
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print('Most Common day:', common_weekday)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_starthour = df['hour'].mode()[0]
    print('Most Common Hour:', common_starthour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_SrtStation = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', common_SrtStation)

    # display most commonly used end station
    common_EndStation = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', common_EndStation)


    # display most frequent combination of start station and end station trip
    combination_trip = df['Start Station'] + " , " + df['End Station']
    Frequent_CombStation = combination_trip.value_counts().idxmax()
    print('Most commonly used combination of start station and end station trip: {} to {}'.format(Frequent_CombStation.split(',')[0], Frequent_CombStation.split(',')[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    tal_TravelTime = df['Trip Duration'].sum()
    print('Total travel time: ', tal_TravelTime)


    # display mean travel time
    avg_traveltime = df['Trip Duration'].mean()
    print('Average travel time: {} '.format(avg_traveltime))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Earliest year of birth: " , df['Birth Year'].min())
        print("Most recent year of birth: " , df['Birth Year'].max())
        print("Most common year of birth: " , df['Birth Year'].mode()[0])


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
