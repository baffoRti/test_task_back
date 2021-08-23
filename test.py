# import xmltodict
# import json
#
# file = open("static/XML_data.asp")
# new_json = xmltodict.parse(file.read())
# json.dumps(new_json)
#
#
# def parent_code_by_code(code):
#     for item in new_json["Valuta"]["Item"]:
#         if item['ISO_Char_Code'] == code:
#             return item['ParentCode']
#
#
# print(parent_code_by_code("USD"))
date_1 = "2001-03-14"
new_date_1 = date_1[-2:] + '/' + date_1[-5:-3] + '/' + date_1[0:4]
print(new_date_1)
