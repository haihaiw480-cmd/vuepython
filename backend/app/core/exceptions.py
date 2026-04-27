class BizException(Exception):
    def __init__(self, code=400, msg="error"):
        self.code = code
        self.msg = msg
