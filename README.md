# AITuber System - ホタル

YouTubeライブストリーム用のAI配信者システムです。16歳の女子学生「ホタル」として、視聴者のコメントに自動で返答し、音声合成で話すAITuberシステムです。

## 機能

- YouTubeライブストリームのコメント読み取り
- OpenAI GPTを使用したコメントへの自動返答
- VoiceVoxを使用した音声合成
- OBSでのコメント・返答表示
- 音声デバイスでの再生

## 必要な外部サービス・ソフトウェア

### 必須
- **VoiceVox**: 音声合成エンジン
  - [VoiceVox公式サイト](https://voicevox.hiroshiba.jp/)からダウンロード・インストール
  - ローカルサーバー（デフォルト: `localhost:50021`）で起動する必要があります
- **OBS Studio**: 配信ソフトウェア
  - WebSocket接続プラグインの設定が必要
- **OpenAI API**: GPTによる返答生成
  - OpenAI APIキーが必要

### 推奨
- **VoiceMeeter**: 音声ルーティング（OBSとの音声連携）

## インストール

### 1. Pythonの仮想環境を作成

```bash
python -m venv .venv
```

### 2. 仮想環境を有効化

**Windows:**
```cmd
.\.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. 依存関係をインストール

```bash
pip install -r requirements.txt
```

注意: requirements.txtに依存関係の競合がある場合は、以下の主要パッケージを個別にインストールしてください：

```bash
pip install pytchat obsws-python langchain-openai sounddevice soundfile python-dotenv
```

## 設定

### 1. 環境変数ファイルの作成

`.env.example`をコピーして`.env`ファイルを作成し、以下の設定を行ってください：

```bash
cp .env.example .env
```

### 2. .envファイルの編集

```env
# OBSの設定
OBS_WS_URL=ws://localhost:4455
OBS_WS_HOST=localhost
OBS_WS_PORT=4455
OBS_WS_PASSWORD=your_obs_websocket_password

# OpenAI API設定
OPENAI_API_KEY=sk-your_openai_api_key_here

# 音声出力デバイス設定
OUTPUT_DEVICE_NAME=VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)

# YouTube動画ID（ライブストリーム）
VIDEO_ID=your_youtube_live_video_id
```

### 3. 各種サービスの設定

#### VoiceVox
1. VoiceVoxを起動
2. デフォルトでは`localhost:50021`で動作

#### OBS Studio
1. OBS WebSocketプラグインを有効化
2. WebSocket設定でパスワードを設定
3. テキストソース「question」と「answer」を作成（コメントと返答表示用）

#### YouTube
1. ライブストリームを開始
2. ライブストリームのURLからVIDEO_IDを取得
   - 例: `https://www.youtube.com/watch?v=VIDEO_ID` の `VIDEO_ID` 部分

## 使用方法

### 1. 外部サービスの起動
- VoiceVoxを起動
- OBS Studioを起動し、WebSocket設定を確認
- YouTubeライブストリームを開始

### 2. AITuberシステムの起動

```bash
python main.py
```

### 3. 動作確認
- YouTubeライブストリームにコメントを投稿
- AIが「ホタル」として返答を生成
- OBSにコメントと返答が表示
- VoiceVoxで音声が生成・再生

## キャラクター設定

**ホタル**（16歳・女子学生）
- 職業: 学生
- 趣味: 睡眠、夜の散歩
- 性格: 他人思い、優柔不断、おっちょこちょい
- 出身: 東京
- 好きな食べ物: おすし
- 嫌いな食べ物: なす

## トラブルシューティング

### よくある問題

1. **VoiceVox接続エラー**
   - VoiceVoxが起動していることを確認
   - ポート50021が使用可能であることを確認

2. **OBS WebSocket接続エラー**
   - OBS WebSocketが有効になっていることを確認
   - .envファイルのパスワード・ポート設定を確認

3. **YouTube コメント取得エラー**
   - VIDEO_IDが正しいことを確認
   - ライブストリームが実際に配信中であることを確認

4. **音声出力エラー**
   - OUTPUT_DEVICE_NAMEが正しいデバイス名であることを確認
   - `python -m sounddevice`で利用可能なデバイスを確認

## 開発・テスト

### 個別コンポーネントのテスト

```bash
# VoiceVox接続テスト
cd src
python voicevox_adapter.py

# OBS接続テスト
python obs_adapter.py

# OpenAI接続テスト  
python opneai_adapter.py
```

### 仮想環境の無効化

```bash
deactivate
```

## ライセンス

このプロジェクトの詳細なライセンス情報については、リポジトリを確認してください。

## 注意事項

- OpenAI APIの使用には料金が発生します
- YouTubeのAPIレート制限にご注意ください
- VoiceVoxは個人利用・商用利用の規約を確認してください
