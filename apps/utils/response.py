"""
常用的Response以及Django的Response、DRF的Response
"""
from django.http.response import DjangoJSONEncoder, JsonResponse


class OpDRFJSONEncoder(DjangoJSONEncoder):
    """
    重寫DjangoJSONEncoder
    (1)默認返回支持中文格式的json字串
    """

    def __init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False,
                 indent=None, separators=None, default=None):
        super().__init__(skipkeys=skipkeys, ensure_ascii=False, check_circular=check_circular,
                         allow_nan=allow_nan, sort_keys=sort_keys, indent=indent, separators=separators,
                         default=default)


class SuccessJsonResponse(JsonResponse):
    """
    標準JsonResponse, SuccessJsonResponse(data)SuccessJsonResponse(data=data)
    (1)僅SuccessResponse無法使用時才能推薦使用SuccessJsonResponse
    """

    def __init__(self, data, msg='success', encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs):
        std_data = {
            "code": 200,
            "data": data,
            "msg": msg,
            "status": 'success'
        }
        super().__init__(std_data, encoder, safe, json_dumps_params, **kwargs)


class ErrorJsonResponse(JsonResponse):
    """
    標準JsonResponse, 僅ErrorResponse無法使用時才能使用ErrorJsonResponse
    (1)默認錯誤碼返回2001, 也可以指定其他返回碼:ErrorJsonResponse(code=xxx)
    """

    def __init__(self, data, msg='error', code=201, encoder=OpDRFJSONEncoder, safe=True, json_dumps_params=None,
                 **kwargs):
        std_data = {
            "code": code,
            "data": data,
            "msg": msg,
            "status": 'error'
        }
        super().__init__(std_data, encoder, safe, json_dumps_params, **kwargs)
