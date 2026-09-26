---
name: abap-library
description: 維護與擴充 Casper 的「ABAP 圖書館」單檔 HTML（ABAP圖書館_S4HANA.html）。當使用者說「把 XXX 加進 ABAP 圖書館」、「補一章 CDS View / 除錯 / 實務案例」、「重建 ABAP 圖書館」、「更新 ABAP 手冊」、「整理 09_SAP_AB_ABAP編程 底下的資料」，或要把 SAP ABAP 教材、PDF、docx、原始碼整理成可查閱的技術庫時，務必使用本 skill——即使對方沒有明講「HTML」或「圖書館」三個字。本 skill 內含固定的章節片段格式、S/4HANA 1809+ 程式碼標準、建置與驗證流程，能確保新增內容與既有各章體例完全一致。
---

# ABAP 圖書館 · 擴充與維護

## 這個 skill 做什麼

把 `C:\Users\tocas\Dropbox\09_SAP_AB_ABAP編程` 底下的 SAP ABAP 學習資料，
持續整併進 **一個單檔、離線可開、可全文搜尋的 HTML 圖書館**：`ABAP圖書館_S4HANA.html`。

現況：72 章（ch00、ch01-1 ~ ch04-4、第五部原廠教材專區 ch05-0 ~ ch05-25、第六部實戰專題 ch06-1 ~ ch06-13、第七部程式範例庫 ch07-1 ~ ch07-7、第八部實戰源碼庫 ch08-1 ~ ch08-8、ap-01）、1347 個小節、1259 段程式碼。第一～四部取材自 `00_SAP_DOC` 的十六本自編教材；第五部取材自 `L28_强晟_19本原廠教材筆記_含原廠教材` 與 `L29_原廠教材`；第六部取材自 `L35_SAP调试技术`、`15_實務案例` 與 `15_累計心得`；第七部取材自 `L36_ABAP_OOP_SAMPLE-master`；第八部取材自 `L31_ABAP36套源碼`（部署前必跑 src/secretscan.py）。
建置原始碼的唯一來源是公開 GitHub repo `tocasper-eng/abap`：推到 `main` 後，CI 會自動建置、掃描、測試，並部署到 https://tocasper-eng.github.io/abap/ 。
`CLAUDE.md`（repo 根目錄和 Dropbox 根目錄各一份，內容相同）是完整的專案說明，**動手前先讀它**。

執行環境有兩種：
- **本機 Claude Code**：工作區是 `%LOCALAPPDATA%\abap-library-src\repo`，可以讀 Dropbox 的原始教材。
- **claude.ai/code 雲端**：讀不到 Dropbox 教材，只做不需要本機素材的工作。

---

## 執行流程

### 步驟 0 — 確認範圍

先用 Glob／`ls` 看目標資料夾有什麼，再問使用者（或在無人值守時自行判斷並說明假設）：
要納入哪些檔案？成為新的一章，還是併進既有章節？

### 步驟 1 — 確認工作區

本機工作區是 `%LOCALAPPDATA%\abap-library-src\repo`（`src/` 下有 `sections/`、`template.html`、`build.py`、`secretscan.py`、`verify.py`）。
先 `git -C <repo> status` 確認工作區乾淨，再 `git -C <repo> pull`（雲端 session 可能改過）。
資料夾不見的話，重新 clone：`gh repo clone tocasper-eng/abap "$LOCALAPPDATA/abap-library-src/repo"`。

**公開 repo 的資安規則**：機密字串清單（`secretscan-deny.txt`）絕不可入庫；commit 訊息和文件也不可寫客戶名、個資或金鑰原文。

### 步驟 2 — 取材

素材直接從 `C:\Users\tocas\Dropbox\09_SAP_AB_ABAP編程\…` 讀取。抽出來的中間 txt 放 session 的 scratchpad，不要放進 Dropbox。
docx 用 python-docx 抽文字（**要連表格一起抽**，表格列輸出成 `|a | b|`）：

```python
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn
def blocks(doc):
    for c in doc.element.body.iterchildren():
        if c.tag==qn('w:p'): yield Paragraph(c,doc)
        elif c.tag==qn('w:tbl'): yield Table(c,doc)
```

PDF 用 `pdf` skill；教材多為截圖，文字量遠小於檔案大小是正常的，缺的部分用 SAP 標準知識補寫成可操作步驟。

### 步驟 3 — 平行整理（重要）

**一章一個 subagent**，每個 agent：
- 讀完自己那一份 txt
- 依下方「片段格式」與「程式碼標準」產出 HTML 片段
- 用 Write 寫進 `sections/chXX-X.html`
- **只回傳 120 字以內的摘要，不要把 HTML 貼回主對話**（會爆 context）

一次派 6～8 個 agent，寫在同一則訊息裡讓它們平行跑。

### 步驟 4 — 組裝與驗證

在 `repo/src` 下執行：

```bash
python build.py                          # 產出 ../index.html，並印出章數統計
python secretscan.py sections/*.html     # 印出 CLEAN 才算通過（雲端沒有清單檔，會 exit 2，交給 CI 檢查）
PYTHONIOENCODING=utf-8 python verify.py  # 用 Chrome 驗證，最後一行要印出 OK
```

