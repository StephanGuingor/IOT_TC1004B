import api.main as m

def test_main():
    if 0 == 1:
        return 1
    r = m.add(5,5)
    assert r == 10