#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用本機 Chrome 開 index.html 做冒煙測試：章數、程式碼上色、搜尋、主控台錯誤。

用法：python verify.py [html路徑]   （預設 ../index.html）
需求：pip install playwright（用 channel='chrome'，不必 playwright install）
"""
import os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
html = Path(sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, '..', 'index.html')).resolve()
url = html.as_uri()

errs = []
with sync_playwright() as pw:
    b = pw.chromium.launch(channel='chrome')
    pg = b.new_page()
    pg.on('console', lambda m: m.type == 'error' and errs.append(m.text))
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(url)
    pg.wait_for_timeout(1000)
    chapters = pg.locator('section.chapter').count()

    pg.goto(url + '#ch02-2')
    pg.wait_for_timeout(1500)
    hl = pg.locator('#ch02-2 pre code[data-hl]').count()
    codes = pg.locator('#ch02-2 pre code').count()

    pg.fill('#q', 'CL_SALV_TABLE')
    pg.wait_for_timeout(1000)
    hits = pg.locator('#results .hit').count()
    b.close()

print(f'章數 {chapters}｜ch02-2 上色 {hl}/{codes}｜搜尋 CL_SALV_TABLE 命中 {hits}｜主控台錯誤 {len(errs)}')
for e in errs:
    print('  !', e)
ok = chapters > 0 and codes > 0 and hl == codes and hits > 0 and not errs
print('OK' if ok else 'FAIL')
sys.exit(0 if ok else 1)
