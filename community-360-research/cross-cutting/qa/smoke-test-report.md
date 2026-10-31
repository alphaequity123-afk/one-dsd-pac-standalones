# Smoke test: One DSD People, Access and Culture, end to end


Test date: October 31, 2026 (UTC). Scope agreed with Gary: the live main app, the calendar and course site, the AI assistant and voice endpoints (a small number of real questions), database health through Railway, and the automatic rebuild in GitHub. The four older copies of the app were checked only for whether they respond. Everything here was done from outside the app, in a real browser or with direct web requests, because the app's source code is only on Gary's computer.

Companion documents: `forensic-findings.md` (causes, fixes and decisions needed), `stress-test-report.md` (load test), and `evidence/` (raw results).

## 1. The main app: every page

**Method.** A browser crawler started from `/home`, `/site-map`, `/` and `/minnesota-communities`, followed every internal link it found, and recorded for each page the HTTP status, load time, title, console errors, failed or 4xx/5xx requests, and broken images. A first pass waited for the network to go completely quiet; a second pass waited for the load event plus 2.5 seconds, which is how a visitor experiences a page.

**Result.** The crawler visited its limit of 600 page addresses: 492 returned 200; 57 were document downloads, which a browser hands to the download manager instead of showing (all 24 distinct downloads were checked separately in section 3 and work); 51 returned 404, and on inspection all 51 were the crawler's own mistake (it misread a page's base address and built wrong links to the course slide decks; checked properly, all 72 slide decks download correctly). No broken images on any page. Typical load time to a readable page, measured the way a visitor sees it: median 2.9 s, 90th percentile 3.4 s, slowest 9.6 s (`/one-dsd/programs/positive-supports`). Raw results: `evidence/crawl-app.json`.

The one real defect the crawl surfaced: 207 distinct read-aloud narration files are missing (finding 4).

**What the automated passes flagged, and what each turned out to be:**
- `net::ERR_ABORTED` on navigation links across many pages: these are the app's own link prefetches being cancelled when the visitor navigates away. Normal behaviour, not failures.
- 41 pages that never went network-quiet in the first pass: 24 are document downloads (see section 3), which a browser cannot "finish" as a page; the other 17 are the self-directed learning pages, which keep a small amount of network activity going after load. All 41 load correctly when measured the way a visitor sees them.
- Missing read-aloud narration files on the learning and course pages: a real defect, described in `forensic-findings.md` finding 4.

**Interactive inventory.** Every page that returned 200 was loaded again and inspected for forms, buttons and inputs, for pages stuck on "Opening your page", for empty content, and for error text. 159 pages were inventoried (`evidence/page-inventory.json`): 22 carry a form. No page was stuck loading, none showed error text, and none was empty except the root `/`, which is a short entry page that leads to `/home`. The page `/program/plan` carries only about 30 words: the workflow test showed it is a missing page linked from two places (finding 2).

## 2. The main app: user workflows

Each workflow below was driven in a real browser by a tester following the steps a staff member would take, read-only: no form that would create a record on the server was submitted, and the AI assistant was not asked anything in this part (it is covered in section 4).

| Workflow | Result | Problems found |
|---|---|---|
| Home page and site search | works with problems | Self-directed course page (reachable from 'waiver' search results) requests a missing read-aloud JSON file (404) and logs a console error (low); Header logo labelled '...home' takes visitors back to the splash gate '/' rather than /home (low) |
| Minnesota communities list and a community page | works | Search box does not filter as you type; results appear only after Enter/Search (low) |
| Start page form | works | Form has no non-JavaScript fallback: selects have no name attributes and the GET action just reloads /start (low) |
| Learn hub, filters, courses and read-aloud | works with problems | Read-aloud index files are missing (404), so no listen control is ever shown on course pages (medium); Deep link ?course=F02 lands at the top of the catalog rather than at the course viewer (low); 'Save this course to My work' on the self-directed viewer gives no visible confirmation (low) |
| Library search and saving | works with problems | 'Read this resource' primary button label is invisible (text colour equals background) (medium); CLAS page search with no matches shows empty sections and stale counts instead of a 'no results' message (low) |
| Find the right person helper | works | Form is submittable with the DSD radio left on its default; no explicit choice required (low); Two mn.gov result links could not be verified from the test environment (bot-check redirect) (low) |
| Audio library playback and share | works with problems | Two recordings play at the same time (medium); Playback position is lost on reload (low) |
| Equity toolkit practice tool | works | 'Keep these links with my notes' gives no visible confirmation (low); Practice decision quiz state is lost on reload (low) |
| Contribute page and any intake forms (no submission) | works | none |
| My work, plan and progress pages | works with problems | /program/plan is a dead route linked from /start and /program/model (high); Unknown routes return HTTP 200 instead of 404 (low); /program/progress offers no way to record progress despite its name (low) |
| Practice scenarios | works with problems | Scenario index URL /one-dsd/scenarios returns 404 (low); Scenario list is collapsed when arriving at /one-dsd#scenarios (low); No persistence or memory of choices in scenarios; task's assumption of branching flow does not match the site (low) |
| One DSD program pages, equity review and sharing | works | One transient connection drop on the Operationalizing equity Word download (low); Embedded videos have no <track> captions element; captions are only a separate download (low) |

Where saved data lives: saved resources, learning progress, practice plans and My Work all persist across reloads, in the visitor's own browser only. Nothing is stored on the server, and the site tells visitors so. A different browser or computer starts empty.

What each tester did, step by step, with every request and its status, is in `evidence/workflow-tests.json`. No form that would create a record on the server was submitted.

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

- **Real browser, two sessions, seven questions.** Five were answered in 24 to 36 seconds, with follow-up questions understood in context, and "Clear this conversation" worked. The first question in each session showed "We couldn't finish that answer just now". An independent check against Railway's own records showed both were caused by this test environment's network, which stopped waiting after about 20 to 30 seconds: the app answered one of them successfully after 33.8 seconds and was still working on the other. Railway recorded no server error for the assistant during the test.
- **Direct requests.** Nine short questions were answered correctly in 11 to 42 seconds, including seven sent at the same moment. A question asked again later gave a full, accurate answer.
- **What this means.** The assistant works, but it is slow enough that any network that cuts connections at about 30 seconds will show staff the failure message (finding 5). It also starts each release without its search index ready (finding 6), and bursts of questions hit the research provider's limit (finding 7).
- **Voice.** The settings endpoint responds; the worker endpoint is protected. No microphone test was possible from an automated browser.
- Evidence: `evidence/ask-e2e.json`, `evidence/ask-repeat.json`, `evidence/ask-post.json`, `evidence/ask-retest.json`, `evidence/finding-verification.json` (findings F2 to F5), and the screenshot `evidence/ask-e2e-screenshot.png`.

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

The dead link to `/program/plan`, missing pages that answer 200, the missing read-aloud files, the slow Ask answers, the search index warming late, the research rate limit, the Ask endpoint's lack of a per-visitor limit, the invisible button label, overlapping audio, and the slow listing pages under load. Each has a described fix in `forensic-findings.md`.

## 11. Limits of this test

- Plain-HTTP redirection and the TLS certificate could not be checked from this environment (its network allows only HTTPS).
- The AI assistant was limited to about 17 real requests to keep credit spending small.
- No microphone, camera or screen-reader testing.
- The older copy services were not tested beyond confirming they respond.
