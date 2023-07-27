#!/bin/python


from urllib.request import urlopen


url = "http://www.baidu.com"

res = urlopen(url)

# print(res.read().decode("utf-8"))

with open("./mybaidu.html", "w") as f:
    f.write(res.read().decode("utf-8"))
