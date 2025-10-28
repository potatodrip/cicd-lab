from app import greetings

def test_greetings():
	assert greet("World") == "Hello, World"
