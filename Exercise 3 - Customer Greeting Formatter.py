def format_greeting(name, title="Customer"):
    """Return a personalized greeting using the customer's first name."""
    name = name.strip()          
    if name == "":               
        return "Hello, Valued Customer!"
    name = name.title()          
    first_name = name.split()[0] 
    return f"Hello, {first_name} ({title})!"
 
 
full_name = input("What's your full name? ")
print(format_greeting(full_name))
 

