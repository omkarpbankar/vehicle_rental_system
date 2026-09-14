class Vehicle:
    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    @staticmethod
    def is_valid_duration(days):
        """Validates whether the rental duration is valid (greater than zero)."""
        return isinstance(days, int) and days > 0

    def calculate_rent(self, days):
        """Calculates total rent for the given number of days."""
        if not self.is_valid_duration(days):
            raise ValueError("Rental duration must be a positive integer greater than zero.")
        return self.rental_price_per_day * days

    def __str__(self):
        return f"{self.brand} {self.model} ({self.vehicle_number})"

class Car(Vehicle):
    def __init__(self, vehicle_number, brand, model, rental_price_per_day, number_of_seats):
        super().__init__(vehicle_number, brand, model, rental_price_per_day)
        self.number_of_seats = number_of_seats

    def __str__(self):
        return super().__str__() + f" - {self.number_of_seats} Seater Car"

class Bike(Vehicle):
    def __init__(self, vehicle_number, brand, model, rental_price_per_day, engine_capacity):
        super().__init__(vehicle_number, brand, model, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def __str__(self):
        return super().__str__() + f" - {self.engine_capacity}cc Bike"


if __name__ == "__main__":
    print("--- Vehicle Rental System Demonstration ---\n")
    
    # Create 2 cars
    car1 = Car("CAR-1001", "Toyota", "Camry", 45.0, 5)
    car2 = Car("CAR-2002", "Honda", "Odyssey", 70.0, 7)

    # Create 2 bikes
    bike1 = Bike("BIKE-1001", "Yamaha", "MT-07", 30.0, 689)
    bike2 = Bike("BIKE-2002", "Kawasaki", "Ninja 400", 25.0, 399)

    vehicles = [car1, car2, bike1, bike2]
    
    # Test valid rental duration
    rental_days = 4
    print(f"Calculating rent for {rental_days} days:")
    for v in vehicles:
        try:
            total_rent = v.calculate_rent(rental_days)
            print(f"{v} | Rent: ${total_rent:.2f}")
        except ValueError as e:
            print(f"Error for {v}: {e}")
            
    print("\n" + "-"*40 + "\n")
    
    # Test invalid rental duration
    invalid_days = 0
    print(f"Attempting to calculate rent for {invalid_days} days on {car1}:")
    try:
        car1.calculate_rent(invalid_days)
    except ValueError as e:
        print(f"Validation Error caught: {e}")
