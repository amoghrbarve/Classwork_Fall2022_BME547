# def test_check_HDL():
#     from blood_calc import check_HDL
#     answer = check_HDL(85)
#     expected = "Normal"
#     assert answer == expected

# def test_check_HDL_borderline():
#     from blood_calc import check_HDL
#     answer = check_HDL(55)
#     expected = "Borderline"
#     assert answer == expected

# def test_check_HDL_low():
#     from blood_calc import check_HDL
#     answer = check_HDL(20)
#     expected = "Low"
#     assert answer == expected
import pytest
@pytest.mark.parametrize("input_HDL,expected",[(85,"Normal"),(55,"Borderline"),(20,"Low")])
def test_check_HDL(input_HDL,expected):
    from blood_calc import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected