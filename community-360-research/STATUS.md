# Community 360 research: status

**Checked:** October 30, 2026

## Where things stand

Web access from this session is blocked for every source site tried, and `git push` to GitHub is refused. Both have to be fixed before the community profiles can be researched. Details below. Meanwhile, the parts that do not need the web have been built: a calculated cultural calendar, a note on how cultural calendars work, and brief links for every calendar entry.

## Done

- `calendar/cultural-calendar.json`: 110 observances across the 39 communities, with 2026, 2027 and 2028 dates where they can be calculated, the rule that sets each date, how certain the date is, what it marks, and a link to the existing brief page for each community. `howCelebratedInMinnesota`, `minnesotaEvents` and `workplaceNote` are empty: they need opened sources.
- `calendar/cultural-calendar.ics`: 287 all-day events for the fixed and calculated dates. Moon-sighted and announced dates are left out.
- `calendar/calendar-by-month.md`: month-by-month reading view with brief links.
- `calendar/how-cultural-calendars-work.md`.

The observances were drawn from two places: the "Dates of Significance" section of each of the existing 41 briefs (read from the repository's own brief data, not the live site, which could not be opened), and standard national and religious calendars. The dates are computed locally with calendar libraries, as described in the how-it-works note; they have not yet been checked against an opened official announcement.

## In progress

- None. The research cannot start until the network is opened.

## Not started

- All 39 community profiles, business lists and corrections files.
- `cross-cutting/small-communities-methods.md`.
- Minnesota event listings, celebration descriptions and workplace notes for the calendar.

## Blocked: web access

Each of these failed both through the page-fetch tool and through a direct HTTPS request on October 30, 2026 (the network policy refuses to resolve the host):

- one-dsd-people-access-culture-production.up.railway.app (the existing community pages)
- www.mncompass.org, www.census.gov, data.census.gov, mn.gov, www.health.state.mn.us
- www.mnhs.org, www.mnopedia.org, www.umn.edu, ici.umn.edu
- sahanjournal.com, www.startribune.com, www.mprnews.org, www.minnpost.com
- visitsaintpaul.com, www.rivercentre.org, www.hmongcc.org, hmongtimes.com, www.google.com

Web search works but returns only titles and snippets. The project rules say a snippet is never a checked source, so the profiles were not started.

Fix: in the cloud environment's settings (environment menu in the session title bar, then Edit, then Network access), choose full internet access. A list of named domains is not practical, because the research needs hundreds of sites across 39 communities. Steps: https://code.claude.com/docs/en/cloud-environments#network-access

## Blocked: GitHub push

`git push` returns 403: Claude does not have GitHub access to this repository for the organization. The GitHub connector can read the repository but cannot create branch references either (the same 403). Fix: reconnect GitHub at https://claude.ai/connect-github and make sure the Claude GitHub App is installed on `Gary-design63/one-dsd-web`.

## Could not be established

- Everything the profiles require, for now, because no source could be opened.
- Karen New Year has no 2026 Gregorian date in the calculation (it fell on December 19, 2025 and next falls on January 8, 2027); confirm with Minnesota Karen organizations which weekend they celebrate.
