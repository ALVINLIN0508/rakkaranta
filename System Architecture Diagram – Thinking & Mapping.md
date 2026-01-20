# 3-tier architecture
[ Client / Frontend ]
        ↓
[ Backend / Application Layer ]
        ↓
[ Database ]

## Frontend (Web App)
├─ Public Pages
│   ├─ Cabin overview
│   ├─ Services overview
│   └─ Availability calendar
│
├─ Guest Intranet (PIN Login)
│   ├─ My cabin info
│   ├─ Book services
│   ├─ My reservations
│   └─ Notifications
│
└─ Admin Dashboard
    ├─ Occupancy view
    ├─ Service schedules
    └─ Usage summary

## Backend API
│
├─ Auth / Access Module
│   ├─ Generate PIN
│   ├─ Validate PIN
│   └─ Expire PIN after checkout
│
├─ Cabin Booking Module
│   ├─ Check availability
│   ├─ Create cabin booking
│   └─ Link booking → cabin
│
├─ Service Booking Module
│   ├─ Sauna scheduling
│   ├─ EV charger booking
│   ├─ Laundry / Gym / Boat
│   └─ Prevent double booking
│
├─ Notification Module
│   ├─ Booking confirmation
│   ├─ Reminders (optional)
│   └─ Admin alerts
│
├─ Admin Module
│   ├─ Occupancy overview
│   ├─ Daily schedules
│   └─ Usage statistics
│
└─ Audit & Security Module
    ├─ Booking logs
    ├─ Role-based access
    └─ Timestamp tracking

## Database
│
├─ Cabins
│   └─ cabin_id, capacity, amenities
│
├─ CabinBookings
│   └─ booking_id, cabin_id, dates, PIN
│
├─ Services
│   └─ service_id, type (sauna, EV, gym)
│
├─ ServiceSlots
│   └─ service_id, time_slot, availability
│
├─ ServiceReservations
│   └─ reservation_id, cabin_id, slot_id
│
├─ PIN_Access
│   └─ PIN, valid_from, valid_to, cabin_id
│
└─ Logs
    └─ action, user_role, timestamp

