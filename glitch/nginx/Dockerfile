# ステージ1: フロントエンドのビルド
FROM node:lts-buster-slim AS frontend-builder

WORKDIR /app

# フロントエンドの依存関係をコピー
COPY frontend/app/glitch/package*.json ./glitch/

WORKDIR /app/glitch

# 依存関係をインストール
RUN npm install

# フロントエンドのソースコードをコピー
COPY frontend/app/glitch .

# フロントエンドをビルド
RUN npm run build

# ステージ2: NGINXサーバー
FROM nginx:alpine

# NGINXの設定ファイルをコピー
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

# ビルドされたフロントエンドの静的ファイルをコピー
COPY --from=frontend-builder /app/glitch/dist /usr/share/nginx/html