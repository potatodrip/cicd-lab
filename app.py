__version__ = "1.0.0"


def greetings(name: str):
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greetings("CI/CD test"))
