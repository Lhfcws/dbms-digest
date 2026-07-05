# Sources

The living source list for the weekly DBMS digest. Priority is a rough guide to scan order
(P1 = check every week, P2 = check most weeks, P3 = sample / opportunistic).
When you find a new high-signal source, append it under the right section with a one-line note
and a priority. When a source goes dormant or turns into pure marketing, mark it `[dormant]`
or `[mostly-marketing]` rather than deleting it, so it isn't re-added next week.

**Feed list:** the machine-readable RSS/Atom feeds scanned each run live in
`references/feeds.opml` (all languages; also importable into any feed reader). Keep it in sync
with this file — add confirmed feeds, drop dead ones.

## Aggregators & newsletters (start here — best fan-out)

- **DB Weekly** — broader weekly database newsletter (Cooperpress); covers the wider DBMS world. P1. https://dbweekly.com/
- **Hacker News (database filter)** — sample for database/systems threads with real discussion across engines. P2. https://hn.algolia.com/?query=database+OR+sql+OR+duckdb+OR+clickhouse+OR+sqlite+OR+mysql+OR+postgres

## DBMS & distributed data

- **Andy Pavlo / CMU DB Group blog** — industry analysis, annual "Databases in <year>" retrospective, seminar series. P1. https://www.cs.cmu.edu/~pavlo/blog/ and https://db.cs.cmu.edu/
- **DBMS Musings (Daniel Abadi)** — isolation/consistency, distributed DB theory made readable. P2. http://dbmsmusings.blogspot.com/
- **Murat Demirbas — Metadata blog** — distributed systems & database papers, paper reviews. P2. https://muratbuffalo.blogspot.com/
- **The New Stack — Databases** — news/trends; mixed, filter for substance. P3. https://thenewstack.io/data/
- **QuestDB blog** — time-series engine internals and skeptical benchmarking-methodology writing. P3. https://questdb.com/blog/
- **awesome-database-learning** — curated internals reading list; mine for new primary sources. P3. https://github.com/pingcap/awesome-database-learning

## Commercial engines (new techniques & inventions — filter marketing hard)

- **SQL Server — Microsoft engineering blogs & docs** — "What's new" + engine internals; mine for real optimizer/storage/columnstore/Hekaton-style techniques, not feature sheets. P2. https://techcommunity.microsoft.com/category/sql-server/blog/sqlserver
- **Bob Ward / SQL Server team deep-dives** — internals talks and write-ups. P3. https://learn.microsoft.com/en-us/sql/
- **Oracle Optimizer blog** — CBO internals and new optimizer features straight from the team. P2. https://blogs.oracle.com/optimizer/
- **Oracle Database Insider / Maria Colgan** — In-Memory, new-version internals. P3. https://blogs.oracle.com/database/
- **Franck Pachot** — cross-engine internals (Oracle, Postgres, YugabyteDB, MongoDB); excellent technique-level comparisons. P2. https://dev.to/franckpachot
- **MySQL Server Blog / engineering** — InnoDB, optimizer, replication internals. P3. https://dev.mysql.com/blog-archive/
- **Percona blog (MySQL/Postgres/Mongo)** — often substantive engineering; filter the product posts. P3. https://www.percona.com/blog/

## Migration experience (real-world reports — prioritise)

- **Stormatics** — ops/incident postmortems with broadly applicable root-cause analysis and recovery patterns. P2. https://stormatics.tech/
- **AWS Database Blog — migrations** — Oracle/SQL Server → Aurora war stories; technical, watch for product push. P2. https://aws.amazon.com/blogs/database/
- _Also surface migration posts that appear via DB Weekly and HN — they show up there regularly._

## Research venues (cutting edge — check for new proceedings / preprints)

