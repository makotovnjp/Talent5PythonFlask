# Thu vien standard

# ThirdParty
from flask import Blueprint, jsonify, request, render_template

# Thu vien ben trong

# Blueprintのインスタンス生成
boi = Blueprint("phongthuy", __name__)

# làm thế nào để định nghĩa POST, GET


# app decorator
@boi.route('/phongthuy/', methods=('GET', 'POST'))
def boi_toan():
    if request.method == 'POST':
        ret = _post_boi_toan(request)
    elif request.method == 'GET':
        ret = _get_boi_toan(request)

    return render_template("result.html", ret)


# Module: function noi bo nen them _(protect), __(private)
def _post_boi_toan(req):
    # Nhận thông tin năm và xử lý
    # Query Parameter
    # Body (Json) {"man": 1998}
    """body = req.json
    print("body = {}".format(body))

    year_of_man = body.get("man")
    year_of_woman = body.get("woman")"""
    year_of_man = req.form["man"]
    year_of_woman = req.form["woman"]
    print("year_of_man = {}".format(year_of_man))
    print("year_of_woman = {}".format(year_of_woman))

    # Xem ngũ hành
    nam_mang = _ngu_hanh(year_of_man)
    nu_mang = _ngu_hanh(year_of_woman)
    print("Nam Mang:", nam_mang)
    print("Nu mang:", nu_mang)

    # Xem hợp tuổi

    hop = _hop_tuoi(nam_mang, nu_mang)
    print("Hai nguoi", hop)

    return nam_mang, nu_mang, hop


def _get_boi_toan(req):
    return "OK"

# Tính ngũ hành theo https://phongthuyhomang.vn/cach-tinh-thien-can-dia-chi-va-ngu-hanh-nam-sinh-cuc-nhanh/

def _ngu_hanh(year):

    # Tính thiên can và can

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

    # Tính địa chi và chi

    dia_chi = year % 12
    if dia_chi == 4 or dia_chi == 5 or dia_chi == 10 or dia_chi == 11:
        chi = 0
    if dia_chi == 6 or dia_chi == 7 or dia_chi == 0 or dia_chi == 1:
        chi = 1
    if dia_chi == 8 or dia_chi == 9 or dia_chi == 2 or dia_chi == 3:
        chi = 2

    # Tính giá trị hành

    hanh = can + chi
    if hanh > 5:
        hanh = hanh - 5
    if hanh == 1:
        mang = "KIM"
    elif hanh == 2:
        mang = "THUY"
    elif hanh == 3:
        mang = "HOA"
    elif hanh == 4:
        mang = "THO"
    else:
        mang = "MOC"
    return mang

def _hop_tuoi(nam, nu):

    if nam == nu:
        tuoi = "Khong hop cung khong khac"
    else:
        if nam == "KIM":
            if nu == "THUY" or nu == "THO":
                tuoi = "Hop nhau"
            if nu == "MOC" or nu == "HOA":
                tuoi = "Khac nhau"
        elif nam == "THUY":
            if nu == "KIM" or nu == "MOC":
                tuoi = "Hop nhau"
            if nu == "HOA" or nu == "THO":
                tuoi = "Khac nhau"
        elif nam == "MOC":
            if nu == "HOA" or nu == "THUY":
                tuoi = "Hop nhau"
            if nu == "KIM" or nu == "THO":
                tuoi = "Khac nhau"
        elif nam == "HOA":
            if nu == "THO" or nu == "MOC":
                tuoi = "Hop nhau"
            if nu == "KIM" or nu == "THUY":
                tuoi = "Khac nhau"
        else:
            if nu == "HOA" or nu == "KIM":
                tuoi = "Hop nhau"
            if nu == "THUY" or nu == "MOC":
                tuoi = "Khac nhau"
    return tuoi

