"""
系统探索牛客网所有可用的公开 API
"""
import requests, json, re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.nowcoder.com/school/schedule',
}

base = 'https://gw-c.nowcoder.com/api/sparta'

# === 从 JS 源码中提取所有 API 路径 ===
print("=== 从 JS 源码提取 API ===")
r = requests.get(
    'https://static.nowcoder.com/nowpick/web/nowcoder/3.2.694/javascripts-wp-c/page/jobHome/main.entry.js',
    headers={'User-Agent': 'Mozilla/5.0'}, timeout=15
)
# Extract all function/endpoint paths related to school/job
paths = set()
for pat in [
    r'"(/api/sparta/[a-zA-Z][^"]+)"',
    r"'([^']*/api/sparta/[^']+)'",
    r'`([^`]*/api/sparta/[^`]*)`',
    r'"path":"([^"]+)"',
]:
    matches = re.findall(pat, r.text)
    for m in matches:
        paths.add(m)

print(f'Found {len(paths)} unique API paths')
for p in sorted(paths):
    print(f'  {p}')

# === 测试每个 API ===
print('\n=== 测试 API 是否需要登录 ===')
tested = set()
for path in sorted(paths):
    if path in tested:
        continue
    tested.add(path)

    # Clean path
    clean = path.strip('/')
    url = f'{base}/{clean}' if not path.startswith('http') else path

    try:
        resp = requests.get(url, headers=headers, timeout=8)
        ct = resp.headers.get('Content-Type', '')
        if 'json' in ct:
            try:
                data = resp.json()
                success = data.get('success', data.get('code') == 0)
                msg = data.get('msg', '')
                code = data.get('code', '')
                if not success and ('login' in str(msg).lower() or code == 999):
                    print(f'  ❌ {clean}: needs login')
                else:
                    print(f'  ✅ {clean}: {resp.status_code} success={success} msg={msg}')
                    # Show data structure
                    d = data.get('data')
                    if isinstance(d, dict):
                        print(f'      data keys: {list(d.keys())[:8]}')
                    elif isinstance(d, list):
                        print(f'      data list[{len(d)}]')
            except:
                print(f'  ❓ {clean}: non-JSON response')
        else:
            print(f'  ❓ {clean}: Content-Type={ct[:40]}')
    except Exception as e:
        pass  # skip errors
