import tkinter as tk
from PIL import Image, ImageTk


def window1():
    # Hide the main window
    root.withdraw()
    
    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("BKF2")
    new_window.geometry("700x400")
    new_window['bg'] = 'white'
    

    # Add a label to the new window
    label1 = tk.Label(new_window, text="PLANE LOOKUP", font =(14))
    label1['bg'] = 'white'
    label1.place(x=260,y=10)

    label2 = tk.Label(new_window, text='BK Force')
    label2['bg'] = 'white'
    label2.place(x=310,y=40)

    label2 = tk.Label(new_window, text='Search your aircraft')
    label2.place(x=100,y=100)
    label2['bg'] = 'white'

    entry = tk.Entry(new_window, width = 30)
    entry.pack(side=tk.LEFT, padx=10)  # Padding bên trái và bên phải của ô nhập liệu
    entry.place(x=230, y=100)
    entry['bg'] = '#DDDDDD'
    entry.focus()


    def search():
        #Data base
        class Airplane:
            def __init__(self, make, model, year, capacity, weight, distance):
                self.make = make
                self.model = model
                self.year = year
                self.capacity = capacity
                self.weight = weight
                self.distance = distance
               

            def display_info(self):
                save_text = f"Brand:{self.make:>{20}}\nModel:{self.model:>{20}}\nYear:{self.year:>{21}}\nCapacity:{self.capacity:>{17}}\nMaxLoad:{self.weight:>{18}}\nMaxRange:{self.distance:>{17}}"
                return save_text
        
            def update_info(self, make=None, model=None, year=None, capacity=None, weight=None,distance=None):
                if make:
                    self.make = make
                if model:
                    self.model = model
                if year:
                    self.year = year
                if capacity:
                    self.capacity = capacity
                if weight:
                    self.weight = weight
                if distance:
                    self.distance = distance



        class Fleet:
            def __init__(self):
                self.airplanes = []

            def add_airplane(self, airplane):
                self.airplanes.append(airplane)

            def remove_airplane(self, airplane):
                self.airplanes.remove(airplane)

            def display_fleet(self):
                for airplane in self.airplanes:
                    airplane.display_info()

            def find_airplane(self, make=None, model=None):
                for airplane in self.airplanes:
                    if (make and airplane.make == make) or (model and airplane.model == model):
                        return airplane
                return None

        #plane stored:
        if __name__ == "__main__":
            fleet = Fleet() 
            # Create some airplane instances
            #BOEING family
            b707 = Airplane("Boeing", "B707", 1958, '140-189','~151,000kg','~8,160km')
            fleet.add_airplane(b707)

            b717 = Airplane("Boeing", "B717", 1999, '106-117','~54,884kg','~3,820km')
            fleet.add_airplane(b717)

            b727 = Airplane("Boeing", "B727", 1964, '140-189','95,300kg','~4,720km')
            fleet.add_airplane(b727)

            b737 = Airplane("Boeing", "B737", 1968, '85-215','~78,000kg','~6,300km')
            fleet.add_airplane(b737)

            b747 = Airplane("Boeing", "B747", 1970, '366-524','~420,000kg','~14,000km')
            fleet.add_airplane(b747)

            b757 = Airplane("Boeing", "B757", 1983, '200-289','~120,000kg','~7,000km')
            fleet.add_airplane(b757)

            b767 = Airplane("Boeing", "B767", 1982, '181-375','~190,000kg','~10,500km')
            fleet.add_airplane(b767)

            b777 = Airplane("Boeing", "B777", 1995, '314-396','~350,000kg','~14,000km')
            fleet.add_airplane(b777)

            b787 = Airplane("Boeing", "B787", 2011, '242-330','~250,000kg','~13,000km')
            fleet.add_airplane(b787)

            #AIRBUS family
            a300 = Airplane("Airbus", "A300", 1974, '228-345','~165,000kg','~7,500km')
            fleet.add_airplane(a300)

            a310 = Airplane("Airbus", "A310", 1983, '190-280','~100,000kg','~7,000km')
            fleet.add_airplane(a310)

            a320 = Airplane("Airbus", "A320", 1988, '124-244','~80,000kg','~7,000km')
            fleet.add_airplane(a320)

            a330 = Airplane("Airbus", "A330", 1993, '247-440','~250,000kg','~13,000km')
            fleet.add_airplane(a330)

            a340 = Airplane("Airbus", "A340", 1993, '261-380','~350,000kg','~15,000km')
            fleet.add_airplane(a340)

            a350 = Airplane("Airbus", "A350", 2015, '300-440','~300,000kg','~15,500km')
            fleet.add_airplane(a350)

            a380 = Airplane("Airbus", "A380", 2007, '555-853','~560,000kg','~15,000km')
            fleet.add_airplane(a380)

            a220 = Airplane("Airbus", "A220", 2016, '100-160','~68,000kg','~6,300km')
            fleet.add_airplane(a220)
        
            #AIRBUS detail
            a220_100 = Airplane("Airbus", "A200-100", 2016, '108-133','~63,100kg','~6,390km')
            fleet.add_airplane(a220_100)
            
            a220_300 = Airplane("Airbus", "A200-300", 2016, '130-160','~70,900kg','~6,297km')
            fleet.add_airplane(a220_300)

            a300_600 = Airplane("Airbus", "A300-600", 1974, '210-250','~165,000kg','~7500km')
            fleet.add_airplane(a300_600)

            a310_300 = Airplane("Airbus", "A310-300", 1983, '280','~164,000kg','~9,600km')
            fleet.add_airplane(a310_300)

            a318 = Airplane("Airbus", "A318", 2003, '107-132','~68,000kg','~5,700km')
            fleet.add_airplane(a318)
            
            a319 = Airplane("Airbus", "A319", 1996, '124-156','~75,000kg','~6,945km')
            fleet.add_airplane(a319)
            
            a320neo = Airplane("Airbus", "A320-NEO", 1988, '150-186','~78,000kg','~6,480km')
            fleet.add_airplane(a320neo)    
            
            a321 = Airplane("Airbus", "A321", 1994, '185-236','~97,000kg','~7,400km')
            fleet.add_airplane(a321)

            a330_200 = Airplane("Airbus", "A330-200", 1998, '210-406','~242,000kg','~13,450km')
            fleet.add_airplane(a330_200)

            a330_300 = Airplane("Airbus", "A330-300", 1993, '250-440','~242,000kg','~11,750km')
            fleet.add_airplane(a330_300)

            a330_800 = Airplane("Airbus", "A330-800", 2020, '220-406','~251,000kg','~15,094km')
            fleet.add_airplane(a330_800)

            a330_900 = Airplane("Airbus", "A330-900", 2018, '260-460','~251,000kg','~13,334km')
            fleet.add_airplane(a330_900)

            a340_300 = Airplane("Airbus", "A340-300", 1993, '295-440','~276,000kg','~13,500km')
            fleet.add_airplane(a340_300)

            a340_500 = Airplane("Airbus", "A340-500", 2002, '316-375','~372,000kg','~16,670km')
            fleet.add_airplane(a340_500)

            a340_600 = Airplane("Airbus", "A340-600", 2002, '326-475','~380,000kg','~14,450km')
            fleet.add_airplane(a340_600)

            a350_900 = Airplane("Airbus", "A350-900", 2013, '300-350','~280,000kg','~15,000km')
            fleet.add_airplane(a350_900)

            a350_1000 = Airplane("Airbus", "A350-1000", 2018, '350-410','~319,000kg','~16,100km')
            fleet.add_airplane(a350_1000)

            a380_800 = Airplane("Airbus", "A380-800", 2007, '555-853','~560,000kg','~15,200km')
            fleet.add_airplane(a380_800)


        searching = entry.get()
        found_plane1 = fleet.find_airplane(model= searching.upper())
        if found_plane1:
            labelrs = tk.Label(new_window, text = (str(found_plane1.display_info())), width = 25, height = 8)
            labelrs.place(x=230, y = 130)
       
        else:
            labelrs = tk.Label(new_window, text = 'Does not have information', )
            labelrs.place(x=230,y=150)
      

    search_button = tk.Button(new_window, text="Search", command = search, width = 20)
    search_button.place(x=420, y =95)
    
    # Add a button to go back to the main window
    back_button = tk.Button(new_window, text="Back", command=lambda: go_back(new_window),width=10)
    back_button.pack(pady=20)
    back_button.place(x =310, y = 350)


def go_back(new_window):
    # Destroy the new window
    new_window.destroy()
    
    # Show the main window again
    root.deiconify()


# Create the main window
root = tk.Tk()
root.title("BKF1")

# Set the size of the window
width, height = 700, 400
root.geometry(f"{width}x{height}")
root.attributes('-topmost', False)

# Load the image using PIL
image = Image.open('C:/Users/Admin/Documents/Python code/airforce.jpg')  # Replace with your image file
background_image = ImageTk.PhotoImage(image.resize((width, height)))

# Create a canvas widget
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack(fill=tk.BOTH, expand=True)

# Add the image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)



# Nút
button = tk.Button(root, text="START", font =('Impact',20), width = 8, command= window1)
button.pack(side=tk.LEFT, padx=10)  # Padding bên trái và bên phải của nút
button.place(x=520, y=300)

# Run the main loop
root.mainloop()

