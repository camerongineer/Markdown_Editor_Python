
def get_text():
    return input('Text: ')


def get_label():
    return input('Label: ')


def get_url():
    return input('URL: ')


def get_level():
    level = input('Level: ')
    while not level.isdigit() or int(level) not in range(1, 6):
        print('The level should be within the range of 1 to 6')
        level = input('Level: ')
    return int(level)


def get_num_rows():
    while True:
        try:
            number_of_rows = int(input('Number of rows: '))
            if number_of_rows < 1:
                raise ValueError
            return number_of_rows
        except (ValueError, TypeError):
            print('The number of rows should be greater than zero')


def append_new_line(in_text, num_lines=1):
    out_text = in_text + ("\n" * num_lines)
    return out_text


def plain_format():
    return get_text()


def bold_format():
    bold_text = get_text()
    return f'**{bold_text}**'


def italic_format():
    italic_text = get_text()
    return f'*{italic_text}*'


def header_format():
    header_level = get_level()
    header_text = ("#" * header_level) + ' ' + get_text()
    return append_new_line(header_text)


def link_format():
    link_label = get_label()
    link_url = get_url()
    return f'[{link_label}]({link_url})'


def inline_code_format():
    inline_code_text = get_text()
    return f'`{inline_code_text}`'


def list_format(ordered=True):
    num_rows = get_num_rows()
    list_string = ''
    for i in range(1, num_rows + 1):
        type_ch = f'{i}.' if ordered else '*'
        string = input(f'Row #{i}: ')
        list_string += f'{type_ch} {string}\n'
    return list_string


def ordered_list_format():
    return list_format(ordered=True)


def unordered_list_format():
    return list_format(ordered=False)


def new_line_format():
    return append_new_line('')


formats = {
    'plain': plain_format,
    'bold': bold_format,
    'italic': italic_format,
    'header': header_format,
    'link': link_format,
    'inline-code': inline_code_format,
    'ordered-list': ordered_list_format,
    'unordered-list': unordered_list_format,
    'new-line': new_line_format
}


def get_formatted_string(user_input):
    return formats[user_input]()
