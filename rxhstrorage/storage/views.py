from django.shortcuts import render, HttpResponse
from storage import models
from django.http.response import JsonResponse
from datetime import datetime


# Create your views here.
def form(request):
    tips = ''
    title_tips = ''
    handler_tips = ''
    all_cls = models.MaterialCls.objects.all()
    all_mat = models.Material.objects.all()
    if request.method == 'POST':
        form_data = request.POST.copy()
        # print(form_data)
        time = datetime.now()  # 创建时间
        title = form_data.get('title', '')  # 产品名称
        if not title:
            title_tips = '产品名称必填！！！'
        master = form_data.get('master', '')  # 产品名称
        accountant = form_data.get('accountant', '')  # 产品名称
        locker = form_data.get('locker', '')  # 产品名称
        handler = form_data.get('handler', '')  # 产品名称
        if not handler:
            handler_tips = '经办人必填！！！'
        # 处理form_data 的cls mat数据为'' 的情况
        for k, v in form_data.items():
            # print(k, v)
            if k.startswith('cls') or k.startswith('mat'):
                if not v:
                    # print('kkid', k)
                    form_data[k] = 0

        data = {
            'row1': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_1')).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_1')).first(),  # 类别名称
                'amount': form_data.get('amount_1', ),  # 数量
                'unit_price': form_data.get('unit_price_1', ),  # 单价
                'price': form_data.get('price_1', ),  # 价格
                'remarks': form_data.get('remarks_1', ),  # 备注
            },
            'row2': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_2', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_2', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_2', ),  # 数量
                'unit_price': form_data.get('unit_price_2', ),  # 单价
                'price': form_data.get('price_2', ),  # 价格
                'remarks': form_data.get('remarks_2', ),  # 备注
            },
            'row3': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_3', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_3', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_3', ),  # 数量
                'unit_price': form_data.get('unit_price_3', ),  # 单价
                'price': form_data.get('price_3', ),  # 价格
                'remarks': form_data.get('remarks_3', ),  # 备注
            },
            'row4': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_4', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_4', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_4', ),  # 数量
                'unit_price': form_data.get('unit_price_4', ),  # 单价
                'price': form_data.get('price_4', ),  # 价格
                'remarks': form_data.get('remarks_4', ),  # 备注
            },
            'row5': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_5', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_5', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_5', ),  # 数量
                'unit_price': form_data.get('unit_price_5', ),  # 单价
                'price': form_data.get('price_5', ),  # 价格
                'remarks': form_data.get('remarks_5', ),  # 备注
            },
            'row6': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_6', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_6', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_6', ),  # 数量
                'unit_price': form_data.get('unit_price_6', ),  # 单价
                'price': form_data.get('price_6', ),  # 价格
                'remarks': form_data.get('remarks_6', ),  # 备注
            },
            'row7': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_7', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_7', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_7', ),  # 数量
                'unit_price': form_data.get('unit_price_7', ),  # 单价
                'price': form_data.get('price_7', ),  # 价格
                'remarks': form_data.get('remarks_7', ),  # 备注
            },
            'row8': {
                'cls': models.Material.objects.filter(cls_id=form_data.get('cls_8', 0)).first(),  # 类别名称
                'mat': models.Material.objects.filter(pk=form_data.get('mat_8', 0)).first(),  # 类别名称
                'amount': form_data.get('amount_8', ),  # 数量
                'unit_price': form_data.get('unit_price_8', ),  # 单价
                'price': form_data.get('price_8', ),  # 价格
                'remarks': form_data.get('remarks_8', ),  # 备注
            },
        }
        # print(time, title, master, accountant, locker, handler)
        # print(data)

        mat_list = [(v['mat'].pk if v['mat'] else 0, float(v['amount']) if v['amount'] else 0) for row, v in
                    data.items()]
        for dic in mat_list:
            mat_id, mat_amount = dic
            if mat_id and mat_amount:
                '''先查询出仓库的量'''
                # print(mat_id)
                mat_set = models.Material.objects.filter(pk=mat_id)
                mat_obj = mat_set.first()
                old_amonut = float(mat_obj.amount)
                if old_amonut >= mat_amount:
                    '''减完剩余的量'''
                    new_amount = old_amonut - mat_amount
                    '''更新'''
                    mat_set.update(amount=new_amount)
                else:
                    '''输入的量太大了'''
                    tips = f'{mat_obj.name}:输入的数量比原来的数量大，请查看后在输入！！！'
        res = handler_tips or title_tips

        if not res:
            if not tips:
                return render(request, 'table.html', {
                    'time': time,
                    'title': title,
                    'accountant': accountant,
                    'master': master,
                    'locker': locker,
                    'handler': handler,
                    'data': data,
                })

    return render(request, 'mat_form.html',
                  {'all_cls': all_cls, 'all_mat': all_mat, 'tips': tips, 'title_tips': title_tips,
                   'handler_tips': handler_tips,
                   })


def return_detail(request):
    cls_pk = request.POST.get('cls_pk')
    mats = models.Material.objects.filter(cls_id=cls_pk)
    mats_list = list(mats.values())
    return JsonResponse(mats_list, safe=False)


