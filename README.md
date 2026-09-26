# ABAP 圖書館 · S/4HANA 版

把多年累積的 SAP ABAP 學習資料，整理成 **一個單檔、離線可開、可全文搜尋的 HTML 技術庫**。
所有程式碼都已改寫為 **SAP S/4HANA 1809（ABAP 7.53）以後**可直接使用的現代 ABAP 寫法。

> 線上閱讀：https://tocasper-eng.github.io/abap/
> 推到 `main` 後由 GitHub Actions 自動建置（`src/build.py`）、機密掃描、瀏覽器測試並部署 Pages。
> 想離線閱讀，就在線上版按「另存網頁」，或本機執行 `cd src && python build.py` 產生單檔 `index.html`。

---

## 內容

| 部 | 章 | 主題 |
|---|---|---|
| 導覽 | ch00 | 總覽、四部曲學習路線、體例、TCODE 與資料表速查 |
| 第一部 · 資料字典 | ch01-1 ~ ch01-4 | 編寫第一支程式（SE38 / Package / Request / STMS）、ABAP 資料字典、三層 VIEW 與重要主數據、SQVI 與 SQ01 Query |
| 第二部 · 內表與 SQL | ch02-1 ~ ch02-4 | 基本語法與日期字串、內表 / ABAP SQL / 7.40+ 新語法、ALV 報表、模組化編程 |
| 第三部 · 視窗報表與增強 | ch03-1 ~ ch03-4 | 選擇畫面、OOALV 與 Screen 設計、User Exit 與 Customer Exit、BAdI 與 Enhancement Framework |
| 第四部 · 進階技巧 | ch04-1 ~ ch04-4 | RFC 與 BAPI、Dialog 對話式程式、SmartForms、BDC / Mail / FTP / 背景作業 |
| 第五部 · 原廠教材專區 | ch05-0 ~ ch05-25 | 强晟 19 本 BC 課程筆記 × SAP 原廠教材（L28、L29）：BC100～BC490、BC4xx 表單三部曲、IDoc/AIF、NET310 Web Dynpro、SAPNW，每章附原教材頁碼對照與勘誤 |
| 第六部 · 實戰專題 | ch06-1 ~ ch06-3 | 除錯的絕招：開發者除錯實戰、顧問的除錯術、資料追蹤與效能調優實戰 |
| 第七部 · 程式範例庫 | ch07-1 ~ ch07-7 | ABAP OOP 原則．模式．實踐：134 支範例改寫為現代語法（類別、繼承多型、SOLID、設計模式、進階技術、綜合實戰） |
| 第八部 · 實戰源碼庫 | ch08-1 ~ ch08-8 | 36 套真實專案程式拆解：增強、表單列印與寄信、FI/MM/SD 報表、主資料批導、外部介面整合（機密資訊已全部去識別化） |
| 附錄 | ap-01 | 舊語法 → S/4HANA 現代寫法速查 |

**規模**：62 章 · 1182 個小節 · 1111 段程式碼 · 706 則 S/4HANA 注意事項 · 434 則實務技巧

## 功能

- 側欄四部曲目錄，展開到小節層級
- 全文搜尋（按 `/` 快速聚焦），可搜語法、TCODE、資料表、函數名
- ABAP 語法自動上色、每段程式碼一鍵複製
- 深色 / 淺色模式、單章列印、上一章／下一章
- 單檔自含，無外部相依、無 CDN、離線可用

## 程式碼標準

一律使用 S/4HANA 1809+ 的現代寫法：

- 內嵌宣告 `DATA( )` / `@DATA( )`、ABAP SQL 主機變數一律加 `@`、SELECT 明列欄位
- 建構式運算 `VALUE #( )`、`CORRESPONDING #( )`、`REDUCE`、`FOR`、`COND`、`SWITCH`、`NEW`
- 字串範本 `|{ }|`、表格運算式 `it[ k = v ]`、`line_exists( )`
- ALV 以 `CL_SALV_TABLE` 為主，需編輯或細控事件才用 `CL_GUI_ALV_GRID`
- 例外一律 class-based（`TRY … CATCH cx_…`）

不再使用：`TABLES:`、`WITH HEADER LINE`、`OCCURS 0`、`MOVE`、`ADD/SUBTRACT`、`SELECT … ENDSELECT`、
無 `@` 的主機變數、`REUSE_ALV_GRID_DISPLAY`、`EXEC SQL`、新程式中的 `FORM/PERFORM`。
舊寫法只出現在對照表與明確標示的反例中。

## 從原始檔重新建置

```
src/
  sections/     每章一個 HTML 片段（純 <section>…</section>）
  template.html 外殼：CSS + 導覽 + 搜尋 + ABAP 上色 + 複製按鈕
  build.py      依 PARTS 順序把片段組進 template.html
```

```bash
cd src && python3 build.py     # 產生 ../index.html
```

新增章節時：把片段放進 `src/sections/`，並在 `src/build.py` 的 `PARTS` 加上章節代號。
完整的寫作規範、標籤白名單、程式碼標準見 [`CLAUDE.md`](CLAUDE.md) 與 [`SKILL.md`](SKILL.md)。

## 授權與來源

內容整理自個人的 SAP ABAP 教學講義與實務筆記，供個人與教學查閱使用。
SAP、S/4HANA、ABAP 等為 SAP SE 之商標。原始教材（PDF、docx、影片）因版權未納入本 repo，
已在 `.gitignore` 排除。
