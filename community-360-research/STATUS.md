# Community 360 research: status

**Checked:** October 31, 2026

## Where things stand

26 of 39 communities are finished. Karen, Somali, African American, Latino, Mexican, Vietnamese, Oromo, Ethiopian, rural and Indian have gaps listed below, because web search ran out during their research. The research is moving from one computer to a cloud session. `RESEARCH-BRIEF.md` holds the full instructions for each community.

## Done

- **Communities:** hmong, karen, somali, african-american, latino, mexican, vietnamese, oromo, ethiopian, rural, indian, korean, filipino, japanese, chinese, lao, khmer, thai, burmese, bosnian, russian-speaking, ukrainian, lebanese, arabic-speaking, colombian, ecuadorian.
- `cross-cutting/small-communities-methods.md`.
- **Calendar dates:** checked against opened sources (`calendar/tools/date-checks.json`). 591 of 811 dated entries have an opened source that confirms the date.
- **Calendar tools:** `calendar/tools/merge_calendar.py` and `build_viewer.py` rebuild the JSON, `.ics`, month view, viewer and index from `calendar/seed-by-community/` and each community's `calendar-entries.json`.

## In progress

- In the cloud session (started October 31, 2026): liberian, nigerian, kenyan, amharic, guatemalan, salvadoran, cuban, puerto-rican, french, deaf-deafblind-hard-of-hearing now running. The rest of the 28 are listed under Not started.

## Next, after the 28 communities

Gary asked for a second pass on the 10 communities that web search left thin: karen, somali, african-american, latino, mexican, vietnamese, oromo, ethiopian, rural, indian. Each profile's "What could not be established" section names what is thin. Add to the existing files rather than starting over, follow the same brief and checks, and commit and push after each one.

ethiopian, oromo, vietnamese, indian and rural are finished, and nothing is still running on Gary's computer. The Railway `cultural-calendar` service is connected to this branch, so do not change anything on Railway.

## Not started

american, european-american, minnesota.

## Still to do on the calendar

- Fill Minnesota details and organizer dates as each community finishes.
- Update `calendar/how-cultural-calendars-work.md` from `calendar/calendar-methods-sources.md`. The note still says it was written without opened sources.

## How dates are treated

- Commercial calendar sites do not confirm a date. They only add a note.
- Official sources that disagree confirm nothing. Holi 2027 stays unconfirmed because the Government of India's holiday list says March 23 and the panchang says March 22.
- Moon-sighted dates are never shown as confirmed.
- On October 31, 2026, Korean and Lebanese dates that rested only on commercial holiday sites (publicholidays.co.kr, calendarlabs.com) were changed to unconfirmed. Two dates from Gary's computer still rest on such sources: the Hmong American Day Festival 2026 (a Scouting outreach calendar) and Onam 2026 (drikpanchang.com).
- The `.ics` file carries confirmed dates only.

## Blocked sources

Hmong and the methods note could not open these: Star Tribune, Christian Century, the state charter school directory, Carleton's Religions in Minnesota, mn.gov pages (State Demographic Center, Department of Veterans Affairs), the University of Minnesota Conservancy, state courts, the Senate roster, Department of Education pages, and ICPSR.

- Ecuadorian could not open: Sahan Journal (too many requests), Minnesota Reformer, Yelp, Explore Minnesota, Toast, the University of Minnesota autism monitoring site and a Stanford dissertation record.

- Colombian could not open: Sahan Journal (too many requests), Explore Minnesota, Mayo Clinic, KARE 11, a Colombian consulate flyer, Minnesota Women's Press, MinnPost search, and the La Colonia and Los Andes websites.

- Arabic-speaking could not open: mn.gov, Star Tribune, Minnesota Reformer, Axios, Explore Minnesota and PubMed; Sahan Journal, the Spokesman-Recorder and MinnPost refused requests for long stretches, so Sahan's Sudan, Lebanon and Syria stories and the Spokesman's Sudan story were not read.

- Lebanese could not open: Sahan Journal and the West St. Paul Reader (too many requests), MDH Minnesota Student Survey pages, Macalester's thesis archive, the Texas A&M catalog, USCIS, federalregister.gov and Minnesota Lawyer.

- Ukrainian could not open: the DHS Ukrainians in Minnesota page (mn.gov), Sahan Journal and MinnPost (too many requests), KARE 11, Baptist Press, Festival of Nations and the Minnesota Orchestra.

