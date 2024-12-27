import csv
import matplotlib.pyplot as plt

filename = 'monthly_passengers.csv'

# Initialize dictionary for group data
data = {}

# Read csv file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get the year, month, and total number of passengers from csv
    ISO_index = header_row.index('ISO3')
    total_index = header_row.index('Total')
    total_num_index = header_row.index('Total_OS')
    for row in reader:
        try:
            country = row[ISO_index]
            # Handle NA values in Total_OS
            if row[total_num_index] == "NA":
                total_num = float(row[total_index])  # Use 'Total' if 'Total_OS' is NA
            else:
                total_num = float(row[total_num_index])  # Use 'Total_OS' otherwise
            # Group data by country
            if country in data:
                data[country] += total_num
            else:
                data[country] = total_num
        except ValueError:
            print(f"Missing or invalid data for row: {row}")

# Sort data
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)[:10]
countries = [item[0] for item in sorted_data]
total_nums = [item[1] for item in sorted_data]

# Visualize the figure
fig, ax = plt.subplots()
ax.bar(countries, total_nums, edgecolor = "white", linewidth = 0.7)

plt.xticks(rotation=45)
plt.title('Top 10 countries')
plt.xlabel('Country')
plt.ylabel('Total Passengers')
plt.tight_layout()

plt.show()