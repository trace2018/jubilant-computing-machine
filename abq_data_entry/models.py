import os
import json

class SettingsModel:
    """A model for save settings"""

    variables = {
            "autofill date": {"type": "bool", "value": True},
            "autofill sheet data": {"type": "bool", "value": True}
            }

    def __init__(self, filename="abq_settings.json", path="~"):

        self.filepath = os.path.join(os.path.expanduser(path), filename)
        self.load()

    def set(self, key, value):
        """Set a variable value"""
        if (key in self.variables and type(value).__name__ == self.variables[key]["type"]):
            self.variables[key]["value"] = value
        else:
            raise ValueError("Bad key or wrong variable type")

    def save(self, settings=None):
        """Save the current settings to the file"""
        json_string = json.dumps(self.variables)
        with open(self.filepath, "w") as fh:
            fh.write(json_string)

    def load(self):
        """Load the settings from the file"""

        if not os.path.exists(self.filepath):
            return

        with open(self.filepath, "r") as fh:
            raw_values = json.loads(fh.read())

        for key in self.variables:
            if key in raw_values and "value" in raw_values[key]:
                raw_value = raw_values[key]["value"]
                self.variables[key]["value"] = raw_value
