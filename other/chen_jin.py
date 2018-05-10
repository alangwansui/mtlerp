# -*- coding: utf-8 -*-
import _mssql
import re
from sqlserver import SQLServer


def vcut_outside_get_qty(billcode):
    MSQ = SQLServer(company='cs')
    M_data = MSQ.query_one("""select top 1 * from TBGold_NickelM where billcode = '%s'""" % billcode)

    #获取明细
    S_datas = MSQ.query(
        """select BillsubCode,BillSeq,GoodsCode,ApplicationQty,Batchcode,OtherRequest1,ISPCS from TBGold_NickelS where Billcode='%s'""" % billcode)
    for data in S_datas:
        #print  data
        GoodsCode = data['GoodsCode']
        Batchcode = data['Batchcode']
        RltvBillCode = MSQ.query_one_field("""select top 1 BillCode from TPTechnicsFlowM where BatchCode = '%s'""" % Batchcode)
        TechnicPara = MSQ.query_one_field(
            """select TechnicPara from TPTechnicsFlowS where billcode = '%s' and workcentercode = 'W42'""" % RltvBillCode)
        TechnicPara1 = MSQ.query_one_field(
            """select TechnicPara from TPTechnicsFlowS where billcode = '%s' and workcentercode = 'W39'""" % RltvBillCode)

        #print GoodsCode, Batchcode, RltvBillCode, TechnicPara, TechnicPara1

        GoodsPlength, GoodsPWidth = 0, 0

        ##M档案号
        if GoodsCode[0].upper() == 'M':
            length_width = re.findall('[\d.]+MM', TechnicPara)
            if len(length_width) != 2:
                print u'error===工艺参数无法解析===%s %s %s' % (RltvBillCode, GoodsCode, TechnicPara)
            else:
                GoodsPlength = int(float(length_width[0][:-2]))
                GoodsPWidth = int(float(length_width[1][:-2]))
        ##非M档案号
        else:
            MLength = MSQ.query_one_field("""select MLength from TPTechnicsFlowM where BatchCode = '%s'""" % Batchcode)
            MWidth = MSQ.query_one_field("""select MWidth from TPTechnicsFlowM where BatchCode = '%s'""" % Batchcode)
            GoodsPlength = int(float(MLength))
            GoodsPWidth = int(float(MWidth))

        #print '####',GoodsCode, GoodsPlength, GoodsPWidth, TechnicPara1

        #
        Gold , Nickel, GTL, GBL= None, None, None, None

        Gold_str = re.findall(u'金厚.([\d.]+)', TechnicPara1)
        print '====__', Gold_str
        if not Gold_str:
            print u'金厚参数错误 %s %s' % (GoodsCode,TechnicPara1)
        else:
            Gold = float(Gold_str[0])

        Nickel_str =  re.findall(u'镍厚.([\d.]+)', TechnicPara1)
        if not Nickel_str:
            print u'镍厚参数错误 %s %s' % (GoodsCode,TechnicPara1)
        else:
            Nickel = float(Nickel_str[0])

        GTL_str =  re.findall(u'GTL.([\d.]+)', TechnicPara1)
        if not GTL_str:
            print u'GTL参数错误 %s %s' % (GoodsCode,TechnicPara1)
        else:
            GTL = float(GTL_str[0])

        GBL_str =  re.findall(u'GBL.([\d.]+)', TechnicPara1)
        if not GBL_str:
            print u'GTL参数错误 %s %s' % (GoodsCode,GBL_str)
        else:
            GBL = float(GBL_str[0])

        print u'======档案号%s=====金厚%s 镍厚%s  GTL%s  GBL%s ' % (GoodsCode,Gold,Nickel,GTL,GBL)
if __name__ == '__main__': 
    vcut_outside_get_qty('ZSCS180507006')
	
    


