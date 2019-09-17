import os
import requests
from tags import TAGS

TAGS_FILE_NAME = 'tags.txt'
TAGS_DATA_NAME = 'tags.js'


def fill_tags():
    if os.path.exists(TAGS_FILE_NAME):
        os.remove(TAGS_FILE_NAME)

    with open(TAGS_FILE_NAME, 'a+') as tag_file:
        for i in range(1, 10):
            response = requests.get('https://api.stackexchange.com/search', params={
                'site': 'stackoverflow.com',
                'tagged': ';'.join(TAGS),
                'page': i,
                'pagesize': 100,
            })

            body = response.json()

            for item in body.get('items', []):
                for tag in item.get('tags', []):
                    tag_file.write(f'{tag}\n')


def get_tags_data():
    tag_data = {}
    with open(TAGS_FILE_NAME, 'r') as tag_file:
        for line in tag_file.readlines():
            tag = line.strip()
            if tag in tag_data:
                tag_data[tag] += 1
            else:
                tag_data[tag] = 1
    return tag_data


def write_tag_data_to_js_array():
    if os.path.exists(TAGS_DATA_NAME):
        os.remove(TAGS_DATA_NAME)

    with open(TAGS_DATA_NAME, 'w+') as data_file:
        data_file.write('window.stackData = [')
        for tag, count in get_tags_data().items():
            data_file.writelines([
                '{',
                "name: '{}',".format(tag),
                'count: {},'.format(count),
                '},',
            ])
        data_file.write('];')


if __name__ == '__main__':
    fill_tags()
    write_tag_data_to_js_array()
