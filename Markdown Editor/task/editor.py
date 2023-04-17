from format import formats
from format import get_formatted_string


def help_command():
    print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n' +
          'Special commands: !help !done')


def done_command():
    exit()


def menu():
    formatted_lines = []
    while True:
        user_input = input('\nChoose a formatter: ')
        if user_input in formats.keys():
            formatted_lines.append(get_formatted_string(user_input))
            for line in formatted_lines:
                print(line, end='')
        elif user_input == '!help':
            help_command()
        elif user_input == '!done':
            save(formatted_lines)
            done_command()
            break
        else:
            print('Unknown formatting type or command')


def save(formatted_lines):
    with open('output.md', 'w') as file:
        file.writelines(formatted_lines)


if __name__ == '__main__':
    menu()
