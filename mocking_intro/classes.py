class ProductionClass:
    def do_something(self):
        raise RuntimeError("This should never be called, we need to mock this!")
