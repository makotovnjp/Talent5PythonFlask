# Import standard library

# Import thư viện bên ngoài
from flask import Blueprint, request


# Import module/package trong project


boi_toan = Blueprint('boi__toan', __name__)

@boi_toan.route('/boitoan/', methods = ('GET', 'POST', 'PUT', 'DELETE'))
def BoiToan():
    if request.method == 'POST':
        result = _post_BoiToan(request)
    # elif request.method == 'GET':
    #     result = _get_BoiToan(request)
    # elif request.method == 'PUT':
    #     result = _put_BoiToan(request)
    else:
        result = 'other'
    return result

def _post_BoiToan(req):
    body = req.json
    print('body = {}'.format(body))

    man_year = body.get('man')
    print('man_year = {}'.format(man_year))

    if man_year == 1999:
        return 'tho'
    else:
        return 'abc'

def _get_BoiToan(req):
    return 'ok'

def _put_BoiToan(req):
    return 'ok'

def _delete_BoiToan(req):
    return 'ok'