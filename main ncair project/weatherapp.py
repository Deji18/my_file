import tkinter as tk  # Importing the tkinter library for GUI
import requests  # Importing the requests library for making API calls

# Class for handling weather data fetching
class WeatherApp:
    def __init__(self, main):
        self.main = main
        main.title("Deji's Weather App")
        main.geometry("400x600")
        main.configure(bg="#d1e7dd")  # Background color

        # Create the header label
        self.create_header()

        # Create the location entry
        self.create_location_entry()

        # Create the submit button
        self.create_submit_button()

        # Create the weather icon label
        self.create_weather_icon()

        # Create the weather info label
        self.create_weather_label()

    def create_header(self):
        header = tk.Label(self.main, text="Where are you interested in?", bg="#d1e7dd", fg="#0d6efd", font=("Arial", 12, "bold"))
        header.pack(pady=10)  # Add padding around the widget

    def create_location_entry(self):
        self.location_entry = tk.Entry(self.main, width=30, font=("Times New Roman", 12))
        self.location_entry.pack(pady=5)  # Add padding around the widget

    def create_submit_button(self):
        submit_button = tk.Button(self.main, text="Get Weather", command=self.show_weather, bg="#0d6efd", fg="white", font=("Arial", 12, "bold"))
        submit_button.pack(pady=10)  # Add padding around the widget

    def create_weather_icon(self):
        self.weather_icon = tk.Label(self.main, bg="#d1e7dd")
        self.weather_icon.pack(pady=10)  # Add padding around the widget

    def create_weather_label(self):
        self.weather_label = tk.Label(self.main, text="", bg="#d1e7dd", font=("Arial", 12), wraplength=300, anchor="center")
        self.weather_label.pack(pady=20)  # Add padding around the widget

    def show_weather(self):
        location = self.location_entry.get()  # Get the city name from the entry widget
        weather_data = self.get_weather_data(location)  # Fetch weather data

        if weather_data:
            self.update_weather_display(weather_data)  # Update the display with weather data

    def get_weather_data(self, area):
        api_key = "c461aadfa1aea669f67162f2469ba382"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={area}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            weather = response.json()

            # Check if the API request was successful
            if weather.get("cod") != 200:
                self.weather_label.config(text="City not found", fg="red")
                return None

            return weather  # Return the weather data if successful

        except Exception:
            self.weather_label.config(text="Error retrieving data. Check your network connection.", fg="red")
            return None

    def update_weather_display(self, weather):
        area_name = weather["name"]
        temp = weather["main"]["temp"]
        humidity = weather["main"]["humidity"]
        pressure = weather["main"]["pressure"]
        description = weather["weather"][0]["description"]
        icon_code = weather["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        # Updating the weather label with the retrieved data
        self.weather_label.config(
            text=(
                f"City: {area_name}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Pressure: {pressure} hPa\n"
                f"Description: {description}"
            ),
            fg="navy"
        )

        # Updating the weather icon
        icon_image = tk.PhotoImage(data=requests.get(icon_url).content)
        self.weather_icon.config(image=icon_image)
        self.weather_icon.image = icon_image  # Keep a reference to avoid garbage collection

# Main function to start the application
def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

# Run the application
if __name__ == "__main__":
    main()
