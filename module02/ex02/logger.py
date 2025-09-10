import time
import os
from functools import wraps

LOGFILE = "machine.log"

def _username():
    return os.getenv('USER') or os.getenv('USERNAME') or 'unknown'

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = end - start
        name = func.__name__.replace('_', ' ').title()
        user = _username()
        left = f"({user})Running: {name}"
        pad_len = max(1, 20 - len(left))
        entry = f"{left}{' ' * pad_len}[ exec-time = {exec_time:.3f} s ]\n"
        try:
            with open(LOGFILE, 'a') as f:
                f.write(entry)
        except Exception:
            pass
        return result
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.01)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(0.01)
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    # run a small demo
    if os.path.exists(LOGFILE):
        os.remove(LOGFILE)
    machine = CoffeeMachine()
    for i in range(0, 3):
        machine.make_coffee()
    machine.add_water(70)
