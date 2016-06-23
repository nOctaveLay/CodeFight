# Consider a lonely Uber driver working in a big city. He has N requests that he has to grant exactly in the given order.
# The route is already mapped out for him and we can assume that he picks up a new passenger at exactly the same spot where he drops off the previous one.
#Knowing the requests' details and the thime it takes to travel from one to the next, determine the minimum amount of time the given route will take,
#or return -1 if it is impossible to service all the requests.
#Note that as you're given the driver's daily plan, the answer is smaller than the number of seconds in a day (24 60 60 = 86400).

#Example
#For travelTimes = [500,500], readyTimes = [1000,3000] and cancelTimes = [2000,4000] the output should be validRoute(travelTimes, readyTimes, cancelTimes) = 1500

#The bestplan the Uber driver can follow is this one:
	#Pick up the first rider at 2000 (he/she cannot do it later because cancelTimes[0] = 2000).
	#Spend 500 seconds delivering the first rider to the desired location.
	#Wait for 500 seconds until the second rider is ready to go.
	#Spend 500 seconds delivering the second rider to the desired location.

def validRoute(travelTimes, readyTimes, cancelTimes):

	earliestStartTime = 0
	latestStartTime = 24 * 60 * 60
	totalWorkTime = 0
	for i in range(len(readyTimes)):
		print(i)
		if ((readyTimes[i] + travelTimes[i]) > cancelTimes[i]):
			print(-1)
			return -1
		latestStartTime = min(latestStartTime,cancelTimes[i]-totalWorkTime)
		if latestStartTime + totalWorkTime <readyTimes[i]:
			totalWorkTime = readyTimes[i] - latestStartTime
		earliestStartTime = max(earliestStartTime,readyTimes[i]-totalWorkTime)
		totalWorkTime += travelTimes[i]
	print(totalWorkTime)
	return totalWorkTime

validRoute([1,1,1],[3000,2000,5000],[3500,3000,6000])