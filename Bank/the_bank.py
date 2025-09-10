# the_bank.py

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = Account.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank:
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        # Check type
        if not isinstance(new_account, Account):
            print("Error: Not an Account instance")
            return False
        # Check if name already exists
        for acc in self.accounts:
            if acc.name == new_account.name:
                print(f"Error: Account with name '{acc.name}' already exists")
                return False
        # Add account
        self.accounts.append(new_account)
        return True

    def is_corrupted(self, account):
        # Check even number of attributes
        if len(account.__dict__) % 2 == 0:
            return True
        # Check if any attribute starts with 'b'
        if any(attr.startswith('b') for attr in account.__dict__):
            return True
        # Must have attribute starting with 'zip' or 'addr'
        if not any(attr.startswith('zip') or attr.startswith('addr') for attr in account.__dict__):
            return True
        # Must have 'name', 'id', 'value'
        for attr in ['name', 'id', 'value']:
            if not hasattr(account, attr):
                return True
        # Check types
        if not isinstance(account.name, str):
            return True
        if not isinstance(account.id, int):
            return True
        if not isinstance(account.value, (int, float)):
            return True
        return False

    def transfer(self, origin_name, dest_name, amount):
        if amount < 0:
            print("Error: Amount must be positive")
            return False

        # Find accounts
        origin = dest = None
        for acc in self.accounts:
            if acc.name == origin_name:
                origin = acc
            if acc.name == dest_name:
                dest = acc

        if origin is None or dest is None:
            print("Error: One or both accounts not found")
            return False

        # Check corruption
        if self.is_corrupted(origin):
            print(f"Error: Origin account '{origin_name}' is corrupted")
            return False
        if self.is_corrupted(dest):
            print(f"Error: Destination account '{dest_name}' is corrupted")
            return False

        # Same account, valid but no fund move
        if origin == dest:
            return True

        # Check funds
        if origin.value < amount:
            print("Error: Not enough funds in origin account")
            return False

        # Perform transfer
        origin.transfer(-amount)
        dest.transfer(amount)
        return True
