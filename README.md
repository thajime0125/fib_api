# fib_api
フィボナッチ数列の任意の第n項を返すREST APIをFastAPIを用いて実装

## 使用言語・環境
- python: 3.11.5
- poetry: 1.6.1
- pyenv: 2.3.25

## 使用ライブラリ
- fastapi: ^0.103.0
- uvicorn: ^0.23.2
- httpx: ^0.24.1

## 構成
- main.py
    - 主な処理を実装したファイル
- test_main.py
    - ユニットテスト用ファイル

## ローカル実行手順(poetry+pyenv)
1. Clone
    ```
    git clone https://github.com/thajime0125/fib_api.git
    ```
2. Setup
    ```
    cd fib_api
    pyenv install 3.11.5
    poetry env use 3.11.5
    poetry install
    ```
3. Run
    ```
    poetry run uvicorn main:app
    ```
4. Get Request
    ```
    curl 'http://localhost:8000/fib?n=3'
    ```
    またはブラウザで http://localhost:8000/fib?n=3 にアクセス