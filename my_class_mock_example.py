# A sample class to demonstrate mocking
class MyClass:
    def __init__(self, dependency):
        self.dependency = dependency

    def my_method(self, value):
        # More logic
        return self.dependency.some_method(value)
# my class unit tests (fake Dependency - mock) - unit tests

# integration tests  - how dependency and myclass work together



class Dependency:
    def some_method(self, a):
        return a*2


# dependency unit tests
