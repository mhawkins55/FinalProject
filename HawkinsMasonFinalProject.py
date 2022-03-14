#import tkinter 
import tkinter as tk 
from tkinter import font
import requests
# Size of the Application
HEIGHT=500
WIDTH=600
#test function for testing the entry 
def test_function(entry):
	print("This is the entry: ", entry)
#API URL and API secure key
#bf9ed90149b0940b258266dbea66c7a1
#api.openweathermap.org/data/2.5/forecast?q={city name},{state code}&appid={API key}
# Selected information to be displayed 
def format_response(weather):
	try:
		name = weather ['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemprature (°F): %s' %(name, desc, temp)
	except:
		final_str ='Invalid Input, Try Again!'

	return final_str
# Application run API url and implemts API key to retrieve weather 
def get_weather(city):
	weather_key='bf9ed90149b0940b258266dbea66c7a1'
	url='https://api.openweathermap.org/data/2.5/weather'
	params ={'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)





root = tk.Tk()
# Canvas details
canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH )
canvas.pack()
# Implmentation of background image 
background_image = tk.PhotoImage(file='sunset1.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0, relwidth=1, relheight=1)
#frame size and color details
frame= tk.Frame(root, bg='#ffcdd2', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry frame font, and details
entry= tk.Entry(frame, font=('Andale Mono',18))
entry.place(relwidth=0.65, relheight=1)

# button details (font, font size) also use lamdba here
button = tk.Button(frame, text="Get Weather", font=('Andale Mono',12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# lower frame schematics 
lower_frame = tk.Frame(root,bg='#ffe082', bd=10 )
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label Schematics 
label =tk.Label(lower_frame, font=('Andale Mono',18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()

