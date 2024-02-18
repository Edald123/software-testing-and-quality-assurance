import unittest
from unittest import mock
import os
import abstractions


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = abstractions.Hotel('Test Hotel', 10)
        self.customer = abstractions.Customer('Test Customer')

    def test_reserve_room(self):
        self.assertTrue(self.hotel.reserve_room(self.customer))
        self.assertEqual(self.hotel.rooms, 9)
        self.assertIn(self.customer.name, self.hotel.reservations)

    def test_cancel_reservation(self):
        self.hotel.reserve_room(self.customer)
        self.assertTrue(self.hotel.cancel_reservation(self.customer))
        self.assertEqual(self.hotel.rooms, 10)
        self.assertNotIn(self.customer.name, self.hotel.reservations)

    def test_update_reservation(self):
        self.hotel.reserve_room(self.customer)
        new_customer = abstractions.Customer('New Customer')
        self.assertTrue(self.hotel.update_reservation(
            self.customer.name, new_customer.name)
            )
        self.assertIn(new_customer.name, self.hotel.reservations)
        self.assertNotIn(self.customer.name, self.hotel.reservations)

    def test_to_json(self):
        self.assertEqual(
            self.hotel.to_json(), 
            '{"name": "Test Hotel", "rooms": 10, "reservations": []}'
            )

    def test_from_json(self):
        json_str = '{"name": "Test Hotel", "rooms": 10, "reservations": []}'
        hotel = abstractions.Hotel.from_json(json_str)
        self.assertEqual(hotel.name, 'Test Hotel')
        self.assertEqual(hotel.rooms, 10)
        self.assertEqual(hotel.reservations, [])


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = abstractions.Customer('Test Customer')

    def test_to_json(self):
        self.assertEqual(self.customer.to_json(), '{"name": "Test Customer"}')

    def test_from_json(self):
        json_str = '{"name": "Test Customer"}'
        customer = abstractions.Customer.from_json(json_str)
        self.assertEqual(customer.name, 'Test Customer')


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.hotel_name = 'Test Hotel'
        self.customer_name = 'Test Customer'
        self.hotel = abstractions.Hotel(self.hotel_name, 10)
        self.customer = abstractions.Customer(self.customer_name)
        abstractions.save_to_file(self.hotel, f'{self.hotel_name}.hotel')
        abstractions.save_to_file(
            self.customer, f'{self.customer_name}.customer'
            )

    def tearDown(self):
        if os.path.exists(f'{self.hotel_name}.hotel'):
            os.remove(f'{self.hotel_name}.hotel')
        if os.path.exists(f'{self.customer_name}.customer'):
            os.remove(f'{self.customer_name}.customer')

    def test_save_and_load_from_file(self):
        loaded_hotel = abstractions.load_from_file(
            abstractions.Hotel, f'{self.hotel_name}.hotel'
            )
        self.assertEqual(loaded_hotel.name, self.hotel_name)
        self.assertEqual(loaded_hotel.rooms, 10)

    def test_create_and_delete_hotel(self):
        abstractions.create_hotel('New Hotel', 5)
        self.assertTrue(os.path.exists('New Hotel.hotel'))
        abstractions.delete_hotel('New Hotel')
        self.assertFalse(os.path.exists('New Hotel.hotel'))

    def test_create_and_delete_customer(self):
        abstractions.create_customer('New Customer')
        self.assertTrue(os.path.exists('New Customer.customer'))
        abstractions.delete_customer('New Customer')
        self.assertFalse(os.path.exists('New Customer.customer'))

    def test_modify_hotel(self):
        abstractions.modify_hotel(self.hotel_name, 5)
        modified_hotel = abstractions.load_from_file(
            abstractions.Hotel, f'{self.hotel_name}.hotel'
            )
        self.assertEqual(modified_hotel.rooms, 5)

    def test_modify_customer(self):
        abstractions.modify_customer(self.customer_name, 'New Customer Name')
        modified_customer = abstractions.load_from_file(
            abstractions.Customer, 'New Customer Name.customer'
            )
        self.assertEqual(modified_customer.name, 'New Customer Name')

    def test_create_and_cancel_reservation(self):
        abstractions.create_reservation(self.customer_name, self.hotel_name)
        hotel = abstractions.load_from_file(
            abstractions.Hotel, f'{self.hotel_name}.hotel'
            )
        self.assertIn(self.customer_name, hotel.reservations)
        abstractions.cancel_reservation(self.customer_name, self.hotel_name)
        hotel = abstractions.load_from_file(
            abstractions.Hotel, f'{self.hotel_name}.hotel'
            )
        self.assertNotIn(self.customer_name, hotel.reservations)


class TestDisplayFunctions(unittest.TestCase):
    def setUp(self):
        self.hotel_name = 'Test Hotel'
        self.customer_name = 'Test Customer'
        self.hotel = abstractions.Hotel(self.hotel_name, 10)
        self.customer = abstractions.Customer(self.customer_name)
        abstractions.save_to_file(self.hotel, f'{self.hotel_name}.hotel')
        abstractions.save_to_file(
            self.customer, f'{self.customer_name}.customer'
            )

    def tearDown(self):
        if os.path.exists(f'{self.hotel_name}.hotel'):
            os.remove(f'{self.hotel_name}.hotel')
        if os.path.exists(f'{self.customer_name}.customer'):
            os.remove(f'{self.customer_name}.customer')

    @mock.patch('builtins.print')
    def test_display_hotel(self, mock_print):
        abstractions.display_hotel(self.hotel_name)
        mock_print.assert_any_call('Hotel Name: Test Hotel')
        mock_print.assert_any_call('Available Rooms: 10')
        mock_print.assert_any_call('Reservations:')

    @mock.patch('builtins.print')
    def test_display_customer(self, mock_print):
        abstractions.display_customer(self.customer_name)
        mock_print.assert_any_call('Customer Name: Test Customer')


if __name__ == '__main__':
    unittest.main()
