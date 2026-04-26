# gog Commands for Writing Insights

Exact commands for creating segment folders, insight Docs, and populating them with markdown-formatted content. All run through the `gog` CLI (v0.12.0+).

## Root folder IDs

| Org | Root Folder ID | Account |
|---|---|---|
| **Brain Bridge** | `1NtO0j9Y85VlYBfJHu7vCzOZDFVdIth0g` | `aaron@brainbridge.app` |
| **AI Trailblazers** | `1HZ71XysToA6WY4YIi7ubNfn_K3c9jenI` | `aaron@aitrailblazers.org` |

The AITB root is on the shared drive `0AIkaB4BxP-erUk9PVA`, so the whole AITB team can access and edit insights.

## Check if a segment folder exists

```bash
gog drive search "name='<segment-slug>' and mimeType='application/vnd.google-apps.folder' and '<root-folder-id>' in parents" --raw-query --account <account> --json
```

If the result has a folder, reuse its ID. Otherwise create one.

## Create a segment folder

```bash
gog drive mkdir "<segment-slug>" --parent <root-folder-id> --account <account>
```

Example:
```bash
gog drive mkdir "fractional-cfos-small-b2b" --parent 1NtO0j9Y85VlYBfJHu7vCzOZDFVdIth0g --account aaron@brainbridge.app
```

Returns the folder ID. Store it for the subsequent Doc creation.

## Create an insight Doc

```bash
gog docs create "<YYYY-MM-DD — short insight title>" --parent <segment-folder-id> --account <account>
```

Returns the Doc ID and link.

## Write markdown-formatted content to the Doc

Use the clear + placeholder + find-replace pattern. The `--format=markdown` flag renders headings, lists, emphasis, and code blocks correctly.

1. **Clear the doc** (in case it has any default content):
   ```bash
   gog docs clear <docId> --account <account> -y
   ```

2. **Write a placeholder**:
   ```bash
   gog docs write <docId> --text "PLACEHOLDER_CONTENT" --account <account>
   ```

3. **Replace the placeholder with the markdown file**:
   ```bash
   gog docs find-replace <docId> "PLACEHOLDER_CONTENT" --content-file <path-to-.md> --format=markdown --account <account>
   ```

The markdown file should be the insight content — the front-matter block, headline, paragraph, quote, and implications.

## Reading insights

### List all insight Docs in a segment folder

```bash
gog drive ls --parent <segment-folder-id> --account <account> --json
```

Returns titles (with dates) and Doc IDs.

### Read a specific insight Doc

```bash
gog docs read <docId> --account <account>
```

Returns the full text. Pipe through `head -30` if you only want the front matter + headline.

### Search insights across a segment

```bash
gog drive search "fullText contains '<query>' and '<segment-folder-id>' in parents" --raw-query --account <account> --json
```

Drive's full-text indexing covers Google Docs content (with some latency after writes).

## Creating or updating the segment definition Doc

If a segment folder doesn't have a `Segment Definition — <Segment Name>` Doc yet:

```bash
gog docs create "Segment Definition — <Segment Name>" --parent <segment-folder-id> --account <account>
```

Then write using the template from `references/segment-definition-template.md` via the same clear + placeholder + find-replace pattern.

To update an existing segment definition (full rewrite — the definition is the distillation, not an append-log):

```bash
gog docs clear <segment-definition-doc-id> --account <account> -y
gog docs write <segment-definition-doc-id> --text "PLACEHOLDER_CONTENT" --account <account>
gog docs find-replace <segment-definition-doc-id> "PLACEHOLDER_CONTENT" --content-file <path-to-updated-.md> --format=markdown --account <account>
```

Bump the `Last Updated` date and `Insight Count` in the front matter every time.

## Common failure modes

- **"accessible by" or permission errors** — usually means wrong `--account`. BB Docs belong to `aaron@brainbridge.app`; AITB Docs belong to `aaron@aitrailblazers.org`. They don't cross-read by default.
- **Shared drive issues for AITB** — always pass the shared drive folder as `--parent`, not a personal folder. The AITB root folder ID `1HZ71XysToA6WY4YIi7ubNfn_K3c9jenI` IS on the shared drive, so this works automatically when you use it as `--parent`.
- **find-replace not rendering markdown** — make sure you pass `--format=markdown`. Without it, the content is inserted as literal text including the hash symbols and YAML delimiters.
- **Placeholder string already exists in the file** — pick a distinctive placeholder like `PLACEHOLDER_CONTENT_X9Y2` if `PLACEHOLDER_CONTENT` might collide.

## File naming conventions

- Segment folders: kebab-case, descriptive, starts with org-relevant context.
  - Good: `fractional-cfos-small-b2b`, `roofing-contractors-tx-storm-chase`, `aitb-event-sponsors-midsize-tech`
  - Bad: `CFOs`, `customers`, `segment-1`
- Insight Docs: `YYYY-MM-DD — <short title>`. The em dash is intentional — it parses naturally in Drive search.
  - Good: `2026-04-24 — Jay R2P variable billing pushback`, `2026-04-18 — AccuLynx predictable-pricing pattern`
  - Bad: `Jay interview`, `insights`, `2026-04-24`
- Segment definition Doc: `Segment Definition — <Human-Readable Name>`. Always at the top of the folder.
