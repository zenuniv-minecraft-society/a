# Layout

## Root

- `README.md`: 参加者向けの入口
- `docs/`: 詳しいドキュメント
- `scripts/`: 検証スクリプト

## Docs

- `docs/community/`: 役割、連絡場所、コミュニティ説明
- `docs/servers/`: サークル関連サーバーのカタログとサーバー別情報
- `docs/events/`: イベント運用
- `docs/activity/`: 活動記録と時系列ログ
- `docs/operations/`: 問い合わせや運用情報
- `docs/decisions/`: 構造や方針の判断記録
- `docs/repository/`: リポジトリ作業ルール
- `docs/reference/`: 用語と参照元

## Activity

`docs/activity/timeline/YYYY/MM/DD/` に日付単位の記録を置きます。月や年にREADMEを置き、親から子へ辿れる状態を保ちます。

## README

ディレクトリが人間の入口になる場合、READMEを置きます。READMEは索引と境界条件を書き、詳細は子ファイルへ分けます。
