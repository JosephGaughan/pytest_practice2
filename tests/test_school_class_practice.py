from lib.school_class_practice import *
import pytest

def test_school():
    school_test = School("St Test", "Clitheroe", 99)
    assert school_test.pupils == 99

def test_school_age():
    school_test = School("St Test", "Clitheroe", 99)
    school_test.school_age(1025)
    assert school_test.age == 1000

def test_negative_pupil_number_error():
    with pytest.raises(Exception) as e:
        school_test = School("St Test", "Clitheroe", -99)
    assert str(e.value) == "Number of pupils cannot be nagative."