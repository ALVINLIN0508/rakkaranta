#!/usr/bin/env python3
"""
Hotel Booking System - Main Application
Command-line interface for managing hotel bookings.
"""

from datetime import datetime
from hotel_booking import Hotel


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("Hotel Booking System")
    print("=" * 50)
    print("1. Add a room")
    print("2. View available rooms")
    print("3. Book a room")
    print("4. View all bookings")
    print("5. Cancel a booking")
    print("6. Exit")
    print("=" * 50)


def add_room(hotel: Hotel):
    """Add a new room to the hotel."""
    print("\n--- Add a Room ---")
    room_number = input("Enter room number: ").strip()
    
    if hotel.find_room(room_number):
        print(f"Error: Room {room_number} already exists.")
        return
    
    room_type = input("Enter room type (e.g., Single, Double, Suite): ").strip()
    
    try:
        price = float(input("Enter price per night: $"))
        if price <= 0:
            print("Error: Price must be positive.")
            return
    except ValueError:
        print("Error: Invalid price.")
        return
    
    try:
        room = hotel.add_room(room_number, room_type, price)
        print(f"Successfully added: {room}")
    except ValueError as e:
        print(f"Error: {e}")


def view_available_rooms(hotel: Hotel):
    """Display all available rooms."""
    print("\n--- Available Rooms ---")
    available_rooms = hotel.get_available_rooms()
    
    if not available_rooms:
        print("No rooms available.")
    else:
        for room in available_rooms:
            print(room)


def book_room(hotel: Hotel):
    """Book a room for a guest."""
    print("\n--- Book a Room ---")
    
    # Show available rooms first
    available_rooms = hotel.get_available_rooms()
    if not available_rooms:
        print("No rooms available for booking.")
        return
    
    print("Available rooms:")
    for room in available_rooms:
        print(f"  {room}")
    
    room_number = input("\nEnter room number to book: ").strip()
    guest_name = input("Enter guest name: ").strip()
    
    if not guest_name:
        print("Error: Guest name cannot be empty.")
        return
    
    try:
        check_in_str = input("Enter check-in date (YYYY-MM-DD): ").strip()
        check_in = datetime.strptime(check_in_str, "%Y-%m-%d")
        
        check_out_str = input("Enter check-out date (YYYY-MM-DD): ").strip()
        check_out = datetime.strptime(check_out_str, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return
    
    booking = hotel.book_room(guest_name, room_number, check_in, check_out)
    if booking:
        print(f"Successfully created: {booking}")
    else:
        print("Booking failed. Please check the error message above.")


def view_all_bookings(hotel: Hotel):
    """Display all bookings."""
    print("\n--- All Bookings ---")
    bookings = hotel.get_all_bookings()
    
    if not bookings:
        print("No bookings found.")
    else:
        for booking in bookings:
            print(booking)


def cancel_booking(hotel: Hotel):
    """Cancel a booking."""
    print("\n--- Cancel a Booking ---")
    
    bookings = hotel.get_all_bookings()
    if not bookings:
        print("No bookings to cancel.")
        return
    
    print("Current bookings:")
    for booking in bookings:
        print(f"  {booking}")
    
    try:
        booking_id = int(input("\nEnter booking ID to cancel: "))
        if hotel.cancel_booking(booking_id):
            print(f"Successfully cancelled booking #{booking_id}.")
        else:
            print("Cancellation failed. Please check the error message above.")
    except ValueError:
        print("Error: Invalid booking ID.")


def main():
    """Main application loop."""
    hotel = Hotel("Grand Hotel")
    
    # Add some sample rooms for demonstration
    hotel.add_room("101", "Single", 100.0)
    hotel.add_room("102", "Double", 150.0)
    hotel.add_room("201", "Suite", 300.0)
    
    print(f"Welcome to {hotel.name}!")
    print("Sample rooms have been added for demonstration.")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_room(hotel)
        elif choice == "2":
            view_available_rooms(hotel)
        elif choice == "3":
            book_room(hotel)
        elif choice == "4":
            view_all_bookings(hotel)
        elif choice == "5":
            cancel_booking(hotel)
        elif choice == "6":
            print("\nThank you for using the Hotel Booking System!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
