def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "You have entered an incorrect number of arguments for this command."
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."

    return inner
