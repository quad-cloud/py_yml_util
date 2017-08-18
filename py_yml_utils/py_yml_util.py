import yaml
import requests
import os


def main():
    yaml_file('https://raw.githubusercontent.com/unitedstates/congress-legislators/master/executive.yaml')
    get_birthday(first="Thomas", last="Jefferson")


def yaml_file(url):
    r = requests.get(url)
    r.raw.read()
    with open(path1, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)


def get_birthday(**kwargs):
    with open(path1, 'r') as f:
        data = yaml.load(f)
        for name1 in data:
            if(name1['name'] == kwargs):
                print("birthday:", name1['bio']['birthday'])


def _get_file_path():
    path = os.path.dirname(os.path.abspath(__file__))
    split_path = os.path.split(path)
    return os.path.join(split_path[0], 'templates')


path1 = os.path.join(_get_file_path(), 'sample.yml')


if __name__ == '__main__':
    main()
