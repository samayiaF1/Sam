def rainfall(year):

    inches = []
    count = 0
    for i in range(year):
        for r in range(1,13):
            print("Enter the rainfall amount for the month {} in inches:".format(r))
            count += 1
            last = float(input())
            inches.append(last)
        totalRainfall = sum(inches)
        totalMonths = count
        return totalMonths, totalRainfall
    if __name__ == "__main__":
        year = int(input("Enter the number of years (Greater than 0):\n"))
        print("For year ",year,":")
        while year <= 0:
            year = int(input("Enter the number of years"))
            totalMonths,totalRainfall = rainfall(year)
            average = totalRainfall/totalMonths
            print("For {} months".format(totalMonths))
            print("Total rainfall: ",totalRainfall)
            print("Average monthly rainfall: ",totalRainfall/totalMonths)
