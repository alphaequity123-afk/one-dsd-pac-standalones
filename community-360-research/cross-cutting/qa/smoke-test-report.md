# Smoke test: One DSD People, Access and Culture, end to end

Status: draft in progress. Sections marked [[PENDING]] are being filled in as the last automated passes finish.

Test date: October 31, 2026 (UTC). Scope agreed with Gary: the live main app, the calendar and course site, the AI assistant and voice endpoints (a small number of real questions), database health through Railway, and the automatic rebuild in GitHub. The four older copies of the app were checked only for whether they respond. Everything here was done from outside the app, in a real browser or with direct web requests, because the app's source code is only on Gary's computer.

Companion documents: `forensic-findings.md` (causes, fixes and decisions needed), `stress-test-report.md` (load test), and `evidence/` (raw results).

## 1. The main app: every page

**Method.** A browser crawler started from `/home`, `/site-map`, `/` and `/minnesota-communities`, followed every internal link it found, and recorded for each page the HTTP status, load time, title, console errors, failed or 4xx/5xx requests, and broken images. A first pass waited for the network to go completely quiet; a second pass waited for the load event plus 2.5 seconds, which is how a visitor experiences a page.

**Result.** [[PENDING: total pages crawled, status counts, console errors, 404 resources, broken images, slowest pages]]

**What the automated passes flagged, and what each turned out to be:**
- `net::ERR_ABORTED` on navigation links across many pages: these are the app's own link prefetches being cancelled when the visitor navigates away. Normal behaviour, not failures.
- 41 pages that never went network-quiet in the first pass: 24 are document downloads (see section 3), which a browser cannot "finish" as a page; the other 17 are the self-directed learning pages, which keep a small amount of network activity going after load. All 41 load correctly when measured the way a visitor sees them.
- Missing read-aloud narration files on the self-directed learning pages: a real defect, described in `forensic-findings.md` finding 4.

**Interactive inventory.** Every page that returned 200 was loaded again and inspected for forms, buttons and inputs, for pages stuck on "Opening your page", for empty content, and for error text. [[PENDING: counts]] No page was stuck loading, none showed error text, and none was empty except the root `/`, which is a short entry page that leads to `/home`. The page `/program/plan` carries only about 30 words; see the My Work workflow below for whether that is by design.

## 2. The main app: user workflows

Each workflow below was driven in a real browser by a tester following the steps a staff member would take, read-only: no form that would create a record on the server was submitted, and the AI assistant was not asked anything in this part (it is covered in section 4).

[[PENDING: one short block per workflow: Home and search; Communities list and page; Start page form; Learn, courses and read-aloud; Library and saving; Find the right person; Audio library; Equity toolkit practice tool; Contribute and intake (no submission); My work, plan and progress; Practice scenarios; One DSD program pages and sharing. Verdict, what worked, what did not, where saved data lives.]]

## 3. The main app: endpoints and files

| Check | Result |
|---|---|
| All 39 community pages (`/minnesota-communities/<id>`) | 39 of 39 return 200, each with its heading, in 0.2 to 0.4 s |
| 24 document downloads (`/api/downloads/...`: equity framework, operationalizing-equity program, measurement worksheet, support directory; each in docx, xlsx, pptx, pdf, html, txt) | 24 of 24 return 200 with a real file of the expected type; sizes from 5 KB to 1.8 MB; all under 0.6 s |
| `/api/health` | 200, `{"status":"ok"}`; POST, PUT and DELETE correctly refused (405) |
| `/api/page-text` | 400 "Unknown page" without a route; 200 with a valid route |
| `/api/ask/voice` | 200, reports voice settings (transcription on, speech off) |
| `/api/ask/voice/worker` | 401 to outsiders (protected); it is long-polled every 15 s by Gary's voice worker, which is why Railway's service-wide latency figure reads about 15 s |
| `/api/media` | 405 to GET (write-only endpoint) |
| `/share/` and `/share` | 308 redirect to `/share`, which returns 404; share links with an identifier were tested in the sharing workflow in section 2 |
| Unknown pages (`/nonexistent-page-xyz`) | proper 404 page |
| `robots.txt`, `sitemap.xml` | 404 (none published; the app also sends `X-Robots-Tag: noindex`, so this is consistent with keeping the site out of search engines) |
| Probes for `.env`, `.git/config`, `/admin`, `/api/debug`, `/wp-login.php` | all 404 |

