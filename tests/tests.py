from build_toolbox.function_tools import say_hello, long_word

def test_say_hello():
    result = say_hello()
    assert result == 'Hello'

def test_long_word(word):
    result = long_word(word)
    assert result == result > 5

