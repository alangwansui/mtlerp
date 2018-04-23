# -*- coding: utf-8 -*-
import _mssql
import re
from sqlserver import SQLServer

def vcut_outside_get_qty():
    MSQ = SQLServer(company='cs')
    OusideS_datas = MSQ.query("""select top 100 * from TBVCUT_OusideS where substate = 20 """)
    for outside_data in OusideS_datas:
        LC, VC, JumpQty, GoodsPlength, GoodsPWidth = 0, 0, 0, 0, 0

        OusideS_id = outside_data['id']
        GoodsCode = outside_data['GoodsCode']
        BatchCode = outside_data['BatchCode']
        BatchCode_real = BatchCode + '01'

        vut_info = MSQ.query_one("""select CutPerimeter,VC,JumpQty from TBGoodsTechOther where GoodsCode = '%s' and CutPerimeter > 0""" % GoodsCode)
        if vut_info:
            JumpQty = vut_info['JumpQty'] or 0
            LC = vut_info['CutPerimeter'] and int(vut_info['CutPerimeter']) or 0
            VC = vut_info['VC'] and int(vut_info['VC']) or 0

        tech_info = MSQ.query_one("""select BillCode from TPTechnicsFlowM where BatchCode = '%s'""" % BatchCode_real)
        param1 = MSQ.query_one("""select TechnicPara from TPTechnicsFlowS where billcode='%s'and workcentercode = 'W42'""" % tech_info['BillCode'])
        if param1:
            length_width = re.findall('[\d.]+MM', param1['TechnicPara'])
            if len(length_width) == 2:
                GoodsPlength = int(float(length_width[0][:-2]))
                GoodsPWidth = int(float(length_width[1][:-2]))
            else:
                print 'vcut 参数有误 %s' %  tech_info['BillCode']

        MSQ.write("""update TBVCUT_OusideS set LC=%s,VC=%s,JumpQty=%s,GoodsPlength=%s,GoodsPWidth=%s  where id=%s""" % (LC, VC, JumpQty, GoodsPlength,GoodsPWidth, OusideS_id))


