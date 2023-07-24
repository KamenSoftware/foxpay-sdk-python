class CodeEnum:

    SUCCESS = {'code':10000,'message':'成功'}

    CONFIG_NOT_NULL = {'code': 61000, 'message': '配置不能为空'}

    PARAM_NOT_NULL = {'code': 61001, 'message': '请求参数对象不能为空'}

    RESPONSE_SIGN_ERROR = {'code': 61002, 'message': '响应签名异常'}

    REQUEST_SIGN_ERROR = {'code': 61003, 'message': '请求签名异常'}

    PARAM_ERROR = {'code': 61004, 'message': '参数异常'}

    CONFIG_ERROR = {'code': 61005, 'message': '配置异常'}

    FILE_ERROR = {'code': 61006, 'message': '读取文件异常'}