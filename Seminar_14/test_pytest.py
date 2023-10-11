import pytest
from Seminar_14.z1 import clear_text


def test1():
    assert clear_text('Te...выппмxt') == 'text'

def test2():
    assert clear_text('Te....Xвыаываt') == 'text'


if __name__ == '__main__':
    pytest.main(['-v'])
