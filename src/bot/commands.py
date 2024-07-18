import utils.constants
from src.bot.decorator import input_error


@input_error
def change_phone_by_name(args, contacts):
    name = str.capitalize(args[0])
    if name not in contacts:
        raise KeyError
    new_phone = args[1]
    contacts[name] = new_phone
    return f"{name} phone number changed to {new_phone}."


@input_error
def get_phone_by_name(args, contacts):
    name = str.capitalize(args[0])
    return f"{name}: {contacts[name]}"


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
