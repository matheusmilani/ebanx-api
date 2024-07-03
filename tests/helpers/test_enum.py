from helpers.enum import *

class TestEnums:
    def test_event(self):
        assert EventType().enum_to_name(1) == 'deposit'
        assert EventType().enum_to_name(2) == 'withdraw'
        assert EventType().enum_to_name(3) == 'transfer'
        assert EventType().enum_to_name(93) == 'Invalid Number'

        assert EventType().name_to_enum('deposit') == 1
        assert EventType().name_to_enum('withdraw') == 2
        assert EventType().name_to_enum('transfer') == 3
        assert EventType().name_to_enum('notExist') == 'Invalid Name'