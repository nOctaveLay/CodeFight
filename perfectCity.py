def perfectCity(departure, destination):
    result = 0
    for x in range(2):
        if (math.floor(departure[x]) == math.floor(destination[x])):
            floorSum = departure[x] - math.floor(departure[x])
            floorSum += destination[x] -math.floor(destination[x])
            if (floorSum > 1):
                print(floorSum)
                result+= 2-floorSum
            else:
                print(floorSum)
                result += floorSum
        else:
            result += abs(departure[x] - destination[x])
    return result