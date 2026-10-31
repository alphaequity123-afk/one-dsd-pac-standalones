# Community 360 research: status

**Checked:** October 31, 2026

## Where things stand

14 of 39 communities are finished. Karen, Somali, African American, Latino, Mexican, Vietnamese, Oromo, Ethiopian, rural and Indian have gaps listed below, because web search ran out during their research. The research is moving from one computer to a cloud session. `RESEARCH-BRIEF.md` holds the full instructions for each community.

## Done

- **Communities:** hmong, karen, somali, african-american, latino, mexican, vietnamese, oromo, ethiopian, rural, indian, korean, filipino, japanese.
- `cross-cutting/small-communities-methods.md`.
- **Calendar dates:** checked against opened sources (`calendar/tools/date-checks.json`). 591 of 811 dated entries have an opened source that confirms the date.
- **Calendar tools:** `calendar/tools/merge_calendar.py` and `build_viewer.py` rebuild the JSON, `.ics`, month view, viewer and index from `calendar/seed-by-community/` and each community's `calendar-entries.json`.

## In progress

- In the cloud session (started October 31, 2026): chinese, lao now running. The rest of the 28 are listed under Not started.

## Next, after the 28 communities

Gary asked for a second pass on the 10 communities that web search left thin: karen, somali, african-american, latino, mexican, vietnamese, oromo, ethiopian, rural, indian. Each profile's "What could not be established" section names what is thin. Add to the existing files rather than starting over, follow the same brief and checks, and commit and push after each one.

ethiopian, oromo, vietnamese, indian and rural are finished, and nothing is still running on Gary's computer. The Railway `cultural-calendar` service is connected to this branch, so do not change anything on Railway.

## Not started

amharic, american, arabic-speaking, bosnian, burmese, colombian, cuban, deaf-deafblind-hard-of-hearing, ecuadorian, european-american, french, guatemalan, kenyan, khmer, lebanese, liberian, minnesota, nigerian, puerto-rican, russian-speaking, salvadoran, thai, ukrainian.

## Still to do on the calendar

- Fill Minnesota details and organizer dates as each community finishes.
- Update `calendar/how-cultural-calendars-work.md` from `calendar/calendar-methods-sources.md`. The note still says it was written without opened sources.

## How dates are treated

- Commercial calendar sites do not confirm a date. They only add a note.
- Official sources that disagree confirm nothing. Holi 2027 stays unconfirmed because the Government of India's holiday list says March 23 and the panchang says March 22.
- Moon-sighted dates are never shown as confirmed.
- The `.ics` file carries confirmed dates only.

## Blocked sources

Hmong and the methods note could not open these: Star Tribune, Christian Century, the state charter school directory, Carleton's Religions in Minnesota, mn.gov pages (State Demographic Center, Department of Veterans Affairs), the University of Minnesota Conservancy, state courts, the Senate roster, Department of Education pages, and ICPSR.

- Japanese could not open: Consulate-General of Japan in Chicago, Minneapolis Institute of Art collection pages, the Legacy grants site, Minnesota courts, Minnesota Reformer, Densho Encyclopedia, Explore Minnesota, Solstice magazine and Como Zoo's Japanese garden page.

- Filipino could not open: Star Tribune, MinnPost, KARE 11, Axios, Bring Me The News, Minnesota Council on Asian Pacific Minnesotans pages, the MDH resource directory and the Festival of Nations site.

- Korean could not open: JangmiArts, the Korean Cultural Association, Adoption Literacy, Minnesota Reformer, Axios, the UMN Conservancy, one Korean Quarterly article, and most Korean church sites. Sahan Journal sometimes refuses requests for a while (too many requests).

## Could not be established so far

