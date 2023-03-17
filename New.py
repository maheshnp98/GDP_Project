import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import requests

# Load GDP data from source link
url = 'https://www.statista.com/statistics/263591/global-gross-domestic-product-gdp/'
data = pd.read_html(url, header=0)[0]

# Rename columns and set Year as index
data.columns = ['Year', 'GDP (USD billions)']
data.set_index('Year', inplace=True)

# Call API to retrieve USD to INR conversion rate
url = 'https://api.exchangeratesapi.io/latest?base=USD&symbols=INR'
response = requests.get(url)
data = response.json()
conversion_rate = data['rates']['INR']
print(f'USD to INR conversion rate: {conversion_rate}')

# Define function to convert GDP values to INR
def convert_to_INR(event):
    global data
    global conversion_rate
    data['GDP (USD billions)'] = data['GDP (USD billions)'] * conversion_rate / 1e9
    plt.clf()
    plt.plot(data)
    plt.title('Global GDP (INR billions)')
    plt.xlabel('Year')
    plt.ylabel('GDP (INR billions)')
    plt.show()

# Add conversion button to chart
ax_convert = plt.axes([0.7, 0.05, 0.1, 0.075])
btn_convert = Button(ax_convert, 'Convert')
btn_convert.on_clicked(convert_to_INR)

# Show the chart
plt.plot(data)
plt.title('Global GDP (USD billions)')
plt.xlabel('Year')
plt.ylabel('GDP (USD billions)')
plt.show()



# # Plot the chart
# plt.plot(data)
# plt.title('Global GDP (USD billions)')
# plt.xlabel('Year')
# plt.ylabel('GDP (USD billions)')
# plt.show()