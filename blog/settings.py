import os
import pathlib
import yaml



BASEDIR = pathlib.Path(__file__).parent.parent
config_path = os.path.join(BASEDIR, 'config', 'blog.yaml')


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
