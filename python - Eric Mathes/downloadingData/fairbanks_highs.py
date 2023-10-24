import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/fairbanks.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)
    #print(header_row)

    #for index, column_header in enumerate(header_row):
    #   print(index,column_header)

    # Get dates and high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%d/%m/%Y")
        try:
            low = int(row[5])
            high = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

# plot the high and low temperatures
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs,c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates,highs,lows, facecolor = 'blue', alpha = 0.1)

# format plot
plt.title("Daily high temperatures, Sept 2023", fontsize=24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()