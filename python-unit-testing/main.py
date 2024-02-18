import abstractions as a


def main():
    a.create_hotel('Hotel California', 100)
    a.create_customer('John Doe')
    a.create_reservation('John Doe', 'Hotel California')
    a.display_hotel('Hotel California')
    print('------------------')
    a.display_customer('John Doe')
    print('------------------')
    a.modify_hotel('Hotel California', 200)
    a.modify_customer('John Doe', 'Jane Doe')
    a.display_hotel('Hotel California')
    print('------------------')
    a.display_customer('Jane Doe')
    print('------------------')
    a.cancel_reservation('Jane Doe', 'Hotel California')
    a.display_hotel('Hotel California')
    print('------------------')
    a.delete_hotel('Hotel California')
    a.delete_customer('Jane Doe')


if __name__ == "__main__":
    main()
