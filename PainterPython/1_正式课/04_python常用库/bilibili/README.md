# 执行说明


1. 运行`python create_sqlite_empty.py`，这时会生成一个comments.db这样一个数据库文件。

2. 编辑`videos.txt`，替换成你想要抓取的视频链接。

3. 执行`python get_bilibili_comment.py`，脚本会请求获取视频的评论信息，并存储到数据库中。


4. 执行`python read_sqlite.py`，可以读取数据库。