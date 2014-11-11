from nose.tools import *

import sys

sys.path.append("../")

from bilregistret.vehicles import Car

def test_Car_should_have_model():
    car=Car("volvo amazon")
    assert car.model == "saab"