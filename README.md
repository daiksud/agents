# daiksud/agents

[APM](https://microsoft.github.io/apm/) を利用した、AIエージェント向けの
共有スキルと指示のパッケージです。

## 内容

- エージェントが作成するコミットとプルリクエスト向けの Conventional Commits ガイド
- エージェントスキルの作成・改善に使用する Anthropic の `skill-creator` スキル

`skill-creator` スキルは、パッケージのインストール時に
[`anthropics/skills`](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
から解決されます。

## インストール

```bash
apm install daiksud/agents
apm compile --target codex
```

`apm install` はパッケージと依存関係を配置します。Codexで
`.apm/instructions/` の内容を利用するには、続けて
`apm compile --target codex` を実行してください。Codexが参照する
ルートの `AGENTS.md` が生成されます。
