# Forensic findings: One DSD People, Access and Culture

Test date: October 31, 2026 (UTC). Gary gave permission to inspect and change the Railway project, test the live app, and spend a small amount of AI credit on real questions.

This document records what was found, how it was established, what was fixed, and what still needs a change. Every finding below was checked twice by independent reviewers before it was written down here: one compared it against the saved evidence, and one re-checked it against the live system and Railway's own logs. Their verdicts are in `evidence/finding-verification.json`. Where a reviewer showed a first finding was wrong or overstated, the corrected version is what appears below, and the correction is noted.

Companion documents: `smoke-test-report.md` (every page and workflow tested), `stress-test-report.md` (load test), and `evidence/` (raw results).

## What the system is

One Railway project, `one-dhs-dsd-pac`, with eight services in `production`:

| Service | What it is | State found |
|---|---|---|
| `one-dsd-people-access-culture` | The main app (Next.js) | Live and healthy; deployed by upload from Gary's computer, with no GitHub source connected |
| `cultural-calendar` | The calendar site and the course, served from this repository | Live; was out of date (finding 1, now fixed) |
| `Postgres` | The database | Live since October 5; no errors since October 24 |
| `pac-daily-orchestrator` | Meant to run scheduled work | Switched off (finding 9) |
| Four older services | Earlier copies of the app | Still running in public (finding 10) |

The app's source code is only on Gary's computer, a Windows Surface Pro. Cloud sessions cannot reach Windows folders through Remote Control, so every finding about the app was established from outside it: in a real browser, by direct requests, and from Railway's logs and metrics. Code-level fixes are described, not made.

## Findings, most important first

### 1. Fixed: the calendar site had stopped updating

**What was wrong.** Railway rebuilt the calendar site at 01:21 UTC and then did nothing for the many pushes that followed over the next four and a half hours. The live site had 386 calendar entries while the branch had 576, and the course address returned "not found".

**Why.** Railway deploys a push automatically only when a member of the Railway project has a connected GitHub account with contributor access to the repository. The repository's only collaborator is `alphaequity123-afk`; the GitHub account connected to the Railway project appears to be `Gary-design63`. Railway showed no skipped, waiting or approval-pending deployments: the pushes simply never reached it.

**What was done.** Reconnecting the service's source makes Railway build the latest commit at once. That was done at 05:41 and 06:06 UTC, and the live site is current: 576 entries and the course at `/course/`.

**What Gary needs to do (one of these), or the problem will come back with the next edit:**
- In GitHub, add `Gary-design63` as a collaborator with write access on `alphaequity123-afk/one-dsd-pac-standalones`, and make sure the Railway GitHub App can see that repository. Then, in Railway, open the `cultural-calendar` service settings and confirm automatic deployments are on for branch `community-360-research`.
- Or connect the `alphaequity123-afk` GitHub account to the Railway account instead.

**A leftover to clear.** One harmless change is staged on the Railway environment and not applied: the calendar service's root directory re-saved with the same value. In the dashboard it shows as one pending change. Apply it or discard it.

### 2. Dead link: "Plan and review your work" leads to a missing page

The page `/program/plan` shows the site's "We could not find that page" message. Two live links send people there: on `/start`, inside "More ways to connect, lead, and find support", the card "Help shape practical change" ("Plan and review your work"); and on `/program/model`, the card "Choose learning for your question". Severity: high, because a visitor following the site's own guidance hits a dead end.

**Fix (code).** Point both links at the right page (probably `/my-work/plan`), or create `/program/plan`.

### 3. Missing pages answer "200 OK" instead of "404 Not Found"

Some missing addresses under `/program/` (for example `/program/plan`, and any made-up address there) show the not-found message but report success to the browser. Visitors see the right message, but link checkers and monitoring cannot detect broken links, which is how finding 2 went unnoticed. Other parts of the site answer missing pages correctly with 404.

**Fix (code).** Make the not-found page return status 404 everywhere.

### 4. Read-aloud does not work on the learning pages

