import pandas as pd

Outlooks = pd.Series(['sunny', 'overcast', 'rainy'])
Temperatures = pd.Series(['hot', 'mild', 'cool'])
Humidities = pd.Series(['high', 'normal'])
Windies = pd.Series([True, False])

Weather = pd.DataFrame( { 'Outlooks': Outlooks, 'Temperatures': Temperatures, 
	'Humidities': Humidities, 'Windies': Windies} )

data = pd.read_csv("datasets/weather.nominal.csv", sep=',')

print("What's the weather like today?")
outlook = input("Outlook (0. Sunny, 1. Overcast, 2. Rainy): ")
temperature = input("Temperature (0. Hot, 1. Mild, 2. Cool): ")
humidity = input("Humidity (0. High, 1. Low): ")
windy = input("Windy? (0. Yes, 1. No): ")

ac_outlook = Weather['Outlooks'][int(outlook)]
ac_temperature = Weather['Temperatures'][int(temperature)]
ac_humidity = Weather['Humidities'][int(humidity)]
ac_windy = Weather['Windies'][int(windy)]

# calculate probabiliry of yes given weather
total_yes = data.query("play == 'yes'")['play'].count()
outlook_c_yes = data.query("outlook == @ac_outlook & play == 'yes'")['play'].count() + 1
temperature_c_yes = data.query("temperature == @ac_temperature & play == 'yes'")['play'].count() + 1
humidity_c_yes = data.query("humidity == @ac_humidity & play == 'yes'")['play'].count() + 1
windy_c_yes = data.query("windy == @ac_windy & play == 'yes'")['play'].count() + 1
e1 = outlook_c_yes / (total_yes + data.outlook.nunique())
e2 = temperature_c_yes / (total_yes + data.temperature.nunique())
e3 = humidity_c_yes / (total_yes + data.humidity.nunique())
e4 = windy_c_yes / (total_yes + data.windy.nunique())
p_yes = total_yes / data['play'].count()
p_yes_g_weather = round(e1 * e2 * e3 * e4 * p_yes, 4)

# calculate probability of no given weather
total_no = data.query("play == 'no'")['play'].count()
outlook_c_no = data.query("outlook == @ac_outlook & play == 'no'")['play'].count() + 1 
temperature_c_no = data.query("temperature == @ac_temperature & play == 'no'")['play'].count() + 1
humidity_c_no = data.query("humidity == @ac_humidity & play == 'no'")['play'].count() + 1
windy_c_no = data.query("windy == @ac_windy & play == 'no'")['play'].count() + 1
e1 = outlook_c_no / (total_no + data.outlook.nunique())
e2 = temperature_c_no / (total_no + data.temperature.nunique())
e3 = humidity_c_no / (total_no + data.humidity.nunique())
e4 = windy_c_no / (total_no + data.windy.nunique())
p_no = total_no / data['play'].count()
p_no_g_weather = round(e1 * e2 * e3 * e4 * p_no, 4)

# calculate lambda
l = p_yes_g_weather + p_no_g_weather

probability_of_yes = p_yes_g_weather / l * 100
probability_of_no = p_no_g_weather / l * 100

print("Probability of Play = yes is", round(probability_of_yes, 2),"%")
print("Probability of Play = no is", round(probability_of_no, 2),"%")
