"""
Unit tests for the Hotel Booking System.
"""

import unittest
from datetime import datetime, timedelta
from hotel_booking import Room, Booking, Hotel


class TestRoom(unittest.TestCase):
    """Test cases for the Room class."""
    
    def test_room_creation(self):
        """Test creating a room."""
        room = Room("101", "Single", 100.0)
        self.assertEqual(room.room_number, "101")
        self.assertEqual(room.room_type, "Single")
        self.assertEqual(room.price, 100.0)
        self.assertTrue(room.is_available)
    
    def test_room_string_representation(self):
        """Test string representation of a room."""
        room = Room("102", "Double", 150.0)
        self.assertIn("102", str(room))
        self.assertIn("Double", str(room))
        self.assertIn("150", str(room))
        self.assertIn("Available", str(room))


class TestBooking(unittest.TestCase):
    """Test cases for the Booking class."""
    
    def test_booking_creation(self):
        """Test creating a booking."""
        room = Room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        booking = Booking(1, "John Doe", room, check_in, check_out)
        
        self.assertEqual(booking.booking_id, 1)
        self.assertEqual(booking.guest_name, "John Doe")
        self.assertEqual(booking.room, room)
        self.assertEqual(booking.check_in, check_in)
        self.assertEqual(booking.check_out, check_out)
    
    def test_booking_cost_calculation(self):
        """Test booking cost calculation."""
        room = Room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)  # 2 nights
        booking = Booking(1, "John Doe", room, check_in, check_out)
        
        self.assertEqual(booking.total_cost, 200.0)
    
    def test_booking_string_representation(self):
        """Test string representation of a booking."""
        room = Room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        booking = Booking(1, "John Doe", room, check_in, check_out)
        
        booking_str = str(booking)
        self.assertIn("1", booking_str)
        self.assertIn("John Doe", booking_str)
        self.assertIn("101", booking_str)
        self.assertIn("200.00", booking_str)


class TestHotel(unittest.TestCase):
    """Test cases for the Hotel class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.hotel = Hotel("Test Hotel")
    
    def test_hotel_creation(self):
        """Test creating a hotel."""
        self.assertEqual(self.hotel.name, "Test Hotel")
        self.assertEqual(len(self.hotel.rooms), 0)
        self.assertEqual(len(self.hotel.bookings), 0)
    
    def test_add_room(self):
        """Test adding a room to the hotel."""
        room = self.hotel.add_room("101", "Single", 100.0)
        
        self.assertEqual(len(self.hotel.rooms), 1)
        self.assertEqual(room.room_number, "101")
        self.assertEqual(room.room_type, "Single")
        self.assertEqual(room.price, 100.0)
    
    def test_find_room(self):
        """Test finding a room by room number."""
        self.hotel.add_room("101", "Single", 100.0)
        self.hotel.add_room("102", "Double", 150.0)
        
        room = self.hotel.find_room("101")
        self.assertIsNotNone(room)
        self.assertEqual(room.room_number, "101")
        
        room = self.hotel.find_room("999")
        self.assertIsNone(room)
    
    def test_get_available_rooms(self):
        """Test getting available rooms."""
        room1 = self.hotel.add_room("101", "Single", 100.0)
        room2 = self.hotel.add_room("102", "Double", 150.0)
        
        available = self.hotel.get_available_rooms()
        self.assertEqual(len(available), 2)
        
        room1.is_available = False
        available = self.hotel.get_available_rooms()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].room_number, "102")
    
    def test_book_room_success(self):
        """Test successfully booking a room."""
        self.hotel.add_room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        
        booking = self.hotel.book_room("John Doe", "101", check_in, check_out)
        
        self.assertIsNotNone(booking)
        self.assertEqual(booking.guest_name, "John Doe")
        self.assertEqual(booking.room.room_number, "101")
        self.assertEqual(len(self.hotel.bookings), 1)
        
        room = self.hotel.find_room("101")
        self.assertFalse(room.is_available)
    
    def test_book_room_not_found(self):
        """Test booking a non-existent room."""
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        
        booking = self.hotel.book_room("John Doe", "999", check_in, check_out)
        self.assertIsNone(booking)
    
    def test_book_room_not_available(self):
        """Test booking a room that's already booked."""
        self.hotel.add_room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        
        booking1 = self.hotel.book_room("John Doe", "101", check_in, check_out)
        self.assertIsNotNone(booking1)
        
        booking2 = self.hotel.book_room("Jane Smith", "101", check_in, check_out)
        self.assertIsNone(booking2)
    
    def test_book_room_invalid_dates(self):
        """Test booking with invalid dates."""
        self.hotel.add_room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 17)
        check_out = datetime(2026, 1, 15)
        
        booking = self.hotel.book_room("John Doe", "101", check_in, check_out)
        self.assertIsNone(booking)
    
    def test_cancel_booking_success(self):
        """Test successfully canceling a booking."""
        self.hotel.add_room("101", "Single", 100.0)
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        
        booking = self.hotel.book_room("John Doe", "101", check_in, check_out)
        self.assertIsNotNone(booking)
        
        result = self.hotel.cancel_booking(booking.booking_id)
        self.assertTrue(result)
        self.assertEqual(len(self.hotel.bookings), 0)
        
        room = self.hotel.find_room("101")
        self.assertTrue(room.is_available)
    
    def test_cancel_booking_not_found(self):
        """Test canceling a non-existent booking."""
        result = self.hotel.cancel_booking(999)
        self.assertFalse(result)
    
    def test_get_all_bookings(self):
        """Test getting all bookings."""
        self.hotel.add_room("101", "Single", 100.0)
        self.hotel.add_room("102", "Double", 150.0)
        
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        
        self.hotel.book_room("John Doe", "101", check_in, check_out)
        self.hotel.book_room("Jane Smith", "102", check_in, check_out)
        
        bookings = self.hotel.get_all_bookings()
        self.assertEqual(len(bookings), 2)
    
    def test_booking_id_increment(self):
        """Test that booking IDs increment correctly."""
        self.hotel.add_room("101", "Single", 100.0)
        self.hotel.add_room("102", "Double", 150.0)
        
        check_in = datetime(2026, 1, 15)
        check_out = datetime(2026, 1, 17)
        
        booking1 = self.hotel.book_room("John Doe", "101", check_in, check_out)
        booking2 = self.hotel.book_room("Jane Smith", "102", check_in, check_out)
        
        self.assertEqual(booking1.booking_id, 1)
        self.assertEqual(booking2.booking_id, 2)


if __name__ == "__main__":
    unittest.main()
