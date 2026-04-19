from maple_app.data import *
from maple_app import app
from flask import render_template, request, flash
from config import *

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here      
        api_key = request.form.get('api_key')
        result = json.loads(api_key_check(api_key))
        print("###############################")
        #print(result)
        print(type(result))
        if result["result_code"] == 200:
            # 로그인 성공 시 캐릭터 정보 페이지로 리디렉션
            #return render_template('character_info.html', character_data=result["result_data"])
            return result["result_data"]
        else:
            # 로그인 실패 시 에러 메시지 표시
            flash(result["result_message"] + ": " + result["result_fail_reason"], 'error')
            return render_template('login.html')
    
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
