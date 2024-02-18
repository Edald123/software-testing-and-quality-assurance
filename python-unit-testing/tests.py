import unittest
from abstractions import Hotel, Customer


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel('Test Hotel', 10)
        self.customer = Customer('Test Customer')

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
        self.assertTrue(
            self.hotel.update_reservation(self.customer.name, 'New Customer')
            )
        self.assertNotIn(self.customer.name, self.hotel.reservations)
        self.assertIn('New Customer', self.hotel.reservations)


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('Test Customer')

    def test_to_json(self):
        json_str = self.customer.to_json()
        self.assertIn('Test Customer', json_str)

    def test_from_json(self):
        json_str = self.customer.to_json()
        new_customer = Customer.from_json(json_str)
        self.assertEqual(new_customer.name, 'Test Customer')


if __name__ == '__main__':
    unittest.main()
