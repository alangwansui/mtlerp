# -*- coding: utf-8 -*-
import _mssql
import re
from sqlserver import SQLServer

def customer_change_saler(from_name, to_name):
    MSQ = SQLServer(company='sz')





"""
select * from  TBCustmer where handlercode = '3101'
--  林鸿恒    转给    张文利
--  3101              2566

select EmployeeCode,EmployeeName  from TBEmployee where EmployeeName in ('林鸿恒','张文利')
update  TBCustmer set handlercode = '2566' where handlercode = '3101'
select * from TBCustmer where handlercode = '2566'
"""