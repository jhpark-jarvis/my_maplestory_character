import requests
import json
import bs4


def api_key_check(api_key):
    """
    NEXON Open API 키 검증 및 계정 정보 조회
    
    Args:
        api_key (str): NEXON Open API 키
        
    Returns:
        dict: {
            'result_code': int (200=성공, 그 외=실패),
            'result_message': str,
            'result_fail_reason': str,
            'result_data': dict (성공 시 API 응답 데이터)
        }
    """
    target_url = 'https://open.api.nexon.com/maplestory/v1/character/list'
    
    # 개발/테스트용 API 키 체크
    if "test_" in api_key:
        return _create_error_response(
            400,
            "개발/테스트용 API키입니다.",
            "개발/테스트용 API키 사용"
        )
    
    try:
        res = requests.get(
            target_url,
            headers={
                "accept": "application/json",
                "x-nxopen-api-key": api_key
            }
        )
        res_text = bs4.BeautifulSoup(res.text, "html.parser")
        res_json = json.loads(res_text.text)
        
        if res.status_code == 200:
            return _create_success_response(res_json)
        else:
            return _create_error_response(
                res.status_code,
                "API 키 검증 실패",
                res_json.get('error', {}).get('message', '알 수 없는 오류')
            )
            
    except json.JSONDecodeError as e:
        return _create_error_response(
            500,
            "JSON 파싱 오류",
            str(e)
        )
    except Exception as e:
        return _create_error_response(
            500,
            "API 요청 실패",
            str(e)
        )


def get_account_list(api_response_data):
    """
    API 응답에서 계정 목록 추출
    
    Args:
        api_response_data (dict): api_key_check 결과의 result_data
        
    Returns:
        list: 계정 정보 목록
    """
    return api_response_data.get('account_list', [])


def get_account_first_character(account_list):
    """
    각 계정의 첫 번째 캐릭터 이름 추출
    
    Args:
        account_list (list): 계정 정보 목록
        
    Returns:
        list: 첫 번째 캐릭터 이름 목록
    """
    return [
        account['character_list'][0]['character_name'] 
        if account.get('character_list') else ''
        for account in account_list
    ]


def _create_success_response(data):
    """성공 응답 생성"""
    return {
        "result_code": 200,
        "result_message": "API 키 검증 성공",
        "result_fail_reason": "",
        "result_data": data
    }


def _create_error_response(code, message, reason):
    """실패 응답 생성"""
    return {
        "result_code": code,
        "result_message": message,
        "result_fail_reason": reason,
        "result_data": ""
    }
