import tkinter as tk
import backend

class WeatherReport(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_entry_field()

        self.location_text = "No Report Loaded"
        self.create_report_frame()

    def create_entry_field(self):
        self.frm_entry = tk.Frame(self)
        self.ent_location = tk.Entry(self.frm_entry)
        self.btn_request = tk.Button(self.frm_entry, text="Get Report", command=self.make_request)
        self.frm_entry.pack()
        self.ent_location.pack(side=tk.LEFT)
        self.btn_request.pack(side=tk.RIGHT)

    def create_report_frame(self):
        
        self.frm_report = tk.Frame(self)
        
        self.frm_title = tk.Frame(self.frm_report)
        self.lbl_location = tk.Label(self.frm_title, text=self.location_text)
        
        self.frm_data = tk.Frame(self.frm_report)
        self.frm_timestamp = tk.Frame(self.frm_data)
        self.lbl_timestamp_title = tk.Label(self.frm_timestamp, text="Data Timestamp")
        self.lbl_timestamp_value = tk.Label(self.frm_timestamp, text="")
        self.frm_temp = tk.Frame(self.frm_data)
        self.lbl_temp_title = tk.Label(self.frm_temp, text="Temperature")
        self.lbl_temp_value = tk.Label(self.frm_temp, text="N/A")
        self.frm_class = tk.Frame(self.frm_data)
        self.lbl_class_title = tk.Label(self.frm_class, text="Weather")
        self.lbl_class_value = tk.Label(self.frm_class, text="")
        
        # pack items:
        self.frm_report.pack()
        self.frm_title.pack()
        self.lbl_location.pack()
        self.frm_data.pack()
        self.frm_timestamp.pack()
        self.lbl_timestamp_title.pack(side=tk.LEFT)
        self.lbl_timestamp_value.pack(side=tk.RIGHT)
        self.frm_temp.pack()
        self.lbl_temp_title.pack(side=tk.LEFT)
        self.lbl_temp_value.pack(side=tk.RIGHT)
        self.frm_class.pack()
        self.lbl_class_title.pack(side=tk.LEFT)
        self.lbl_class_value.pack(side=tk.RIGHT)

    def get_location_field(self):
        self.location_text = self.ent_location.get()
    
    def make_request(self):
        """
        Make API call to OpenWeather using backend.py
        """
        self.get_location_field()

        # Make request to API:
        caller = backend.Caller()
        response = caller.current_data(self.location_text)      # will need to implement a "not-found" answer
        report = backend.CurrentReport(response)

        # update data:
        self.lbl_location.config(text=self.location_text)
        timestamp = report.get_date() + " " + report.get_time()
        self.lbl_timestamp_value.config(text=timestamp)
        self.lbl_temp_value.config(text=report.get_temp())
        self.lbl_class_value.config(text=report.get_classification())


root=tk.Tk()
window = WeatherReport(root)
window.mainloop()