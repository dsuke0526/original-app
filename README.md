# original-app(mangakataro)

## 説明
manngakataroの始め方
### 必要なライブラリ
requirements.txt参照
### ライブラリなどのインストール方法
 
```bash
pip install -r requirements.txt
git clone https://github.com/dsuke0526/original-app.git
```
### 基本的な使い方
仮想環境
```bash
python -m venv myvenv
myvenv\Scripts\activate
```
Djangoのインストール
```bash
pip install -r requirements.txt
```
プロジェクトの作成
```bash
django-admin.exe startproject mysite .
python manage.py migrate
```
ウェブサーバを起動
```bash
python manage.py runserver
```
#### 補足
requirements.txt
Django~=3.2.15
