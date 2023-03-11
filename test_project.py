from project import chck_crct_args, slct_house, slct_grade
import pytest

def test_chck_crct_args():
    with pytest.raises(SystemExit):
        chck_crct_args()



def test_slct_house():
    assert slct_house("courage") == "Gryffindor"
    assert slct_house("dedication") == "Hufflepuff"
    assert slct_house("wisdom") == "Ravenclaw"
    assert slct_house("ambition") == "Slytherin"


def test_function_n():
    assert slct_grade(2009) == "Grade 9"
    assert slct_grade(2015) == "Grade 3"
    assert slct_grade(2013) == "Grade 5"
