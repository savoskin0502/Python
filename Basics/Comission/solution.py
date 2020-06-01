
class Value:

    def __init__(self):
        self.value = None

    @staticmethod
    def _take_commission(value, commission):
        return (1 - commission) * value

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._take_commission(value, commission=obj.commission)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission
