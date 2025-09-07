from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.cols = 1
        self.result = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        self.add_widget(self.result)
        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]
        grid = GridLayout(cols=4)
        for row in self.buttons:
            for label in row:
                grid.add_widget(Button(text=label, on_press=self.on_button_press, font_size=32))
        self.add_widget(grid)

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.result.text = ""
        elif text == "=":
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = "Error"
        else:
            self.result.text += text

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()
