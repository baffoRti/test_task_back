from django.http import JsonResponse, HttpResponse

from xml.etree import ElementTree
import xmltodict
import json
import requests
from datetime import datetime

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
    try:
        date_1_obj = datetime.strptime(date_1, "%Y-%m-%d")
    except ValueError:
        return HttpResponse("Request error")
    try:
        date_2_obj = datetime.strptime(date_2, "%Y-%m-%d")
    except ValueError:
        return HttpResponse("Request error")
    if date_1_obj > date_2_obj:
        return HttpResponse("Request error")
    new_date_1 = date_1_obj.strftime("%d/%m/%Y")
    new_date_2 = date_2_obj.strftime("%d/%m/%Y")
    parent_code = parent_code_by_code(code)
    response = requests.post(
        f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={new_date_1}&date_req2={new_date_2}&VAL_NM_RQ={parent_code}")
    xml_text = ElementTree.fromstring(response.content)
    if len(xml_text) == 0:
        return HttpResponse("Request error")
    json_data = {
        "date_1": f"{xml_text[0][1].text.replace(',', '.')[:5]}",
        "date_2": f"{xml_text[-1][1].text.replace(',', '.')[:5]}",
        "diff": f"{round((float(xml_text[-1][1].text.replace(',', '.')) - float(xml_text[0][1].text.replace(',', '.'))), 2)}"
    }
    json.dumps(json_data)
    return JsonResponse(json_data)
