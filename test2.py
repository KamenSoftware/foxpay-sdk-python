from services.FoxPayService import FoxPayService

#创建订单
orderCreateParam = {
    'subject' : 'qxy1',   #
    'order_no' : 'qxy1',
    'amount' : '1.2',
    'notify_url' : '',
    'redirect_url' : '',
    'time_out' : 1000,
    'locale' : 'zh-CN',
    'remark' : 'test'
}

#查询订单
queryParam = {
    'trade_no' : '',
    'order_no' : 'qxy1'
}

#关闭订单
closeOrderParam = {
    'trade_no' : '',
    'order_no' : 'qxy23'
}

#提现凭证获取
transParamPrepareParam = {
    'order_no' : 'abcr1',
    'amount' : '1.2',
    'to_address' : 'TNFWzUREyAPFoLeFjNdYc3R48MKkw2mLbZ',
    'notify_url' : '',
    'remark' : '',
    'gas_type':'2'
}

#提现确认
transParam = {
    'trans_token' : 'a30b44f254eb44cb96afcb510304871bk2ist0',
}

#提现记录查询
getTransParam = {
    'trade_no' : '',
    'order_no' : 'qxy1'
}

service = FoxPayService()

#创建订单
# data = service.orderCreate(orderCreateParam)

#查询订单
data = service.orderQuery(queryParam)

#关闭订单
# data = service.closeOrder(closeOrderParam)

#查询资产
# data = service.getBalance()

#提现凭证获取
# data = service.transPrepare(transParamPrepareParam)

#提现确认
# data = service.trans(transParam)

#提现记录查询
# data = service.getTrans(getTransParam)

print(data)
