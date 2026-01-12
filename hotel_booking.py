"""
Hotel Booking System
A simple hotel room booking and management system.
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Room:
    """Represents a hotel room."""
    
    def __init__(self, room_number: str, room_type: str, price: float):
        """
        Initialize a room.
        
        Args:
            room_number: Unique identifier for the room
            room_type: Type of room (e.g., 'Single', 'Double', 'Suite')
            price: Price per night
        """
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True
    
    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room {self.room_number} ({self.room_type}) - ${self.price}/night - {status}"


class Booking:
    """Represents a hotel booking."""
    
    def __init__(self, booking_id: int, guest_name: str, room: Room, 
                 check_in: datetime, check_out: datetime):
        """
        Initialize a booking.
        
        Args:
            booking_id: Unique identifier for the booking
            guest_name: Name of the guest
            room: Room object being booked
            check_in: Check-in date
            check_out: Check-out date
        """
        self.booking_id = booking_id
        self.guest_name = guest_name
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.total_cost = self._calculate_cost()
    
    def _calculate_cost(self) -> float:
        """Calculate total cost of the booking."""
        nights = (self.check_out - self.check_in).days
        return nights * self.room.price
    
    def __str__(self):
        return (f"Booking #{self.booking_id}: {self.guest_name} - "
                f"Room {self.room.room_number} - "
                f"{self.check_in.strftime('%Y-%m-%d')} to {self.check_out.strftime('%Y-%m-%d')} - "
                f"${self.total_cost:.2f}")


class Hotel:
    """Manages hotel rooms and bookings."""
    
    def __init__(self, name: str):
        """
        Initialize a hotel.
        
        Args:
            name: Name of the hotel
        """
        self.name = name
        self.rooms: List[Room] = []
        self.bookings: List[Booking] = []
        self.next_booking_id = 1
    
    def add_room(self, room_number: str, room_type: str, price: float) -> Room:
        """
        Add a room to the hotel.
        
        Args:
            room_number: Unique identifier for the room
            room_type: Type of room
            price: Price per night
            
        Returns:
            The created Room object
            
        Raises:
            ValueError: If room_number is empty or price is not positive
        """
        if not room_number or not room_number.strip():
            raise ValueError("Room number cannot be empty")
        if price <= 0:
            raise ValueError("Price must be positive")
        
        room = Room(room_number, room_type, price)
        self.rooms.append(room)
        return room
    
    def get_available_rooms(self) -> List[Room]:
        """
        Get list of available rooms.
        
        Returns:
            List of available Room objects
        """
        return [room for room in self.rooms if room.is_available]
    
    def find_room(self, room_number: str) -> Optional[Room]:
        """
        Find a room by room number.
        
        Args:
            room_number: Room number to search for
            
        Returns:
            Room object if found, None otherwise
        """
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None
    
    def book_room(self, guest_name: str, room_number: str, 
                  check_in: datetime, check_out: datetime) -> Optional[Booking]:
        """
        Book a room for a guest.
        
        Args:
            guest_name: Name of the guest
            room_number: Room number to book
            check_in: Check-in date
            check_out: Check-out date
            
        Returns:
            Booking object if successful, None otherwise
        """
        if not guest_name or not guest_name.strip():
            print("Error: Guest name cannot be empty.")
            return None
        
        room = self.find_room(room_number)
        
        if not room:
            print(f"Error: Room {room_number} not found.")
            return None
        
        if not room.is_available:
            print(f"Error: Room {room_number} is not available.")
            return None
        
        if check_in >= check_out:
            print("Error: Check-out date must be after check-in date.")
            return None
        
        booking = Booking(self.next_booking_id, guest_name, room, check_in, check_out)
        self.bookings.append(booking)
        room.is_available = False
        self.next_booking_id += 1
        
        return booking
    
    def cancel_booking(self, booking_id: int) -> bool:
        """
        Cancel a booking.
        
        Args:
            booking_id: ID of the booking to cancel
            
        Returns:
            True if successful, False otherwise
        """
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                booking.room.is_available = True
                self.bookings.remove(booking)
                return True
        
        print(f"Error: Booking #{booking_id} not found.")
        return False
    
    def get_all_bookings(self) -> List[Booking]:
        """
        Get all bookings.
        
        Returns:
            List of all Booking objects
        """
        return self.bookings
