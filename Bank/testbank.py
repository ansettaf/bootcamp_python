# test_bank.py
from the_bank import Account, Bank

# Create bank
bank = Bank()

# Create accounts
alice = Account("Alice", value=100, addr="Street 1", zip_code="12345")
bob = Account("Bob", value=50, addr="Street 2", zip_code="67890")

# Add accounts to bank
bank.add(alice)
bank.add(bob)

# Perform transfer
bank.transfer("Alice", "Bob", 30)

# Print results
print(alice.value)  # Expected: 70
print(bob.value)    # Expected: 80
