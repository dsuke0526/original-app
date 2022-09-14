# original-app(mangakataro)

## 説明
manngakataroの始め方
### 必要なライブラリ
requirements.txt
Django~=3.2.15
### 基本的な使い方
クローン
```bash
git clone https://github.com/dsuke0526/original-app.git
```
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
