from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Create a button widget
        self.button = Button(
            text="Press me!",
            font_size=32,
            on_press=self.on_button_press
        )
        return self.button

    def on_button_press(self, instance):
        # Change the button text when pressed
        instance.text = "Button Pressed!"

# Run the app
if __name__ == "__main__":
    MyApp().run()
