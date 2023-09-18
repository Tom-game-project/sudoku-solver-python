# 数独ソルバー

## 速度を向上させたい

- v1

- v2

  - v2_1

  ```diff
  - True in [0 in i for i in arr]
  
  + any([0 in i for i in arr])
  ```

  結果少し早くなった

  - v2_2

- v3

  内包表記
  
  setの削除
