# Name:Shyam Gupta
# netID:ft1685
# HW 2 Solution
 

#Asking users for input
miles = int(input("Input number of miles that you will drive: "))
speed = int(input("Input speed that you will drive at (m/h): "))          
stops = int(input("Input number of stops you plan to make: "))
duration = int(input("Input average duration of time at stops (in minutes): "))  # I am assuming that the duration is the time spent at each stop

#Printing empty space for new line for formatting 
print(" ") 

#Calcualting total time of trip

time_minutes = ((miles/speed)*60) + (stops*duration)      # Multiplying by 60 to show time in minutes


#Printing output
print(f'The calculated total time your trip will take will be : {time_minutes} minutes')
