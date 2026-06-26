# Writing Policy

書き方の方針はここにまとめます。

## 基本

- 読む人に必要な情報から書く。
- root READMEには細かい接続先や履歴を詰め込みすぎない。
- 古くなりやすい接続先、状態、確認結果には確認日を添える。
- 1ファイルは200行以内にする。

## 置き場所

- サークル概要、参加導線、連絡場所: `docs/community/`
- サーバー一覧、接続先、サーバー別情報: `docs/servers/`
- イベントの基本形と企画メモ: `docs/events/`
- 日付つきの活動記録: `docs/activity/timeline/`
- 接続できないときの報告導線: `docs/operations/`
- 構造や方針の判断: `docs/decisions/`
- 用語と参照元: `docs/reference/`
- リポジトリ構造や検証: `docs/repository/`

## サーバー情報

新しいサーバーを載せるときは、ID、表示名、管理・連絡先、参加条件、接続先、稼働状態、最終確認日を分かる範囲で書く。サーバー固有の詳細は `docs/servers/<server-id>/` に分ける。

## 用語

- Minecraft関連の固有名は [../reference/terminology.md](../reference/terminology.md) に合わせる。
- 文脈が明らかな箇所では `Java Edition`、`Bedrock Edition` と短くしてよい。
- `Simple Voice Chat` は省略せずに書く。
- GeyserとFloodgateは役割が違うため、必要なら分けて説明する。
