# Forensic findings: One DSD People, Access and Culture

Test date: October 31, 2026 (UTC). Tester: the cloud session Gary opened for the Community 360 research, with his permission to inspect and change the Railway project, test the live app, and spend a small amount of AI credit on real questions.

This document records what was found, how it was established, what was fixed, and what still needs a decision or a code change. The companion documents are `smoke-test-report.md` (every page and workflow tested, with results), `stress-test-report.md` (load test), and the `evidence/` folder (raw results exactly as the tools produced them).

## What the system is

The program runs on one Railway project, `one-dhs-dsd-pac`, with eight services in its `production` environment:

| Service | What it is | State found |
|---|---|---|
| `one-dsd-people-access-culture` | The main app (Next.js), public at `one-dsd-people-access-culture-production.up.railway.app` | Live, healthy, deployed by direct upload from Gary's computer; no GitHub source connected |
| `cultural-calendar` | The calendar site and the course, served from this repository's `community-360-research/calendar` folder | Live; was stale (see finding 1) |
| `Postgres` | The database | Live since October 5; no errors since October 24 |
| `pac-daily-orchestrator` | Meant to run scheduled work against the app | Live but switched off: its only job is to print "Scheduled orchestration disabled" |
| `one-dhs-pac-clone`, `one-dhs-dsd-restored`, `one-dsd-prototype`, `one-dhs-dsd-demo` | Older copies of the app | All four still running and publicly reachable (see finding 7) |

The main app's source code exists only on Gary's computer. The repository `one-dsd-web` on GitHub was last updated September 25 and is behind what is deployed. Gary's computer offers folders to Remote Control, but his computer does not make them available to cloud sessions, so the code could not be opened from here. Every finding about the app below was established from the outside: by using it in a real browser, calling its endpoints, and reading its logs and metrics through Railway.

## Findings, most serious first

### 1. Fixed: the calendar site was stale and the course was not published

**What was wrong.** Railway last rebuilt the calendar site at 01:21 UTC. About forty pushes followed over the next four hours, and none produced a deployment. The live site had 386 calendar entries while the branch had 576, and the course address returned "not found".

