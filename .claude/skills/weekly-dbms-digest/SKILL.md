---
name: weekly-dbms-digest
description: Build a weekly, ad-free digest of database internals, research, and cutting-edge tech — new techniques and inventions in open-source and commercial engines (SQL Server, Oracle, MySQL, etc.), real-world migration experience reports, and community discussion. Use this skill whenever the user asks for the "weekly digest", "Postgres digest", "DBMS digest", "database news roundup", "what happened in databases this week", or when a scheduled task asks to generate the weekly database digest. The skill curates high-signal sources, finds items published in the last 7 days, ruthlessly filters out advertising / vendor promotion / marketing fluff, fact-checks claims, and emits a terse headline + one-line list of links. It also discovers and records new emerging sources each run so the source list stays fresh.
---

# Weekly DBMS Digest

Produce a short, high-signal weekly digest of what actually happened in the database world: new technologies, real engineering, cutting-edge inventions, and research. This explicitly includes new techniques and inventions in **commercial engines** (SQL Server, Oracle, MySQL, DB2, etc.) and **real-world migration experience** reports — the reader cares about what other databases are doing and what actually happens when people move data between them. The reader is a database internals developer who is allergic to marketing. The single most important job of this skill is to **separate signal from sales**: surface genuine technical/research content and discard (or clearly flag) advertisement, company promotion, and marketing material.

The output is deliberately terse: each item is a **headline + one line** with a link. The reader wants to scan 15–30 items in two minutes and click into the 3–4 that matter.

## Workflow

Follow these steps in order. Don't skip the filtering and fact-check steps — they are the whole point.

### 0. Fetching technique (read this first — it unblocks everything below)

`web_fetch` will only retrieve a URL that has already appeared **in a prior search
result or a previously fetched page** ("provenance"). A cold `web_fetch` of a feed or
archive URL you just typed will fail with *"URL not in provenance set"*. This is the single
biggest reason past runs skipped the non-English sources. Defeat it
deliberately, every run:

1. **Seed with a search.** Run a `WebSearch` whose results contain the index/feed/page you
   want (e.g. search the site name or topic). The result
   URLs are now fetchable.
2. **Chain through fetched pages.** Every link **on a page you fetched** is itself now
   fetchable. So fetch an index page, then fetch the items it links to, then their
   Previous/Next/thread links — you can walk an entire week this way without another search.
3. **Feeds the same way.** To read an RSS/Atom feed whose URL won't fetch cold, first fetch
   (or search) the site's HTML page; its `<link rel=alternate>`/feed URL becomes fetchable.
4. **JS-heavy or empty results → browser.** If a fetch returns an empty shell or a loading
   page (client-rendered sites: modb.pro, Reddit `.rss`, Lobsters tag feed), switch to
   the Claude-in-Chrome browser tools to render it. Never `curl`/script around a failed fetch.
5. **If a page is too large**, it is saved to a file path the tool reports — but that path is
   on the host, not in the sandbox mount, so you usually can't open it. Prefer fetching a
   narrower URL (a single thread, a single month) over a giant index.

### 1. Establish the time window

The digest covers the **last 7 days** by default (or the span since the previous digest if the user gives one). Compute the date range with `date` so you don't rely on a guessed "today". Items published outside the window are excluded, even if interesting — note them only if genuinely seminal.

### 2. Gather candidate items from known sources

Read `references/sources.md` for the curated source list, grouped into broad DBMS, research venues, commercial engines, and aggregators/newsletters. Work through the high-priority sources first. Prefer aggregators (DB Weekly) to fan out quickly, then go direct to primary blogs for anything promising.

**Feed-first ingestion (all languages).** The fastest, most reliable, language-agnostic scan is the curated feed list in `references/feeds.opml` — an OPML list of RSS/Atom feeds. Each run, fetch every feed and keep items whose publish date falls in the window; RSS/Atom is plain XML, so a normal fetch works — no browser, no language barrier. Three cases need the **Claude-in-Chrome** browser instead: feeds blocklisted for plain fetch (Reddit's `.rss` is — confirmed), live feeds that come back empty/unparseable through plain fetch (Lobsters' tag feed does — it's fine in a real reader), and sources with no feed yet (several Chinese aggregators). Maintain `feeds.opml` like the other source lists: add a feed when you find/confirm one (discover the URL in the browser if the site doesn't advertise it), and drop a feed only when it's genuinely dead (404 / gone) — not when plain fetch merely returns empty (read those via the browser instead). It's also importable into any reader.

