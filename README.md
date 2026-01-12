# SYSTEM ARCHITECTURE

[User Browser]
     |
     v
[React Frontend]  (static files)
     |
     v  HTTPS (REST API)
[Node.js Backend API]
     |
     +--> [PostgreSQL Database]
     |
     +--> [Redis Cache] (optional but nice)
     |
     +--> [Email/SMS Service] (optional)


## React Frontend
Pages: Home/Search, Hotel Detail, Room Select, Booking Form, Login/Profile
Calls backend APIs to:
search hotels
show hotel/room details
create booking
view user bookings

## Node.js Backend (single service is enough)
One backend app with simple modules:

Auth: login/register, JWT
Hotels: hotels + rooms data
Search: search hotels (can be just SQL queries)
Bookings: create/cancel bookings, prevent double booking

## PostgreSQL (main database)
Stores:
users
hotels
rooms
bookings
Redis (optional)
Cache hotel search results (faster)
Store short “booking holds” (temporary reservation for a few minutes)

## Email/SMS (optional)
Send booking confirmation email

## Simple booking flow (important part)
User searches hotels (React → Backend → DB)
User chooses hotel + dates + room
React sends booking request:
POST /bookings
Backend checks availability in DB:
If available: create booking
If not: return “room not available”
Backend returns booking confirmation
(Optional) backend sends confirmation email

## Minimal database tables
users(id, name, email, password_hash)
hotels(id, name, city, address, description)
rooms(id, hotel_id, room_type, price_per_night, total_rooms)
bookings(id, user_id, hotel_id, room_id, check_in, check_out, status)
Status can be: CONFIRMED or CANCELLED.
## API endpoints
POST /auth/register
POST /auth/login
GET /hotels?city=... (search list)
GET /hotels/:id (details + rooms)
POST /bookings (create booking)
GET /bookings/me (my bookings)
POST /bookings/:id/cancel

