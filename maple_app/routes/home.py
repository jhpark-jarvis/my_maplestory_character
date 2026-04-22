from flask import Blueprint, render_template, request, flash, jsonify
import json
from maple_app.services.nexon_api_service import (
    api_key_check,
    get_account_list,
    get_account_first_character
)

# Blueprint 정의
home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
def login():
    """로그인 페이지"""
    return render_template('login.html')


@home_bp.route('/account_list', methods=['GET', 'POST'])
def account_list():
    """계정 목록 조회 페이지"""
    
    if request.method == 'GET':
        return _handle_account_list_get()
    elif request.method == 'POST':
        return _handle_account_list_post()


def _handle_account_list_get():
    """GET: API 키 검증 후 계정 목록 페이지 렌더링"""
    api_key = request.args.get('api_key')
    
    if not api_key:
        flash("API 키가 제공되지 않았습니다.", 'error')
        return render_template('login.html')
    
    # API 키 검증
    result = api_key_check(api_key)
    
    if result['result_code'] == 200:
        return render_template('account_list.html', api_key=api_key)
    else:
        error_msg = f"{result['result_message']}: {result['result_fail_reason']}"
        flash(error_msg, 'error')
        return render_template('login.html')


def _handle_account_list_post():
    """POST: 폼에서 제출된 계정 정보 처리"""
    api_key = request.form.get('api_key')
    
    if not api_key:
        flash("API 키가 제공되지 않았습니다.", 'error')
        return render_template('login.html')
    
    # API 키 검증
    result = api_key_check(api_key)
    
    if result['result_code'] == 200:
        account_data = result['result_data']
        accounts = get_account_list(account_data)
        first_characters = get_account_first_character(accounts)
        
        return render_template(
            'account_list.html',
            account_data=json.dumps(accounts, ensure_ascii=False),
            account_count=len(accounts),
            account_list=json.dumps(
                [acc['account_id'] for acc in accounts],
                ensure_ascii=False
            ),
            account_first_character=json.dumps(first_characters, ensure_ascii=False)
        )
    else:
        error_msg = f"{result['result_message']}: {result['result_fail_reason']}"
        flash(error_msg, 'error')
        return render_template('login.html')
