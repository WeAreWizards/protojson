import random

from barnum import gen_data

import addressbook_pb2


# Barnum generates US data but that's ok for the example
names = [gen_data.create_name() for _ in range(0, 15)]
phones = [gen_data.create_phone() for _ in range(0, 30)]
postcodes = [gen_data.create_city_state_zip() for _ in range(0, 15)]
streets = [gen_data.create_street() for _ in range(0, 30)]

contacts = []
for name in names:
    address = {}
    # Simulate the fact that postcode are optionals
    if random.choice([True, False]):
        address['postcode'] = random.choice(postcodes)[0]
    address['address_lines'] = random.sample(streets, random.randint(0, 2))

    phone_numbers = []
    for _ in range(0, random.randint(0, 2)):
        phone_numbers.append({
            'type': random.choice(['MOBILE', 'LANDLINE']),
            'number': random.choice(phones)
        })
    contacts.append({
        'first_name': name[0],
        'last_name': name[1],
        'address': address,
        'phone_numbers': phone_numbers
    })


def get_protobuf_data():
    """Need to protobuf-ize the data"""
    pb_contacts = []
    for contact in contacts:
        address =addressbook_pb2.Address()
        if contact['address'].get('address_lines'):
            address.address_lines.extend(contact['address']['address_lines'])
        if 'postcode' in contact['address']:
            address.postcode = contact['address']['postcode']
        pb_contacts.append(addressbook_pb2.Contact(
            first_name=contact['first_name'],
            last_name=contact['last_name'],
            address=address,
            phone_numbers=[
                addressbook_pb2.Phone(
                    type=addressbook_pb2.MOBILE if num['type'] == 'MOBILE' else addressbook_pb2.LANDLINE,
                    number=num['number']
                )
                for num in contact['phone_numbers']
            ]
        ))
    return addressbook_pb2.AddressBook(contacts=pb_contacts)