Every learning and course page tries to load a narration file from `/learning/geffen-read-aloud/courses/`. All of them are missing: across the crawl, 207 distinct narration files returned 404, on the self-directed course viewer and on 153 course pages. Because the file is missing, the "Listen through the page" control stays hidden, so staff never see the read-aloud option and get no explanation. Each page also logs an error, and the course viewer requests the missing file again on every page turn.

**Fix (content and code).** Publish the narration files, or remove the feature's request when the files are not meant to exist.

### 5. The Ask assistant is slow enough that some networks will cut it off

**What was first reported, and the correction.** In the browser tests, 2 of 7 first questions showed "We couldn't finish that answer just now" with an error status. An independent reviewer matched those two requests to Railway's own records: the app actually answered one successfully after 33.8 seconds, and the other was still working at 30.1 seconds when the test machine's network proxy gave up. Railway recorded no server error for the Ask service at all. The failures were caused by the test environment, not the app.

**What is true.** Answers take a long time: 16 to 36 seconds in the browser tests, and 11 to 42 seconds by direct request. Any network, proxy or device that stops waiting after about 30 seconds, as the test machine's did, will show staff the failure message even though the app is still working on the answer. Some government and office networks do impose such limits.

**Fix (code).** Stream the answer as it is written, or send something back within a few seconds and fill it in, so no connection sits silent for 30 seconds. Show a retry button on the failure message.

### 6. The search index warms up only when the first questions arrive

During the test, the first eight questions (over about six and a half minutes) each logged that the program's own material could not yet be searched by meaning (`pac_local_semantic_unavailable`, reason `index_warming`). Questions after that did not. The index is evidently prepared lazily, starting with the first question after each deployment, so for the first several minutes after every release the assistant answers without searching the program's own material as designed.

**Fix (code).** Warm the index at startup, before the app reports itself ready.

### 7. Bursts of questions hit the research provider's rate limit

Seven questions sent at the same moment produced four "rate limit exceeded" refusals from the outside research provider, and three more research attempts in the same burst found no usable sources. All seven questions still received answers (they did not need outside research), so staff would not have noticed. A burst that did need research would get weaker answers.

**Fix (code).** Queue research calls, or cap how many run at once.

### 8. The Ask endpoint has no visible per-visitor limit

The Ask endpoint can be called by a script from outside the site. A burst of such requests was answered in full, with no limit observed at that volume. The method is in the private copy of this report given to Gary, not here, because this repository is public. The app has a rate-limit setting configured, so a limit may exist at higher volumes. One database error on October 24 shows the limit's table was missing at that moment, though not that the limit failed open.

**Fix (code).** Confirm the limiter works and refuses requests when its table is unavailable; add a per-visitor cap on questions per minute.

### 9. Scheduled orchestration is switched off

