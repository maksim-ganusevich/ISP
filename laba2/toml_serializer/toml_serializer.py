import inspect
import builtins
from additional.additional import convert, deconvert

class Toml():
    def __init__(self):
        self.pos = 0
        self.nums = [str(i) for i in range(10)]
        self.depth = 0

    def dumps(self, obj):
        r = convert(obj)
        return self.to_str(r)

    def dump(self, obj, fp):
        with open(fp, 'w+') as f:
            f.write(self.dumps(obj))

    def to_str(self, obj, name='', path=''):
        if isinstance(obj, (int, float, str, bool, type(None))):
            return self.to_str_primitive(obj, name)
        if isinstance(obj, (list, tuple, set)):
            return self.to_str_collection(obj, name)
        if isinstance(obj, dict):
            return self.to_str_dict(obj, name, path)

    def to_str_primitive(self, obj, name):
        res = ''
        if  name != '':
            res += f'{name} = '        
        if obj is None:
            res += 'null'
        elif isinstance(obj, bool):
            res += 'true' if obj else 'false'
        elif isinstance(obj, (int, float)):
            res += str(obj)
        elif isinstance(obj, str):
            if name == '':
                res += f'{obj}'
            else:
                res += f'"{obj}"'
        return res

    def to_str_collection(self, obj, name):
        res = ''
        if len(name):                    
            res += f'{name} = '
        res += '[ ' + f'"__{type(obj).__name__}__", '    
        for x in obj:
            if isinstance(x, str): 
                res += ' '+ f'"{self.to_str(x)}"' + ','
            else:
                res += ' '+ self.to_str(x) + ','
        res += ']\n'
        return res

    def to_str_dict(self, obj, name, path):
        res = ''
        if len(name):
            if path == '':
                path += name
            else:
                path += '.' + name
            if res[-2:] == '\n\n':
                res += f'[{path}]\n'
            else:
                res += f'\n[{path}]\n'
            if obj == {}:
                return res 

        for k, v in obj.items():
            if res[-2:] == '\n\n' and path != '':
                res += f'[{path}]\n'
            new_res = self.to_str(v, self.to_str(str(k)), path)
            res += new_res
            if res[-1] != '\n':
                res += '\n'
        if res[-2:] != '\n\n':
            res += '\n'
        return res
