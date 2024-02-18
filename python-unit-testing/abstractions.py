import json
import os


class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def reserve_room(self, customer):
        if self.rooms > 0:
            self.rooms -= 1
            self.reservations.append(customer.name)
            return True
        else:
            return False

    def cancel_reservation(self, customer):
        if customer.name in self.reservations:
            self.rooms += 1
            self.reservations.remove(customer.name)
            return True
        else:
            return False

    def update_reservation(self, old_name, new_name):
        if old_name in self.reservations:
            self.reservations.remove(old_name)
            self.reservations.append(new_name)
            return True
        else:
            return False

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        hotel = cls(data['name'], data['rooms'])
        hotel.reservations = data['reservations']
        return hotel


class Customer:
    def __init__(self, name):
        self.name = name

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['name'])


def save_to_file(obj, filename):
    with open(filename, 'w') as file:
        file.write(obj.to_json())


def load_from_file(cls, filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return cls.from_json(file.read())
    else:
        return None


def create_hotel(name, rooms):
    hotel = Hotel(name, rooms)
    save_to_file(hotel, f'{name}.hotel')


def delete_hotel(name):
    if os.path.exists(f'{name}.hotel'):
        os.remove(f'{name}.hotel')


def display_hotel(name):
    hotel = load_from_file(Hotel, f'{name}.hotel')
    if hotel:
        print(f'Hotel Name: {hotel.name}')
        print(f'Available Rooms: {hotel.rooms}')
        print('Reservations:')
        for customer in hotel.reservations:
            print(f' - {customer}')


def modify_hotel(name, new_rooms):
    hotel = load_from_file(Hotel, f'{name}.hotel')
    if hotel and new_rooms is not None:
        # Calculate the difference between the old and new total
        # number of rooms
        room_difference = new_rooms - (hotel.rooms + len(hotel.reservations))
        # Adjust the number of available rooms based on the difference
        hotel.rooms += room_difference
        # Ensure that the number of available rooms does not become negative
        hotel.rooms = max(hotel.rooms, 0)
        save_to_file(hotel, f'{name}.hotel')


def create_customer(name):
    customer = Customer(name)
    save_to_file(customer, f'{name}.customer')


def delete_customer(name):
    if os.path.exists(f'{name}.customer'):
        os.remove(f'{name}.customer')


def display_customer(name):
    customer = load_from_file(Customer, f'{name}.customer')
    if customer:
        print(f'Customer Name: {customer.name}')


def modify_customer(old_name, new_name):
    customer = load_from_file(Customer, f'{old_name}.customer')
    if customer:
        customer.name = new_name
        save_to_file(customer, f'{new_name}.customer')
        if old_name != new_name:
            os.remove(f'{old_name}.customer')
            # Update customer name in all hotels
            for hotel_file in os.listdir():
                if hotel_file.endswith('.hotel'):
                    hotel = load_from_file(Hotel, hotel_file)
                    if hotel.update_reservation(old_name, new_name):
                        save_to_file(hotel, hotel_file)


def create_reservation(customer_name, hotel_name):
    customer = load_from_file(Customer, f'{customer_name}.customer')
    hotel = load_from_file(Hotel, f'{hotel_name}.hotel')
    if customer and hotel:
        if hotel.reserve_room(customer):
            save_to_file(hotel, f'{hotel_name}.hotel')


def cancel_reservation(customer_name, hotel_name):
    customer = load_from_file(Customer, f'{customer_name}.customer')
    hotel = load_from_file(Hotel, f'{hotel_name}.hotel')
    if customer and hotel:
        if hotel.cancel_reservation(customer):
            save_to_file(hotel, f'{hotel_name}.hotel')
