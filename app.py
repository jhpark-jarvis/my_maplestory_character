from maple_app.data import *
from maple_app import app
from flask import render_template, request, flash, jsonify
from config import Config

@app.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/account_list', methods=['GET', 'POST'])
def account_list():
    if request.method == 'GET':
        api_key = request.form.get('api_key')
        result = json.loads(api_key_check(api_key))
        
        if result["result_code"] == 200:
            return render_template('account_list.html')
        
        elif api_key is None:
            flash("API 키가 제공되지 않았습니다.", 'error')
            return render_template('login.html')
        
        else:
            # 로그인 실패 시 에러 메시지 표시
            flash(result["result_message"] + ": " + result["result_fail_reason"], 'error')
            return render_template('login.html')
        
    if request.method == 'POST':
        # Handle POST request for account_list
        api_key = request.form.get('api_key')
        result = json.loads(api_key_check(api_key))
        if result["result_code"] == 200:
            account_list = []
            account_first_character = []
            for id in result["result_data"]["account_list"]:
                account_list.append(id["account_id"])
                account_first_character.append(id["character_list"][0]["character_name"])
            
            # 로그인 성공 시 캐릭터 정보 페이지로 리디렉션
            return render_template('account_list.html'
                                   , account_data=json.dumps(result["result_data"]["account_list"])
                                   , account_count = len(result["result_data"]["account_list"])
                                   , account_list = json.dumps(account_list, ensure_ascii=False)
                                   , account_first_character = json.dumps(account_first_character, ensure_ascii=False)
                                   )

if __name__ == '__main__':
    app.config.from_object(Config)
    app.config['JSON_AS_ASCII'] = False  # JSON 응답에서 한글이 깨지지 않도록 설정
    app.run(debug=True)
    
    
