============================= test session starts ==============================
platform darwin -- Python 3.10.0, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/stephan/IOT_TC1004B
plugins: cov-3.0.0
collected 1 item

api/main_test.py F                                                       [100%]

=================================== FAILURES ===================================
__________________________________ test_main ___________________________________

    def test_main():
        r = m.add(5,5)
>       assert r == 5
E       assert 10 == 5

api/main_test.py:5: AssertionError

---------- coverage: platform darwin, python 3.10.0-final-0 ----------
Name               Stmts   Miss Branch BrPart  Cover
----------------------------------------------------
api/__init__.py        0      0      0      0   100%
api/main.py            2      0      0      0   100%
api/main_test.py       4      0      0      0   100%
----------------------------------------------------
TOTAL                  6      0      0      0   100%

=========================== short test summary info ============================
FAILED api/main_test.py::test_main - assert 10 == 5
============================== 1 failed in 0.21s ===============================