Use web search and page fetches to collect: title, URL, author/source, publish date, and enough of the body to judge it. Cast a wide net here — filtering happens next.

**Scan non-English sources too.** Query the Chinese DB ecosystem each run — the Chinese aggregators (modb.pro, PingCAP, OceanBase, Alibaba Cloud) publish heavily and are mostly invisible to English search. Work the Chinese set in `references/sources.md`. Search in the **native language** (e.g. 数据库) — the best regional engineering write-ups never surface in English search. Apply the same anti-marketing and fact-check bar, and be careful not to let a machine translation distort a technical claim — verify numbers/behaviour against the original or a primary source. Other languages can be re-added as new non-English sources are discovered. Present non-English items in the `## International` section per the non-English formatting rule below.

**Tooling for non-English / JS-heavy sources.** Plain page fetches only see raw HTML, so client-rendered or region-specific sites (Chinese aggregators like modb.pro, PolarDB / Alibaba Cloud, PingCAP — also Reddit) often return stale or empty content. In order of preference: (1) use each source's **native RSS/Atom feed** (listed in `references/sources.md`) — feeds are dated, language-native, and fetch cleanly; (2) when there's no usable feed, **render the page with the Claude-in-Chrome browser tools** rather than a plain fetch; (3) treat web search as English/US-biased — use it to confirm, not to discover, non-English items. The Chinese ecosystem in particular publishes heavily and is mostly invisible to English search, so lean on its feeds and the browser.

### 3. Scan community discussion -- the "Community pulse"

Read `references/community-sources.md` and scan the **scannable** community sources (the `[public]` / `[js]` ones) for the time window: forums and link aggregators (Hacker News, Lobsters), the database subreddits, Q&A hot lists (DBA Stack Exchange), and any pinned public Telegram channels. The goal is **what people actually argued about this week**, ranked by real engagement (HN points + comments, Reddit upvotes + comments, SE votes/answers) -- not by mere existence.

Pick the 3-8 threads with the most substantive discussion. **Dedupe against the rest of the digest**: if a thread is just reactions to an article already listed above, fold it in or skip it -- the Community pulse is for discussion that is itself the story (design debates, war stories, surprising benchmarks people are passing around). Apply the same anti-marketing filter, and link to the thread itself.

Follow `community-sources.md`'s upkeep rules every run: **discover** new active DB communities (a fresh subreddit, a Discourse forum, a public Telegram/Matrix channel) and append keepers to its Discovery log; **prune** any listed source that's been silent for ~3 months, is gone, or has turned promotional by moving it to that file's Retired log (with date + reason) so it leaves the weekly scan but isn't blindly re-added.

### 4. Conferences -- open CFPs and upcoming events

Two date-windowed sections, each tied to **this** week so the same item never appears in two digests.

