# Vehicle Rental System

A simple Python-based mini vehicle rental application that demonstrates Object-Oriented Programming (OOP) concepts such as inheritance, static methods, and basic validation.

## Features

- **Base `Vehicle` Class:** Defines core attributes like `vehicle_number`, `brand`, `model`, and `rental_price_per_day`.
- **Subclasses:** 
  - `Car`: Inherits from `Vehicle` and adds a `number_of_seats` attribute.
  - `Bike`: Inherits from `Vehicle` and adds an `engine_capacity` (cc) attribute.
- **Rent Calculation:** Includes a method (`calculate_rent`) to compute the total rent based on the requested number of days.
- **Input Validation:** Uses a static method (`is_valid_duration`) to ensure that the rental duration is a positive integer greater than zero.

## How to Run

1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the project.
4. Execute the script:
   ```bash
   python vehicle_rental.py
   ```

## Demonstration

The `vehicle_rental.py` script includes a built-in demonstration block that runs when you execute the file directly. It:
1. Creates instances of `Car` and `Bike`.
2. Calculates and prints the total rent for a given valid duration (e.g., 4 days).
3. Demonstrates the error handling by attempting to calculate rent for an invalid duration (e.g., 0 days) and catching the `ValueError`.