- Russian-speaking could not open: mn.gov pages (State Demographic Center, state aging-resources directory), MDH refugee data downloads, rajmn.org, sunflowerdaycare.us, the Migration Policy Institute state language page, Minnesota Reformer and the Wilder 2000 survey PDF.

- Bosnian could not open: Mayo Clinic pages, mn.gov DHS pages (one PDF opened), conservancy.umn.edu, the OSA Archivum catalog of American Refugee Committee Balkan records, press.un.org, jurist.org, MinnPost and some Sahan Journal pages (too many requests).

- Burmese could not open: KARE 11, CAIR, Carleton College religion exhibits, mn.gov board pages, Minnesota Lawyer, AsAm News, Minnesota Digital Library, Ucanews, Frontier Myanmar, Lost Footsteps, Shan Herald, Desiring God, and some Sahan Journal pages (too many requests).

- Thai could not open: Explore Minnesota, legacy.mn.gov, the Council on Asian Pacific Minnesotans board page, Star Tribune, KARE 11, Sahan Journal (too many requests) and the archived copy of the former Compass Thai page.

- Khmer could not open: Carleton's Religions in Minnesota exhibit, KARE 11, the PubMed Central and MDPI copies of a 2024 Cambodian refugee mental health study, the state's aging and disability resource directory, Explore Minnesota, LegiScan, and a Sahan Journal story on Cambodian food trucks (too many requests).

- Lao could not open: most Sahan Journal articles (too many requests), legacy.mn.gov, the UMN Conservancy, GuideStar, Census QuickFacts, mn.gov resource pages, Bush Foundation and pluralism.org.

- Chinese could not open: legacy.mn.gov, Minnesota Lawyer, KARE 11, Explore Minnesota, Minnesota Reformer, and mn.gov pages for aging resources and the Council on Asian Pacific Minnesotans board.

- Japanese could not open: Consulate-General of Japan in Chicago, Minneapolis Institute of Art collection pages, the Legacy grants site, Minnesota courts, Minnesota Reformer, Densho Encyclopedia, Explore Minnesota, Solstice magazine and Como Zoo's Japanese garden page.

- Filipino could not open: Star Tribune, MinnPost, KARE 11, Axios, Bring Me The News, Minnesota Council on Asian Pacific Minnesotans pages, the MDH resource directory and the Festival of Nations site.

- Korean could not open: JangmiArts, the Korean Cultural Association, Adoption Literacy, Minnesota Reformer, Axios, the UMN Conservancy, one Korean Quarterly article, and most Korean church sites. Sahan Journal sometimes refuses requests for a while (too many requests).

## Could not be established so far

