class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.make} {self.model} has started.")
        else:
            print(f"The {self.make} {self.model} is already running.")
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.make} {self.model} is already stopped.")
    
    def honk(self):
        print(f"The {self.make} {self.model} is honking.")

    def print_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Running: {'Yes' if self.is_running else 'No'}")


my_car = Car("Toyota", "Camry", 2023, "Black")

my_car.print_info()

my_car.start()

my_car.print_info()

my_car.stop()

my_car.print_info()

my_car.honk()