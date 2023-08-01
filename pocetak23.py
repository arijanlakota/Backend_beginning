#json
#1
import json
# pyDict = json.loads('{ "Name":"David", "Class":"I", "Age":6 }')
# print(pyDict)
#2
# pythonObject = {"elvedin":1,"arijan":2}
# jsonObject = json.dumps(pythonObject)
#3
# pythonObject = {"hasan":1,"suvo":1}
# jsonObject = json.dumps(pythonObject)
# print(type(jsonObject))
#4
# pythonObject = {
#     'wow':
#     {"yeah":
#      {"cool":
#       {"bro":{
#           "shu":2
#       }}
#       }
#     }
# }
# jsonObject = json.dumps(pythonObject,indent=4,sort_keys=True)
# print(jsonObject)
#5
# jsonObject='{"name": "David", "age": 6, "class": "I"}'
# pythonObject = json.loads(jsonObject)
# print(pythonObject)
#6
# oldFile = open('sample1.json','r')
# jsonObject = oldFile.read()
# pythonObject = json.loads(jsonObject)
# newWile = open('newJSON.json','w')
# newJSobject = json.dumps(pythonObject)
# newWile.write(newJSobject)
#7
# def encode_complex(object):
#     # check using isinstance method
#     if isinstance(object, complex):
#         return [object.real, object.imag]
#     # raised error if object is not complex
#     raise TypeError(repr(object) + " is not JSON serialized")
#8
# def is_complex_num(objct):
#     if '__complex__' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct
# jsonObject = '{"__complex__":true, "real":2 ,"img":5}'
# pythonObject = json.loads(jsonObject,object_hook=is_complex_num)
# print(pythonObject)
#9
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
jsonObject = json.loads(python_obj)
print(jsonObject)
