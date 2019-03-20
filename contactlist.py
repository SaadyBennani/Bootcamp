# contactlist.py


class ContactList:
    """
    contact list as dictionary of dictionaries implementation
    """

    def __init__(self, csv=None, header=None):
        """
        initializes ContactList from csv file or header
        """
        if csv is None:
            self.header = header
            self.contacts = {}
        else:
            self.csv_to_contactlist(csv)


def csv_to_contactlist(self, csv):
    """
reads csv file and parses into a dict of dicts
    """
    with open(csv, 'r') as file:
        lines = file.read().lower().split('\n')

        if not header:
            header = lines[0].lower().split(',')

    contact_list = {}

    for i in range(1, len(lines[:-1:])):
        line = lines[i]
        comp = line.split(',')
        contact = dict(zip(header, comp))
        contact_list[contact['name']] = contact

    self.contacts = contact_list
    self.header = header

    return contact_list


header = ['name', 'favorite fruit', 'favorite color']


def create(contact_list, contact):
    """
    adds a new contact to the contact list
    """
    if contact_list.get(contact['name']):
        return f"Error: {contact['name']} already exists!"

    contact_list['name'] = contact
    return f"Created new contact for {contact['name']}"


def read(contact_list, name):
    """
    returns contact with contact name
    """
    return contact_list.get(name, f'Error: {name} does not exist.')


def update(contact_list, name, updated_info):
    """
    updates existing contact with updated updated info
    """
    if contact_list.get(name):
        contact_list[name].update(updated_info)
        return f'Updated contact: {name}'
    return f'Error: {name} does not exist'


def delete(contact_list, name):
    """
    deletes a contact
    """
    if contact_list.get(name):
        del contact_list[name]
    return f'{name} does not exist'


def print_contact(contact):
    """
    prints a specified contact
    """
    if type(contact) is dict:
        for k, v in contact.items():
            print(f'{k}: {v}')
    else:
        print(contact)


def list_all(contact_list):
    """
    prints all conacts within contact list
    """
    for contact in contact_list:
        print_contact(contact_list[contact])
        print()


def save(contact_list, header, csv):
    """
    writes contact list as csv file
    """
    contacts = [', '.join(header)]
    for name in contact_list:
        contact = contact_list[name]
        contacts.append(', '.join(contact.values()))
    with open(csv, 'w') as f:
        f.write('\n'.join(contacts))
    return f'saving contacts as {csv}...'


contacts = csv_to_contactlist('contacts.csv', header)
loop = True

valid_inputs = [
        'c', 'create',
        'r', 'read',
        'u', 'update',
        'd', 'delete',
        'e', 'list', 'ls',
        'x', 'exit', 'quit',
        'h', 'help']

commands = """
    Commands:
    (c)reate
    (r)ead
    (u)pdate
    (d)elete
    (e)xpand list
    e(x)it
    (h)elp
    """

print('***************Contact List***************')
print(commands)

while loop:
    print('~'*60)
    while True:
        cmd = input('>').strip().lower()
        if cmd in valid_inputs:
            break
        print('Invalid input.')
        print(commands)

    if cmd in ['x', 'exit', 'quit', 'q']:
        print(save(contacts, header, 'contact_list2.csv'))
        loop = False
        print('Goodbye')

    elif cmd in ['e', 'list', 'ls']:
        list_all(contacts)

    elif cmd in ['h', 'help']:
        print(commands)

    elif cmd.startswith('c'):
        contact = {}
        for header in header:
            contact[header] = input(f'{header}: ')
        print(create(contacts, contact))

    elif cmd.startswith('r'):
        name = input('name: ')
        contact = read(contacts, name)
        print_contact(contact)

    elif cmd.startswith('u'):
        name = input('name: ')
        contact = {}
        for header in header:
            val = input(f'{header}: ')
            if val:
                contact[header] = val
        print(update(contacts, name, contact))

    elif cmd.startswith('d'):
        name = input('name: ')
        confirmation = input('are you sure')
        if confirmation in ['y', 'yes']:
            print(delete(contacts, name))
        else:
            print('Aborting...')
