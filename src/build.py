#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 sections/*.html 組裝成單一自含的 ABAP 圖書館 HTML"""
import re, os, json, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
SEC = os.path.join(BASE, 'sections')

PARTS = [
    ("導覽", [("ch00", None)]),
    ("第一部 · 資料字典：讓模組顧問自由自在的飛",
     [("ch01-1", None), ("ch01-2", None), ("ch01-3", None), ("ch01-4", None)]),
    ("第二部 · 內表與 SQL：模組顧問進化成 ABAPER",
     [("ch02-1", None), ("ch02-2", None), ("ch02-3", None), ("ch02-4", None)]),
    ("第三部 · 視窗報表與增強：顧問會程式等於空間無限",
     [("ch03-1", None), ("ch03-2", None), ("ch03-3", None), ("ch03-4", None)]),
    ("第四部 · 進階技巧：目標成為專職的 ABAPER",
     [("ch04-1", None), ("ch04-2", None), ("ch04-3", None), ("ch04-4", None)]),
    ("第五部 · 原廠教材專區 A：導覽與程式基礎（BC100～BC404）",
     [("ch05-0", None), ("ch05-25", None), ("ch05-1", None), ("ch05-2", None), ("ch05-3", None), ("ch05-4", None), ("ch05-5", None)]),
    ("第五部 · 原廠教材專區 B：報表與使用者介面（BC405～BC412）",
     [("ch05-6", None), ("ch05-7", None), ("ch05-8", None), ("ch05-9", None), ("ch05-10", None)]),
    ("第五部 · 原廠教材專區 C：資料庫、介面與增強（BC414～BC440）",
     [("ch05-11", None), ("ch05-12", None), ("ch05-13", None), ("ch05-14", None), ("ch05-15", None), ("ch05-16", None), ("ch05-17", None)]),
    ("第五部 · 原廠教材專區 D：表單列印（BC460～BC480）",
     [("ch05-18", None), ("ch05-19", None), ("ch05-20", None)]),
    ("第五部 · 原廠教材專區 E：效能、介面與平台（BC490・IDoc/AIF・NET310・SAPNW）",
     [("ch05-21", None), ("ch05-22", None), ("ch05-23", None), ("ch05-24", None)]),
    ("第六部 · 實戰專題：除錯的絕招（L35）",
     [("ch06-1", None), ("ch06-2", None), ("ch06-3", None)]),
    ("第六部 · 實戰專題 B：專案實務案例（15_實務案例）",
     [("ch06-4", None), ("ch06-5", None), ("ch06-6", None), ("ch06-7", None), ("ch06-8", None)]),
    ("第七部 · 程式範例庫：ABAP OOP 原則．模式．實踐（L36）",
     [("ch07-1", None), ("ch07-2", None), ("ch07-3", None), ("ch07-4", None), ("ch07-5", None), ("ch07-6", None), ("ch07-7", None)]),
    ("第八部 · 實戰源碼庫：36 套專案程式（L31）",
     [("ch08-1", None), ("ch08-2", None), ("ch08-3", None), ("ch08-4", None), ("ch08-5", None), ("ch08-6", None), ("ch08-7", None), ("ch08-8", None)]),
    ("附錄", [("ap-01", None)]),
]

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    for a, b in (('&lt;', '<'), ('&gt;', '>'), ('&amp;', '&'), ('&quot;', '"'), ('&#39;', "'"), ('&nbsp;', ' ')):
        s = s.replace(a, b)
    return ' '.join(s.split())

sections_html = []
nav = []
stats = {'ch': 0, 'h3': 0, 'code': 0, 'warn': 0, 'tip': 0, 'note': 0}

for part_title, chapters in PARTS:
    part_entry = {'title': part_title, 'chapters': []}
    for chid, _ in chapters:
        path = os.path.join(SEC, chid + '.html')
        html = open(path, encoding='utf-8').read().strip()

        # 章名：取 h2 內文
        m = re.search(r'<h2[^>]*>(.*?)</h2>', html, re.S)
        title = strip_tags(m.group(1)) if m else chid

        # 移除 h2 上重複的 id（section 已經有同名 id）
        html = re.sub(r'(<h2)\s+id="[^"]*"', r'\1', html, count=1)

        # 補上缺 id 的 h3 / h4，並收集小節目錄
        counter = {'n': 0}
        subs = []

        def fix_head(mo):
            tag, attrs, inner = mo.group(1), mo.group(2), mo.group(3)
            idm = re.search(r'id="([^"]+)"', attrs)
            counter['n'] += 1
            if idm:
                hid = idm.group(1)
            else:
                hid = '%s-auto%02d' % (chid, counter['n'])
                attrs = attrs + ' id="%s"' % hid
            if tag == 'h3':
                subs.append({'id': hid, 't': strip_tags(inner)})
            return '<%s%s>%s</%s>' % (tag, attrs, inner, tag)

        html = re.sub(r'<(h3|h4)([^>]*)>(.*?)</\1>', fix_head, html, flags=re.S)

        stats['ch'] += 1
        stats['h3'] += len(subs)
        stats['code'] += len(re.findall(r'<pre><code', html))
        for k in ('warn', 'tip', 'note'):
            stats[k] += len(re.findall(r'<div class="%s"' % k, html))

        part_entry['chapters'].append({'id': chid, 't': title, 'subs': subs})
        sections_html.append(html)
    nav.append(part_entry)

body = '\n\n'.join(sections_html)
navjson = json.dumps(nav, ensure_ascii=False)
built = datetime.date.today().isoformat()

tpl = open(os.path.join(BASE, 'template.html'), encoding='utf-8').read()
out = (tpl.replace('/*__NAV__*/null', navjson)
          .replace('<!--__BODY__-->', body)
          .replace('__BUILT__', built)
          .replace('__STAT_CH__', str(stats['ch']))
          .replace('__STAT_H3__', str(stats['h3']))
          .replace('__STAT_CODE__', str(stats['code'])))

dest = os.path.abspath(os.path.join(BASE, '..', 'index.html'))
os.makedirs(os.path.dirname(dest), exist_ok=True)
open(dest, 'w', encoding='utf-8').write(out)
print('OK', dest, '%.2f MB' % (len(out.encode('utf-8')) / 1048576), stats)
