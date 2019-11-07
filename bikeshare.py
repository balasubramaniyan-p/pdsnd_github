# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:19:54 2019

@author: Balasubramaniyan.P
"""


def main():
    while True:
    
        print('-'*40)
        import time
        import pandas as pd
        import numpy as np
        import statistics as stat
        
        pd.set_option('display.max_rows', None)
        
        print('Hello! Let\'s explore some US bikeshare data!')
        print('-'*40)
        
        city = input ("Enter the city you like to explore: ")
        city=city.lower()
        while city not in ['chicago','new_york_city','washington']:
            print('Data for {} is not available. Please type any city of these cities "chicago","new_york_city" or "washington"'.format(city))
            city = input ("Enter the city you like to explore (try again): ")
            city=city.lower()    
        print ("You selected the city: {}".format(city)) 
        print('-'*40)       
        month = input ("Enter the month you like to explore or all if you want to display all the months(months available are Jan-Jun): ")
        month=month.lower()
        month=month[0:3]
        while month not in ['all','jan','feb','mar','apr','may','jun']:
            print('Data for {} is not available. Please type month name or all'.format(month))
            month = input ("Enter the month you like to explore (try again eg: all,jan,feb,.....,jun): ")
            month=month.lower()
        print ("You selected the month: {}".format(month))
        
        print('-'*40)
        
        if month=='all' :
            month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        else:
            month=[month]
        
        day = input ("Enter the day you like to explore or all if you want to display all the days: ")
        day=day.lower()
        day=day[0:3]
        while day not in ['all','mon','tue','wed','thu','fri','sat','sun']:
            print('Data for {} is not available. Please type day name or all'.format(day))
            day = input ("Enter the day you like to explore (try again eg: all,mon,tue,wed,thu,fri,sat,sun): ")
            day=day.lower()
        print ("You selected the day: {}".format(day)) 
        
        print('-'*40)
        
        if day=='all':
            day=['mon','tue','wed','thu','fri','sat','sun']
        else:
            day=[day]  
            
        print ("Loading data.....") 
        
        start = time.time()

            
        filename=city+".csv"
        df = pd.read_csv(filename)    
        df['Start Time']=pd.to_datetime(df['Start Time'])    
        df['End Time']=pd.to_datetime(df['End Time'])
        df['Month-str'] = df['Start Time'].dt.strftime('%b').str.lower()    
        df['day']=df['Start Time'].dt.strftime('%a').str.lower()
        df['hour']=df['Start Time'].dt.strftime('%H')
        
        
         
        df1=df[df['Month-str'].isin(month)] 
        df2=df1[df1['day'].isin(day)] 
        
        
        def time_stats(df2):
            print ("Please wait while we calculate and display statistics on the most frequent times of travel.") 
            return df2['Month-str'].mode()[0],df2['day'].mode()[0],df2['hour'].mode()[0]
        
        common_month,common_day,common_hour=time_stats(df2)
        print('-'*40)    
        print("Here are the results\n Common month is {} \n Common Day of week is {} \n Common hour of the day is {} (in 24hr format)".format(common_month,common_day,common_hour))    
        print('-'*40)  
        
        def station_stats(df2):
            print ("Please wait while we calculate and display statistics on the most popular stations and trip.")
            #df2["combi"]=df2["Start Station"]+" To \n"+df2["End Station"]
            return df2['Start Station'].mode()[0],df2['End Station'].mode()[0],(df2["Start Station"]+" To \n"+df2["End Station"]).mode()[0]
        
        common_start,common_end,common_combi=station_stats(df2)
        print('-'*40)    
        print("Here are the results\n Common Start Stattion is {} \n Common End Stattion is {} \n Common trip is from {}".format(common_start,common_end,common_combi))    
        print('-'*40)
        print("Details on trip duration are \n 1.total travel time is {} \n 2.average time travel is {}".format(df["Trip Duration"].sum(),df["Trip Duration"].mean()))    
        print('-'*40)
        print("Details on user type are \n  {}".format(df["User Type"].value_counts()))
        if city in ['chicago','new_york_city']:
            print('-'*40)
            print("Details on Gender are \n  {}".format(df["Gender"].value_counts()))
            print('-'*40)
            print("Details on Birth Year are \nearlist:{}\nmost recent:{}\nmost common year of birth:{}".format(df2["Birth Year"].min(),df2["Birth Year"].max(),df2["Birth Year"].mode()[0]))
            
            
        print('-'*40) 
        end = time.time()
        elapsed = end - start
        print('-'*40+"\ntime elapsed: {}".format(elapsed))
        
        restart= input('\nWould you like to restart? Enter yes or no.\n')   
        
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


    
     
    