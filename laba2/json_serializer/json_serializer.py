import inspect
import builtins
from additional.additional import convert, deconvert


class Json:
    def __init__(self):
        self.pos = 0
        self.nums = [str(i) for i in range(10)]

    def dumps(self, obj):
        return self.to_str(convert(obj))

    def dump(self, obj, fp):
        with open(fp, 'w+') as f:
            f.write(self.dumps(obj))

    def to_str(self, obj, name=''):
        if isinstance(obj, (int, float, str, bool, type(None))):
            return self.to_str_primitive(obj, name)
        if isinstance(obj, (list, tuple, set)):
            return self.to_str_collection(obj, name)
        if isinstance(obj, dict):
            return self.to_str_dict(obj, name)
        return self.to_str_class_obj(obj, name)

    def to_str_primitive(self, obj, name):
        res = ''
        if  name != '':
            res += f'{name}: '        
        if obj is None:
            res += 'null'
        elif isinstance(obj, bool):
            res += 'true' if obj else 'false'
        elif isinstance(obj, (int, float)):
            res += str(obj)
        elif isinstance(obj, str):
            res += f'"{obj}"'
        return res

    def to_str_collection(self, obj, name):
        res = ''
        if len(name):
            res += f'{name}: '
        res += '[' + f'"__{type(obj).__name__}__", '
        for x in obj:
            res += self.to_str(x) + ', '
        if len(res) > 2 and res[-2] == ',':
            res = res[:-2]
        res += ']'
        return res

    def to_str_dict(self, obj, name):
        res = ''
        if len(name):
            res += f'{name}: '
        res += '{'
        for k, v in obj.items():
            res += self.to_str(v, self.to_str(str(k))) + ', '        
        if len(res) > 2 and res[-2] == ',':
            res = res[:-2]
            self.pos -= 2
        res += '}'
        self.pos += 2
        return res
    
    