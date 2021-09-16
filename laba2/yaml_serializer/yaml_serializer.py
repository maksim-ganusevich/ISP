import inspect
import builtins
from additional.additional import convert, deconvert


class Yaml:
    def __init__(self):
        self.pos = 0
        self.nums = [str(i) for i in range(10)]

    def dumps(self, obj):
        return self.to_str(convert(obj))

    def dump(self, obj, fp):
        with open(fp, 'w+') as f:
            f.write(self.dumps(obj))

    def to_str(self, obj, name='', tab = ''):
        if isinstance(obj, (int, float, str, bool, type(None))):
            return self.to_str_primitive(obj, name, tab)
        if isinstance(obj, (list, tuple, set)):
            return self.to_str_collection(obj, name, tab)
        if isinstance(obj, dict):
            return self.to_str_dict(obj, name, tab)

    def to_str_primitive(self, obj, name, tab):
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
            res += f'{obj}'
        return res

    def to_str_collection(self, obj, name, tab):
        res = ''
        if len(name):
            res += f'{name}:\n'
        res += tab + '- '+ f"'__{type(obj).__name__}__'"+ '\n'
        for x in obj:
            if isinstance(x, str):
                res += tab + '- '+ f"'{self.to_str(x)}'" + '\n'
            else:
                res += tab + '- '+ self.to_str(x) + '\n'
        return res

    def to_str_dict(self, obj, name, tab):
        res = ''
        if len(name):
            res += f'{name}:'
            if obj == {}:
                res += ' {}\n'
                return res 
            res += '\n'
            tab += '  '
        for k, v in obj.items():
            res += tab + self.to_str(v, self.to_str(str(k)), tab)
            if res[-1] != '\n':
                res += '\n'    
        return res