The `pac-daily-orchestrator` service only prints "Scheduled orchestration disabled", has no schedule, and never restarts. Anything that expects a daily run (the app's settings mention a daily review and consultation retention and recovery) is not happening. If that is intended, the service can be deleted; if not, it needs a schedule and a real command.

### 10. Two older full copies of the app are still running in public, with live AI keys

Four older services are live, each on a public address. Two of them, `one-dhs-pac-clone` and `one-dhs-dsd-restored`, are full working copies of the app with 50 GB storage volumes and live AI provider keys, so they can spend credit if anyone finds them; `one-dhs-dsd-restored` also holds database connection settings. The other two, `one-dsd-prototype` and `one-dhs-dsd-demo`, are static pages with no keys or storage. (Corrected: the first version said all four were full copies and three had volumes.) Addresses are in the private copy of this report.

**Fix (decision).** Decide which, if any, to keep. Delete or sleep the rest, and rotate any keys shared with production.

### 11. The main app is deployed by hand, with many failed attempts

The main app has no GitHub source; each release is an upload. The last week shows 22 failed deployments, in clusters, including 7 failures in 33 minutes on October 30 and 2 more just before the current release at 00:59 UTC October 31. (Corrected from 12, which counted only the last five days.) Nothing is wrong with the running app, but there is no record of exactly what code is live and no way to roll back by version.

**Fix (process).** Put the app's source in a private GitHub repository and deploy from it. Steps for Gary are in section "Getting the code into GitHub" below.

### 12. Smaller interface problems found in the workflow tests

- **Invisible button label (medium).** On library resource pages, the main "Read this resource" button is blue text on a blue background, so it shows as an empty blue box. Confirmed on `/library/ja-plain-language`, `/library/ja-language-access-checklist` and `/library/lm-interpreter`.
- **Two recordings play at once (medium).** In the audio library, starting a chapter in one podcast does not pause another that is already playing.
- **Low:** the header logo goes to the welcome splash page rather than `/home`; the scenario index `/one-dsd/scenarios` is a missing page; the course viewer opens at the top of the catalog rather than at the chosen course; "Save" on the course viewer and the toolkit gives no confirmation; the library search on the CLAS page shows empty sections rather than "no results"; the communities filter waits for Enter rather than filtering as you type; embedded videos have no on-screen captions track (captions are a separate download); and the Start page and Find the Right Person forms need JavaScript. Full details and steps to reproduce are in `evidence/workflow-tests.json`.

### 13. Memory stays high after load

The app normally uses about 0.9 GB of working memory. During the load test it rose to 4.2 GB, and three hours later it still sits at 4.2 GB with the processor idle. That is far below the 24 GB limit, and it may simply be the way Node keeps memory it has used. Watch it over the coming days: if it keeps climbing with each busy period, there is a leak, and the app will need a restart until it is fixed.

### 14. Database

Postgres has run without restart since October 5. The only errors in the window examined were on October 24: four failed password attempts and one missing-table error. None since. It runs on one node; Railway offers volume backups and a high-availability option if wanted.

### 15. Fixed: two problems in the course site

- `/course` without a trailing slash showed the page unstyled with broken links. All course links are now absolute, and the address works both ways.
- Nothing on the calendar linked to the course. The calendar page now does.

## Verified working

- 492 distinct pages and states crawled with status 200; all 39 community pages, all 24 document downloads, and all 72 course slide decks load correctly.
- Twelve user workflows driven end to end in a real browser: five work fully, seven work with the problems listed above, none is broken.
- Saving resources, learning progress and plans works and persists across reloads, in the visitor's own browser only (nothing is stored on the server, and the site says so).
- Security at the edges is strong: strict HTTPS with preload, a content security policy, frame denial, no cookies for anonymous visitors, protected internal endpoints, and probes for configuration files and admin pages all refused.
- Under 25 simultaneous visitors for five minutes: zero server errors (see `stress-test-report.md`).
- The automatic rebuild in GitHub ran three times successfully and once rebuilt the calendar on its own.

## Getting the code into GitHub

Because the app's code is on a Windows computer, the only way to fix findings 2 to 8 and 11 from a cloud session is to put the code in GitHub:

1. On the Surface, open the Claude desktop app in the folder that holds the app's code (the one with `package.json`).
2. Ask it to create a new private repository under `alphaequity123-afk` named `one-dsd-people-access-culture` and push the folder, excluding any `.env` or other secret files.
3. Share the repository name with the cloud session, which can then attach it, make the fixes, and connect the app to deploy from GitHub.

## Limits of this test

- The app's source could not be read; causes are inferred from behaviour and logs.
- Plain-HTTP redirection and the TLS certificate could not be checked from this environment, whose network allows only HTTPS.
- About 17 real questions were sent to the Ask assistant; no microphone, camera or screen-reader testing was done.
- The crawler stopped at its limit of 600 page addresses. Pages beyond that are of the same kinds already covered (course pages and their states).
- The older copy services were checked by the reviewers only for what they are, not tested.

## Recommendation on refactoring

Do not rewrite the app: it is fast at rest, secure at the edges, and its faults are specific. Spend the effort on engineering hygiene first (source in GitHub, deployment from GitHub, a staging copy, the older copies retired, these checks run before each release), then fold the research work (the 39 profiles, the calendar, the course) into the app itself, so there is one address and the Ask assistant can draw on all of it.
