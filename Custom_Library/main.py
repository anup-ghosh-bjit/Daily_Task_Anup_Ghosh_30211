from mypassgen import generate_pass

# Generate a random password with all default options (length is required)
password = generate_pass(length=8,special=True,uppercase=True,lowercase=True,numbers=False)
print("Random password:", password)