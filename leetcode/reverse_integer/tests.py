from solution import Solution


def test_return_zero_when_input_is_zero():
    sol = Solution()
    result = sol.reverse(0)
    assert result == 0


def test_return_int_when_int_is_less_than_ten():
    sol = Solution()
    result = sol.reverse(9)
    assert result == 9

    result = sol.reverse(-8)
    assert result == -8


def test_return_reversed_when_not_negative_input():
    sol = Solution()
    result = sol.reverse(12)
    assert result == 21


def test_return_reversed_when_negative_input():
    sol = Solution()
    result = sol.reverse(-12)
    assert result == -21

def test_return_reversed_when_negative_input_big():
    sol = Solution()
    result = sol.reverse(-12345678)
    assert result == -87654321