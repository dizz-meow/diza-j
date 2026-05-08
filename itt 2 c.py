import datetime
rooms = {}  # {room_id: {'type': str, 'capacity': int, 'price': float, 'available': bool}}
customers = {}  # {customer_id: {'name': str, 'email': str}}
bookings = {}  # {booking_id: {'customer_id': int, 'room_id': int, 'total': float}}
class RoomNotAvailableError(Exception): pass
class InvalidCustomerError(Exception): pass
class PaymentError(Exception): pass

def log_error(error_msg):
    """Logs errors to hotel_errors.txt with timestamps."""
    with open("hotel_errors.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] ERROR: {error_msg}\n")

def add_room(room_id, room_type, capacity, price):
    rooms[room_id] = {'type': room_type, 'capacity': capacity, 'price': price, 'available': True}

def register_customer(customer_id, name, email):
    customers[customer_id] = {'name': name, 'email': email}

def check_availability(room_id):
    if room_id not in rooms:
        return False
    return rooms[room_id]['available']

def book_room(booking_id, customer_id, room_id, occupants, payment_success=True):
    try:
        if customer_id not in customers:
            raise InvalidCustomerError(f"Customer ID {customer_id} not found.")
        
        if room_id not in rooms:
            raise ValueError(f"Room ID {room_id} does not exist.")
            
        if occupants > rooms[room_id]['capacity']:
            raise OverflowError(f"Occupants ({occupants}) exceed capacity ({rooms[room_id]['capacity']}).")

        if not rooms[room_id]['available']:
            raise RoomNotAvailableError(f"Room {room_id} is already booked.")

        if not payment_success:
            raise PaymentError("Payment failed during transaction.")

    except (InvalidCustomerError, ValueError, OverflowError, RoomNotAvailableError, PaymentError) as e:
        log_error(str(e))
        print(f"Booking Failed: {e}")
        raise
    else:
        rooms[room_id]['available'] = False
        bookings[booking_id] = {
            'customer_id': customer_id,
            'room_id': room_id,
            'total': rooms[room_id]['price']
        }
        print(f"Booking {booking_id} successful for Room {room_id}!")
    finally:
        print(f"Attempt for booking {booking_id} finished.")

def cancel_booking(booking_id):
    try:
        if booking_id not in bookings:
            raise FileNotFoundError(f"Booking record {booking_id} not found.")
        
        room_id = bookings[booking_id]['room_id']
        rooms[room_id]['available'] = True
        del bookings[booking_id]
        print(f"Booking {booking_id} cancelled successfully.")
    except FileNotFoundError as e:
        log_error(str(e))
        print(f"Cancellation Error: {e}")

def generate_bill(booking_id):
    if booking_id in bookings:
        b = bookings[booking_id]
        c = customers[b['customer_id']]
        print(f"\n--- BILL ---\nCustomer: {c['name']}\nRoom ID: {b['room_id']}\nTotal: ${b['total']}\n------------")
    else:
        print("No bill found for this ID.")
print("--- Initializing Hotel ---")
add_room(101, "Deluxe", 2, 150.0)
add_room(102, "Suite", 4, 300.0)
register_customer(1, "Alice", "alice@example.com")

print("\n1. Successful Booking Case:")
try:
    book_room("B001", 1, 101, 2)
    generate_bill("B001")
except: pass

print("\n2. Room Unavailability Case:")
try:
    book_room("B002", 1, 101, 1) # Room 101 is already taken
except: pass

print("\n3. Invalid Customer Case:")
try:
    book_room("B003", 99, 102, 1) # Customer 99 doesn't exist
except: pass

print("\n4. Capacity Overflow Case:")
try:
    book_room("B004", 1, 102, 10) # Max capacity of room 102 is 4
except: pass

print("\n5. Payment Failure Case:")
try:
    book_room("B005", 1, 102, 2, payment_success=False)
except: pass

print("\n6. Missing Record (FileNotFoundError simulation):")
cancel_booking("B999")
