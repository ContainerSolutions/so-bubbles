import os

CATEGORIES_DATA_NAME = 'category_competence.js'

CATEGORIES_DATA = {
    'CI/CD': [
        '3;5',
        '3;4',
        '3;4',
        '3;4',
        '3;4',
        '3;4',
        '3;5',
    ],
    'Development': [
        '3;5',
        '4;5',
        '3;4',
        '4;5',
        '3;4',
        '3:3',
        '3;5',
    ],
    'Infrastructure': [
        '4;5',
        '5;5',
        '4;5',
        '3;5',
        '3;5',
        '4;5',
        '4;5',
    ],
    'Security': [
        '2;5',
        '3;5',
        '3;5',
        '2;5',
        '2;5',
        '2;5',
        '3;5',
    ],
    'Serverless': [
        '1;5',
        '1;5',
        '1;5',
        '2;5',
        '1;5',
        '1;5',
        '2;5',
    ]
}


def get_category_data():
    category_data = {}
    for key, values in CATEGORIES_DATA.items():
        category_data[key] = sum([int(v[0:1]) for v in values])
    return category_data


def write_category_data_to_js_array():
    if os.path.exists(CATEGORIES_DATA_NAME):
        os.remove(CATEGORIES_DATA_NAME)

    with open(CATEGORIES_DATA_NAME, 'w+') as data_file:
        data_file.write('window.stackData = [')
        for category, count in get_category_data().items():
            data_file.writelines([
                '{',
                "name: '{}',".format(category),
                'count: {},'.format(count),
                '},',
            ])
        data_file.write('];')


if __name__ == '__main__':
    # fill_tags()
    # get_category_data()
    write_category_data_to_js_array()
