import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from collections import Counter
from django.shortcuts import redirect
from .models import *
import tushare as ts
import pandas as pd
import numpy as np
import json
import re
# Create your views here.
def toLogin_view(request):
    return render(request,'login.html')
def Login_view(request):
    u=request.GET.get("user",'')
    p=request.GET.get("pwd", '')
    if u and p:
        c= StudentInfo.objects.filter(stu_name=u,stu_psw=p).count()
        if c>=1: return HttpResponse("login sucessfully")
        else: return HttpResponse("wrong password")
    else:
        return HttpResponse("login fail")
def toregister_view(request):
    return render(request,'register.html')
def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    if u and p:
        stu=StudentInfo(stu_id=str(random.randrange(1111,9999)),stu_name=u,stu_psw=p)
        stu.save()
        return HttpResponse("register sucessfully")
    else:
        return HttpResponse("Please enter name and passwords")

def chart_view(request):
    return render(request,'chart.html')

def stock_data(request):
        ts.set_token('cf2fafdae440b51e0cd2f2aef9eb7481bae441a0bc6b22f599c13752')
        pro = ts.pro_api()
        ts_code = request.GET.get('ts_code', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        # check
        if ts_code and start_date and end_date:
            data = pro.fund_portfolio(
                ts_code=ts_code,
                start_date=start_date,
                end_date=end_date,
                fields='mkv,amount,stk_mkv_ratio,ann_date'
            )
        else:
            return JsonResponse({'error': 'Missing parameters'}, safe=False)
        data_dict = data.to_dict('records')
        result = []
        for item in data_dict:
            result.append({
                'mkv': item['mkv'],
                'amount': item['amount'],
                'stk_mkv_ratio': item['stk_mkv_ratio'],
                'ann_date': item['ann_date']
            })
        data_json = json.dumps(result)
        return JsonResponse(data_json, safe=False)

def code_data2(request):
    last_row_id = code.get_last_row_id()
    last_row_id2 = newresult.get_last_row_id()
    if last_row_id:
        last_row = code.objects.get(id=last_row_id)
        newresult_row = newresult.objects.get(id=last_row_id2)  # 假设newresult对象的id与code对象的id相同
        code_content = {
            'code1Content': last_row.code1Content,
            'code2Content': last_row.code2Content,
            'code3Content': last_row.code3Content,
            'code4Content': last_row.code4Content,
            'code5Content': last_row.code5Content,
            'code6Content': last_row.code6Content,
            'code7Content': last_row.code7Content,
            'code8Content': last_row.code8Content,
            'code9Content': last_row.code9Content,
            'code10Content': last_row.code10Content,
            'begin_score': newresult_row.begin_score,
            'end_score': newresult_row.end_score
        }
        return JsonResponse(code_content)


def code_data(request):
    last_row_id = code.get_last_row_id()
    if last_row_id:
        last_row = code.objects.get(id=last_row_id)
        code_content = {
            'code1Content': last_row.code1Content,
            'code2Content': last_row.code2Content,
            'code3Content': last_row.code3Content,
            'code4Content': last_row.code4Content,
            'code5Content': last_row.code5Content,
            'code6Content': last_row.code6Content,
            'code7Content': last_row.code7Content,
            'code8Content': last_row.code8Content,
            'code9Content': last_row.code9Content,
            'code10Content': last_row.code10Content
        }
        return JsonResponse(code_content)




def stock_chart(request):
    return render(request,'stock_data.html')

def get_data(request):
    goods = sale.objects.all()
    data = []
    for g in goods:
        data.append({
            'goodsA': g.goodsA,
            'goods1': g.goods1,
            'goodsB': g.goodsB,
            'goods2': g.goods2
        })
    return JsonResponse(data, safe=False)
def test(request):
    return render(request,'test.html')
def drag(request):
    return render(request,'drag.html')
def Rresult(request):
    return render(request,'Rresult.html')
def resultmatch(request):
    return render(request,'resultmatch.html')
def wait(request):
    return render(request,'wait.html')
def wait2(request):
    return render(request,'wait2.html')
def match2(request):
    return render(request,'match2.html')
def match(request):
    return render(request,'match.html')
def view_s(request):
    ranking1_instance = Newrank()
    last_row_id = Newrank.objects.get_last_row_id()
    if last_row_id:
        last_row = Newrank.objects.get(id=last_row_id)
        droppable1Content = last_row.droppable1Content
        droppable2Content = last_row.droppable2Content
        droppable3Content = last_row.droppable3Content
        response = '成功拖拽的标签1：{},成功2：{},成功3：{}'.format(droppable1Content, droppable2Content, droppable3Content)
    else:
        response = '没有找到数据'
    ranking1_instance = Newrank()
    count = ranking1_instance.count_non_empty_values()
    weights = ranking1_instance.calculate_weights(count)
    return HttpResponse(response)

def your_view(request):
    ranking_instance = Newrank()
    data = list(Newmark7.objects.values( 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12','x13', 'x14', 'x15','x16','x17', 'x18', 'x19'))
    column_names = ['x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15','x16','x17', 'x18', 'x19']
    fund_data = pd.DataFrame(data, columns=column_names)
    last_row_id =Newrank.objects.get_last_row_id()
    if last_row_id:
        last_row = Newrank.objects.get(id=last_row_id)
        droppable_content = {
            'droppable1Content': last_row.droppable1Content,
            'droppable2Content': last_row.droppable2Content,
            'droppable3Content': last_row.droppable3Content,
            'droppable4Content': last_row.droppable4Content,
            'droppable5Content': last_row.droppable5Content,
            'droppable6Content': last_row.droppable6Content,
            'droppable7Content': last_row.droppable7Content,
            'droppable8Content': last_row.droppable8Content,
            'droppable9Content': last_row.droppable9Content,
            'droppable10Content': last_row.droppable10Content,
        }
    variables = {
        'class1Content': None,
        'class2Content': None,
        'class3Content': None,
        'class4Content': None,
        'class5Content': None,
        'class6Content': None,
        'class7Content': None,
        'class8Content': None,
        'class9Content': None,
        'class10Content': None,
        'class11Content': None,
        'class12Content': None,
        'class13Content': None,
        'class14Content': None
    }
    values = []
    for i in range(10):
        if(droppable_content[f'droppable{i + 1}Content']):
            variables[f'class{i+1}Content'] = droppable_content[f'droppable{i + 1}Content'].split(',')
            values.extend(variables[f'class{i+1}Content'])
        else:
            continue
    variables = {
        'class1Content': None,
        'class2Content': None,
        'class3Content': None,
        'class4Content': None,
        'class5Content': None,
        'class6Content': None,
        'class7Content': None,
        'class8Content': None,
        'class9Content': None,
        'class10Content': None,
        'class11Content': None,
        'class12Content': None,
        'class13Content': None,
        'class14Content': None
    }

    for i in range(len(values)):
        variables[f'class{i + 1}Content']=values[i]
    length=len(values)
    values2 = []
    column_indices = []
    # index = [['x2'], ['x3'], ['x8'], ['x5'], ['x9'], ['x12']]
    index = ['x2', 'x3', 'x8', 'x5', 'x9', 'x12']
    if length < 6:
        for i in range(length):
            if variables.get(f'class{i+1}Content') in index:
                index.remove(variables[f'class{i+1}Content'])
        for i in range(6 - length):
            k = length + i + 1
            variables[f'class{k}Content'] = index[i]
        for i in range(len(variables)):
            if variables[f'class{i+1}Content'] in column_names:
                column_indices.append(column_names.index(variables[f'class{i+1}Content']))
        k = 0
        for i in range(6):
            if droppable_content[f'droppable{i+1}Content']:
                continue
            else:
                droppable_content[f'droppable{i+1}Content'] = variables[f'class{length + k + 1}Content']
                k=k+1
    if length >= 6:
        for value in values:
            if value in column_names:
                column_indices.append(column_names.index(value))
    weights = []
    total_weight = 0.0
    num_commas = {}
    for i in range(10):
        content = droppable_content[f'droppable{i + 1}Content']
        if content is not None and content != '':
            num_commas[i] = content.count(',')
        else:
            pass
    for i in range(10):
        if droppable_content[f'droppable{i + 1}Content'] is not None and droppable_content[f'droppable{i + 1}Content'] !='':
            if num_commas[i] != 0:
                weight = 1 / (i + 1)
                for _ in range(num_commas[i] + 1):
                    weights.append(weight)
                    total_weight += weight
            elif num_commas[i] == 0:
                weight = 1 / (i + 1)
                weights.append(weight)
                total_weight += weight
    weights = [w / total_weight for w in weights]
    weights = np.array(weights)
    weights = weights.reshape(1, -1)
    original_columns = fund_data.columns
        # 根据column_indices选择对应的列名
    selected_columns = original_columns[column_indices]
    selected_columns = np.array(fund_data[selected_columns])
    selected_columns = selected_columns.astype(float)
    weight_data=selected_columns*weights
    weight_data=  weight_data.astype(float)
    scores = np.sum(weight_data, axis=1)
    sorted_scores = np.sort(scores)
    score_value = np.partition(sorted_scores, -11)[-11]  # 选择前十最大的分值作为score_value
    filtered_data = fund_data[scores >= score_value]['x15']
    dict_data = filtered_data.to_dict()

    code_content = {
        'code1Content': None,
        'code2Content': None,
        'code3Content': None,
        'code4Content': None,
        'code5Content': None,
        'code6Content': None,
        'code7Content': None,
        'code8Content': None,
        'code9Content': None,
        'code10Content': None,
    }
    value = {}
    for i in range(len(dict_data)):
        value[i] = list(dict_data.values())[i]
    for i in range(len(value)):
        if value[i]:
            code_content[f"code{i + 1}Content"] = value[i]
    code_data = code(code1Content=code_content['code1Content'], code2Content=code_content['code2Content'],
                     code3Content=code_content['code3Content'], code4Content=code_content['code4Content'],
                     code5Content=code_content['code5Content'], code6Content=code_content['code6Content'],
                     code7Content=code_content['code7Content'], code8Content=code_content['code8Content'],
                     code9Content=code_content['code9Content'], code10Content=code_content['code10Content'])

    code_data.save()
    score_value2 = np.partition(sorted_scores, -1)[-1]
    score_data=newresult(end_score=score_value,begin_score=score_value2)
    score_data.save()

    response = '非空数量：{},非空数量：{},非空数量：{}'.format(score_value,fund_data,code_content['code1Content'])
    return HttpResponse(response)

def extract_content(request):
    if request.method == 'POST':
        droppable_content = {
            'droppable1Content': request.POST.get('droppable1Content'),
            'droppable2Content': request.POST.get('droppable2Content'),
            'droppable3Content': request.POST.get('droppable3Content'),
            'droppable4Content': request.POST.get('droppable4Content'),
            'droppable5Content': request.POST.get('droppable5Content'),
            'droppable6Content': request.POST.get('droppable6Content'),
            'droppable7Content': request.POST.get('droppable7Content'),
            'droppable8Content': request.POST.get('droppable8Content'),
            'droppable9Content': request.POST.get('droppable9Content'),
            'droppable10Content': request.POST.get('droppable10Content'),
        }
        transformed_content_list = []
        for i in range(9):
            if droppable_content[f'droppable{i + 1}Content']:
                content_list = droppable_content[f'droppable{i + 1}Content'].split(',')
                transformed_content_list.clear()
                for content in content_list:
                    if content == 'fund scale':
                        transformed_content_list.append('x2')
                    elif content == 'Accumulated unit net value':
                        transformed_content_list.append('x3')
                    elif content == 'The average number of products managed per fund manager (large)':
                        transformed_content_list.append('x4')
                    elif content == 'Jensen':
                        transformed_content_list.append('x5')
                    elif content == 'Investment style (mature)':
                        transformed_content_list.append('x6')
                    elif content == 'Education level':
                        transformed_content_list.append('x7')
                    elif content == 'Treynor':
                        transformed_content_list.append('x8')
                    elif content == 'Sharpe':
                        transformed_content_list.append('x9')
                    elif content == 'Shareholders equity at the beginning of the period':
                        transformed_content_list.append('x10')
                    elif content == 'Shareholders equity at the end of the period':
                        transformed_content_list.append('x11')
                    elif content == 'Fund shares (large)':
                        transformed_content_list.append('x12')
                    elif content == 'The average tenure of fund managers (high)':
                        transformed_content_list.append('x13')
                    elif content == 'Team stability':
                        transformed_content_list.append('x14')
                    elif content == 'The average number of products managed per fund manager (small)':
                        transformed_content_list.append('x16')
                    elif content == 'Investment style (conservative)':
                        transformed_content_list.append('x17')
                    elif content == 'Fund shares (small)':
                        transformed_content_list.append('x18')
                    elif content == 'The average tenure of fund managers (low)':
                        transformed_content_list.append('x19')
                droppable_content[f'droppable{i + 1}Content'] = ','.join(transformed_content_list)
            else:
                continue

        ranking1_object = Newrank(droppable1Content=droppable_content['droppable1Content'],
                                  droppable2Content=droppable_content['droppable2Content'],
                                  droppable3Content=droppable_content['droppable3Content'],
                                  droppable4Content=droppable_content['droppable4Content'],
                                  droppable5Content=droppable_content['droppable5Content'],
                                  droppable6Content=droppable_content['droppable6Content'],
                                  droppable7Content=droppable_content['droppable7Content'],
                                  droppable8Content=droppable_content['droppable8Content'],
                                  droppable9Content=droppable_content['droppable9Content'],
                                  droppable10Content=droppable_content['droppable10Content'])

        ranking1_object.save()
        your_view(request)
        # 在这里处理接收到的表单数据
        # response = '非空数量：{},'.format(droppable_content['droppableContent'])
        # return HttpResponse(response)
        return redirect('/polls/wait/')
    return HttpResponse('error')

def match_data(request):
    if request.method == 'POST':
        match_content = {
            'match1Content': request.POST.get('match1Content'),
            'match2Content': request.POST.get('match2Content'),
            'match3Content': request.POST.get('match3Content'),
            'match4Content': request.POST.get('match4Content'),
            'match5Content': request.POST.get('match5Content'),
            'match6Content': request.POST.get('match6Content'),
            'match7Content': request.POST.get('match7Content'),
            'match8Content': request.POST.get('match8Content'),
            'match9Content': request.POST.get('match9Content'),
            'match10Content': request.POST.get('match10Content'),
        }
        for i in range(10):
            if match_content[f'match{i + 1}Content']:
                if match_content[f'match{i + 1}Content'] == 'fund scale':
                    match_content[f'match{i + 1}Content'] = 'x2'
                elif match_content[f'match{i + 1}Content'] == 'Accumulated unit net value':
                    match_content[f'match{i + 1}Content'] = 'x3'
                elif match_content[f'match{i + 1}Content'] == 'The average number of products managed per fund manager':
                    match_content[f'match{i + 1}Content'] = 'x4'
                elif match_content[f'match{i + 1}Content'] == 'Jensen':
                    match_content[f'match{i + 1}Content'] = 'x5'
                elif match_content[f'match{i + 1}Content'] == 'Investment style':
                    match_content[f'match{i + 1}Content'] = 'x6'
                elif match_content[f'match{i + 1}Content'] == 'Education level':
                    match_content[f'match{i + 1}Content'] = 'x7'
                elif match_content[f'match{i + 1}Content'] == 'Treynor':
                    match_content[f'match{i + 1}Content'] = 'x8'
                elif match_content[f'match{i + 1}Content'] == 'Sharpe':
                    match_content[f'match{i + 1}Content'] = 'x9'
                elif match_content[f'match{i + 1}Content'] == 'Shareholders equity at the beginning of the period':
                    match_content[f'match{i + 1}Content'] = 'x10'
                elif match_content[f'match{i + 1}Content'] == 'Shareholders equity at the end of the period':
                    match_content[f'match{i + 1}Content'] = 'x11'
                elif match_content[f'match{i + 1}Content'] == 'Fund shares':
                    match_content[f'match{i + 1}Content'] = 'x12'
                elif match_content[f'match{i + 1}Content'] == 'The average tenure of fund managers':
                    match_content[f'match{i + 1}Content'] = 'x13'
                elif match_content[f'match{i + 1}Content'] == 'Team stability':
                    match_content[f'match{i + 1}Content'] = 'x14'
            else:
                continue
        level1Content = request.POST.get('level1Content')
        level2Content = request.POST.get('level2Content')
        level3Content = request.POST.get('level3Content')
        level4Content = request.POST.get('level4Content')
        level5Content = request.POST.get('level5Content')
        level6Content = request.POST.get('level6Content')
        level7Content = request.POST.get('level7Content')
        level8Content = request.POST.get('level8Content')
        level9Content = request.POST.get('level9Content')
        level10Content = request.POST.get('level10Content')

        match_object = Newmatch(match1Content=match_content['match1Content'], match2Content=match_content['match2Content'],
                               match3Content=match_content['match3Content'], level1Content=level1Content,
                               level2Content=level2Content, level3Content=level3Content,
                               match4Content=match_content['match4Content'], match5Content=match_content['match5Content'],
                               match6Content=match_content['match6Content'], match7Content=match_content['match7Content'],
                               match8Content=match_content['match8Content'], match9Content=match_content['match9Content'],
                               match10Content=match_content['match10Content'], level4Content=level4Content,
                               level5Content=level5Content, level6Content=level6Content,
                               level7Content=level7Content, level8Content=level8Content,
                               level9Content=level9Content, level10Content=level10Content)

        match_object.save()
        # response = '非空数量：{},'.format(match_content['match3Content'])
        # return HttpResponse(response)
        # 在这里处理接收到的表单数据
        match_views(request)

        return redirect('/polls/wait2/')
    return HttpResponse('error')

def match_views(request):
    last_row_id = Newmatch.get_last_row_id()
    if last_row_id:
        last_row = Newmatch.objects.get(id=last_row_id)
        match_content = {
            'match1Content': last_row.match1Content,
            'match2Content': last_row.match2Content,
            'match3Content': last_row.match3Content,
            'match4Content': last_row.match4Content,
            'match5Content': last_row.match5Content,
            'match6Content': last_row.match6Content,
            'match7Content': last_row.match7Content,
            'match8Content': last_row.match8Content,
            'match9Content': last_row.match9Content,
            'match10Content': last_row.match10Content
        }
        level_content = {
            'level1Content': last_row.level1Content,
            'level2Content': last_row.level2Content,
            'level3Content': last_row.level3Content,
            'level4Content': last_row.level4Content,
            'level5Content': last_row.level5Content,
            'level6Content': last_row.level6Content,
            'level7Content': last_row.level7Content,
            'level8Content': last_row.level8Content,
            'level9Content': last_row.level9Content,
            'level10Content': last_row.level10Content
        }
        empty_count = sum(value == '' for value in match_content.values())
        length=10-empty_count
        variables = {
            'class1Content': None,
            'class2Content': None,
            'class3Content': None,
            'class4Content': None,
            'class5Content': None,
            'class6Content': None,
            'class7Content': None,
            'class8Content': None,
            'class9Content': None,
            'class10Content': None,
            'class11Content': None,
            'class12Content': None,
            'class13Content': None,
            'class14Content': None
        }
        if length < 6:
            index = ['x5', 'x4', 'x3', 'x10', 'x8', 'x12','x14']
            level = ['2', '4', '5', '3', '2', '5','4']
            for i in range(length):
                match_value = match_content[f'match{i + 1}Content']
                if match_value in index:  # 如果match的值存在于level列表中
                    removed_index = index.index(match_value)
                    index.remove(match_value)
                    level.pop(removed_index)
                else:
                    pass
            for i in range(6 - length):
                k = length + i + 1
                match_content[f'match{k}Content'] = index[i]
                level_content[f'level{k}Content'] = level[i]
        else:
            pass
        empty_count = sum(value == '' for value in match_content.values())
        length = 10 - empty_count
        for i in range(length+1):
            match_value = match_content[f'match{i + 1}Content']
            if match_value == 'x2':
                variables[f'class{i + 1}Content'] = 5
            elif match_value == 'x3':
                variables[f'class{i + 1}Content'] = 5
            elif match_value == 'x4':
                variables[f'class{i + 1}Content'] = 4
            elif match_value == 'x5':
                variables[f'class{i + 1}Content'] = 2
            elif match_value == 'x6':
                variables[f'class{i + 1}Content'] = 2
            elif match_value == 'x7':
                variables[f'class{i + 1}Content'] = 3
            elif match_value == 'x8':
                variables[f'class{i + 1}Content'] = 2
            elif match_value == 'x9':
                variables[f'class{i + 1}Content'] = 2
            elif match_value == 'x10':
                variables[f'class{i + 1}Content'] = 3
            elif match_value == 'x11':
                variables[f'class{i + 1}Content'] = 3
            elif match_value == 'x12':
                variables[f'class{i + 1}Content'] = 5
            elif match_value == 'x13':
                variables[f'class{i + 1}Content'] = 4
            elif match_value == 'x14':
                variables[f'class{i + 1}Content'] = 4

        data = list(
            score.objects.values('x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13',
                                 'x14', 'x15'))
        store={}
        for i in range(length):
            match_value = match_content[f'match{i + 1}Content']
            data = pd.DataFrame(data)
            result1 = [None, None]
            result1[0] = data[match_value].tolist()
            result1[1] = data['x1'].tolist()
            sorted_result1 = [list(x) for x in zip(*sorted(zip(result1[0], result1[1])))]
            sorted_result1 = np.array(sorted_result1)
            denominator = int(variables[f'class{i + 1}Content'])
            k = 19254 // denominator
            lenx = int(level_content[f'level{i + 1}Content'])
            if lenx == 1:
                begin = 0
                end = 0 + k
            elif lenx == 2:
                begin = k
                end = 2 * k
            else:
                begin = (lenx - 1) * k
                end = lenx * k
            selected_split1 = sorted_result1[:, begin:end]
            if i<2:
                index=0
            elif i>4:
                index=0
            else:
                index=1
            store[i]=selected_split1[1]

        # common_values=set(store[0])
        # for key in range(len(store)):
        #     for i in range(len(store[key])):
        #         store[key][i] = int(store[key][i])
        # common_values = set(store[0])
        # common_values1 = common_values.intersection(set(store[1]))
        # result3=len(common_values1)
        common_values = set(store[0])
        for i in range(1,len(store)):
            common_values = common_values.intersection(set(store[i]))  # 依次与后面的列求交集
        result1 = len(common_values)

        common_values = set(store[0])
        for i in range(1, len(store)):
            common_values = common_values.intersection(set(store[i]))  # 依次与后面的列求交集
            counter = Counter(common_values)
            counter_keys, counter_values = zip(*counter.items())
        counter = Counter(common_values)
        result2 = counter.most_common(10)  # 获取频次最高的前10个元素

        xfit = data['x15']
        value={}
        for i in range(len(counter_keys)):
            k=int(counter_keys[i])-1
            value[i] = xfit[k]
        m=int(counter_keys[0])-1

        code_content = {
            'code1Content': None,
            'code2Content': None,
            'code3Content': None,
            'code4Content': None,
            'code5Content': None,
            'code6Content': None,
            'code7Content': None,
            'code8Content': None,
            'code9Content': None,
            'code10Content': None,
        }

        for i in range(len(value)):
            if value[i]:
                 code_content[f"code{i + 1}Content"]=value[i]
            else:
                continue

        code_data = code(code1Content=code_content['code1Content'], code2Content=code_content['code2Content'],
                         code3Content=code_content['code3Content'], code4Content=code_content['code4Content'],
                         code5Content=code_content['code5Content'], code6Content=code_content['code6Content'],
                         code7Content=code_content['code7Content'], code8Content=code_content['code8Content'],
                         code9Content=code_content['code9Content'], code10Content=code_content['code10Content'])

        code_data.save()
        response = '非空数量：{},非空数量：{},非空数量：{}'.format(value,counter_keys,code_content['code9Content'])

        return HttpResponse(response)
    else:
        response = '原始数据长度不足5'