from flask import Blueprint, render_template, request, flash, jsonify, session
import json
from maple_app.services.nexon_api_service import (
    api_key_check,
    get_account_list,
    get_account_first_character,
    get_character_list,
    get_character_detail
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
        # API 키를 세션에 저장 (계정 선택 후 캐릭터 조회할 때 사용)
        session['api_key'] = api_key
        
        account_data = result['result_data']
        accounts = get_account_list(account_data)
        first_characters = get_account_first_character(accounts)
        
        # accounts와 first_characters를 zip으로 처리하여 templates에 전달
        account_pairs = list(zip(accounts, first_characters))
        
        return render_template(
            'account_list.html',
            accounts=accounts,
            first_characters=first_characters,
            account_pairs=account_pairs,
            account_count=len(accounts)
        )
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
        # API 키를 세션에 저장 (계정 선택 후 캐릭터 조회할 때 사용)
        session['api_key'] = api_key
        
        account_data = result['result_data']
        accounts = get_account_list(account_data)
        first_characters = get_account_first_character(accounts)
        
        # accounts와 first_characters를 zip으로 처리하여 templates에 전달
        account_pairs = list(zip(accounts, first_characters))
        
        return render_template(
            'account_list.html',
            accounts=accounts,
            first_characters=first_characters,
            account_pairs=account_pairs,
            account_count=len(accounts)
        )
    else:
        error_msg = f"{result['result_message']}: {result['result_fail_reason']}"
        flash(error_msg, 'error')
        return render_template('login.html')


@home_bp.route('/characters/<account_id>', methods=['GET'])
def characters(account_id):
    """특정 계정의 모든 캐릭터 목록 조회"""
    # 세션에서 API 키 확인
    api_key = session.get('api_key')
    
    if not api_key:
        flash("API 키 세션이 만료되었습니다. 다시 로그인해주세요.", 'error')
        return render_template('login.html')
    
    # 캐릭터 목록 조회
    result = get_character_list(account_id, api_key)
    
    if result['result_code'] == 200:
        character_list = result['result_data'].get('character_list', [])
        return render_template(
            'characters.html',
            account_id=account_id,
            character_list=character_list,
            character_count=len(character_list)
        )
    else:
        error_msg = f"{result['result_message']}: {result['result_fail_reason']}"
        flash(error_msg, 'error')
        return render_template('account_list.html')
