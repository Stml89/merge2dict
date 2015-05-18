#__author__ = 'stml'
#!/usr/bin/env python

a = { 'a': 1,
      'b': 2,
      'c': 3
      }

b = { 'c': 3,
      'd': 4,
      'e': 5
      }

class Dict:

    def check_rezult(self, dict_for_check):
        ab = {'a': [1, None], 'b': [2, None], \
            'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

        if (dict_for_check != ab):
            return False
        else:
            return True

    def merge_two_dicts(self, x, y):
        return dict((k, [x.get(k), y.get(k)])
                    for k in set(x.keys() + y.keys()))

if __name__ == "__main__":
    object_dict = Dict()
    temp_dict = object_dict.merge_two_dicts(a, b)
    result = object_dict.check_rezult(temp_dict)
    if result:
        print "pass"
    else:
        print "false"