#!/bin/python

class User:
    def __init__(self, user_id, nickname, avatar) -> None:
        self.user_id = user_id
        self.nickname = nickname
        self.avatar = avatar

class Note:

    def __init__(self, note_id, user_id, user_name, avatar):
        self.note_id = note_id
        self.user = User(user_id, nickname=user_name, avatar=avatar)
        self.title = ""
        self.desc = ""
        self.tags = []
        self.images = []
        self.interact_info = InteractInfo()

class InteractInfo:
    def __init__(self, likes, collects, shares):
        self.likes = likes
        self.collects = collects
        self.shares = shares

class Comment:
    def __init__(self):
        self.