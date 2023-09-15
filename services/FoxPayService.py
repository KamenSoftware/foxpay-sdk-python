from exception.FoxPayException import FoxPayException
from enums.CodeEnum import CodeEnum
from util.Request import Request

class FoxPayService:

    #创建订单地址
    ORDER_CREATE_URL = '/sdk/application/createApplicationOrder'

    #查询订单地址
    ORDER_QUERY_URL = '/sdk/application/getApplicationOrder'

    #关闭订单地址
    CLOSE_ORDER_URL = '/sdk/application/closeApplicationOrder'

    #查询金额地址
    GET_BALANCE_URL = '/sdk/application/getBalance'

    #提现凭证获取地址
    TRANS_PREPARE_URL = '/sdk/application/transPrepare'

    #提现确认地址
    TRANS_URL = '/sdk/application/trans'

    #提现记录查询地址
    GET_TRANS_URL = '/sdk/application/getTrans'

    request = Request()

    #创建订单
    def orderCreate(self,params = {}):

        if not params:
            raise FoxPayException(CodeEnum.PARAM_NOT_NULL)

        if not params['order_no']:

            raise FoxPayException(CodeEnum.PARAM_ERROR,'order_no')

        if not params['subject']:

            raise FoxPayException(CodeEnum.PARAM_ERROR,'subject')

        if not params['amount']:

            raise FoxPayException(CodeEnum.PARAM_ERROR,'amount')

        if not params['time_out']:

            raise FoxPayException(CodeEnum.PARAM_ERROR,'time_out')

        if not params['locale']:

            raise FoxPayException(CodeEnum.PARAM_ERROR,'locale')

        return self.request.orderRequest(self.ORDER_CREATE_URL,params,'POST')


    #查询订单
    def orderQuery(self,params = {}):

        if not params:
            raise FoxPayException(CodeEnum.PARAM_NOT_NULL)

        if not params['order_no'] and not params['trade_no']:

            raise FoxPayException(CodeEnum.PARAM_ERROR,'order_no or trade_no')

        return self.request.orderRequest(self.ORDER_QUERY_URL, params, 'POST')

    #关闭订单
    def closeOrder(self,params = {}):

        if not params:
            raise FoxPayException(CodeEnum.PARAM_NOT_NULL)

        if not params['order_no'] and not params['trade_no']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'order_no or trade_no')

        return self.request.orderRequest(self.CLOSE_ORDER_URL, params, 'POST')

    #查询金额
    def getBalance(self):

        return self.request.orderRequest(self.GET_BALANCE_URL, {}, 'GET')

    #提现凭证获取
    def transPrepare(self,params = {}):

        if not params:
            raise FoxPayException(CodeEnum.PARAM_NOT_NULL)

        if not params['order_no']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'order_no')

        if not params['amount']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'amount')

        if not params['to_address']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'to_address')

        if not params['gas_type']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'gas_type')

        return self.request.orderRequest(self.TRANS_PREPARE_URL, params, 'POST')

    #提现确认
    def trans(self,params = {}):

        if not params:
            raise FoxPayException(CodeEnum.PARAM_NOT_NULL)

        if not params['trans_token']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'trans_token')

        return self.request.orderRequest(self.TRANS_URL, params, 'POST')


    #提现记录查询
    """
        params请求参数：
            trade_no    流水号 (二选一或都填)    string
            order_no	商户号 (二选一或都填)    string
        返回参数：
            trade_no：流水号            string
            order_no：商户订单号          string
            trans_token：交易凭证    string
            status：提现状态：1 待提现，2 处理中，3 提现成功，4 提现失败       int
            to_address：提现地址     string
            notify_url：回调地址 string
            amount：数量   string
            fee：手续费 string
            balance：到账金额    string
            pay_time：支付时间   long
            tx_hash：交易 hash string
            remark：备注   string
            create_time：创建时间    long
            gas_type：手续费扣除：2 交易金额 3 账户余额    string
    """
    def getTrans(self,params = {}):

        if not params:
            raise FoxPayException(CodeEnum.PARAM_NOT_NULL)

        if not params['order_no'] and not params['trade_no']:
            raise FoxPayException(CodeEnum.PARAM_ERROR, 'order_no or trade_no')

        return self.request.orderRequest(self.GET_TRANS_URL, params, 'POST')