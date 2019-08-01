from {{cookiecutter.package_name}} import base


def test_fib() -> None:
    assert base.fib(0) == 0
    assert base.fib(1) == 1
    assert base.fib(2) == 1
    assert base.fib(3) == 2
    assert base.fib(4) == 3
    assert base.fib(5) == 5
    assert base.fib(10) == 55
