class LocaleEnum:

    LANGUAGE = {
        'ZH_CN': ('zh-CN', '中文简体'),
        'ZH_TW': ("zh-TW", "中文繁体"),
        'EN_US': ("en-US", "英文"),
        'JA_JP': ("ja-JP", "日文")
    }

    def getLocale(self):

        return self.LANGUAGE['ZH_CN'][0]