## 4. The AI assistant (Ask) and voice

- **Real browser, two sessions, seven questions.** Session one: question 1 failed (HTTP 502 from `POST /api/ask` after 20 s; the page showed "We couldn't finish that answer just now"), the follow-up succeeded (26 s, about 3,900 characters, with the conversation carried forward), and "Clear this conversation" worked. Session two, five fresh browser contexts: the first question failed the same way (502 after 33 s); the other four succeeded in 24 to 36 s. Evidence: `evidence/ask-e2e.json`, `evidence/ask-repeat.json`, screenshot in `evidence/`.
- **The question that failed cold succeeded warm.** "What does the Disability Services Division do?" returned a full, accurate answer (8.6 KB) when asked again a few minutes later (`evidence/ask-retest.json`).
- **Direct calls.** Eight short direct calls to the endpoint ("Reply with one word: hello") were all answered correctly in 11 to 42 s, including seven sent at the same moment (`evidence/ask-post.json`). The server logs during that burst show the research provider refusing requests for rate limiting; those answers did not need research so the user saw no effect.
- **Voice.** Settings endpoint responds; worker endpoint is protected; no microphone test was possible from an automated browser.
- Causes and needed fixes are in `forensic-findings.md`, findings 2 and 3.

## 5. The calendar and course site

| Check | Result |
|---|---|
| Deployment current | Yes, after the fix described in finding 1: 576 calendar entries live (was 386), course live |
| All pages (`/`, `/course/`, `/course/index.html`, six modules, essay) | 10 of 10 return 200 in 0.7 to 1.5 s; no console errors, no failed requests, no broken images (crawled before and after the deploy) |
| `/course` without the trailing slash | Fixed during the test: now styled and linked correctly (was unstyled with broken links) |
| Link from the calendar to the course | Added during the test |
| `cultural-calendar.json` | Parses; 576 entries |
| `cultural-calendar.ics` | Valid calendar header; 542 events |
| `calendar-by-month.md` | Served (270 KB) |
| Content notes | Present in modules 4 and 5 |
| Pictorial icons | None anywhere (Gary's rule) |

## 6. Automatic rebuild in GitHub

The workflow `.github/workflows/rebuild-research-site.yml` ran three times during the day, all successful. On the third run it found the calendar out of date and committed a rebuild on its own (commit 750020e), which proves the whole path: edit a research file on GitHub, the pages rebuild, Railway publishes them. The one remaining gap is on Railway's side (finding 1): Railway must be told to deploy pushes from this repository automatically.

## 7. Database

Checked through Railway only (read-only): the Postgres service has run since October 5 without restart; the only errors in the examined window were on October 24 (four failed password attempts and one missing-table error); none since. Details in `forensic-findings.md`, finding 8.

## 8. Load

Summarised in `stress-test-report.md`: 25 simultaneous visitors for five minutes, 5,279 requests, zero server errors, typical response half a second, listing pages 2 to 4 seconds, memory up to 4.2 GB.

## 9. Fixed during the test

1. Calendar site redeployed with the current content (twice, as pushes accumulated).
2. Course pages switched to absolute links so `/course` works with or without a trailing slash.
3. Calendar page now links to the course.
4. The two problems above were pushed to GitHub, and the automatic rebuild produced the live pages.

## 10. Not fixed here, because the app's code is on Gary's computer

The Ask assistant failures, the never-ready search index, the missing read-aloud files, the lack of a per-visitor limit on the Ask endpoint, and the slow listing pages under load. Each has a described fix in `forensic-findings.md`.

## 11. Limits of this test

- Plain-HTTP redirection and the TLS certificate could not be checked from this environment (its network allows only HTTPS).
- The AI assistant was limited to about 15 real requests to keep credit spending small.
- No microphone, camera or screen-reader testing.
- The older copy services were not tested beyond confirming they respond.
