#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MapleStory Character Finder - API 테스트 스크립트
"""

import json
from maple_app.services.nexon_api_service import (
    api_key_check,
    get_account_list,
    get_account_first_character,
    get_character_list
)

# 사용자가 제공한 API 키
TEST_API_KEY = open('API_KEY.txt', 'r').read().strip()  # test_api_key.txt 파일에서 API 키 읽기
TEST_API_KEY = TEST_API_KEY.replace('LIVE_KEY=', '')  # 혹시 모를 따옴표 제거

print("\n" + "="*80)
print("MapleStory Character Finder - API 테스트")
print("="*80 + "\n")

# API 키 검증 테스트
print("[1] API 키 검증 테스트")
print("-" * 80)
result = api_key_check(TEST_API_KEY)
account_data = None

if result['result_code'] == 200:
    print("API 키 검증 성공")
    print(f"   - 결과 코드: {result['result_code']}")
    print(f"   - 메시지: {result['result_message']}")
    
    account_data = result['result_data']
    
    # 계정 목록 조회 테스트
    print("\n[2] 계정 목록 조회 테스트")
    print("-" * 80)
    accounts = get_account_list(account_data)
    print(f"계정 조회 성공")
    print(f"   - 총 계정 수: {len(accounts)}")
    
    if accounts:
        print(f"\n계정 정보:")
        for i, account in enumerate(accounts, 1):
            print(f"      {i}. 계정 ID: {account.get('account_id', 'N/A')}")
    
    # 첫 캐릭터 조회 테스트
    print("\n[3] 각 계정의 첫 캐릭터 조회 테스트")
    print("-" * 80)
    first_characters = get_account_first_character(accounts)
    print(f"첫 캐릭터 조회 성공!")
    
    if first_characters:
        print(f"\n캐릭터 정보:")
        for i, (account, char) in enumerate(zip(accounts, first_characters), 1):
            print(f"      {i}. {account.get('account_id', 'N/A')} -> {char}")
    
    # 캐릭터 상세 조회 테스트
    if accounts:
        print("\n[4] 캐릭터 상세 목록 조회 테스트")
        print("-" * 80)
        first_account_id = accounts[0].get('account_id')
        print(f"테스트 계정 ID: {first_account_id}")
        
        char_result = get_character_list(first_account_id, TEST_API_KEY)
        
        if char_result['result_code'] == 200:
            character_list = char_result['result_data'].get('character_list', [])
            print(f"캐릭터 목록 조회 성공")
            print(f"   - 캐릭터 수: {len(character_list)}")
            
            if character_list:
                print(f"\n캐릭터 상세 정보 (최대 5개 표시):")
                for i, char in enumerate(character_list[:5], 1):
                    print(f"\n      {i}. 이름: {char.get('character_name', 'N/A')}")
                    print(f"         직업: {char.get('character_class', 'N/A')}")
                    print(f"         레벨: {char.get('character_level', 'N/A')}")
                    print(f"         월드: {char.get('world_name', 'N/A')}")
        else:
            print(f"캐릭터 목록 조회 실패")
            print(f"   - 오류: {char_result['result_message']}")
            print(f"   - 상세: {char_result['result_fail_reason']}")
    
    print("\n" + "="*80)
    print("모든 테스트 완료")
    print("="*80 + "\n")
    
else:
    print(f"API 키 검증 실패")
    print(f"   - 결과 코드: {result['result_code']}")
    print(f"   - 메시지: {result['result_message']}")
    print(f"   - 상세: {result['result_fail_reason']}")
    print("\n" + "="*80)
