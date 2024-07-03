class EventType:
    def __init__(self):
        self.switcher_by_name = {
            'deposit': 1,
            'withdraw': 2,
            'transfer': 3
        }

        self.switcher_by_number = {
            1: 'deposit',
            2: 'withdraw',
            3: 'transfer',
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Invalid Number')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Invalid Name')