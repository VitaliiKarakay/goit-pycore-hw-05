from src.bot.commands import parse_input
from src.bot.handlers import handle_invalid_command, command_handlers


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Input 'help' for a list of commands.")
    should_exit = False
    while not should_exit:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        handler = command_handlers.get(command, handle_invalid_command)
        should_exit = handler(args, contacts)


if __name__ == "__main__":
    main()
