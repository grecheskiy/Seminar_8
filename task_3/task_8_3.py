import yaml


def write_dict_to_yaml(dict, file):
    with open(file, 'w') as f_n:
        yaml.dump(dict, f_n, default_flow_style=False, allow_unicode=True)

    with open(file) as f_n:
        f_n_content = yaml.load(f_n)

    print(f_n_content == dict)


if __name__ == "__main__":
    my_dict = {
        '100€': [1, 2, 3, 4],
        '200€': 8000,
        '300€': {
            'first': [1, 2, 3, 4],
            'second': 800,
        }
    }

    write_dict_to_yaml(my_dict, 'file.yaml')
