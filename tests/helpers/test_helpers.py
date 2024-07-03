from helpers import *


class TestHelpers:
    def test_remove_repeated(self):
        list_1 = [1,2,3,1]
        assert remove_repeated(list_1) == [1,2,3]

    def test_is_none_or_zero(self):
        assert isNoneOrZero(0) == True
        assert isNoneOrZero(None) == True
        assert isNoneOrZero('None') == False
        assert isNoneOrZero('aasdasd') == False