- **Japanese:** 74 opened sources. Web search ran out partway (the shared limit of 200 searches per round), and the rest was done by opening pages directly. Thin: groceries, bakeries and professional firms (none confirmed open), religion, and Minnesota disability and health evidence. Not established: how many Japanese nationals and company transferees live here, religious makeup, events for Hinamatsuri, Kodomo no Hi, Tanabata or Setsubun, the Cha-Ami Japanese Cultural Center's address, and Judge Susan Burke's current status. 4 of 23 businesses could not be confirmed open.
- **Filipino:** 65 opened sources; web search worked throughout but Minnesota material was thin. The business list is short (12: 3 open, 8 could not be confirmed open, 1 closed) and no Filipino law, accounting, insurance, tax, travel or salon business, chamber or media outlet was found. Not established: any 2026 or 2027 date for Philippine Day, Pasko sa Nayon, Simbang Gabi or other Minnesota Filipino events (the organizers post only on social media, which could not be read), Filipino-specific health or disability data (the state table is suppressed), Iglesia ni Cristo, Protestant or Muslim Filipino congregations, occupations, and Philippine language counts.
- **Korean:** full depth (105 opened sources, web search worked throughout). Not established: a government count separating Korean adoptees from immigrants (estimates run 10,000 to 15,000), any Korean chamber of commerce or Korean-owned professional firm, a Minnesota group for Korean families with disabilities, and Minnesota data on how Korean immigrant families understand disability. 10 of 21 businesses could not be confirmed open, including Sole Cafe, Hoban and Dong Yang; Young Joni and Kim's have closed.
- **Indian:** web search reached its limit partway. 73 of 89 businesses could not be confirmed open, and most of that list comes from an undated directory. Not established: 2026 dates for the Woodbury Diwali, Gujarati Samaj Garba, Vaisakhi, Gurpurab, Onam and any Indian-organized Eid, Mar Thoma, Orthodox and other Christian congregations beyond the Syro-Malabar mission, any mosque described as Indian-rooted, state disability data for Indian residents, faith counts, caste, working-class evidence and current elected officials.
- **Rural:** web search reached its limit partway, so religion, small-town civic life and immigrant-owned businesses are thin. Not established: counts of closed or merged rural congregations, any page on rural mosques, synods or Amish communities, 2026 direct support vacancies and assessment waits by county, dates for King Turkey Day and the pheasant and waterfowl openers, and exact USDA farm totals and producer race. 19 of 58 businesses could not be confirmed open. Greater Minnesota totals are added up from Census county tables.
- **Ethiopian:** web search reached its limit partway. Not established: current Minnesota reaction to the renewed fighting of October 2026, Tigrayan or Amhara Minnesotan voices on the war, separate counts for Amhara, Tigrayan or Gurage people, occupation data, Ethiopian-owned law, tax, accounting, clinic and salon businesses, named mosques, and disability evidence beyond one Compass figure. 14 of 30 businesses could not be confirmed open.
- **Oromo:** web search reached a limit of 200 searches for the working session, so sections 3, 4, 7 and 11 and parts of 5, 9 and 12 are thin, and law, tax, travel, salon, grocery and clinic businesses were not surveyed (13 businesses listed, 5 unconfirmed). Not established: an actual Oromo count (estimates run from 8,500 to over 100,000; the firmest figure is 3,297 students with Oromo as home language, 2024-25), any Minnesota Waaqeffanna congregation, current faith shares, a confirmed Oromo elected official, and Oromo-specific income, health or disability data.
- **Vietnamese:** web search ran out partway. Not established: a Minnesota deportation count, effects of Operation Metro Surge, disability, health and clinic evidence beyond Compass and state counts, elected officials, Protestant, Cao Đài and Hòa Hảo groups, town-level population, and 2026 dates for Black April and Little Mekong Night Market. 21 of 48 businesses could not be confirmed open. Compass really does publish the same median income for Hmong and Vietnamese households ($92,644), with different margins.
- **Mexican:** web search ran out, so sections 2, 3, 4, 5, 8, 9, 10, 11 and 13 are thinner than the brief asked, along with law, accounting, insurance, tax, salon, travel, bakery and Greater Minnesota businesses. 29 of 57 businesses could not be confirmed open. Not established: current Mexican-only counts by town, Mexican nationals among those arrested in Operation Metro Surge, any Mexican-specific Minnesota disability study, and public Posadas, Via Crucis, Reyes or 2026 Guadalupe schedules.
- **African American:** web search ran out, so law and accounting firms, charter schools, arts organizations, Black professionals and current school data are thin. Not established: a count separating descendants of U.S. slavery from other U.S.-born Black people, current county and city counts, Black wealth or faith shares, and any Black-led disability or Black Deaf organization (absence not proven). 44 of the 72 businesses listed as open rest only on the Spokesman-Recorder's July 2026 finalist list. The Rondo Days 2026 date comes from MPR's "Saturday" in a July 15 story.
- **Latino:** web search ran out, so recent reporting from Worthington, Willmar and Austin is missing and no professional firms were confirmed. 23 of 42 businesses could not be confirmed open. Not established: Latino wealth, undocumented counts, union membership, a dated firm count, Indigenous-language speakers, religious affiliation, waiver use and special education by ethnicity.
- **Somali:** web search ran out partway, so sections 5, 7, 8 and 10 and the Greater Minnesota businesses are thinner than the rest and need another pass. Not established: household wealth, a current Somali chamber of commerce, theological differences, Somali Christians and people of no faith, dress, marriage and elder-care customs, adult and non-autism disability evidence, Somali-specific Eid al-Adha events, and statewide Somali graduation rates. 19 of 56 businesses could not be confirmed open, and many Lake Street guide entries do not state Somali ownership.
- **Karen:** a real Karen count or Karen-only economic data (only Burmese figures and estimates), any Minnesota disability count or study, and Karen elected officials. Web search ran out before these were reached: state refugee arrival tables, Karen roles in the 1947 Panglong agreement, PACER's Karen materials, lead screening, and whether several shops are still open. 14 of 20 businesses could not be confirmed open. Union Day was dropped because no Minnesota observance was found, not because Karen views of it were checked.
- **Hmong:** household wealth, use of waivers or personal care assistance, a total for deportations to Laos, religious shares, occupations, a Hmong Deaf community, and any 2027 New Year dates. The profile lists the rest.
- **Calendar:** how Minnesota mosques decide their dates, because the one report found could not be opened. Also no opened date for future Islamic observances, Ashura or Mawlid 2026, Holodomor, Rondo Days, or Vyshyvanka 2027 and 2028.
