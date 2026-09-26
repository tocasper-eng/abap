# CLAUDE.md — ABAP 圖書館專案說明

給未來的 Claude（以及未來的我）：這份檔案說明「ABAP 圖書館」是什麼、長什麼樣、怎麼繼續往下編。
**動手改之前，請先完整讀完本檔。**

---

## 1. 這個專案是什麼

把 `Dropbox\09_SAP_AB_ABAP編程` 底下累積多年的 SAP ABAP 學習資料（PDF、docx、pptx、影片、原始碼），
整理成 **一個單檔、可離線開啟、可全文搜尋的 HTML 圖書館**，當作隨時查閱的個人技術庫。

- 擁有者：Casper（GitHub `tocasper-eng`），SAP 顧問／講師
- 產出主檔：`ABAP圖書館_S4HANA.html`（放在 `09_SAP_AB_ABAP編程` 根目錄）
- 語言：**繁體中文**（SAP 專有名詞、程式碼保持英文原樣）
- 語法基準：**SAP S/4HANA 1809（ABAP Platform 1809，SAP_BASIS 7.53）以上**

---

## 2. 目前的內容（v2：核心版 ＋ 原廠教材專區）

第一版取材自 `00_SAP_DOC\` 的十六本自編教材（2509 版），已完成：

| 部 | 章 | 主題 |
|---|---|---|
| 導覽 | ch00 | 總覽、學習路線、體例、TCODE 與資料表速查 |
| 第一部 | ch01-1 ~ ch01-4 | 編寫第一支程式／資料字典／三層 VIEW 與主數據／SQVI SQ01 Query |
| 第二部 | ch02-1 ~ ch02-4 | 基本語法／內表與 ABAP SQL 與 7.40+ 新語法／ALV／模組化 |
| 第三部 | ch03-1 ~ ch03-4 | 選擇畫面／OOALV 與 Screen／User Exit 與 Customer Exit／BAdI 與 Enhancement Framework |
| 第四部 | ch04-1 ~ ch04-4 | RFC 與 BAPI／Dialog 對話式程式／SmartForms／BDC MAIL FTP 背景作業 |
| 第五部 A | ch05-0、ch05-25、ch05-1 ~ ch05-5 | 專區導覽／BC100 程式設計入門（L29）／BC400 Workbench／BC401 ABAP Objects（併 2007 BC404 OO）／BC402 程式設計技術／BC403 除錯／BC404 ADT |
| 第五部 B | ch05-6 ~ ch05-10 | BC405 報表／BC406 進階清單／BC407 QuickView・SAP Query／BC410 Dynpro／BC412 Enjoy Controls |
| 第五部 C | ch05-11 ~ ch05-17 | BC414 資料庫更新・LUW・鎖／BC415 RFC・BAPI／BC420 資料傳輸／BC425 增強與修改／BC427 Enhancement Framework／BC430 資料字典／BC440 ITS 與現代替代 |
| 第五部 D | ch05-18 ~ ch05-20 | BC460 SAPscript／BC470 SmartForms／BC480 Adobe Forms |
| 第五部 E | ch05-21 ~ ch05-24 | BC490 效能調校／IDoc 與 BIT750 AIF／NET310 Web Dynpro ABAP／SAPNW 平台概覽 |
| 第六部 | ch06-1 ~ ch06-3 | 實戰專題・除錯的絕招：開發者除錯實戰／顧問的除錯術（定位錯誤、找增強點）／資料追蹤與效能調優實戰 |
| 第六部 B | ch06-4 ~ ch06-8 | 實戰專題・專案實務案例：開發規範與系統移轉（命名規則、SE10/STMS、SE11 匯出、SCAL）／資料下載實戰（ZMMI0001、ZPPI0001、MARD→Excel）／缺料表與 MIGO 檢驗批／DBCO 與外部資料庫（ADBC、儲存程序）／介面輸出與財務程式（採購變更、VK11 FTP、ZFIP001） |
| 第六部 C | ch06-9 ~ ch06-13 | 實戰專題・累計心得：日期與時間處理大全（29 個函數）／找表的功夫（由欄位與畫面找表、常用表清單）／開發者基本功（SYST、使用者資訊、BC400 劃記與自己的工具庫）／ACDOCA 與 HR 資料表／資料匯出與分析（TXT、Power BI 與 Indirect Access、z-score） |
| 第七部 | ch07-1 ~ ch07-7 | 程式範例庫・ABAP OOP 原則．模式．實踐：例外與程序式基礎／類別與物件／封裝繼承多型／SOLID／設計模式／進階技術（RTTS、BAL、ALV、持久化、BAdI）／綜合實戰 |
| 第八部 | ch08-1 ~ ch08-8 | 實戰源碼庫・36 套專案程式：增強實例／SD 報價訂單發票表單（PayPal）／月對帳單與外貿單據／採購領料憑證表單與退料／FI 報表／MM・SD 報表／主資料與 BOM 途程批導／外部介面整合 |
| 第九部 | ch09-1 ~ ch09-5 | 模組二次開發案例：主機管理與開發導論（TCODE、權限、內部稽核）／MM 五案例（BAPI 讀庫存、Excel 更新前置時間、BAPI_PR_CREATE、採購確認、GR／IR 與重複發票）／PP：MRP Element 與工單報表 ZCO03／PP：物料修改日誌 ZMMQ0003 與插件位置 ZMMI0005／跨模組工具（資料表上下載、幣別小數位、QM 客製清單） |
| 第十部 | ch10-1 ~ ch10-5 | S/4HANA 新世代開發：CDS View 基礎（DDIC-based view 與 view entity）／CDS 進階（DCL、擴充、Analytics、OData、效能）／AMDP 與 SQLScript／RAP 基礎（managed、EML、1809 的 CDS＋BOPF 替代方案）／RAP 進階（驗證、決定、動作、draft、unmanaged 包裝 BAPI） |
| 附錄 | ap-01 | 舊語法 → S/4HANA 現代寫法速查 |

第五部（2026-09 新增）取材自 `L28_强晟_19本原廠教材筆記_含原廠教材\`：强晟 2007/2008 簡體筆記 19 本 ＋ SAP 原廠英文教材 Col15~Col19 19 份（含 IDoc guide）。
每章第一節是「單元 ↔ 强晟筆記頁碼 ↔ 原廠 Unit/Lesson 頁碼」對照表；各章已修正的教材錯誤都在文中註明。
注意：BIT750 是 AIF 課程不是 IDoc 課；2007 的 BC404 是 OO、新版 BC404 是 ADT。

`L29_原廠教材\`（9 份，2026-09-26 併入）多為同課其他版本：BC100 新開 ch05-25；BC400（Col16 2018、官方簡中 Col63 2009）→ ch05-1、BC410（官方簡中 Col63）→ ch05-9、BC425（Col92 2010）→ ch05-14、BC470（2006）→ ch05-19、BC490（2001、Col10 2017 掃描檔）→ ch05-21，各章以「L29 版本對照」表＋「L29 補充」小節呈現。掃描檔（無文字層）用 PyMuPDF 轉 PNG 再看圖。

第六部（2026-09-26 新增）取材自 `L35_SAP调试技术\`：29 份簡中／英文技術文章（docx 截圖已抽出給 agent 看圖整理）、《ABAP开发从入门到精通》第 6 章（掃描頁）、2 份 pptx；5 支 mp4（約 14GB）無法轉錄，只在 ch06-2 做檔名索引。

第七部（2026-09-26 新增）取材自 `L36_ABAP_OOP_SAMPLE-master\`：《SAP ABAP 面向对象程序设计 – 原则.模式.实践》隨書 134 支範例（第 1、2、4～9 章；第 3 章 UML 無範例）＋勘誤表。書本內文不在資料夾，講解由程式整理；每章第一節「範例索引」涵蓋全部範例編號；缺原始碼的全域類別依呼叫方式重建並標註。

第八部（2026-09-26 新增）取材自 `L31_ABAP36套源碼\`：某醫療器材公司實際上線的 38 個客製案例（txt/docx 原始碼、截圖、Excel 範本）。每案例依「業務情境 → 選擇畫面與輸出 → 程式架構 → 關鍵段落現代改寫 → 原程式問題 → 上線注意」拆解，不整支貼原始碼。
**資安規則（公開網站）**：素材含真實 API 金鑰、app_key、客戶 email、員工姓名與銀行帳號、公司名與網址，成品一律以佔位符取代；部署前必跑 `python src/secretscan.py src/sections/*.html`（只允許 `<APP_KEY>` 這類佔位符命中）。第六部是「實戰專題」，之後 15_累計心得 等實戰素材也可以放在這一部。

第六部 B（2026-09-26 新增）取材自 `09_ABAP二次開發_report_painter\15_實務案例\`：17 份 docx（其中 5 份幾乎只有截圖，已看圖整理成操作步驟），`ABAP_06_A_ABAＰ的發佈.avi` 只做註記。素材中的客戶公司名、內網 IP、FTP 帳號、DB 名稱都已改成佔位符，相關字串已加入機密清單。原程式大量使用 DBCO＋`EXEC SQL` 寫外部 SQL Server，一律改寫成 ADBC（`CL_SQL_CONNECTION`）。

第六部 C（2026-09-26 新增）取材自 `09_ABAP二次開發_report_painter\15_累計心得\`：txt／sql／xlsx／docx／PDF 共 16 檔。兩份 BC400（2020, Course Version 18）PDF 文字相同，只取 Casper 版的 37 個劃記放進 ch06-11（BC400 本體見 ch05-1）。`09_zscore`、`10_clustering` 是學生真實資料，一律改用合成資料 S01～S12；`11_ 下載TXT到 POWERBI.docx` 是第三方文章，只寫摘要並附出處；PDF 內的 email 已加入機密清單。ch06-12 修正了 Casper ACDOCA 筆記的欄位說明（KTOSL、LINETYPE、TSL／WSL、MANDT→RCLNT、KDAUF）；ch06-9 修正了素材三處錯誤，並回頭修正 ch02-1 速查表中兩個函數的參數名。

第九部（2026-09-26 新增）取材自 `09_ABAP二次開發_report_painter\09_0～09_9\`：實際有內容的只有 09_0 BASIS（3 份）、09_2 MM（新版五案例 docx 2023/10 為主，舊版四案例 PDF 2022/09 用來比對）、09_3 PP（PDF 與 docx 重複，Biz_52 = Biz_59；`11_ 下載TXT到 POWERBI` 已在 ch06-13）、09_9 QM（只有 12 支程式的目錄，ch09-5 依 SAP 標準整理成清單）。**09_1 SD、09_4 FI、09_5 CO、09_6 AA、09_7 HR 資料夾是空的**。`GBIKE` 是 SAP 大學聯盟的示範公司 Global Bike，不是客戶名稱。

第十部（2026-09-26 新增）**沒有本機素材**，全部依 SAP 官方文件撰寫（ABAP Keyword Documentation、SAP Help、SAP-samples GitHub），每節都附出處，5 章共約 170 個官方連結。每章開頭有版本門檻表；超過 1809 的語法都有 warn。查不到確切資料的地方標「未能確認，請以系統為準」（共約 40 處），不要把它們當成已查證的內容。RAP 以自建報價單 `ZQUOTE_H`／`ZQUOTE_I` → `ZI_Quote`／`ZC_Quote`／`ZBP_I_Quote`／`ZUI_QUOTE_O4` 貫穿，**ch10-4 的資料模型為準**，ch10-5 在其上新增 `RejectReason`、`SalesOrder`。狀態碼：N 新建、C 已結案、A 已接受、X 已拒絕。

規模：82 章、1517 個小節、1477 段程式碼、895 則注意事項、523 則實務技巧（v1 為 18 章／319 小節／398 段程式碼）。

### 尚未納入（下次擴充的優先順序）

1. ~~`09_ABAP二次開發_report_painter\15_實務案例\`~~（已完成，第六部 B ch06-4 ~ ch06-8）
2. ~~`09_ABAP二次開發_report_painter\15_累計心得\`~~（已完成，第六部 C ch06-9 ~ ch06-13）
3. ~~`09_ABAP二次開發_report_painter\09_1~09_9\`~~（已完成，第九部 ch09-1 ~ ch09-5；SD／FI／CO／AA／HR 資料夾為空，日後有素材再補）
4. ~~`L36_ABAP_OOP_SAMPLE-master\`~~（已完成，第七部 ch07-1 ~ ch07-7）
5. ~~`L31_ABAP36套源碼\`~~（已完成，第八部 ch08-1 ~ ch08-8）
6. ~~`L35_SAP调试技术\`~~（已完成，第六部 ch06-1 ~ ch06-3）
7. ~~L28、L29 原廠教材~~（v2 已完成，第五部）；尚待補 TAW10/11/12、HA100/300/400 的重點摘要
8. **全新主題**：~~CDS View、AMDP、RAP~~（已完成，第十部 ch10-1 ~ ch10-5）；尚待補 **ABAP Cloud**（Clean Core、released API、tier 1～3、Developer Extensibility）與 **Fiori Elements** 專章（目前只在 ch10-2、ch10-5 講到 UI 註解）

---

## 3. 檔案與建置流程

**唯一來源：GitHub [`tocasper-eng/abap`](https://github.com/tocasper-eng/abap)（公開 repo）。**
推到 `main` 之後，GitHub Actions（`.github/workflows/pages.yml`）會自動執行 build → secretscan → verify，全部通過才部署到
https://tocasper-eng.github.io/abap/ 。任一步失敗就不會發佈，線上仍是舊版。

兩種工作環境：

| 環境 | 適合做什麼 | 工作區 |
|---|---|---|
| **本機 Claude Code**（在 `09_SAP_AB_ABAP編程` 開啟） | 需要讀 Dropbox 原始教材（PDF、docx、原始碼）的擴充 | `%LOCALAPPDATA%\abap-library-src\repo`（GitHub 的 clone；不放在 Dropbox，避免 `.git` 被同步弄壞） |
| **claude.ai/code 雲端 session**（選 `tocasper-eng/abap` repo） | 不需要本機素材的工作：CDS／RAP 等新主題、修錯字、調整版面 | 雲端自動 clone；讀不到 Dropbox 教材 |

本機工作區不見的話，重新 clone 就好：`gh repo clone tocasper-eng/abap "$LOCALAPPDATA/abap-library-src/repo"`。
開工前先 `git pull`，因為可能有在雲端 session 做的修改。

**公開 repo 的資安規則**
- `secretscan.py` 要擋的機密字串清單本身也是機密，**絕不可入庫**。本機主檔在 `09_SAP_AB_ABAP編程\secretscan-deny.txt`，CI 則讀 repo secret `SECRETSCAN_DENY`。
  增刪清單時兩邊都要改：`gh secret set SECRETSCAN_DENY -R tocasper-eng/abap < secretscan-deny.txt`。
- 不要在 commit、CLAUDE.md、SKILL.md 寫入客戶名稱、個資或金鑰原文。
- 雲端 session 沒有清單檔，本機跑 secretscan 會失敗（exit 2）是正常的，交給 CI 檢查即可。

結構：

```
repo/
  .github/workflows/pages.yml   CI：建置、掃描、測試、部署 Pages
  CLAUDE.md            與 Dropbox 根目錄的 CLAUDE.md 保持一致
  .claude/skills/abap-library/SKILL.md   雲端 session 會自動載入；與 Dropbox 根目錄的 SKILL.md 保持一致
  index.html           建置產物，不入庫（.gitignore）
  src/
    sections/          每章一個 HTML 片段（純 <section>…</section>，無 head/style/script）
      ch00.html  ch01-1.html … ch04-4.html  ch05-0.html … ch05-25.html  ch06-1.html … ch06-3.html  ch07-1.html … ch07-7.html  ch08-1.html … ch08-8.html  ap-01.html
    template.html      單檔 HTML 的外殼：CSS + 導覽 + 搜尋 + ABAP 上色 + 複製按鈕
    build.py           把 sections/*.html 依 PARTS 順序組進 template.html，輸出 ../index.html
    secretscan.py      掃描片段中的金鑰、email、帳號等敏感資料
    verify.py          用本機 Chrome 做冒煙測試（章數、程式碼上色、搜尋、主控台錯誤）
```

**建置與驗證**（在 `repo/src` 下執行）：

```bash
python build.py                          # 產出 ../index.html，會印出章數／小節／程式碼統計
python secretscan.py sections/*.html     # 印出 CLEAN 才算通過（<APP_KEY> 這類佔位符不算命中）
PYTHONIOENCODING=utf-8 python verify.py  # 最後一行印出 OK 才算通過
```

`verify.py` 用 `channel='chrome'` 開 Chrome（`pip install playwright` 就夠，不必 `playwright install`；GitHub 的 ubuntu runner 也有預裝 Chrome）。

`build.py` 會自動做三件事，寫片段時不必自己處理：
- 移除 `<h2>` 上與 `<section id>` 重複的 id
- 幫沒有 id 的 `h3` / `h4` 自動補 id
- 依 `<h3>` 產生側欄的小節目錄

新增章節時，要同時在 `build.py` 的 `PARTS` 清單中加上章節代號，否則不會被組進去。

---

## 4. 寫作規範（擴充時必須遵守）

### 4.1 章節片段格式

```html
<section class="chapter" id="ch05-1" data-title="章節標題">
  <h2>第 5-1 章 標題</h2>
  <p class="lede">兩三句話說明這章解決什麼問題。</p>
  <div class="meta">
    <div><b>核心 TCODE</b><span class="tcode">SE38</span></div>
    <div><b>關鍵物件</b>MARA、CL_SALV_TABLE</div>
  </div>
  <h3 id="ch05-1-01">1. 小節標題</h3>
  …
  <h3 id="ch05-1-qa">練習與自我檢核</h3>
</section>
```

- **只用這些標籤**：section, h2, h3, h4, p, ul, ol, li, table/thead/tbody/tr/th/td, pre, code, div(class=note|tip|warn|meta), b, i, span(class=tcode|src|kw), a, br
- **不要** `style` 屬性、不要額外 class、不要 `<script>`
- 小節 id 一律 `章號-01`、`章號-02` … 最後一節用 `章號-qa`
- 程式碼：`<pre><code class="abap">…</code></pre>`，內容要 HTML escape（`&lt;` `&gt;` `&amp;`）
- 方塊：`<div class="note">`補充、`<div class="tip">`實務技巧、`<div class="warn">`S/4HANA 注意事項與常見錯誤
- 原講義只有截圖、內文是依 SAP 標準補寫的地方，標 `<span class="src">（依講義步驟整理）</span>`

### 4.2 程式碼標準（最重要）

**一律寫 S/4HANA 1809+ 可直接使用的現代 ABAP。**

必用：內嵌宣告 `DATA( )`／`@DATA( )`、ABAP SQL 主機變數一律加 `@`、SELECT 明列欄位、
字串範本 `| |`、`VALUE #( )`、`CORRESPONDING #( )`、`REDUCE`、`FOR`、`COND`、`SWITCH`、`NEW`、
`line_exists( )`、`FIELD-SYMBOL( )` 內嵌宣告、`CL_SALV_TABLE`（需編輯或細控才用 `CL_GUI_ALV_GRID`）、
class-based exception（`TRY … CATCH cx_…`）。

禁用（若原教材是舊寫法，直接改寫，不要保留舊程式碼；只在對照表中以文字說明）：
`TABLES:`、`WITH HEADER LINE`、`OCCURS 0`、`MOVE`、`ADD/SUBTRACT/MULTIPLY/DIVIDE`、`COMPUTE`、
`SELECT … ENDSELECT`、沒有 `@` 的主機變數、`REUSE_ALV_GRID_DISPLAY`、`EXEC SQL`、
以及在新程式中用 `FORM/PERFORM`。

用到 7.54 以上才有的語法（`+=`、`DEFINE VIEW ENTITY`、PCRE 等）時，要標明版本門檻。

### 4.3 內容要求

- **不可遺漏重要資料**：TCODE、資料表名、欄位名、函數／BAPI 名、類別名、練習題編號、老師強調的坑與口訣，全部保留
- 教材有錯就修正，並在該處說明原本寫什麼、為什麼錯
- 每章至少 8 個小節、8 段程式碼；核心章節（內表 SQL、ALV、Dialog）請寫得更完整
- 不確定的細節不要瞎掰，寧可寫「講義此處為截圖操作，重點是 ⋯」；必要時上網查 SAP 官方文件並附出處

---

## 5. Casper 的實務經驗（寫內容時要一再強調）

這些是專案上真的踩過的坑，任何相關章節都應該再提一次：

1. **HANA 沒有預設排序。** 成本評價同時存在 item category「H」與 cost component「E」兩種角度，兩者的成本構成欄位數量不同；程式沒排序時一下抓到 H、一下抓到 E，成本結果就會不穩定。任何「取第一筆」的邏輯都必須先明確排序（該案最後的結論是固定抓 H）。
2. **條件用列舉（多筆 EQ）比用區間（BT）安全。** 區間比的是字典序不是業務語意，遇到號碼段不連續、ALPHA 前導零、編碼規則改過就會漏抓或多抓。
3. **先找標準，再想客製。** 標準設定 → BAdI／Enhancement Spot → Enhancement Point → 修改標準，每往右一步升級成本高一個量級。

---

## 6. 交付方式

建置和驗證都通過後，依序執行：

1. **git commit**，訊息沿用 `ABAP 圖書館 v2.x：新增…` 的格式。
2. **git push**（先問過使用者，因為 push 就等於公開發佈）。接著用 `gh run watch -R tocasper-eng/abap` 盯 CI，綠燈才算發佈完成；紅燈就看 log 修正後再推。
   - 雲端 session 通常推到 `claude/…` 分支，不會觸發部署。要發佈就開 PR 合併到 `main`。
3. **本機才需要做**：
   - 把 `repo/index.html` 複製成 `09_SAP_AB_ABAP編程\ABAP圖書館_S4HANA.html`（離線閱讀用）
   - `CLAUDE.md`、`SKILL.md` 有改的話，同步到 Dropbox 根目錄和 `C:\Users\tocas\.claude\skills\abap-library\SKILL.md`

已停用：`deploy.ps1`（已改名為 `deploy.ps1.old`）和 `abap-repo.zip`（保留舊版 git 歷史當封存，不再更新）。

---

## 7. 對話習慣

- 使用者偏好**繁體中文**回覆
- 動手前先確認範圍（要整理哪一塊、深度到哪），但不要問得太瑣碎
- 大工程請用 subagent 平行處理：一個 agent 負責一章，把片段寫進 `sections/`，只回傳簡短摘要，不要把 HTML 貼回主對話（會爆 context）
- 每次擴充後都要重新 `python build.py` 並跑 `verify.py`，不要只改片段就交付

---

_最後更新：2026-09-26 · v2.8（82 章，含 L29、L35、L36、L31、15_實務案例、15_累計心得、09_x 模組案例、第十部 CDS／AMDP／RAP）· GitHub 為唯一來源，CI 自動部署 Pages_