- **VLDB** — proceedings (PVLDB). P2. https://www.vldb.org/pvldb/
- **SIGMOD / ACM SIGMOD Record** — major systems papers. P2. https://sigmod.org/
- **CIDR** — innovative/early systems ideas (e.g. Umbra). P2. https://www.cidrdb.org/
- **FAST (USENIX)** — file and storage technologies; storage-engine, WAL, and I/O papers directly applicable to DB internals. P2. https://www.usenix.org/conference/fast
- **DBWorld (SIGMOD)** — CfPs and community announcements; useful to spot what's hot. P3. https://dbworld.sigmod.org/browse.html
- **arXiv cs.DB** — database preprints. P2. https://arxiv.org/list/cs.DB/recent

## Conferences & CFP trackers (for the Call-for-papers section)

Find conferences with an **open** CFP, plus applied/research venues.
List a CFP only while its deadline is in the future.

**Applied & research DB-systems venues**
- **VLDB** — rolling monthly PVLDB research deadlines. P2. https://www.vldb.org/
- **ACM SIGMOD** — multi-round research deadlines (year-versioned site). P2. https://sigmod.org/
- **CIDR** — innovative/early systems ideas. P2. https://www.cidrdb.org/
- **FAST (USENIX)** — storage systems; frequent DB-relevant work. P2. https://www.usenix.org/conference/fast
- **IEEE ICDE** — https://icde.org/ . P3.
- **DEBS** — distributed & event-based systems. https://debs.org/ . P3.
- **USENIX ATC / OSDI** — systems venues with frequent DB work. https://www.usenix.org/conferences . P3.
- **WikiCFP — databases** — academic CFP aggregator. http://www.wikicfp.com/cfp/call?conference=databases . P3.
- _Practitioner_: P99 CONF, HYTRADBOI. P3.

## Non-English sources (multilingual)

_Scan these in their native language and present items per the non-English formatting rule
(English headline + one-liner, a language tag, original title in parentheses). The same
anti-marketing and fact-check bar applies — verify technical claims against the original, not
just a translation. Currently the active non-English sources are Chinese; other languages
can be re-added as new sources are discovered through the self-update rule._

_Prefer each source's RSS/Atom feed where available (dated, language-native, fetches cleanly).
For JS-heavy or region-specific sites that return stale/empty HTML — Chinese aggregators
(modb.pro), PolarDB / Alibaba Cloud, PingCAP — render them with the
Claude-in-Chrome browser tools instead of a plain fetch. Treat web search as English/US-biased:
use it to confirm, not to discover._

### Chinese `[zh]`
- **PingCAP / TiDB blog (CN)** — distributed SQL internals, Raft, TiKV. P2. https://cn.pingcap.com/blog/
- **OceanBase** — distributed DB engineering write-ups (CN). P3. https://www.oceanbase.com/
- **Alibaba Cloud developer (PolarDB / AnalyticDB)** — engine internals; huge, filter hard. `[js]` P3. https://developer.aliyun.com/
- **modb.pro (墨天轮)** — Chinese DBA community and articles (Oracle, PG, MySQL, domestic engines). P3. https://www.modb.pro/

_Discover more per the self-update rule — pin precise regional blogs/authors/channels
as you find keepers; retire dead ones._

## New sources added (log)

_Append discoveries here with date, name, link, and a one-line reason. Example:_
- (2026-06-18) _seed list created._
- (2026-06-18) modern-sql.com (Markus Winand) — cross-engine SQL-standard conformance and feature comparisons. P2. https://modern-sql.com/
- (2026-06-29) QuestDB blog (questdb.com/blog) — time-series internals + benchmarking-methodology writing; surfaced via a strong HN thread ("Lies, Damn Lies and Database Benchmarks"). P3.
- (2026-06-29) _Operational note (fetch path):_ when plain `WebFetch`/`curl` fail or time out on a primary domain, the **Claude-in-Chrome path + same-origin `fetch()`** is a reliable fallback: navigate to the target domain, then `fetch()` its feed/API in-page and parse (RSS via `DOMParser`, JSON via `.json()`). When the in-page fetch is blocked (query-string privacy guard), navigate to a query-string-free URL first.
