import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8968'
r = requests.get(url, verify=False)
stations = re.findall(r'([A-Z]+)\|([a-z]+)', r.text)
stations = dict(stations)
stations = dict(zip(stations.values(), stations.keys()))
print('stations=')
pprint(stations, indent=4)

# 获取字典
    # 检查文件是否存在

        # 不存在Request生成文件

# 查询代码(string a)
    # 获取字典

    # 排查
