#!/usr/bin/env python3

import datetime
import json

def file_path(config):
    now = datetime.datetime.now()
    year = now.strftime(config['year_format'])
    month = now.strftime(config['month_format'])
    date_time = now.strftime(config['date_time_format'])
    return f"{config['path_to_daily_todos']}/{year}/{month}/{date_time}.md"

def main():
    with open('config.json') as config_file:
        config = json.load(config_file)

    print(file_path(config))


if __name__ == '__main__':
    main()