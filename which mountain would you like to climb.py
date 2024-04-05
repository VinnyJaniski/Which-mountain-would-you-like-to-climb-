responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb? ")

    responses[name] = response

    repeat = input("Do you want another person to take apart at the poll? ")
    if repeat == 'no':
        polling_active = False


print("\n--- Poll Results")
for name, response in responses.items():
    print(name + " would like to climb " + response)