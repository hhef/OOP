class Lightsaber:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        if self._color == "red":
            force_side = "dark"
        else:
            force_side = "light"
        return f"Lightsaber: {self._color}, force: {force_side}"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value in ("red", "blue", "purple", "green"):
            self._color = value
        else:
            raise ValueError("Bad lightsaber color")


lightsaber = Lightsaber("pink")
print(lightsaber)
lightsaber.color = "red"
print(lightsaber)
lightsaber.color = "yellow"
