#!/usr/bin/env python3
"""
Example demonstration of the Hotel Booking System.
This script shows a complete workflow without requiring user interaction.
"""

from hotel_booking import Hotel
from datetime import datetime, timedelta


def main():
    print("=" * 60)
    print("Hotel Booking System - Example Demonstration")
    print("=" * 60)
    
    # Create a hotel
    hotel = Hotel("Grand Plaza Hotel")
    print(f"\n✓ Created hotel: {hotel.name}")
    
    # Add rooms
    print("\n--- Adding Rooms ---")
    hotel.add_room("101", "Single", 100.0)
    hotel.add_room("102", "Double", 150.0)
    hotel.add_room("103", "Double", 150.0)
    hotel.add_room("201", "Suite", 300.0)
    hotel.add_room("202", "Suite", 300.0)
    print(f"✓ Added {len(hotel.rooms)} rooms")
    
    # Display available rooms
    print("\n--- Available Rooms ---")
    for room in hotel.get_available_rooms():
        print(f"  {room}")
    
    # Make some bookings
    print("\n--- Creating Bookings ---")
    today = datetime.now()
    
    booking1 = hotel.book_room(
        "Alice Johnson",
        "101",
        today + timedelta(days=1),
        today + timedelta(days=3)
    )
    print(f"  {booking1}")
    
    booking2 = hotel.book_room(
        "Bob Smith",
        "201",
        today + timedelta(days=2),
        today + timedelta(days=5)
    )
    print(f"  {booking2}")
    
    booking3 = hotel.book_room(
        "Carol White",
        "102",
        today + timedelta(days=1),
        today + timedelta(days=2)
    )
    print(f"  {booking3}")
    
    # Display available rooms after bookings
    print("\n--- Available Rooms After Bookings ---")
    available_rooms = hotel.get_available_rooms()
    print(f"  {len(available_rooms)} room(s) available:")
    for room in available_rooms:
        print(f"    {room}")
    
    # Display all bookings
    print("\n--- All Current Bookings ---")
    for booking in hotel.get_all_bookings():
        print(f"  {booking}")
    
    # Calculate total revenue
    total_revenue = sum(b.total_cost for b in hotel.get_all_bookings())
    print(f"\n--- Statistics ---")
    print(f"  Total rooms: {len(hotel.rooms)}")
    print(f"  Occupied rooms: {len(hotel.rooms) - len(available_rooms)}")
    print(f"  Total bookings: {len(hotel.get_all_bookings())}")
    print(f"  Total revenue: ${total_revenue:.2f}")
    
    # Cancel a booking
    print("\n--- Cancelling Booking ---")
    if booking2:
        print(f"  Cancelling: {booking2}")
        hotel.cancel_booking(booking2.booking_id)
        print("  ✓ Booking cancelled")
    
    # Show updated availability
    print("\n--- Available Rooms After Cancellation ---")
    available_rooms = hotel.get_available_rooms()
    print(f"  {len(available_rooms)} room(s) available:")
    for room in available_rooms:
        print(f"    {room}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
