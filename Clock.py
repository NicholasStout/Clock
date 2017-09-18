import pandas as pd
import numpy as np

class Clock:
    hour = 0
    minute = 0
    h_angle = 0
    m_angle = 0
    
    def __init__(self, hour_in, minute_in):
        Clock.hour = (hour_in % 12)
        Clock.minute = minute_in
        
        Clock.m_angle = Clock.minute * 6
        Clock.h_angle =(Clock.hour * 30) + (Clock.minute / 2)
        #These will calculate the angle from 12:00 on the clock, iand emulate the movement of the hour hand
        #between full hours, e.g. at 2:30 on a standard clock, the hour hand would be half way between two and three.
        
    def set_minute(self, minute_in):
        Clock.minute = minute_in
        Clock.m_angle = Clock.minute * 6
        Clock.h_angle = (Clock.hour * 30) + (Clock.minute / 2)
        
    def set_hour(self, hour_in):
        Clock.hour = (hour_in % 12)
        Clock.h_angle = (Clock.hour * 30) + (Clock.minute / 2)
        
    def get_angle(self):
        if (Clock.m_angle > Clock.h_angle):
            return (Clock.m_angle - Clock.h_angle)
        else:
            return (Clock.h_angle - Clock.m_angle)
    #This will return the smallest angle between the hour hand and the minute hand
    
#this reads the text file as a table and pulls it into a pandas dataframe
times_str = pd.read_table('input.txt', delimiter=':', names=['hour', 'minute'])
#initializes a Clock object
angle = Clock(12, 0)
#opens the output file
f = open('output.txt', 'w')
#converts the dataframe to numbers instead of strings
times = times_str.convert_objects(convert_numeric=True)

for i in times.itertuples():
    #check to ensure a number was inputted
    if (np.isnan(i.hour) or np.isnan(i.minute)):
        f.write('ERROR\n')
    #check that there are no spaces in the input
    elif (' ' in times_str.minute[i.Index] or ' ' in times_str.hour[i.Index]):
        f.write('ERROR\n')
    #check to ensure a properly formatted minute was inpputted (nothing like 3:3 instead of 3:03)
    elif ((len(times_str.minute[i.Index]) != 2)):
        f.write('ERROR\n')
    #check to ensure the input is within the bounds of time
    elif(i.hour > 23 or i.minute > 59):
        f.write('ERROR\n')
    elif (i.hour < 0 or i.minute < 0):
        f.write('ERROR\n')
    
    #set the clock to the given time and output the angle
    else:
        angle.set_minute(i.minute)
        angle.set_hour(i.hour)
        f.write(str(angle.get_angle()))
        f.write('\n')
        
f.close()
