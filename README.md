# 中華メーカー風 商品説明ジェネレーター
生成AIを用いて、中華メーカー風の商品説明文を生成します。

## 動作環境
- Python 3.8以上
- 必要なライブラリは `requirements.txt` に記載

## 環境変数の設定（APIキーの設定）
このプロジェクトではOpenAIのAPIキーが必要です。
Streamlitの `secrets.toml` に設定してください。

1. `.streamlit/` ディレクトリを作成
   ```bash
   mkdir -p .streamlit
   ```

2. 上記ディレクトリ内に`secrets.toml` ファイルを作成し、APIキーを設定
   ```toml
   [general]
   OPENAI_API_KEY = "あなたのAPIキー"
   OPENAI_API_MODEL = "使用するモデル"
   ```

## インストール方法
### 1. リポジトリをクローン
```bash
git clone https://github.com/KobaSxun/chinese_description_generator.git
cd chinese_description_generator
```

### 2. 必要なライブラリをインストール
```bash
pip install -r requirements.txt
```

## 使い方
### 1. Streamlitアプリを起動
```bash
streamlit run app.py
```

### 2. ブラウザでアクセス
起動後、ブラウザで `http://localhost:8501` にアクセスすると、アプリのUIが表示されます。

## 貢献
バグ報告や機能追加の提案があれば、IssueやPull Requestをお待ちしています！
