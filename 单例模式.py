class SingletonObject:
    def __new__(cls, *args, **kwargs):
        if not hasattr(SingletonObject, "_instance"):
            SingletonObject._instance = object.__new__(cls)
        return SingletonObject._instance

    def __init__(self):
        pass