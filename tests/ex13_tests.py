from nose.tools import *
from ex13.ex13 import *

# def test_push():
#     colors = SLList()
#     colors.push("Pthalo Blue")
#     assert colors.count() == 1
#     colors.push("Ultramarine Blue")
#     assert colors.count() == 2

def test_pop():
    colors = SLList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None