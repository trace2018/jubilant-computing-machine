import tkinter as tk
from datetime import datetime
from . import models as m

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ABQ Data Entry Application")
        self.resizable(width=False, height=False)

        # filename
        datestring = datetime.today().strftime("%Y-%m-%d")
        default_filename = "abq_data_record_{}.csv".format(datestring)
        self.filename = tk.StringVar(value=default_filename)
        
        # settings
        self.settings_model = m.SettingsModel()
        self.load_settings()
        
        # menus
        # TODO menus
    
    def load_settings(self):
        """Load settings into our self.settings dict"""
        vartypes = {
            "bool": tk.BooleanVar,
            "str": tk.StringVar,
            "int": tk.IntVar,
            "float": tk.DoubleVar
        }
        
        # create our dict of settings variables from the model's settings
        self.settings = {}
        for key, data in self.settings_model.variables.items():
            vartype = vartypes.get(data["type"], tk.StringVar)
            self.settings[key] = vartype(value=data["value"])
        
        # put a trace on the variables so they get stored when changed
        for var in self.settings.values():
            var.trace("w", self.save_settings)
    
    def save_settings(self, *args):
        """Save the current settings to a preferences file"""
        for key, variable in self.settings.items():
            self.settings_model.set(key, variable.get())
        self.settings_model.save()
            