- **Ecuadorian:** 78 opened sources. Web search ran out after about 50 searches (the shared limit), and the rest was done by opening pages directly. Not established: a Minnesota count of Kichwa (Quichua) or other Indigenous-language speakers, Ecuadorian occupations, wealth or disability data beyond one Compass rate, any Ecuadorian-owned law, tax, insurance or media business, and any Ecuadorian evangelical congregation. 8 of 16 businesses could not be confirmed open, including Chimborazo's Minneapolis restaurant after a June 2026 fire.
- **Colombian:** 84 opened sources; web search worked throughout. Only 10 businesses (5 open, 5 could not be confirmed open) for a community of about 10,000. Not established: any 2025 or 2026 Minnesota Colombian festival or Independence Day event, any active Colombian association, congregation, chamber or media outlet, and Colombian-specific disability, health or religion data beyond survey rates. Colombian holiday dates come from a commercial calendar site, so they are shown as unconfirmed until checked against an official source.
- **Arabic-speaking:** 92 opened sources; web search worked throughout. Not established: Minnesota income, health or disability data for any Arab group except Lebanese, any Minnesota organization focused on disability among Arabic-speaking families, arrival histories for Egyptian, Sudanese, Syrian or Yemeni Minnesotans, and any non-food business (chamber, law or accounting firm, clinic). 13 of 22 businesses could not be confirmed open; nearly all businesses found are food businesses.
- **Lebanese:** 69 opened sources; web search worked throughout. Not established: any Minnesota mosque or Druze group identified as Lebanese or any religious breakdown, Lebanese or Middle Eastern and North African disability, school or health data beyond one Compass disability rate, any 2026 Minnesota coverage of the community's reaction to the new war, and who will lead St. Maron after its pastor was named archbishop of Damascus (Aug. 28, 2026). 9 of 20 businesses could not be confirmed open; 3 have closed.
- **Ukrainian:** 82 opened sources; web search worked throughout. Only 7 businesses were found (5 open, 2 could not be confirmed open); no Ukrainian business district, chamber or directory turned up. Not established: how many people who arrived from Ukraine since 2022 still live in Minnesota and what parole or protected status they now hold, a breakdown of Ukrainian workers by industry, disability-service data, and which Christmas date each Orthodox parish now keeps. The Ukrainian Festival is postponed in 2026 and announced for Sept. 17-18, 2027.
- **Russian-speaking:** 83 opened sources; web search worked throughout. Not established: current income, poverty and home-ownership figures for Russian speakers (the newest found are from 2018), any Minnesota disability data or Russian-speaking disability organization, a full list of Slavic evangelical churches, and any dated public Novy God (New Year), Orthodox Christmas or Victory Day event. Census counts (about 13,900 to 15,500 Russian speakers) and community estimates (45,000 to 60,000) remain far apart. No clinic, law office, accounting firm or insurance agency serving Russian speakers could be confirmed; 6 of 14 businesses could not be confirmed open.
- **Bosnian:** 63 opened sources; web search worked throughout, but Minnesota sources are scarce. Only 5 businesses were found (2 open, 2 could not be confirmed open, 1 closed) and none in the Twin Cities could be confirmed. Not established: a reliable count (Compass has no Bosnian profile; the 2024 Census estimate is 2,114 people born in Bosnia, give or take 964), any income, education or disability data for Bosnian Minnesotans, and anything current on the Minneapolis Bosniak mosque's leaders or activities.
- **Burmese (Bamar and other non-Karen groups from Burma):** 54 opened sources; web search worked throughout but Minnesota material is scarce, so this profile is thinner than most. Only 5 businesses or institutions were found (2 open, 3 could not be confirmed open) and no Bamar-owned business. Not established: any count of Bamar people or Bamar-only income, schooling or housing figures (every census number is the Burmese umbrella, which is mostly Karen), any Chin, Kachin, Rohingya or Shan congregation, organization or count in Minnesota, and any dated 2025 or 2026 event at the Chisago City temple.
- **Thai:** 125 opened sources; web search worked throughout. Not established: any Minnesota income, poverty, education or disability figures for Thai Minnesotans (Minnesota Compass has removed its Thai profile and the state's 2026 report folds Thai into Other Asian), an organizer's own page for the 2026 Minnesota Songkran Festival (its May 16-17 dates come only from a Scouting outreach calendar, so they are shown as unconfirmed), and why women are about two thirds of Thai-alone Minnesotans in the 2020 Census. 29 of 54 businesses could not be confirmed open.
- **Khmer (Cambodian):** 74 opened sources; web search worked throughout. The business list is thin (6: 3 open, 3 could not be confirmed open) because few Cambodian-owned businesses are named in public sources; no Cambodian grocery, professional firm or chamber was found. Not established: 2026 dates at Watt Munisotaram (its events page was empty), any Minnesota account of Pchum Ben or April 17 remembrance, any Minnesota disability study specific to Cambodians, and any Cambodian elected official.
- **Lao:** 100 opened sources after a second pass. Still thin on businesses (12: 5 open, 6 could not be confirmed open, 1 closed); no Lao-owned grocery, professional firm or Lao-language media outlet, and no Lao restaurant in Rochester or Worthington was found. Not established: any 2026 Lao New Year event in Minnesota or how Minnesota temples marked the Buddhist holy days (no temple website, calendar or recent news found), any Minnesota study of disability among Lao Minnesotans, and any ethnic Lao elected official. Lao National Day was dropped because no Minnesota observance was found.
- **Chinese:** 87 opened sources; web search worked throughout. Not established: any Minnesota disability data or services for Chinese families or for adoptees from China, counts of Mandarin, Cantonese or other Chinese-language speakers, religious affiliation, any Chinese Buddhist temple, and any Chinese-owned law, accounting or insurance firm or current Chinese-language media outlet. 13 of 29 businesses could not be confirmed open. The Mid-Autumn Moon Festival at Phalen Park was not held in 2026.
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
