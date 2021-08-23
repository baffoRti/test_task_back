from django.http import JsonResponse

from xml.etree import ElementTree
import xmltodict
import json
import requests

file = open("static/XML_data.asp")
new_json = xmltodict.parse(file.read())
json.dumps(new_json)


def parent_code_by_code(code):
    for item in new_json["Valuta"]["Item"]:
        if item['ISO_Char_Code'] == code:
            return item['ParentCode']


def Method_A(request):
    return JsonResponse(new_json["Valuta"])


def Method_B(request, code, date_1, date_2):
    new_date_1 = date_1[-2:] + '/' + date_1[-5:-3] + '/' + date_1[0:4]
    new_date_2 = date_2[-2:] + '/' + date_2[-5:-3] + '/' + date_2[0:4]
    parent_code = parent_code_by_code(code)
    response = requests.post(
        f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={new_date_1}&date_req2={new_date_2}&VAL_NM_RQ={parent_code}")
    xml_text = ElementTree.fromstring(response.content)
    json_data = {
        "date_1": f"{xml_text[0][1].text.replace(',', '.')[:5]}",
        "date_2": f"{xml_text[-1][1].text.replace(',', '.')[:5]}",
        "diff": f"{round((float(xml_text[-1][1].text.replace(',', '.')) - float(xml_text[0][1].text.replace(',', '.'))), 2)}"
    }
    json.dumps(json_data)
    return JsonResponse(json_data)
