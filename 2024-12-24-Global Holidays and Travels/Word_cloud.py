import csv
import wordcloud
import matplotlib.pyplot as plt

filename = 'global_holidays.csv'

# Initialize dictionary for group data
data = {}

# Read csv file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get the name of holiday from csv
    name_index = header_row.index('Name')
    with open('names.txt', 'w') as f:
        for row in reader:
            try:
                name = row[name_index]
                f.write(f"{name}\n")
            except ValueError:
                print(f"Missing or invalid data for row: {row}")

# Visualize the figure
text = open('names.txt').read()
word_cloud = wordcloud.WordCloud().generate(text)
plt.imshow(word_cloud,interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('Holiday_word_cloud.png',dpi=300)


