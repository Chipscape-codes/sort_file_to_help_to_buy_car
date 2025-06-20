import pandas as pd

data = pd.read_csv("used_cars_data.csv")

# Ensure numeric columns are correct
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')
data['Kilometers_Driven'] = pd.to_numeric(data['Kilometers_Driven'], errors='coerce')

print(data.head())
print(data.shape)

city = input("Enter the city name: ").strip().lower()
data1 = data[data['Location'].str.lower() == city].reset_index(drop=True)

c = float(input("Enter the car price max limit: "))
j = float(input("Enter the car price to find the minimum: "))
d = []
f = []
kilometers = []
for i in range(len(data1)):
    if j < data1['Price'][i] < c:
        print(data1['Name'][i], ":", data1['Price'][i])
        d.append(data1['Name'][i])
        f.append(data1['Price'][i])
        kilometers.append(data1['Kilometers_Driven'][i])
dict = {'Name': d, 'Price': f, 'Kilometers_Driven': kilometers}
df = pd.DataFrame(dict)
print(df)


min_price_row = df.loc[df['Price'].idxmin()]
print("Car with lowest price:")
print(min_price_row)


max_price_row = df.loc[df['Price'].idxmax()]
print("\nCar with highest price:")
print(max_price_row)


min_km_row = df.loc[df['Kilometers_Driven'].idxmin()]
print("\nCar with lowest kilometers driven:")
print(min_km_row)


max_km_row = df.loc[df['Kilometers_Driven'].idxmax()]
print("\nCar with highest kilometers driven:")
print(max_km_row)

#spec of the car with lowest price:
min_price_spec = data1.loc[data1['Price'] == min_price_row['Price']]
print("\nSpec of the car with lowest price:")
print(min_price_spec)

#spec of the car with lowest kilometers driven:
min_km_spec = data1.loc[data1['Kilometers_Driven'] == min_km_row['Kilometers_Driven']]
print("\nSpec of the car with lowest kilometers driven:")
print(min_km_spec)