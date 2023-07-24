#  FoxPay PYTHON SDK

## 简介

- 此sdk为方便python开发人员对接foxpay平台收银台功能

- 已实现功能

  - 创建订单

  - 查询订单

  - 关闭订单

  - 查询资产
  
  - 提现凭证获取

  - 提现确认

  - 提现记录查询


## 版本要求



## 安装

### 手动安装

源码下载：[foxpay-sdk](https://github.com/KamenSoftware/foxpay-sdk-python)


#### 依赖拓展

- re

## 项目使用

### config配置
路径：  foxpay/config/config.py
```python

#appid
appid = '7IJNKYVX'
#私钥字符串  (默认先选用私钥字符串)
# privateKey = ''
privateKey = ''
#私钥文件位置
privateKeyFile='C:/Users/40488/Downloads/2023-7-10/private2.pem'
#公钥字符串 (默认先选用公钥字符串)
# publicKey = ''
publicKey = ''
#公钥文件位置
publicKeyFile = 'C:/Users/40488/Downloads/2023-7-10/public2.pem'
#请求域名
url = ''
```


### 使用示例

```python
from services.FoxPayService import FoxPayService

#创建订单
orderCreateParam = {
    'subject' : 'test2334',
    'order_no' : 'test2334',
    'amount' : '1.2',
    'notify_url' : '',
    'redirect_url' : '',
    'time_out' : 1000,
    'locale' : 'zh-CN',
    'remark' : 'test'
}

#查询订单
queryParam = {
    'trade_no' : 'AP2023071310442022925526694',
    'order_no' : ''
}

#关闭订单
closeOrderParam = {
    'trade_no' : '',
    'order_no' : 'test23'
}

#提现凭证获取
transParamPrepareParam = {
    'order_no' : 'test233',
    'amount' : '1.2',
    'to_address' : '0x3810fe9f57f2f792a1522088c1a62d14cd5b86c4',
    'notify_url' : '',
    'remark' : ''
}

#提现确认
transParam = {
    'trans_token' : '8f230fa553b9434f9d19848d1e7ac42dwpg9ym',
}

#提现记录查询
getTransParam = {
    'trade_no' : '',
    'order_no' : 'test233'
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
```