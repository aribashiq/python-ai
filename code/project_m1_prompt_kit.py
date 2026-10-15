
"""Create AI prompts for local businesses."""

# Ask questions to make prompts specific to each business.
name = input("Business name: ")
business = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")
budget = int(input("Monthly budget (PKR): "))

print("\n=========================================")
print(f"     AI Prompt Kit for {name}")
print("=========================================")

# Naming the audience helps make marketing more relevant.
print("\n[1] Marketing")
print(f"Write a short Instagram post for {name}, a {business} in {city}.")
print(f"Target {customers}. Use a friendly tone and 1 call to action.")

# A polite response helps maintain customer trust.
print("\n[2] Customer Service")
print(f"You are the manager of {name}. Write a polite reply to a customer")
print("whose order arrived late. Apologise and offer a small discount.")

# A budget helps AI suggest affordable ideas.
print("\n[3] Growth")
print(f"Suggest 3 low-cost AI ideas for a {business} in {city}.")
print(f"Target {customers} with a budget of {budget} PKR per month.")
