# Substack Posts API

List the posts of any Substack publication with likes, comments, restacks, word counts and authors as JSON.

Powered by [Serpent API](https://apiserpent.com). Full reference: **[Substack Posts API docs](https://apiserpent.com/substack-api)**.

## Quick start

1. Get an API key at [apiserpent.com](https://apiserpent.com). Every account starts with 10 free API calls.
2. Call the endpoint with your key in the `X-API-Key` header:

```bash
curl -G "https://apiserpent.com/api/substack/posts" \
  --data-urlencode "publication=astralcodexten" \
  --data-urlencode "sort=top" \
  -H "X-API-Key: $SERPENT_API_KEY"
```

## Endpoint

`GET https://apiserpent.com/api/substack/posts`

| Parameter | Required | Description |
| --- | --- | --- |
| `publication` | Yes | Substack name (`astralcodexten`), a `substack.com` address, or a custom domain |
| `sort` | No | `new` (default) or `top` |
| `cursor` | No | `next_cursor` from the previous response |

## Response

`success`, `publication`, `sort`, `posts[]` (up to 25), `next_cursor`. Each post has `id`, `title`, `subtitle`, `url`, `published_at`, `audience`, `type`, `tags`, `word_count`, `likes`, `comments`, `restacks`, `cover_image`, `authors[]`, `excerpt`.

See the [docs](https://apiserpent.com/substack-api) for the complete field list and sample responses.

## Examples

| File | Language | Run |
| --- | --- | --- |
| [`example.py`](example.py) | Python 3 (`pip install requests`) | `SERPENT_API_KEY=sk_live_... python example.py` |
| [`example.mjs`](example.mjs) | Node.js 18+ (no dependencies) | `SERPENT_API_KEY=sk_live_... node example.mjs` |

## Use cases

- Newsletter research and benchmarking
- Content trend analysis
- Feeding posts into RAG or summarisation pipelines

## More from Serpent API

- [Serpent API docs](https://apiserpent.com/docs) - Google, Bing, Yahoo, DuckDuckGo and Brave search, plus AI rank tracking
- [All SDKs and tools on GitHub](https://github.com/apiserpent)

## License

MIT
