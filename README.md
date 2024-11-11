# Political_Wing_Detector
# 政黨粉專側翼判斷器 (大三上)

## 主題說明
在當前台灣的社會中，充斥著各個政黨的水軍和側翼粉專所帶來的言論炒作和誤導現象。為了幫助使用者判斷粉絲專頁的政治傾向，我們開發了這款「側翼粉專判斷器」。

## 功能介紹
本專案透過已知政治傾向的粉絲專頁資料進行模型訓練，藉此讓使用者可以判斷特定粉專的內容傾向。系統架構如下：

1. **資料蒐集**：
    - 選取四個具有代表性的側翼粉專：
        - 國民黨：`藍色力量`、`反蔡英文粉絲團`
        - 民進黨：`只是堵藍`、`謝立聖插畫`
    - 利用爬蟲技術抓取各粉專文章內容，並依政治傾向標記為 1（藍）或 2（綠）。
    - 針對 Facebook 動態網頁，使用 JavaScript 和滑動模擬技術實現內容爬取，將結果儲存為 CSV 檔。

2. **資料預處理與模型訓練**：
    - 對爬取的文章資料進行斷句和分詞處理，轉換為模型可讀取的格式。
    - 使用羅吉斯回歸模型（Logistic Regression）訓練並驗證，準確率良好後完成模型建構。

3. **判斷功能**：
    - 使用者將疑似側翼的粉絲專頁內容貼上，系統會對其進行格式化處理並判斷其政治傾向。

## 開發過程中的挑戰
- 許多粉專僅發表圖片或搭配少量文字，導致爬取內容不完整，模型訓練準確度受限。
    - 未來計劃增加圖片文字辨識功能以提高準確率。
- 特定詞句的判斷挑戰：
    - 示例一：「可憐」僅作為輸出結果而非特定判斷詞。
    - 示例二：老師測試「我愛蘇貞昌」（偏綠）與「蘇貞昌可憐」（偏藍），證明模型的多樣性處理尚可。
    - 未來將引入褒貶辭典及政治詞彙辭典，改善情緒與詞彙的判斷準確性。

## 結果展示
![image](https://github.com/user-attachments/assets/1407ce35-4fb1-43fa-85b0-8ea449b29ba7)

 - 輸出為 `偏藍` 或 `偏綠`，表示該內容的預測政治傾向。

## 未來發展
- 增加圖片文字識別功能，進一步強化判斷準確度。
- 導入情感與政治詞彙辭典，以更精確地解析語義。
- 優化模型，提升對短文本和單字判斷的準確度。


