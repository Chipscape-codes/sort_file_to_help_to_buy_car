import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

data = pd.read_csv("used_cars_data.csv")
print(data.shape)
print(data['Location'].head())
city = input("Enter the city name: ").strip().lower()
data1 = data[data['Location'].str.lower() == city].reset_index(drop=True)

c = float(input("Enter the car price max limit in lakhs: "))
j = float(input("Enter the car price to find the minimum in lakhs: "))

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


min_price_spec = data1.loc[data1['Price'] == min_price_row['Price']]
print("\nSpec of the car with lowest price:")
print(min_price_spec)

min_km_spec = data1.loc[data1['Kilometers_Driven'] == min_km_row['Kilometers_Driven']]
print("\nSpec of the car with lowest kilometers driven:")
print(min_km_spec)


sns.histplot(df['Price'], bins=50)
plt.title("Price Distribution")
plt.show()


sns.histplot(data=df, x=df['Kilometers_Driven'], y=df['Price'], hue=data1["Location"], bins=50, palette="colorblind")
plt.title("Price vs Kilometers Driven")
plt.show()

x = df['Kilometers_Driven'].values.reshape(-1, 1)
y = df['Price'].values.reshape(-1, 1)
model1 = KNeighborsRegressor()
model2 = LinearRegression()
model1.fit(x, y)
model2.fit(x, y)
cost =int(input("Enter the kilometers driven to predict the price: "))
print(model1.predict([[cost]]))  
print(model2.predict([[cost]]))  




plt.scatter(x, y, color='blue', label='Data Points')
plt.scatter(cost, model1.predict([[cost]]), color='red', label='Predicted Price')
plt.xlabel('Kilometers Driven')
plt.ylabel('Price')
plt.show()



plt.scatter(x,y,color='blue', label='Data Points')
plt.plot(x, model2.predict(x), color='black')
plt.xlabel('Kilometers Driven')
plt.ylabel('Price')
plt.show()