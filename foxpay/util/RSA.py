import base64
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from exception.FoxPayException import FoxPayException
from enums.CodeEnum import CodeEnum

class RSA:

    #参数字典排序
    def sortDictByFirstLetter(self,dictionary):

        sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
        return sorted_dict

    #获取签名字符串
    def getSign(self,dictionary):

        sorted_dict = self.sortDictByFirstLetter(dictionary)

        sign_key = ''

        for key, value in sorted_dict.items():

            sign_key = sign_key + str(key) + '=' + str(value) + '&'

        sign_key = sign_key[:-1]

        return sign_key

    #格式化私钥
    def formatPriKey(self, private_key):

        start = '-----BEGIN RSA PRIVATE KEY-----\n'
        end = '-----END RSA PRIVATE KEY-----'

        result = ''
        # 分割key，每64位长度换一行
        length = len(private_key)
        divide = 64  # 切片长度
        offset = 0  # 拼接长度
        while length - offset > 0:
            if length - offset > divide:
                result += private_key[offset:offset + divide] + '\n'
            else:
                result += private_key[offset:] + '\n'
            offset += divide

        result = start + result + end

        return result

    #格式化公钥
    def formatPubKey(self, public_key):

        start = '-----BEGIN PUBLIC KEY-----\n'
        end = '-----END PUBLIC KEY-----'

        result = ''
        # 分割key，每64位长度换一行
        length = len(public_key)
        divide = 64  # 切片长度
        offset = 0  # 拼接长度
        while length - offset > 0:
            if length - offset > divide:
                result += public_key[offset:offset + divide] + '\n'
            else:
                result += public_key[offset:] + '\n'
            offset += divide

        result = start + result + end

        return result

    #获取私钥签名
    def getPrivateSign(self,sign_str,private_key):

        private_key = serialization.load_pem_private_key(
                private_key.encode('utf-8'),
                password=None,
                backend=default_backend()
            )

        # 将字符串转换为字节串
        data_to_sign_bytes = sign_str.encode('utf-8')

        # 使用私钥进行 SHA1withRSA 签名
        signature = private_key.sign(
            data_to_sign_bytes,
            padding.PKCS1v15(),
            hashes.SHA1()
        )

        # 将签名结果进行 Base64 编码
        signature_base64 = base64.b64encode(signature).decode('utf-8')

        return signature_base64

    #公钥验签
    def publicVerify(self,data_str,sign,publick_key):

        publick_key = serialization.load_pem_public_key(
            publick_key.encode('utf-8'),
            backend = default_backend()
        )

        data_to_sign_bytes = data_str.encode('utf-8')

        sign_to_bytes = base64.b64decode(sign)   #解码

        try:

            publick_key.verify(sign_to_bytes, data_to_sign_bytes, padding.PKCS1v15(), hashes.SHA1())

        except Exception as e:

            raise FoxPayException(CodeEnum.RESPONSE_SIGN_ERROR)

        return True