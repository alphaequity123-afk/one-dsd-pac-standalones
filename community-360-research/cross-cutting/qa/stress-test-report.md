# Stress test: One DSD People, Access and Culture

Test window: October 31, 2026, 06:21:32 to 06:26:33 UTC (5 minutes). Target: the live app at `one-dsd-people-access-culture-production.up.railway.app`. Level agreed with Gary: moderate, page views only, no AI requests.

## How it was run

- 25 simulated visitors at once, each requesting a page, reading for 0.2 to 0.8 seconds, then requesting the next, for five minutes without pause.
- 154 real page addresses taken from the site crawl (every public page type: home, start, learn, library, practice scenarios, community pages, program pages, support), with the busiest entry pages weighted a little higher.
- Each request's status and time were recorded by the test tool (`evidence/stress.json`). Railway's own measurements for the same window were pulled afterwards as an independent check.
- A single-page crawler and an inventory pass were running at the same time; together they added less than one request per second to the load.

## Results

| Measure | Result |
|---|---|
| Requests completed | 5,279 (17.6 per second) |
| Server errors (5xx) | 0 (Railway's own count for the window: 0 in 10,732 requests) |
| Pages returned successfully | 5,270 with status 200 |
| Failed requests | 9, all dropped connections on the test side ("terminated" or "fetch failed"); none reached a server error |
| Typical response time (median) | 527 ms (at rest, before the test: 7 to 17 ms) |
| 90th percentile | 2,270 ms |
| 95th percentile | 3,298 ms |
| 99th percentile | 4,504 ms |
| Slowest single response | 8,025 ms |
| CPU (Railway) | peak 1.39 vCPU during the test; average 0.002 at rest over the previous two days |
| Memory (Railway) | rose from about 0.9 GB to 4.16 GB during the test, against a 24 GB limit |

Railway's measurement of the `/home` page alone during the busiest five-minute bucket: median 929 ms, 99th percentile 3,763 ms.

### Slowest pages under load (average over the test)

| Page | Average | Slowest | Requests |
|---|---|---|---|
| `/learn/intercultural` | 4.2 s | 6.0 s | 25 |
| `/learn/cultural-intelligence` | 3.8 s | 7.4 s | 36 |
| `/learn/clas` | 3.1 s | 8.0 s | 25 |
| `/practice` | 2.8 s | 6.3 s | 32 |
| `/learn` | 2.3 s | 7.5 s | 57 |
| `/library` | 2.3 s | 7.4 s | 63 |
| `/one-dsd/programs` | 2.2 s | 6.2 s | 36 |
| `/library/lm-how-this-program-works` | 2.1 s | 5.3 s | 25 |
| `/learn/collaboration` | 2.1 s | 4.3 s | 39 |
| `/practice/gp-11` | 1.8 s | 3.6 s | 25 |

## What this means

- **It holds.** Nothing broke, no visitor saw an error, and the service did not restart. For a voluntary staff resource with a few dozen users at a time, this is adequate.
- **Headroom is limited.** At 25 simultaneous visitors the typical page already takes half a second instead of a few hundredths, and the listing pages (Learn, Library, Practice, One DSD programs) take 2 to 4 seconds on average, with the worst at 8 seconds. Twice this load would likely feel slow across the site, and four times this load would start to time out. The listing pages appear to be rendered fresh on every request; they are good candidates for caching or static generation.
- **Memory grew four-fold under load.** 0.9 GB to 4.2 GB is well within the 24 GB limit, but it is worth confirming that memory returns to its baseline after load (a check an hour later is noted in the forensic findings). If it does not, there is a leak.
- **One replica.** The service runs a single instance in one region. A second replica would roughly double the comfortable load and remove a single point of failure, at the cost of a second instance.

## What was not tested

- The AI assistant under load (each question costs money and depends on outside providers; its behaviour under 7 simultaneous questions is described in the forensic findings).
- Heavy load (100 or more simultaneous visitors), by agreement, to avoid an outage on a live service.
- The calendar and course site under load: it is static files served by Railway, and its ten pages all returned within about one second during normal checks.

## Evidence

- `evidence/stress.json`: the complete summary produced by the test tool, including status counts, percentiles, every error sample and the slowest paths.
- Railway's metrics for the same window are quoted above and recorded in `evidence/railway-snapshot.json`.
