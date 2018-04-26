# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import json
import pandas as pd

ret = {}
data_exporter = []
data_line = []
exporter = pd.read_csv('data/port.csv')
for i in range(len(exporter)):
    data_exporter.append({"name": str(exporter.ix[i][0]).rstrip(), "value": exporter.ix[i][2]})
    data_line.append([{"name": str(exporter.ix[i][0]).rstrip()}, {"name": str(exporter.ix[i][1]).rstrip(),\
                                                                  "value": exporter.ix[i][2]}])

data_geo = {}
geo = pd.read_csv('data/geo.csv')
for i in range(len(geo)):
    data_geo[str(geo.ix[i][0]).rstrip()] = [geo.ix[i][1], geo.ix[i][2]]

ret['markPoint'] = data_exporter
ret['geo'] = data_geo
ret['line'] = data_line

data_amount_ex = []
amount_ex = pd.read_csv('data/amount_ex.csv')
for i in range(len(amount_ex)):
    data_amount_ex.append({'name': str(amount_ex.ix[i][0]).rstrip().title().replace(' Of ', ' of ')\
                       .replace(' The ', ' the ').replace(' And ', ' and '), "value": amount_ex.ix[i][1]})


data_amount_im = []
amount_im = pd.read_csv('data/amount_im.csv')
for i in range(len(amount_im)):
    data_amount_im.append({'name': str(amount_im.ix[i][0]).rstrip().title().replace(' Of ', ' of ')\
                       .replace(' The ', ' the ').replace(' And ', ' and '), "value": amount_im.ix[i][1]})


def index(request):
    print ret['geo']
    return render(request, 'index.html')


def top_ten_taxons(request):
    return render(request, 'line_chart.html')


# def home(request):
#     return render(request, 'home.html')
#
#
# def trade_country_map(request):
#     return render(request, 'trade_country_map.html')
#
#
# def map_live(request):
#     return render(request, 'map_live.html')
#
#
# def map_import(request):
#     return render(request, 'map_import.html')
#
#
# def map_export(request):
#     return render(request, 'map_export.html')


def load_live_map(request):
    return HttpResponse(json.dumps(ret), content_type='application/json')


def load_export_map(request):
    return HttpResponse(json.dumps(data_amount_ex), content_type='application/json')


def load_import_map(request):
    return HttpResponse(json.dumps(data_amount_im), content_type='application/json')