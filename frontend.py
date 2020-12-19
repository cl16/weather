import tkinter as tk
import backend

class WeatherReport(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_entry_field()
        
        self.location_text = "No Report Loaded"
        self.data_labels = []
        self.create_report_frame()

        self.weather_data = None

    def create_entry_field(self):
        self.frm_entry = tk.Frame(self)
        self.ent_location = tk.Entry(self.frm_entry)
        self.btn_request = tk.Button(self.frm_entry, text="Get Report", command=self.make_request)
        self.master.bind("<Return>", self.make_request)
        self.frm_entry.grid(row=0)
        self.ent_location.grid(row=0, column=0)
        self.btn_request.grid(row=0, column=1)

    def create_report_frame(self):
        
        self.frm_report = tk.Frame(self)
        self.frm_report.grid(row=1)

        fields = ["City", "Date", "Time", "Weather", "Temperature", "Feels Like"]
        for i in range(len(fields)):
            tk.Label(self.frm_report, relief=tk.RIDGE, width=20, text=fields[i]).grid(row=i, column=0)
            lbl_field_value = tk.Label(self.frm_report, relief=tk.RIDGE, width=20, text="")  # no text until request made & text updated
            lbl_field_value.grid(row=i, column=1)    
            self.data_labels.append(lbl_field_value)    # list for update with lbl.config() later


    def get_location_field(self):
        self.location_text = self.ent_location.get()
    
    def make_request(self, event):
        """
        Make API call to OpenWeather using backend.py

        :param event: placeholder so method can be used in self.master.bind("<Return>",)
        """
        self.get_location_field()

        # Make request to API:
        caller = backend.Caller()
        report = caller.report(self.location_text)
        if caller.response() != True:  # failure in API return
            # update data labels:
            idx = 0
            for lbl in self.data_labels:
                if idx==0:
                    self.data_labels[0].config(text="No Location Data...")
                else:
                    lbl.config(text="")
                idx += 1
            
            return None # end function (break)
    
        # update data:
        self.weather_data = report.simple_report()

        # update data labels:
        idx = 0
        for lbl in self.data_labels:
            lbl.config(text=list(self.weather_data.values())[idx])
            idx += 1

root = tk.Tk()
window = WeatherReport(root)
window.mainloop()