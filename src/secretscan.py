# 掃描成品是否外洩 L31 素材中的機密字串
# 機密字串清單本身也是機密，不放在 repo 裡（repo 是公開的）。依序從以下來源讀取：
#   1. 環境變數 SECRETSCAN_DENY（CI 用 GitHub Secret 注入；以換行或逗號分隔）
#   2. src/secretscan-deny.txt（已列入 .gitignore）
#   3. C:\Users\tocas\Dropbox\09_SAP_AB_ABAP編程\secretscan-deny.txt（本機主檔）
# 找不到清單視為失敗，避免誤以為掃過了。有命中時 exit 1。
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = [os.path.join(BASE, 'secretscan-deny.txt'),
         r'C:\Users\tocas\Dropbox\09_SAP_AB_ABAP編程\secretscan-deny.txt']

def load_deny():
    env = os.environ.get('SECRETSCAN_DENY', '')
    if env.strip():
        return [x.strip() for x in re.split(r'[\n,]', env) if x.strip()]
    for p in FILES:
        if os.path.isfile(p):
            return [x.strip() for x in open(p, encoding='utf-8') if x.strip() and not x.startswith('#')]
    return None

bad = load_deny()
if not bad:
    print('找不到機密字串清單（SECRETSCAN_DENY 或 secretscan-deny.txt），無法掃描')
    sys.exit(2)

pat = re.compile(r'[A-Za-z0-9._%+-]+@(?!example\.(com|org)|company\.com|sap\.com|ncu\.edu\.tw|hotmail\.com)[A-Za-z0-9.-]+\.[a-z]{2,}')
hit = 0
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    for i, b in enumerate(bad, 1):
        if b.lower() in s.lower(): print(f, f'含機密字串（清單第 {i} 項）'); hit += 1
    for m in pat.finditer(s): print(f, 'email', m.group()); hit += 1
    # 值以 < 或 &lt; 開頭的是 <APP_KEY> 這類佔位符，不算
    for m in re.finditer(r"(app_?key|api_?key|secret|token|password)\s*=\s*'(?!&lt;)([^'<]{8,})'", s, re.I): print(f, '疑似金鑰', m.group()); hit += 1
print(f'CLEAN（清單 {len(bad)} 項）' if not hit else f'{hit} 筆需處理')
sys.exit(1 if hit else 0)
