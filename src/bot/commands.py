import utils.constants
from src.bot.decorator import input_error


@input_error
def change_phone_by_name(args, contacts):
    name = args[0]
    new_phone = args[1]
    if str.capitalize(name) in contacts:
        contacts[name] = new_phone
        print(f"{name} phone number changed to {new_phone}.")
    else:
        print(f"{name} not found.")


@input_error
def get_phone_by_name(args, contacts):
    name = str.capitalize(args[0])
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} not found.")


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    name = name.strip().capitalize()
    contacts[name] = phone
    return "Contact added."


@input_error
def print_commands():
    print(utils.constants.COMMANDS)