`verify.py` 會檢查章數、`pre code[data-hl]`（程式碼上色）、搜尋命中數，以及主控台有沒有錯誤。
新增的章節要另外切過去抽查上色，必要時截圖目視檢查。

也要跑標籤驗證：無不允許的標籤、無 `style` 屬性、標籤成對、程式碼已 escape。

### 步驟 5 — 交付

1. 更新 `CLAUDE.md` 的章數統計與「尚未納入」清單（repo 內那份）
2. `git commit`（訊息格式：`ABAP 圖書館 v2.x：新增…`）
3. 使用者同意後才 `git push`，因為 push 就等於公開發佈。接著用 `gh run watch -R tocasper-eng/abap` 盯到 CI 綠燈才算完成。
   雲端 session 則推到自己的分支，開 PR 合併到 `main`。
4. 本機才要做：把 `repo/index.html` 複製成 Dropbox 的 `ABAP圖書館_S4HANA.html`；`CLAUDE.md`、`SKILL.md` 同步到 Dropbox 根目錄，`SKILL.md` 也同步到 `~\.claude\skills\abap-library\`

---

## 片段格式（嚴格）

```html
<section class="chapter" id="ch05-1" data-title="章節標題">
  <h2>第 5-1 章 標題</h2>
  <p class="lede">兩三句話說明這章解決什麼問題、學完能做什麼。</p>
  <div class="meta">
    <div><b>核心 TCODE</b><span class="tcode">SE38</span><span class="tcode">SE11</span></div>
    <div><b>關鍵物件</b>MARA、CL_SALV_TABLE</div>
  </div>

  <h3 id="ch05-1-01">1. 小節標題</h3>
  <p>…</p>
  <table><thead><tr><th>…</th></tr></thead><tbody><tr><td>…</td></tr></tbody></table>
  <pre><code class="abap">REPORT zdemo.</code></pre>
  <div class="note">補充</div>
  <div class="tip">實務技巧</div>
  <div class="warn">S/4HANA 注意事項</div>

  <h3 id="ch05-1-qa">練習與自我檢核</h3>
  <ol><li>…</li></ol>
</section>
```

- 允許標籤僅：section, h2, h3, h4, p, ul, ol, li, table/thead/tbody/tr/th/td, pre, code, div(note|tip|warn|meta), b, i, span(tcode|src|kw), a, br
- 禁止 `style` 屬性、額外 class、`<script>`、`<style>`
- 小節 id：`章號-01`、`章號-02`…，最後一節 `章號-qa`
- 程式碼內容必須 HTML escape
- 全繁體中文；SAP 專有名詞與程式碼保持英文
- 新章節要加進 `build.py` 的 `PARTS`

---

## 程式碼標準（S/4HANA 1809+）

**必用**

| 主題 | 寫法 |
|---|---|
| 宣告 | `DATA(lv_x) = …`、`FIELD-SYMBOL(<fs>)`、`NEW zcl_x( )` |
| ABAP SQL | 明列欄位、主機變數一律 `@`、`INTO TABLE @DATA(lt_x)` |
| 建構式 | `VALUE #( )`、`CORRESPONDING #( )`、`REDUCE`、`FOR`、`COND`、`SWITCH` |
| 字串 | 字串範本 `\|{ lv_x }\|` |
| 內表 | `line_exists( it[ k = v ] )`、`it[ k = v ]`、`LOOP … GROUP BY` |
| ALV | `CL_SALV_TABLE`；需編輯／事件細控才用 `CL_GUI_ALV_GRID` |
| 例外 | `TRY … CATCH cx_… ENDTRY` |

**禁用**（原教材是舊寫法就直接改寫，只在對照表以文字提及）

`TABLES:`、`WITH HEADER LINE`、`OCCURS 0`、`MOVE`、`ADD/SUBTRACT/MULTIPLY/DIVIDE`、`COMPUTE`、
`SELECT … ENDSELECT`、無 `@` 的主機變數、`REUSE_ALV_GRID_DISPLAY`、`EXEC SQL`、新程式用 `FORM/PERFORM`。

用到 7.54 以上語法（`+=`、`DEFINE VIEW ENTITY`、PCRE）要標版本門檻。

---

## 每次都要提醒的三個坑

寫到相關主題時，一定要再寫一次（用 `<div class="warn">`）：

1. **HANA 沒有預設排序。** 成本評價有 item category「H」與 cost component「E」兩種角度、欄位數量不同，程式沒排序就會一下抓 H、一下抓 E，成本結果不穩定（該案結論是固定抓 H）。所有「取第一筆」的邏輯都要先明確排序。
2. **條件用列舉（多筆 EQ）比用區間（BT）安全**：區間比字典序不比業務語意，號碼段不連續、ALPHA 前導零、編碼規則改過就會出錯。
3. **先找標準，再想客製**：標準設定 → BAdI → Enhancement Point → 修改標準。

---

## 內容品質底線

- 不可遺漏 TCODE、資料表、欄位、函數／BAPI、類別、練習題編號、老師的口訣
- 教材有錯要改正並說明原本錯在哪
- 每章至少 8 小節、8 段程式碼
- 講義只有截圖的地方，補成可操作步驟並標 `<span class="src">（依講義步驟整理）</span>`
- 不確定就查 SAP 官方文件並附出處，不要瞎掰
