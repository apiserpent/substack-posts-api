[English](README.md) | **简体中文**

# Substack 文章 API

获取任意 Substack 刊物的文章列表，以 JSON 返回点赞、评论、转发、字数和作者信息。

由 [Serpent API](https://apiserpent.com) 提供。完整文档：**[Substack Posts API 文档](https://apiserpent.com/substack-api)**。

## 快速开始

1. 在 [apiserpent.com](https://apiserpent.com) 注册并获取 API Key，每个账号赠送 10 次免费调用。
2. 在请求头 `X-API-Key` 中带上你的 Key 调用接口：

```bash
curl -G "https://apiserpent.com/api/substack/posts" \
  --data-urlencode "publication=astralcodexten" \
  --data-urlencode "sort=top" \
  -H "X-API-Key: $SERPENT_API_KEY"
```

## 接口

`GET https://apiserpent.com/api/substack/posts`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `publication` | 是 | 刊物名称（如 `astralcodexten`）、`substack.com` 地址或自定义域名 |
| `sort` | 否 | `new`（默认，最新优先）或 `top`（最热优先） |
| `cursor` | 否 | 上一次响应中的 `next_cursor`，用于翻页 |

## 返回结果

顶层字段：`success`、`publication`、`sort`、`posts[]`（每次最多 25 篇）、`next_cursor`。每篇文章包含 `id`、`title`、`subtitle`、`url`、`published_at`、`audience`、`type`、`tags`、`word_count`、`likes`、`comments`、`restacks`、`cover_image`、`authors[]`、`excerpt`。

完整字段列表和响应示例请参阅[文档](https://apiserpent.com/substack-api)。

## 示例代码

| 文件 | 语言 | 运行方式 |
| --- | --- | --- |
| [`example.py`](example.py) | Python 3（`pip install requests`） | `SERPENT_API_KEY=sk_live_... python example.py` |
| [`example.mjs`](example.mjs) | Node.js 18+（无需依赖） | `SERPENT_API_KEY=sk_live_... node example.mjs` |

## 应用场景

- Newsletter 调研与对标分析
- 内容趋势分析
- 为 RAG 或摘要流程提供文章数据

## Serpent API 的更多能力

- [Serpent API 文档](https://apiserpent.com/docs)：Google、Bing、Yahoo、DuckDuckGo 和 Brave 搜索结果，以及 AI 引用排名跟踪
- [GitHub 上的全部 SDK 与工具](https://github.com/apiserpent)

## 许可证

MIT
