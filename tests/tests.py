from mypackage import myModule

def test_top_n():
    """ Make sure top_n is working properly. """
    assert myModule.top_n([8,3,2,7,4], 3) == [8,7,4], 'incorrect output'
    assert myModule.top_n([8,3,2,7,4], 2) == [8,7], 'incorrect output'
    assert myModule.top_n([8,3,2,7,4], 1) == [8], 'incorrect output'   
