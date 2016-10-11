#! /usr/bin/env python3
# coding:utf-8
"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets beijing shanghai 2016-08-25
    tickets code 杭州
    tickets timetable beijing
"""
from docopt import docopt
from stations import stations
from TrainCollection import TrainCollection
import requests

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    # 构建url
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )
    r = requests.get(url, verify=False)
    rows = r.json()['data']['datas']
    options = {}
    trains = TrainCollection(rows, options)
    trains.pretty_print()


if __name__ == '__main__':
    cli()
