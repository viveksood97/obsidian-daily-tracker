#!/usr/bin/env python3

import datetime
import json
import os

def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def file_dir_and_name(config):
    now = datetime.datetime.now()
    year = now.strftime(config['year_format'])
    month = now.strftime(config['month_format'])
    date_time = now.strftime(config['date_time_format'])
    return f"{config['path_to_daily_todos']}/{year}/{month}", f"{date_time}.md"

def main():
    with open('config.json') as config_file:
        config = json.load(config_file)
    file_dir, file_name = file_dir_and_name(config)
    create_dir_if_not_exists(file_dir)
    with open(file_dir + "/" + file_name, 'w') as file:
        file.write(f"# {datetime.datetime.now().strftime(config['date_time_format'])}\n\n")
        file.write(f"## Tasks\n\n")
        file.write(f"## Notes\n\n")


if __name__ == '__main__':
    main()