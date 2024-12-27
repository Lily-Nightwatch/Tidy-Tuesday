import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

filename = 'monthly_passengers.csv'

# Initialize dictionary for group data
data = {}

# Read csv file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get the year, month, and total number of passengers from csv
    year_index = header_row.index('Year')
    month_index = header_row.index('Month')
    total_index = header_row.index('Total')
    total_num_index = header_row.index('Total_OS')
    for row in reader:
        try:
            year_month = datetime.strptime(f"{row[year_index]},{row[month_index]}",'%Y,%m')
            total_OS_num = float(row[total_num_index])
            # Group data with the same date
            if year_month in data:
                data[year_month] += total_OS_num
            else:
                data[year_month] = total_OS_num
        except ValueError:
            if year_month in data:
                total_num = float(row[total_index])
                data[year_month] += total_num
            else:
                data[year_month] = total_num
# Sort data
sorted_data = sorted(data.items())
year_months = [item[0] for item in sorted_data]
total_nums = [item[1] for item in sorted_data]

# Visualize the figure
x = mdates.date2num(year_months)
y = total_nums

fig, ax = plt.subplots()
ax.bar(x,y,width = 30, edgecolor = "white", linewidth = 0.7)

ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.xticks(rotation=45)
plt.title('Monthly Passengers')
plt.xlabel('Date')
plt.ylabel('Total Passengers')
plt.tight_layout

plt.show()
