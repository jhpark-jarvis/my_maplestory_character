# %%

import requests, sys, bs4, json
import pandas as pd

def api_key_check(api_key):
    result_code = 200
    result_message = "Success"
    result_fail_reason = ""
    
    if "test_" in api_key:
        result_code = 400
        result_message = "개발/테스트용 API키 입니다."
        result_fail_reason = "개발/테스트용 API키 사용"
        return_data = {
            "result_code": result_code,
            "result_message": result_message,
            "result_fail_reason": result_fail_reason
        }
        
        json_result = json.dumps(return_data, ensure_ascii=False)
        print(json_result)
        return(json_result)
    

target_url = 'https://open.api.nexon.com/maplestory/v1/character/list'
api_key = open("api_key.txt", "r").read().strip()
api_key = api_key.replace("LIVE_KEY=", "")  # Ensure the API key is correctly formatted
result_code = 200
result_message = "Success"
result_fail_reason = ""

curl_command = f"curl -X 'GET' \
  '{target_url}' \
  -H 'accept: application/json' \
  -H 'x-nxopen-api-key: {api_key}'"
  
res = requests.get(target_url, headers={"accept": "application/json", "x-nxopen-api-key": api_key + ""})
res_text = bs4.BeautifulSoup(res.text, "html.parser")

try:
    res_json = json.loads(res_text.text)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    print(res_text.text)
    result_code = 500
    result_message = "Failed to decode JSON response"
    result_fail_reason = "Invalid JSON format"
    sys.exit(1)


if (res.status_code != 200):
    print(f"Error: {res.status_code}")
    print(res_json)
    result_code = res.status_code
    result_message = "Error occurred while fetching data"
    result_fail_reason = res.reason
    sys.exit(1)
    
account_ids = []
for account in res_json['account_list']:
    account_ids.append(account['account_id'])
    
print(account_ids)

df_characters = pd.DataFrame(res_json['account_list'][0]['character_list'])
print(df_characters)
print(df_characters['world_name'] == '크로아')
df_characters = df_characters[df_characters['world_name'] == '크로아']

df_duplicated = df_characters[df_characters.duplicated(subset=['character_class'], keep=False)]
print(df_duplicated)

df_headers = df_characters.columns.tolist()
# header_template = "<tr>" + "".join([f"<th>{header}</th>" for header in df_headers]) + "</tr>"
# df_characters_template = df_characters.to_html(index=False, header=True)
# return_table_template = f"""<table id=\"myTable\" border=\"1\">
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

