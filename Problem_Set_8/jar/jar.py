class Jar:
    def __init__(self, capacity=12):
        if type(capacity) != int:
            raise ValueError
        if capacity < 0:
            raise ValueError
        self.cookies_capacity = capacity
        self.current_size = 0

    def __str__(self):
        return "🍪" * self.current_size

    def deposit(self, n):
        if n < 0:
            raise ValueError
        future_size = n + self.current_size
        if future_size > self.cookies_capacity:
            raise ValueError
        else:
            self.current_size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError
        if n > self.current_size:
            raise ValueError
        else:
            self.current_size -= n

    @property
    def capacity(self):
        return self.cookies_capacity

    @property
    def size(self):
        return self.current_size


jar = Jar(20)
print(type(jar))
print(jar.capacity)
print(jar.size)
jar.deposit(10)
print(jar.size)