**Why.** Railway only deploys a push automatically when a member of the Railway project has a connected GitHub account with contributor access to the repository (Railway's documented requirement). The repository `alphaequity123-afk/one-dsd-pac-standalones` has exactly one collaborator, `alphaequity123-afk`. The GitHub account connected to the Railway project appears to be a different one, `Gary-design63` (it is the source of the `one-dhs-dsd-restored` service). Railway therefore never acted on the pushes: there were no skipped, waiting or approval-pending deployments, just nothing.

**What was done.** Reconnecting the service's source to the branch makes Railway build the current commit immediately. That was done twice, at 05:41 and 06:06, and the live site is now current: 576 entries, the course live at `/course/`, and the fixes in finding 9 included. Because the connected-account problem remains, the next pushes will again sit undeployed until one of the steps below is taken.

**What Gary needs to do (one of these):**
- In GitHub, add the `Gary-design63` account as a collaborator with write access on `alphaequity123-afk/one-dsd-pac-standalones`, and make sure the Railway GitHub App has access to that repository. Then, in Railway, open the `cultural-calendar` service settings and confirm automatic deployments are on for branch `community-360-research`.
- Or connect the `alphaequity123-afk` GitHub account to the Railway account instead.

Until then, a deploy can be forced from a session like this one by reconnecting the source, or from the Railway dashboard with "Deploy latest commit".

**A leftover to clear.** One Railway change was staged but not committed: re-saving the calendar service's root directory (same value) to recreate its deployment triggers. The commit step needed an approval that did not come through. The staged change is harmless. In the Railway dashboard it shows as one pending change on the environment; apply it or discard it.

### 2. The Ask assistant fails on some first questions

**What happens.** In a real browser, 2 of 7 fresh questions ended with the message "We couldn't finish that answer just now". The server answered those two with HTTP 502 after 20 to 33 seconds. The other five were answered in 20 to 36 seconds. Evidence: `evidence/ask-e2e.json`, `evidence/ask-repeat.json`.

**What the logs show.** Each failure lines up with a `research_failed` event from the live web-research step (provider `perplexity_agent`, depth `current_web`) with the codes `research_unresolved_citation` or `research_no_tool_evidence`. When the research step cannot produce a usable citation, the request fails instead of falling back to an answer from the program's own material. The same question asked again a few minutes later succeeded (`evidence/ask-retest.json`), so this is intermittent and depends on the research provider.

**A second problem underneath.** On every single question during the test, the app logged `pac_local_semantic_unavailable` with `reason: index_warming`, across more than eight minutes. The index that is supposed to search the program's own material first never reported itself ready. Answers still arrived, so the app is working around it, but "the program's own material first" is not happening as designed, and nothing shows this to anyone.

**A third.** Seven questions sent at the same moment drove the research provider into its rate limit (`research_http_429`, "Request rate limit exceeded"). A handful of staff asking at once would see failures. Those particular requests still returned answers because they did not need research.

**What is needed (code changes on Gary's computer).** When research fails, answer from program material and say that current public sources were unavailable, rather than returning 502. Make the index warm at startup, or wait for it on the first request, and alert when it stays unready. Queue or cap concurrent research calls. Show a retry button on the failure message.

### 3. The Ask endpoint accepts requests from outside the site without limit

The Ask endpoint can be called by a script from outside the site; a small burst of such requests sent together were all answered (`evidence/ask-post.json`), and no per-visitor rate limit was observed at that volume. The method and exact numbers are in the private copy of this report given to Gary, not here, because this repository is public. The app has a rate-limit secret and a rate-limit table, so a limit may exist at a higher volume; the test stopped there to avoid spending credit. On October 24 the database logged `relation "pac.runtime_rate_limits" does not exist`, which suggests the limiter was at least once missing its table. If it fails open when the table is missing, that is a silent failure worth a code check.

**What is needed.** Confirm the limiter works and fails closed; add a per-visitor cap on questions per minute; consider a short-lived session token issued by the page.

### 4. Read-aloud narration files are missing on learning pages

The page `/learn/self-directed` requests `/learning/geffen-read-aloud/courses/self-directed-F01.json` and gets 404; the page's audio element has no source. Probing the same pattern for four other courses also returned 404 (`cultural-intelligence-F01`, `collaboration-F01`, `equity-toolkit-F01`, `equity-in-practice-F01`). The full list of pages affected is in `smoke-test-report.md`. The user sees no error; the read-aloud feature simply does nothing.

**What is needed.** Publish the narration files, or hide the control when the file is absent.

### 5. Scheduled orchestration is switched off

`pac-daily-orchestrator` runs an image whose start command only prints "Scheduled orchestration disabled" and exits, with no schedule. Anything in the app that expects a daily run (the app's variables mention a daily review and consultation retention and recovery settings) is not happening. This may be intentional. If so, the service can be deleted to remove the ambiguity; if not, it needs a schedule and a real command.

### 6. The main app is deployed by hand, with many failed attempts

The main app has no GitHub source connected; each deployment is an upload. The last week shows 12 failed deployments before successes, including 10 failures in one hour on October 30 (`evidence/railway-snapshot.json`). Nothing is wrong with the running app, but there is no record of what code is live, no way to roll back by commit, and each release depends on one computer. The strongest single improvement available is to put the app's source in GitHub and deploy from it.

### 7. Four older copies of the app are still running in public

`one-dhs-pac-clone`, `one-dhs-dsd-restored`, `one-dsd-prototype` and `one-dhs-dsd-demo` each answer on a public address with a full copy of the app. Three carry 50 GB volumes, and at least one holds live AI provider keys, so it can spend credit if anyone finds it. Their addresses are in the private copy of this report. They cost money and widen the surface. Gary asked for them to be reported, not tested, so they were left alone.

**What is needed.** Decide which, if any, to keep. Sleep or delete the rest and rotate any keys they share with production.

### 8. Database

Postgres has run without restart since October 5. Its only errors in the window examined were on October 24: four failed password attempts for user `postgres` and the missing rate-limit table noted above. None since. The database is on a single node with a 50 GB volume and no backup schedule visible from here; Railway offers volume backups and a high-availability conversion if those are wanted.

### 9. Fixed: two problems in the course site

- Visiting `/course` without a trailing slash showed the page with its styling and links broken, because the pages used relative links. All course links are now absolute, and the address works both ways (verified live).
- Nothing on the calendar site linked to the course. The calendar page now carries a plain text link to it.

### 10. Verified working

- Every one of the 39 community pages on the live app returns 200.
- Security headers on the app are strong: strict transport security with preload, a content security policy, frame denial, no sniffing, same-origin referrer policy, and camera, microphone and location disabled. No cookies are set for anonymous visitors. Probes for `.env`, `.git`, admin and debug paths all return 404. The voice worker endpoint requires authentication (401 to outsiders).
- Page speed on the app: typical responses in 13 to 29 milliseconds over the past week, with no page slower than 163 milliseconds at the 99th percentile. The 15-second figure Railway reports for the service as a whole is the voice worker's deliberate 15-second long poll, not slowness.
- Server errors over the past week: 35 out of 51,738 requests (0.07 percent). Client errors: 466, mostly 404s.
- Memory: average 0.9 GB, peak 3.0 GB of a 24 GB limit. CPU: negligible. Disk: 0.8 GB of 50 GB.
- The automatic rebuild in GitHub (`.github/workflows/rebuild-research-site.yml`) ran three times, all successful, and on the third run committed a rebuilt calendar on its own, which proves the whole path works.
- The calendar site and course: all 10 pages load with no console errors, no failed requests and no broken images; the calendar data file parses (576 entries) and the `.ics` file carries 542 events.

## Limits of this test

- The app's source could not be read, so causes are inferred from behaviour and logs, and fixes to the app itself are described rather than made.
- Plain-HTTP-to-HTTPS redirection and the TLS certificate could not be checked from this environment, whose network proxy allows only HTTPS. Railway enforces both by default.
- The repository's webhook list is not readable through the GitHub access available here.
- AI questions were limited to about 15 in total to keep credit spending small.
- The four older copies were not tested beyond confirming they respond.

## Recommendation on refactoring

Do not rewrite the app; it is fast, secure at the edges, and its faults are specific. Spend the effort on engineering hygiene first: source in GitHub, deployment from GitHub, a staging environment, the old copies retired, and the checks in this folder run before each release. Then fold the research work (the 39 profiles, the calendar, the course) into the app itself rather than keeping a separate site, so there is one address, one navigation, and the Ask assistant can draw on all of it.