**Call for papers** -- list a CFP **only in the digest for the week its call opened** (the "CfP is now open" announcement falls inside this digest's 7-day window). One announcement -> one digest; never list a CFP that opened in an earlier week or that is merely "still open":
- **Applied & research DB-systems venues** -- VLDB, SIGMOD, CIDR, ICDE, DEBS, USENIX ATC/OSDI, P99 CONF, HYTRADBOI (venue CFP pages, WikiCFP).
Give the conference, location + dates, the **CFP deadline**, and the link; tag *(research)*. If no CFP opened this week, omit the section.

**Upcoming events** -- a one-month heads-up with **no repeats**: list a conference/meetup exactly once, in the digest for the week during which it **enters the 30-day horizon** -- i.e. its start date is **24-30 days after the end (Sunday) of this digest's week** (an event more than 30 days out waits for a later digest; one already <=23 days out was listed last week). For each qualifying event, open the program and pick the **1-3 talks most interesting to an internals developer** -- ideas you could implement or probe in your own engine/product (wire protocol, planner/optimizer, storage, MVCC, replication, memory, concurrency, indexing), **not** generic intro/ops talks; give speaker + a one-line "why it matters". If the program isn't posted yet, list the event and say so. If nothing enters the horizon this week, omit the section. Discover events via the Conferences & CFP trackers in `references/sources.md`.

### 5. Discover emerging sources (self-update)

Each run, spend a little effort looking for **new, high-quality sources** that aren't yet in `references/sources.md`: a new independent engineering blog, a fresh research group page, a newly active newsletter, a conference that just posted proceedings. Good signals are: cited by sources you already trust, written by known contributors, deep technical content with no sales pitch.

When you find a keeper, **append it to `references/sources.md`** under the right section with a one-line note on why it's worth watching. This is how the skill stays current instead of going stale. Conversely, if a listed source has gone dormant or turned into pure marketing, mark it accordingly.

### 6. Filter out marketing, ads, and promotion

This is the core value of the digest. **Exclude** an item (or flag it clearly if it's borderline but still has real content) when it shows the hallmarks of marketing rather than engineering:

- It's primarily announcing a product, pricing, funding round, partnership, award, or "we're now GA" with little technical substance.
- It's a vendor case study whose real purpose is the logo and the CTA, not the method.
- Superlatives without numbers: "blazing-fast", "next-gen", "revolutionary", "game-changing", "enterprise-grade" with nothing measured.
- It ends in a demo booking, free-trial, or "talk to sales" call to action and the body was just a runway to it.
- Reposted press release / sponsored content / listicle SEO bait ("Top 15 databases for 2026").

**Keep** content that teaches or proves something: benchmarks with methodology, internals deep-dives, postmortems, release notes that explain *what changed and why*, research papers, protocol/design discussions, reproducible experiments — even when published on a vendor's blog. A vendor engineering blog post can be excellent; judge the substance, not the domain. When in doubt, ask: "If I strip the company name, is there still something I learned?" If no, cut it.

**Feature-explainer rule (authority gate).** A lot of posts just describe a new or existing feature without adding a new use case, a problem found in the wild, a benchmark, or a non-obvious gotcha. These "here's how feature X works" walkthroughs are only worth including when written by someone with first-hand authority over that feature — its **author, committer, or reviewer** (verify via the project's commit history or release notes). If a generic feature explainer is written by someone *without* that direct involvement, skip it — it's usually a rehash. The exception is the moment a feature first ships (a release/beta announcement), which is news regardless of author. When you do include an authority-written feature post, you may note the author's role, e.g. `[by committer]`.

**Commercial-engine techniques.** Actively look for genuinely new techniques and inventions in SQL Server, Oracle, MySQL, DB2, and similar — new optimizer/storage/replication capabilities, internals write-ups, and engineering deep-dives. Apply the same anti-marketing filter: a real technique or measured result, not a "what's new in version N" sales sheet.

**Release posts get a changes summary.** When an item is the release of a database engine, extension, or utility (e.g. "ClickHouse 26.6", "QuestDB 8.2"), don't just say "new release" — read the changelog/release notes and summarise *what actually changed*: the headline new features, notable fixes, breaking changes, and the minimum/target server version. This is the one place to relax the strict one-line limit — a release item may use a short sub-bullet list of the key changes when that's clearer. Skip pure version-bump posts with no meaningful changes, and still drop release posts whose "changes" are entirely marketing.

**Migration experience.** Actively look for real-world migration experience reports — moving to/from Postgres, Oracle→Postgres, MySQL→Postgres, cross-cloud, version upgrades at scale — where the author shares what actually happened (pitfalls, downtime, data discrepancies, tooling, rollback). These are high-value; prioritise them. Generic "why you should migrate to our product" posts are marketing — cut them.

**Editing guardrail.** The filtering step above tells you what to *remove*. When you
later edit an item's description -- tightening prose, fixing a stale HN point count,
adding detail that was missing -- you must apply the same evidence bar as filtering:
every factual change must be backed by the primary source. Check these high-risk
claim types especially:

| If you are adding...          | You must have fetched...                                 |
|-------------------------------|----------------------------------------------------------|
| A feature name or bug fix     | The release notes / changelog at the linked URL          |
| A technical description       | The abstract, commit message, or body of the linked page |
| A date ("Jun 27", "Jan 13")   | The primary source's own date field or header            |
| A message count ("~10 msgs")  | The archive page for that thread on the relevant days    |
| A conference detail           | The CFP page or official announcement                    |
| An HN score                   | The Algolia API for that story ID                        |

If a link is broken, an API is blocked, or a page is behind auth, the constraint
is: **do not add the claim.** A short honest item is better than a detailed one
whose details you invented. There is no shame in leaving a terse description terse.

### 7. Fact-check -- before including AND before enhancing

This step fires twice per item: once when you are deciding whether to keep it,
and again when you are editing its description. The rule is the same both times:
**do not add a factual claim whose source you have not fetched.**

**When you enhance a terse description** (add detail beyond what the original text says),
fetch the primary source first -- the release notes, the arXiv abstract, the commit
message at the linked hash, the conference CFP page. Read it. Then write your
enhancement so that every specific claim (feature names, bug descriptions, dates,
message counts, conference details) is directly traceable to that fetched source.

**Do not guess.** If the release notes are behind a link you cannot reach, keep the
item terse. An honest one-liner beats a detailed fabrication.

For each surviving item, do a quick sanity pass: does the headline claim match the body?
Are benchmark claims accompanied by setup details (hardware, dataset, versions)?
Is a technical claim actually in a release/commit, or just speculation?
Cross-check surprising claims against a second source (commit, the actual paper).
If a claim can't be substantiated, either drop the item or append a short `[unverified]`
note so the reader knows.

### 8. Write the digest

Use the exact format below. Keep each line to roughly one sentence — the value is in being scannable. Order items by importance (most significant first), lightly grouped by theme. Aim for ~10–25 items; quality over quantity. If a slow week yields little, a short honest digest beats padding.

## Output format

```
# DBMS Weekly — <YYYY-MM-DD> (week of <start>–<end>)

## Database internals & releases
- **[<Headline>](URL)** — <one-line why-it-matters>. *(<Author> · <source>)*
- ...

## Community pulse
- **[<What people were arguing about>](thread URL)** — <one line on the debate / war story / surprise and where it landed>. *(<platform> · <N pts / comments>)*
- ...

## Wider DBMS & distributed data
- **[<Headline>](URL)** — <one line>. *(<Author> · <source>)*
- ...

## Commercial engines (SQL Server, Oracle, MySQL, …)
- **[<Headline>](URL)** — <one line on the new technique/invention>. *(<Author> · <source>)*
- ...

## Migration experience
- **[<Headline>](URL)** — <one line on what actually happened>. *(<Author> · <source>)*
- ...

## Research & cutting edge
- **[<Headline>](URL)** — <one line>. *(<authors / venue>)* _[paper]_
- ...

## International (non-English sources)
- **[<English headline>](URL)** — <one-liner>. *(<Author> · <source>)* [zh] _(orig: <original title>)_
- ...

## Call for papers
- **[<Conference> — <location>, <dates>](CFP URL)** — CFP closes <deadline>. *(research)*
- ...

## Upcoming events
- **[<Event> — <location>, <dates>](schedule URL)** — <one line>. Internals picks:
    - **<Talk title>** (<speaker>) — <why it matters to an internals developer>.
    - ...

## New sources added this week
- **[<source name>](URL)** — <why it's worth following>. *(<author>)*

---

_<N> items · sources scanned: <count> · filtered out as marketing/ads: <count>_
```

Notes on the format:
- **The headline is the link** (`**[Headline](URL)**`) — one big tap target, ideal on a phone; do not add a trailing `[link]`. The one-liner says *why a database internals developer should care*, not just what it is.
- **Every factual claim in the description must be from a source you fetched, not from your training data.** The reader assumes you checked the link. Live up to that. If you are adding detail to a pre-existing item, fetch the primary source before you type the new sentence. Never backfill from domain knowledge alone.
- **End each item with the author/source in italics**, e.g. `*(Andy Pavlo · CMU DB Group)*`. Include the author's name when it isn't already in the one-liner; otherwise just the source/site (or venue, for papers). On a phone this lets the reader triage before tapping.
- Append `[paper]`, `[unverified]`, `[by committer]`, `[vendor blog — substantive]`, or a language tag (`[zh]`) only when useful.
- **Non-English items go in their own `## International` section** (don't scatter them across the topical sections). Each gets an English headline + one-liner, a language tag (`[zh]`), and the original title in italics in parentheses — e.g. `- **[Inside PolarDB's shared-storage buffer pool](URL)** — how it decouples buffer management from local disk. *(Alibaba Cloud · developer.aliyun.com)* [zh] _(orig: …)_`. Verify technical claims against the original, not just the translation. Currently active non-English sources are Chinese; other languages can be re-added as new sources are discovered. For Chinese, `modb.pro` renders via the browser (`cn.pingcap.com` times out on idle); it's PR-heavy, so mine the research / internals items (OceanBase, TiDB, PolarDB) and drop vendor PR.
- **Release items** (extension/utility releases) may break the one-line rule: give a headline line plus an optional short indented sub-list of the key changes (new features, notable fixes, breaking changes, target server version). Example:
  ```
  - **[ClickHouse 26.6](URL)** — new monthly stable with continuous queries and multi-stage distributed execution. *(release notes)*
      - continuous queries over MergeTree as periodic snapshot reads
      - experimental multi-stage distributed execution with shuffle joins
  ```
- **Community pulse items** link to the discussion thread and tag the platform plus a rough engagement signal, e.g. `*(Hacker News · 240 pts, 180 comments)*` or `*(r/databasedevelopment · 95 upvotes)*`. Keep to the 3–8 most-discussed threads, deduped against the rest of the digest.
- **Call-for-papers items** appear only in the digest for the week the CFP **opened** (announcement in-window) — never repeated across weeks; tagged *(research)*.
- **Upcoming-events items** appear once, ~a month ahead — the event starts 24–30 days after this digest's week ends — then a short sub-list of 1–3 internals-relevant talks (speaker + why-it-matters), or a note that the program is TBA.
- **Blank line before every list.** A bullet list must be preceded by a blank line (CommonMark). If a section opens with an intro sentence (e.g. the Call-for-papers "open as of …" line), leave a blank line before the first `-`, or the whole block renders as one paragraph instead of a list.
- **Never name what was filtered.** The stats line carries only *counts* (items dropped as marketing/ads, and optionally an out-of-window count). Never list the specific blogs, companies, people, or products you excluded — no "incl. X, Y …" enumerations and no "excluded: …" notes anywhere in the digest. (Listing the sources you *scanned* is fine — that's coverage stats.)
- **Owner privacy.** Never include a post **authored by** the digest's owner, and never print the owner's name or personal handles anywhere in the digest. The owner's names/handles live in `references/exclude.md` (git-ignored); skip anything authored by or naming them. Posts about the owner's employer written by *other* people are fine.
- **Skip empty sections silently.** Omit any section that has no items — do NOT write "nothing this week", "no items found", or an apology/explanation. A missing section just means nothing qualified; the reader infers that. Never add filler narration about gaps.
- If delivering to Telegram or another plain-text channel later, the same content works; just drop the Markdown headers to bullet groups if the target doesn't render Markdown.

## Example items

**Good (keep):**
`- **[ClickHouse 26.6](URL)** — new monthly stable ships continuous queries over MergeTree (periodic snapshot reads as a first step toward streaming) and experimental multi-stage distributed execution with scatter/broadcast/gather/shuffle exchanges. *(release notes verified on GitHub)*`

`- **[Our MongoDB TLA+ workshop](URL)** — Murat Demirbas reports an order-of-magnitude better onboarding when LLM assistance removes TLA+ syntax as the barrier, letting engineers formally model real replication/storage subsystems. *(muratbuffalo.blogspot.com)*`

`- **[Why is everyone suddenly moving off RDS?](URL)** — 300-comment HN thread trading cost and lock-in war stories; the substance is the migration tactics in the replies, not the headline. *(Hacker News · 300+ comments)*`

**Bad (filter out):**
`- "Acme DB raises $40M Series B to revolutionize the cloud-native AI-ready database" — funding announcement, no technical content. (excluded)`

`- "How do I speed up my query?" — routine user question with no surprising answer. (excluded)`

**Fabrication (the worst kind of wrong -- never do this):**
`- **[Barman 3.18.0](URL)** — brings incremental WAL-file recovery and fixes for parallel backup consistency.` *(The release notes say nothing about either. This was invented by the model because "Barman is a backup tool, so it probably does WAL recovery and parallel backups." Never fill gaps from domain priors.)*

`- **[TimescaleDB 2.28.1](URL)** — maintenance release with hypertable chunking improvements and compression bug fixes.` *(The actual release notes list 10 specific bug fixes, none about chunking or compression. "Hypertable" and "compression" came from knowing what TimescaleDB is, not from reading the notes.)*

`- **Reorder buffer spill O(N^2)->O(N) during vacuum storms** (URL to CF page) — a logical-decoding patch landed in the CommitFest.` *(The item does not exist. The commitfest page, the activity log, and the mailing list archives were searched exhaustively and contain no such patch. This was entirely invented.)*

## Keeping the skill healthy

The source list is the skill's memory. Treat `references/sources.md` as a living file: add what proves valuable, demote what turns into a billboard. Over a few months this should converge on a personal, high-trust set of sources tuned to what the reader actually finds worth reading.
