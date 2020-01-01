import pandas as pd
import datetime

# usr input lists teams to see in order. arrange these in order in an array
userTeams = ['brewers', 'cardinals', 'cubs']
teamSchedules = []

for team in userTeams:
    teamSchedules.append(pd.read_csv("schedules/" + team +"-home-schedule.csv"))
    
for schedule in teamSchedules:
    schedule.drop(schedule.columns[[0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]], axis=1, inplace=True)
    schedule["START TIME"].fillna('00:00 AM', inplace=True)
    schedule["START TIME ET"].fillna('00:00 AM', inplace=True)
    schedule["DATE TIME"] = schedule["START DATE"].map(str) + " " + schedule["START TIME"]
    schedule["DATE TIME ET"] = schedule["START DATE"].map(str) + " " + schedule["START TIME ET"]
    schedule.drop(schedule.columns[[0, 1, 2]], axis=1, inplace=True)
    schedule['DATE TIME'] =  pd.to_datetime(schedule['DATE TIME'], format='%m/%d/%y %H:%M %p')
    schedule['DATE TIME ET'] =  pd.to_datetime(schedule['DATE TIME ET'], format='%m/%d/%y %H:%M %p')
    schedule.set_index('DATE TIME', inplace=True)
    
start = datetime.datetime(2020,5,1,0,0,0)
start = str(start)

end = datetime.datetime(2020,5,15,0,0,0)
# add one day in order to include the ending day value 
# in the list of potential games (date_range excludes the ending value)
end = end + datetime.timedelta(days=1)
end = str(end)

for schedule in teamSchedules:
    print(schedule.loc[start:end])
