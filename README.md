# Hotel Booking System

A simple, easy-to-use hotel room booking and management system built with Python.

## Features

- **Room Management**: Add and manage hotel rooms with different types and pricing
- **Booking System**: Book rooms for guests with check-in and check-out dates
- **Availability Tracking**: View available rooms in real-time
- **Booking Management**: View all bookings and cancel bookings as needed
- **Cost Calculation**: Automatic calculation of total booking cost based on number of nights
- **Command-Line Interface**: User-friendly CLI for all operations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ALVINLIN0508/rakkaranta.git
cd rakkaranta
```

2. No external dependencies required - uses Python standard library only!

## Usage

### Running the Application

Run the main application:
```bash
python main.py
```

### Main Menu Options

1. **Add a room**: Add a new room to the hotel inventory
2. **View available rooms**: See all rooms currently available for booking
3. **Book a room**: Create a new booking for a guest
4. **View all bookings**: Display all current bookings
5. **Cancel a booking**: Cancel an existing booking
6. **Exit**: Close the application

### Example Usage

```
Welcome to Grand Hotel!
Sample rooms have been added for demonstration.

==================================================
Hotel Booking System
==================================================
1. Add a room
2. View available rooms
3. Book a room
4. View all bookings
5. Cancel a booking
6. Exit
==================================================
Enter your choice (1-6): 2

--- Available Rooms ---
Room 101 (Single) - $100.0/night - Available
Room 102 (Double) - $150.0/night - Available
Room 201 (Suite) - $300.0/night - Available
```

## Core Components

### Room Class
Represents a hotel room with:
- Room number (unique identifier)
- Room type (e.g., Single, Double, Suite)
- Price per night
- Availability status

### Booking Class
Represents a guest booking with:
- Booking ID (unique identifier)
- Guest name
- Room reference
- Check-in and check-out dates
- Total cost (automatically calculated)

### Hotel Class
Manages the hotel operations:
- Add rooms to inventory
- Find rooms by room number
- Get available rooms
- Create bookings
- Cancel bookings
- View all bookings

## Running Tests

Run the comprehensive test suite:
```bash
python -m unittest test_hotel_booking.py
```

Or run with verbose output:
```bash
python -m unittest test_hotel_booking.py -v
```

## Project Structure

```
rakkaranta/
├── hotel_booking.py       # Core classes (Room, Booking, Hotel)
├── main.py               # CLI application
├── test_hotel_booking.py # Unit tests
└── README.md            # This file
```

## Requirements

- Python 3.6 or higher

## License

MIT License

## Author

ALVINLIN0508