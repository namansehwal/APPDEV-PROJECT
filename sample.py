import seaborn as sns
import matplotlib.pyplot as plt

x = ['Fruit', 'Vegetable', 'Diary', 'Snacks', 'Beverages', 'Frozen Foods', 'Condiments & Spices', 'Bread & Bakery']
y = [7, 7, 2, 2, 2, 1, 2, 2]

plt.figure(figsize=(20, 10))  # Set the figure size to 10 inches width and 6 inches height

sns.barplot(x=x, y=y)

plt.xticks(rotation=35)  # Rotate x-axis labels by 45 degrees

plt.savefig('static/z.png')

print(typeOf)