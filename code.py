# --------------
import yaml

# Read the data of the format .yaml type
#file=open(path,"r+")
with open(path) as file:
    data=yaml.load(file)
# Find data type of the file
print(type(file))
print(type(data))
data
# In which city, and at which venue the match was played and where was it played ?
venue=data['info']['venue']
print(venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams=data['info']['teams']
print(len(teams))

# Which team won the toss and what was the decision of toss winner ?
data
toss=data['info']['toss']
#print(toss)
print(toss['winner']+" and decision was to "+toss['decision'])
# Find the first bowler and first batsman who played the first ball of the first inning
inning1=data['innings'][0]['1st innings']
deliveries=inning1['deliveries']
#print(deliveries)
first_batsman=deliveries[0][0.1]['batsman']
fir_bowler=deliveries[0][0.1]['bowler']
print(first_batsman)
print(fir_bowler)
#print(inning)
print(first_batsman)
# How many deliveries were delivered in first inning ?
print(len(deliveries))
# How many deliveries were delivered in second inning ?
inning2=data['innings'][0]['1st innings']
deliveries_inn2=inning2['deliveries']
print(len(deliveries_inn2))
# Which team won and how ?
team_won_how=data['info']['outcome']['by']['runs']
team_won=data['info']['outcome']['winner']
print(team_won + "by "+ str(team_won_how) + " runs")
#print(team_won)



