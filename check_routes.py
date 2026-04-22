from flask import Flask
from maple_app import app

print("\n=== 등록된 라우트 ===\n")
print(f"{'URL 경로':<30} {'엔드포인트':<25} {'메서드':<20}")
print("=" * 75)

for rule in app.url_map.iter_rules():
    if rule.endpoint != 'static':
        methods = ','.join(sorted(rule.methods - {'HEAD', 'OPTIONS'}))
        print(f'{rule.rule:<30} {rule.endpoint:<25} {methods:<20}')

print("\n라우팅 확인 완료!\n")
