# -*- coding: utf-8 -*-
import _mssql
import re

class SQLServer(object):
    def __init__(self, company=''):
        if company=='sz':
            self.conn = _mssql.connect(server="192.168.10.2", user='sa', password='719799', database='mtlerp-running', charset='utf8')
        elif company=='cs':
            self.conn = _mssql.connect(server="192.168.10.8", user='sa', password='719799', database='mtlcs-running', charset='utf8')
        elif company == 'wx':
            self.conn = _mssql.connect(server="192.168.10.140", user='sa', password='7197999', database='wx', charset='utf8')

    def query(self, sql):
        res = []
        self.conn.execute_query(sql)
        for i in self.conn:
            res.append(i)
        return res

    def query_one(self, sql):
        self.conn.execute_query(sql)
        for i in self.conn:
            return i

    def write(self, sql):
        if not ('where' in sql):
            raise Exception, 'update语句缺少限定条件，很危险'
        self.conn.execute_query(sql)























