# -*- coding: utf-8 -*-
import peewee

db = peewee.SqliteDatabase("data.db")

class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db

User.create_table()

for line in open("user.tsv", "r"):
    (userId, userCompany, userDiscountRate) = tuple(line[:-1].split(","))
    if userDiscountRate.isdigit():
        User.create(
            userId = userId,
            userCompany = userCompany,
            userDiscountRate = int(userDiscountRate)
        )
