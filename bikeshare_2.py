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
        city = input("Please choose the city you would like to explore : \n 'New York City', 'Chicago', 'Washington' \n")
        if city not in ('chicago', 'new york city', 'washington'):
            print("OPS! Please select one of the cities 'New York City', 'Chicago', 'Washington' to proceed \n ")
        else:
            break
    city = city.lower() # to ensure that city is in lower case'''
    
    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please specify the month you would like to look at: \n January, February, March, April, May, June, or all \n")
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("OPS! Please select one of the folowing month: \n January, February, March, April, May, June, or all \n")
        else:
            break
    month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(" please select the day you want: \n  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all \n")
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("OPS! Please select one of the folowing days: \n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all \n")
        else:
            break
    day = day.lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
     # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Displaying the most common month: ", df['month'].mode()[0], "\n")


    # TO DO: display the most common day of week
    print("Displaying the most common day of week: ", df['day_of_week'].mode()[0], "\n")


    # TO DO: display the most common start hour
   

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print("Displaying the most common starting hour: ", popular_hour, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common Start Station is: ", df['Start Station'].mode()[0], "\n")


    # TO DO: display most commonly used end station
    print("The most common End Station is: ", df['End Station'].mode()[0], "\n")


    # TO DO: display most frequent combination of start station and end station trip
    trip = df.groupby(['Start Station', 'End Station'])
    combination = trip.size().sort_values(ascending = False).head(1)
    print("the most frequent combination of Start Station and End Station trip is:\n", combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Displaing Total Travel Time:\n", df['Trip Duration'].sum(), "\n")


    # TO DO: display mean travel time
    print("Displaying Mean Travel Time: \n", df['Trip Duration'].mean(), "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Displaying counts of User Type: \n", user_types, "\n")
    


    # TO DO: Display counts of gender
    try:
      gender= df['Gender'].value_counts()
      print("Displaying counts of Gender:\n", gender, "\n")
    except KeyError:
      print("Sorry! No Gender Data Available for This City.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      old = df['Birth Year'].min()
      print("Displaying the Earliest year of birth:", old, "\n")
    except KeyError:
      print("Sorry! Earliest year of birth is not valid for this city. \n")

    try:
      young = df['Birth Year'].max()
      print("Displaying Most recent year of birth:", young, "\n")
    except KeyError:
      print("Sorry! Most recent year of birth is not valid for this city. \n")

    try:
      common = df['Birth Year'].value_counts().idxmax()
      print("Displaying most common year of birth:", common, "\n" )
    except KeyError:
      print("Sorry! Most common year of birth is not valid for this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(city):
    print("\n Raw data is available to check... \n")
    display_raw =input(" May you want to have a look on more raw data? Type yes or no.\n" )
    while display_raw == "yes":
        try: 
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                print(chunk," \n")
                display_raw =input(" May you want to have a look on more raw data? Type yes or no.\n" )
 
                if display_raw.lower() != 'yes':
                   print("Thank you!")
                   break
        except KeyboardInterrupt:
            print('Thank you.')

       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()