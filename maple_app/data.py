# %%

import requests, sys, bs4, json
import pandas as pd

def api_key_check(api_key):
    target_url = 'https://open.api.nexon.com/maplestory/v1/character/list'
    result_code = 200
    result_message = "Success"
    result_fail_reason = ""
    result_data = ""

    # 개발/테스트용 API 키 체크
    if "test_" in api_key:
        result_code = 400
        result_message = "개발/테스트용 API키 입니다."
        result_fail_reason = "개발/테스트용 API키 사용"
        return_data = {
            "result_code": result_code,
            "result_message": result_message,
            "result_fail_reason": result_fail_reason,
            "result_data": ""
        }
        
        json_result = json.dumps(return_data, ensure_ascii=False)
        print(json_result)
        return(json_result)
    
    
    curl_command = f"curl -X 'GET' \
    '{target_url}' \
    -H 'accept: application/json' \
    -H 'x-nxopen-api-key: {api_key}'"
    
    res = requests.get(target_url, headers={"accept": "application/json", "x-nxopen-api-key": api_key})
    res_text = bs4.BeautifulSoup(res.text, "html.parser")

    # 잘못된 API 키
    try:
        res_json = json.loads(res_text.text)
        if res.status_code == 200:
            return json.dumps({
                "result_code": res.status_code,
                "result_message": "API 키 로그인 성공",
                "result_fail_reason": "",
                "result_data": res_json
            }, ensure_ascii=False)
        else:
            # %%
            #print(res_json)
            return json.dumps({
                "result_code": res.status_code,
                "result_message": "API 키 로그인 실패",
                "result_fail_reason": res_json['error']['message'],
                "result_data": ""
            }, ensure_ascii=False)
        
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(res_text.text)
        result_code = 500
        result_message = "Failed to decode JSON response"
        result_fail_reason = "Invalid JSON format"
        return_data = {
            "result_code": result_code,
            "result_message": result_message,
            "result_fail_reason": result_fail_reason
        }
        json_result = json.dumps(return_data, ensure_ascii=False)
        print(json_result)
        return(json_result)

"""
account_ids = []
for account in res_json['account_list']:
    account_ids.append(account['account_id'])
    
#print(account_ids)

df_characters = pd.DataFrame(res_json['account_list'][0]['character_list'])
#print(df_characters)
#print(df_characters['world_name'] == '크로아')
df_characters = df_characters[df_characters['world_name'] == '크로아']

df_duplicated = df_characters[df_characters.duplicated(subset=['character_class'], keep=False)]
#print(df_duplicated)

df_headers = df_characters.columns.tolist()
# header_template = "<tr>" + "".join([f"<th>{header}</th>" for header in df_headers]) + "</tr>"
# df_characters_template = df_characters.to_html(index=False, header=True)
# return_table_template = f"""
# <table id=\"myTable\" border=\"1\">
#     <thead>
#         {header_template}
#     </thead>
#     <tbody>
#         {df_characters_template}
#     </tbody>
# </table>"""


# return_table_template = f"""    
#         {df_characters_template}
# </table>"""

# print(return_table_template)


# %%
