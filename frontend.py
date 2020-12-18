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
        self.master.bind("<Return>", self.make_request)
        self.frm_entry.grid(row=0)
        self.ent_location.grid(row=0, column=0)
        self.btn_request.grid(row=0, column=1)

    def create_report_frame(self):
        
        self.frm_report = tk.Frame(self)
        
        self.frm_title = tk.Frame(self.frm_report)
        self.lbl_location = tk.Label(self.frm_title, text=self.location_text)
        
        self.frm_data = tk.Frame(self.frm_report)

        self.lbl_source_city_title = tk.Label(self.frm_data, text="City")
        self.lbl_source_city_value = tk.Label(self.frm_data, text="")

        self.frm_timestamp = tk.Frame(self.frm_data)
        self.lbl_timestamp_title = tk.Label(self.frm_data, text="Data Timestamp", bg="white")
        self.lbl_timestamp_value = tk.Label(self.frm_data, text="")

        self.lbl_class_title = tk.Label(self.frm_data, text="Weather", bg="white")
        self.lbl_class_value = tk.Label(self.frm_data, text="")

        self.lbl_temp_title = tk.Label(self.frm_data, text="Temperature", bg="white")
        self.lbl_temp_value = tk.Label(self.frm_data, text="N/A")

        self.lbl_feels_title = tk.Label(self.frm_data, text="Feels Like")
        self.lbl_feels_value = tk.Label(self.frm_data, text="")
        
        # pack items:
        
        self.frm_report.grid(row=1)
        self.frm_title.grid(row=0)

        self.frm_data.grid(row=1)

        self.lbl_source_city_title.grid(row=0, column=0)
        self.lbl_source_city_value.grid(row=0, column=1)

        self.lbl_timestamp_title.grid(row=1, column=0)
        self.lbl_timestamp_value.grid(row=1, column=1)
        
        self.lbl_class_title.grid(row=2, column=0)
        self.lbl_class_value.grid(row=2, column=1)

        self.lbl_temp_title.grid(row=3, column=0)
        self.lbl_temp_value.grid(row=3, column=1)

        self.lbl_feels_title.grid(row=4, column=0)
        self.lbl_feels_value.grid(row=4, column=1)

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
        response = caller.current_data(self.location_text)      # will need to implement a "not-found" answer
        report = backend.CurrentReport(response)

        # update data:
        self.lbl_location.config(text=self.location_text)
        self.lbl_source_city_value.config(text=report.get_city())
        timestamp = report.get_date() + " " + report.get_time()
        self.lbl_timestamp_value.config(text=timestamp)
        self.lbl_temp_value.config(text=report.get_temp())
        self.lbl_class_value.config(text=report.get_classification())
        self.lbl_feels_value.config(text=report.get_feels())


root=tk.Tk()
root.geometry("500x500")
window = WeatherReport(root)
window.mainloop()