macで動かす場合、まずはseleniumをインストール

```
 pip3 instal selenium    
```

PCにインストールされたchromeとバージョンと一致するchromedriverをダウンロードしておきます。 
[chromedriver](https://chromedriver.chromium.org/downloads)  
```base/webdrivers```に配置しておいてください  
```
mv ~/Downlaod/chromedriver ./base/webfrivers 
```

日本Seleniumユーザーコミュニティさまのテストサイトを利用しています。  
感謝

[テスト用サイト](http://www.selenium.jp/test-site)


実行します

```
pyhon3 ./tests/reserveApp.py
```