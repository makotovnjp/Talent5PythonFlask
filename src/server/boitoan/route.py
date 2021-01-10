# Thu vien standard

# ThirdParty
from flask import Blueprint, jsonify, request

# Thu vien ben trong

# Blueprintのインスタンス生成
boitoan = Blueprint("boitoan", __name__)

# làm thế nào để định nghĩa POST, GET


# app decorator
@boitoan.route('/boitoan/', methods=('GET', 'POST'))
def boi_toan():
    if request.method == 'POST':
        ret = _post_boi_toan(request)
    elif request.method == 'GET':
        ret = _get_boi_toan()

    return ret


# Module: function noi bo nen them _(protect), __(private)
def _post_boi_toan(req):
    # Nhận thông tin năm và xử lý
    # Query Parameter
    # Body (Json) {"man": 1998}
    body = req.json
    try:
        year_of_man = int(body.get("man"))
        year_of_woman = int(body.get("woman"))
    except Exception as ex:
        raise ValueError('Not number {}'.format(ex))

    # Xem ngũ hành
    nam_mang = _ngu_hanh(year_of_man)
    nu_mang = _ngu_hanh(year_of_woman)

    # Noi dung tra lai context, status
    res = {'man': nam_mang, 'woman': nu_mang}

    return res


def _get_boi_toan(req):
    return "OK"


def _ngu_hanh(year):
    """
    tính toán ngũ hành theo năm
    :param year: (str) năm
    :return:
    """
    # Review4: quy tắc code
    # 1 function chỉ làm 1 nhiệm vụ
    # KISS: keep it simple stupid

    # Tính thiên can và can
    can = __tinh_thien_can(year)

    # Tính địa chi và chi
    chi = __tinh_chi(year)

    # Tính giá trị hành
    hanh = can + chi
    if hanh > 5:
        hanh = hanh - 5

    # Review6: METADATA coding
    hanh_mang_table = {
        1: "KIM",
        2: "THUY",
        3: "HOA",
        4: "THO",
        5: "MOC"
    }
    mang = hanh_mang_table[hanh]

    return mang


def __tinh_thien_can(year):
    """
    :param year:
    :return:
    """
    thien_can = year % 10
    if thien_can == 5 or thien_can == 4:
        can = 1
    if thien_can == 6 or thien_can == 7:
        can = 2
    if thien_can == 8 or thien_can == 9:
        can = 3
    if thien_can == 0 or thien_can == 1:
        can = 4
    if thien_can == 2 or thien_can == 3:
        can = 5

    return can


def __tinh_chi(year):
    """
    :param year:
    :return:
    """
    dia_chi = year % 12
    if dia_chi == 4 or dia_chi == 5 or dia_chi == 10 or dia_chi == 11:
        chi = 0
    if dia_chi == 6 or dia_chi == 7 or dia_chi == 0 or dia_chi == 1:
        chi = 1
    if dia_chi == 8 or dia_chi == 9 or dia_chi == 2 or dia_chi == 3:
        chi = 2

    return chi