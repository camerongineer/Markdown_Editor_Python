def help_command():
    print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\n' +
          'Special commands: !help !done')


def done_command():
    exit()


def menu():
    while True:
        formats = ['plain', 'bold', 'italic', 'header', 'link',
                   'inline-code', 'ordered-list', 'unordered-list', 'new-line']
        user_input = input('Choose a formatter: ')
        if user_input in formats:
            print(end='')
        elif user_input == '!help':
            help_command()
        elif user_input == '!done':
            done_command()
            break
        else:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    menu()
