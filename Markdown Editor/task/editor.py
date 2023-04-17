import format
from format import formats


def help_command():
    print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n' +
          'Special commands: !help !done')


def done_command():
    exit()


def menu():
    formatted_string = ''
    while True:
        user_input = input('Choose a formatter: ')
        if user_input in formats.keys():
            formatted_string += format.get_formatted_string(user_input)
            print(formatted_string)
        elif user_input == '!help':
            help_command()
        elif user_input == '!done':
            done_command()
            break
        else:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    menu()
