from config import config
from util.RSA import RSA
import requests
import json
from enums.CodeEnum import CodeEnum

class Request:

    rsa = RSA()

    def orderRequest(self,url,param,method = 'POST'):

        url = config.url + url

        public_key = config.publicKey

        private_key = config.privateKey

        if not public_key or not private_key:

            with open(config.publicKeyFile,'r') as public_file:

                public_key = public_file.read()

            with open(config.privateKeyFile,'r') as private_file:

                private_key = private_file.read()

        else:

            public_key = self.rsa.formatPubKey(public_key)

            private_key = self.rsa.formatPriKey(private_key)

        return self.doOrderRequest(url=url,param=param,public_key=public_key,private_key=private_key,method=method)


    def doOrderRequest(self,url,param,public_key,private_key,method = 'POST'):

        rsa = self.rsa

        sign_str = rsa.getSign(param)

        header_sign = rsa.getPrivateSign(sign_str,private_key)

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'app_id': config.appid,
            'sign': header_sign
        }

        if method.upper() == 'POST' :
            response = requests.post(url=url,headers=headers,data=json.dumps(param))
        else:
            response = requests.get(url=url,headers=headers)

        response_data = response.json()   #响应数据

        if response_data == CodeEnum.SUCCESS['code'] :

            sign = response.headers['sign']  # 响应sign

            sign_str = rsa.getSign(response_data['data'])   #响应数据排序后的字符串

            rsa.publicVerify(sign_str,sign,public_key)   #验签

        return response_data