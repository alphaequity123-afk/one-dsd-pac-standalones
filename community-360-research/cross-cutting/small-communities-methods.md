# Studying immigrant, refugee and small communities in Minnesota: a methods note

**Internal note for staff researchers. Checked October 30, 2026.**

**Scope.** This note covers how researchers study immigrant, refugee and other small communities within a state, and how they study change across generations. Minnesota examples come first wherever an opened source supported them. It does not cover the 11 Tribal Nations or American Indian communities. That work belongs with the Office of Indian Affairs and the DHS Tribal offices.

Calculations marked "worked out for this note" are simple arithmetic on published figures. Sentences marked "our reading" are judgment, not a sourced finding.

## The short version

1. Never report a small-group number without its margin of error, its years, and how the group was defined.
2. Two honest sources can give very different counts for one community, because they measure different things.
3. Use at least two kinds of evidence: numbers to show scale, and qualitative work done with the community to show meaning.
4. Check whether a finding could point to a real person or put a whole community at risk before you share it.
5. A group finding is a reason to ask a better question. It never tells you about the person in front of you.

## 1. Why state estimates for small groups are unstable

### Margins of error

The American Community Survey (ACS) is a sample survey, so each estimate carries a margin of error, the range of plausible values around the estimate caused by sampling. The smaller the group, the wider that range tends to be compared with the estimate.

Minnesota Compass shows this clearly. Its [Somali profile](https://www.mncompass.org/topics/demographics/cultural-communities/somali) gives two totals:

| Figure | Estimate | Margin of error | Range (worked out for this note) | Relative error (worked out for this note) |
|---|---|---|---|---|
| 2024 total | 111,722 | ±20,401 | 91,321 to 132,123 | about 11% |
| 2020-2024 pooled | 85,533 | ±7,711 | 77,822 to 93,244 | about 5.5% |

Relative error here is the coefficient of variation, or CV: the standard error divided by the estimate. The Census Bureau's [handbook chapter](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf) shows how to get the standard error by dividing the margin of error by 1.645, and how to calculate the CV from it.

The gap between those two totals is not only sampling noise. Compass explains that in 2024 the Census Bureau began collecting data in ways that report cultural ancestry more accurately for Black and White respondents. Compass therefore treats the 2024 total as the best measure of community size, and uses the pooled figures for everything else because they rest on a larger sample.

Errors grow fast when you slice a small group further. The [Burmese profile](https://www.mncompass.org/topics/demographics/cultural-communities/burmese) gives a total of 19,372 (±3,438) and a 2020-2024 poverty rate of 22.2% (±7.6), which means a plausible range of about 15% to 30%. Compass [reported 36%](https://www.mncompass.org/data-insights/articles/importance-data-disaggregation-minnesotas-asian-communities) for the same group in a May 2024 article. Some of that difference may be real change and some may be error. The published figures do not let us separate the two.

**Check the confidence level before comparing margins.** [Compass](https://mncompass.org/demographics/cultural-communities/methodology) reports at 90% confidence. The State Demographic Center's [2026 chartbook](https://mn.gov/admin/assets/The%20Economic%20Status%20of%20Minnesotans%202026_tcm36-717691.pdf) often shows 95%. A 95% range is wider, so the two are not directly comparable.

### One-year versus five-year data

The [Census Bureau's guidance](https://www.census.gov/programs-surveys/acs/guidance/estimates.html) describes the trade-off this way. One-year estimates are the most current and the least reliable of the two, and cover areas of 65,000 people or more. Five-year estimates are the most reliable and the least current, cover all areas, and suit very small populations.

Five-year data pool responses across years, so they describe a period, not a moment. That matters for a community changing quickly. Our reading: do not compare overlapping five-year periods as if they were separate years.

### Suppression and minimum sizes

Suppression means holding back a number because it is too unreliable or could identify someone. Each publisher sets its own floor, which is one reason a group can appear in one source and vanish from another.

| Source | Rule |
|---|---|
| [ACS Selected Population Tables, 2017-2021](https://www.census.gov/programs-surveys/acs/data/race-aian/2021.html) | Group needs at least 7,000 people nationally, and the area needs at least 50 unweighted sample persons from the group. Covers 399 groups. |
| [2020 Census Detailed DHC-A](https://census.gov/newsroom/blogs/random-samplings/2023/09/what-you-should-know-detailed-dhc-a.html) | No minimum at nation and state level. At county, place and tract level, at least 22 people. Small statistical noise is added to protect privacy. |
| [Minnesota Compass](https://mncompass.org/demographics/cultural-communities/methodology) | At least 175 unweighted records for a community profile. |
| [State Demographic Center chartbook](https://mn.gov/admin/assets/The%20Economic%20Status%20of%20Minnesotans%202026_tcm36-717691.pdf) | At least 300 survey respondents in the pooled 2019-2023 data, with further suppression for narrower indicators and no geography below the state. |
| [ECLDS and SLEDS](https://dcyf.mn.gov/sites/default/files/2026-04/eclds-damp-data-guide.pdf) (Minnesota's linked education systems) | Cell sizes under 10 are suppressed in public reporting. |

"Unweighted" means the actual number of people who answered, before survey weights are applied. A weighted estimate of several thousand may rest on a few hundred real responses.

### Four different questions, four different populations

The [2024 ACS questionnaire](https://www2.census.gov/programs-surveys/acs/methodology/questionnaires/2024/quest24.pdf) offers several routes to a community, and none of them is complete.

| Question | What it captures | How it can mislead in Minnesota |
|---|---|---|
| Race | Self-identified race, with write-in details | Write-in design and coding [changed beginning in 2020](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2021-03.html), so compare with earlier years cautiously. |
| Ancestry or ethnic origin | An open-ended answer | Starting with 2024 data, detailed groups appear in both race and ancestry tables, and the [overlapping estimates can differ](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2025-01.html). |
| Birthplace | Country of birth | Misses the U.S.-born. About [31.5% of Hmong](https://www.mncompass.org/topics/demographics/cultural-communities/hmong) and [52.2% of Somali](https://www.mncompass.org/topics/demographics/cultural-communities/somali) Minnesotans are foreign-born in Compass's profiles. Country is also not the same as people: the State Demographer's [chart](https://mn.gov/capm/assets/SusanBrower_StateOfAsianPacificMinnesotans_June2026_tcm1051-759113.pdf) labels one line "Laos (includes Hmong)." |
| Language at home | Language spoken by people aged 5 and over, and English ability | In the [detailed table B16001](https://census.gov/content/dam/Census/programs-surveys/acs/tech-doc/user-notes/2016_Language_User_Note.pdf), Hmong has its own row, but Somali is grouped with Amharic and others, and Burmese and Karen fall under "Other languages of Asia." The [Somali grouping is still in 2024 data](https://api.census.gov/data/2024/acs/acs5/variables/B16001_111EA.html). The same note sends users to the public microdata for individual languages not shown in the tables. |

Other coding traps exist. Compass notes that ACS data [recode Karen respondents as Burmese](https://www.mncompass.org/data-insights/articles/importance-data-disaggregation-minnesotas-asian-communities), with nothing to show the original answer. Its methods page adds that recoding can inflate the receiving group, and that some people may not report their community at all, including from fear of persecution.

### "Alone" and "alone or in combination"

The Census Bureau [describes these](https://census.gov/library/stories/2023/09/2020-census-dhc-a-race-overview.html) as a floor and a ceiling. "Alone" counts people who gave one response. "Alone or in any combination" adds people who gave more than one. These terms [apply to the race question only](https://census.gov/newsroom/blogs/random-samplings/2023/09/what-you-should-know-detailed-dhc-a.html).

The difference can be large. In the State Demographer's [June 2026 slides](https://mn.gov/capm/assets/SusanBrower_StateOfAsianPacificMinnesotans_June2026_tcm1051-759113.pdf), Minnesota has 344,621 people who are Asian alone and 71,484 who are Asian in combination, for 416,105 in all. Say which one you used. Our reading: the combined count may matter most for younger generations, because multiracial children are lost in an "alone" count.

### Which tables to use

- **[Detailed tables (B)](https://www.census.gov/programs-surveys/acs/data/data-tables/table-ids-explained.html)** hold the most detail. **Collapsed tables (C)** group some lines together.
- **Selected Population Profile (S0201)** gives broad statistics for subgroups by race, ethnicity, ancestry and place of birth.
- **[Selected Population Tables](https://www.census.gov/programs-surveys/acs/data/race-aian.html)** give the most detail for small groups. A [Census training deck](https://www.census.gov/content/dam/Census/programs-surveys/acs/guidance/training-presentations/ACS_and_%202020_Census_Race_and_Ethnicity_Data.pdf) says they typically come out about every five years. The latest listed is 2017-2021, with added tables in January 2024 to fix over-suppression.
- **2020 Census Detailed DHC-A** gives counts and age by sex, not income or education. The same deck warns against casual comparison with ACS ancestry data, because the methods differ.
- **Microdata** let you build your own groups. [IPUMS USA](https://www.ipums.org/) provides census and ACS microdata back to 1850, and both Minnesota sources below rely on this kind of data.

### What Minnesota Compass and the State Demographic Center publish

**[Minnesota Compass](https://www.mncompass.org/topics/demographics/cultural-communities)**, a Wilder Research project, publishes profiles for 27 cultural communities. Its [methods page](https://mncompass.org/demographics/cultural-communities/methodology) counts a person in a community if any listed rule applies, so one person can be in several. Foreign-born people generally count in their birth country's profile unless their race or ancestry answers say otherwise. Minor children living with parents take on the parents' communities. Compass warns that these are approximations of how communities define themselves.

**The [State Demographic Center's 2026 chartbook](https://mn.gov/admin/assets/The%20Economic%20Status%20of%20Minnesotans%202026_tcm36-717691.pdf)** presents 18 cultural groups, including Hmong, Karen, Lao, Somali, Ethiopian, Liberian, Mexican and Russian. It combines race, birthplace, ancestry and parents' characteristics from pooled 2019-2023 ACS data. Its Hmong and Somali groups include U.S.-born descendants who identify with that heritage.

**The two publishers do not define groups identically.** Hmong alone shows why that matters: 102,491 (±5,546) in [Compass's profile](https://www.mncompass.org/topics/demographics/cultural-communities/hmong) and 111,741 from 2024 ACS data in the [State Demographer's slides](https://mn.gov/capm/assets/SusanBrower_StateOfAsianPacificMinnesotans_June2026_tcm1051-759113.pdf). Report the source and the definition every time.

### A change coming

A [Census Bureau notice](https://public-inspection.federalregister.gov/2025-23329.pdf) says proposed content for the 2027 ACS includes an updated race and ethnicity question following the federal 2024 standard. Expect another break in trend lines if it goes ahead as proposed.

## 2. Reaching people that surveys miss

**Community-partnered and community-based participatory research.** In this approach, community members help shape the questions, the methods and the use of findings. Minnesota has strong models:

- **SoLaHmo.** This [Somali, Latino and Hmong partnership](https://cuhcc.umn.edu/research/solahmo), now at the Community-University Health Care Center, treats community researchers as co-investigators. A [2010 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC5484585) describes the training of community scholars and faculty, and studies designed with them.
- **The Minnesota autism study.** A [2014 Minnesota Department of Health report](https://www.leg.mn.gov/docs/2014/mandated/140404.pdf), by the University of Minnesota School of Public Health, SoLaHmo and the Confederation of Somali Community in Minnesota, first interviewed 33 key informants. It then used what it learned to design interviews with 70 parents: 38 Somali, 15 Hmong and 17 Latino. The same report notes that participatory work can risk trading away rigor, so both must be protected.

**Purposive sampling built on trust.** Purposive sampling means choosing participants on purpose rather than at random. [Spring and colleagues (2003)](https://experts.umn.edu/en/publications/sampling-in-difficult-to-access-refugee-and-immigrant-communities/) studied Somali and Oromo refugees in Minneapolis and St. Paul from 1999 to 2002. They had no complete list to draw from, so they used purposive sampling with deliberate trust-building, then compared their sample with the underlying population. They report no apparent differences. They also found trust was crucial for recovering when outside events threatened the work.

**Community surveys.** Wilder Research's [Speaking for Ourselves](https://www.wilder.org/wilder_research/speaking-for-ourselves-a-study-with-immigrant-and-refugee-communities-in-the-twin-cities-data-book/) interviewed 459 immigrants and adult children of immigrants from Hmong, Karen, Latino, Liberian and Somali communities in Hennepin and Ramsey counties, with an advisory group's guidance.

**Respondent-driven sampling (RDS).** Staff pick a few starting participants, called seeds, who recruit peers using coupons. Those recruits then recruit others, and analysts apply weights to offset the non-random recruitment ([Rudolph and colleagues, 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3674117)). It can yield large samples, but [Gile and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC4877136) warn that its assumptions are hard to check and its estimates vary widely. In their data, people's reports of their network size were only low to moderately reliable. Treat RDS results as informative, not as a substitute for a probability sample.

**Snowball sampling.** Participants refer others, with no weighting model. The risk is reaching only one network. A study of Afghan and Kurdish refugees found that [multiple entry points](https://blogs.biomedcentral.com/bmcseriesblog/?p=41) were crucial for reducing bias. Our reading: in a community with clan, faith, age or political divisions, ask who a given entry point cannot reach.

**Venue-based or location sampling.** Researchers sample people at places they gather during set times. A [seven-country European survey](https://research-portal.najah.edu/migrant/35331/) with no sampling list found that such methods gave meaningful results on core demographics, though some estimates differed from census figures. Our reading: venues select for people who attend them, so a mosque, a church or a market each misses others.

**List frames and surnames.** A list frame is a list used to draw a sample, such as a member roll or a program record. Any list only covers people who are on it. Surname lists try to build a frame from names, and they miss people. [Davern and colleagues (2007)](https://experts.umn.edu/en/publications/are-surname-telephone-oversamples-an-efficient-way-to-better-unde/), using surveys that included Minnesota, reported that the Hmong surname sample captured only 38% of Hmong respondents (this share is called sensitivity), with 34% for Asian lists and 46% to 63% for Hispanic lists. The extra interviews added very little statistical power, so the authors judged these oversamples inefficient. Our reading: also expect errors from marriage and name changes, from names shared across groups, and from people adopting other naming patterns. Check any surname method against self-reported identity.

## 3. Refugee arrival data and secondary migration

**Minnesota first.** The [MDH Refugee Health Program](https://www.health.state.mn.us/communities/rih/stats/index.html) publishes arrivals by region, county and origin, screening data, and yearly reports. "Primary" means people who first resettled in Minnesota. "Secondary" means people who first resettled elsewhere and then moved here.

The [2024 report](https://www.web.health.state.mn.us/communities/rih/stats/24rhrpt.pdf) counts 4,602 primary arrivals, of whom 3,358 (73%) came on a refugee visa. The largest origins were Somalia (1,490), Ukraine (739), Afghanistan (603) and Ethiopia (272). It was notified of 195 secondary arrivals, 155 of them from Somalia, with Stearns County reporting the most (67).

**Limits to state plainly:**

- **Secondary migration is undercounted by design.** MDH says it has [no systematic way](https://www.health.state.mn.us/communities/rih/stats/index.html) to identify all secondary refugees, so its counts reflect only notifications. It received none in 2021. Do not read a change in these counts as a change in migration without other evidence.
- **"Refugee" is a broad label here.** The report groups refugees, asylees, parolees, Cuban and Haitian entrants, special immigrant visa holders and others. It also says it was not notified of every Ukrainian parolee or Cuban and Haitian entrant.
- **Arrival is a first address, not a lasting one.** People may leave, or may never be located. Arrival counts are also not population counts.
- **Origin is not always identity.** The [federal arrivals report](https://www.rpc.state.gov/admissions-and-arrivals/) lists state arrivals by the primary applicant's nationality, and notes that past monthly figures can change on reconciliation. Our reading: nationality will hide ethnic groups, such as Karen people from Burma, and family members with other backgrounds.
- **Recent federal numbers describe a very different program.** The [Congressional Research Service](https://www.everycrsreport.com/reports/IF13277.html) reports that refugee entry was suspended in January 2025 with exceptions, the fiscal 2026 ceiling was 17,500, and 7,730 people were admitted through June 30, 2026, nearly all South African. Low recent arrivals say little about the needs of established communities.

## 4. Linked administrative data

Linked data join records for the same person across agencies. They offer whole populations rather than samples, but only for people who touch those systems.

Minnesota examples:

- **[Minn-LInK](https://ijpds.org/index.php/ijpds/article/view/3721)**, at the University of Minnesota, links more than 20 years of statewide records, including education, child protection, children's mental health, public assistance and justice data, through partnerships with state agencies.
- **[SLEDS](https://sleds.mn.gov/)** matches students from pre-kindergarten through college and into work, and is managed by the state's higher education, education and employment agencies. Its reports cover race and ethnicity and, in at least one report, English learner status.
- **[ECLDS](https://dcyf.mn.gov/sites/default/files/2026-04/eclds-damp-data-guide.pdf)** is the early childhood companion. It reports home language types with 10 or more children, taken from the Minnesota Language Survey.

**Linkage error is not evenly shared.** Name matching misses more people from some groups. A [study of U.S. mortality records](https://pmc.ncbi.nlm.nih.gov/articles/PMC4598042) found lower linkage quality for Hispanic and foreign-born adults; among people who had died, 32.5% of foreign-born Hispanic adults fell in the most certain match class, against 62.6% of U.S.-born non-Hispanic White adults. A [2026 study of North Carolina voter records](https://ijpds.org/index.php/ijpds/article/view/3618) found that name-based linkage missed more Black, Asian and Hispanic people than White people. Our reading: names that are transliterated, reordered or reported differently across agencies may be especially exposed, so ask for match rates by group before trusting a linked result.

Our reading on other limits: these systems hold what programs need, so they rarely hold ethnicity or generation in the detail you want. People who avoid or are shut out of services are missing, and their absence can look like low need.

## 5. School language data

School data are often the best local signal for small language communities, but they measure something specific.

- **The instrument.** Every enrolling student receives the [Minnesota Language Survey](https://www.winonaschools.org/uploaded/Documents/Learning_Teaching/MN_Language_Survey_Aug_2017_fillable_-_English.pdf). It asks what the student first learned, speaks, understands, and uses in regular interaction. One [district procedure](https://www.district287.org/our-district/policies-procedures/board/~board/600-education-programs/post/6001-procedure-identification-of-potential-english-learners-enrollment) calls these MDE's required four questions, says families self-report and may decline, and says the home language is reported to MDE.
- **Legal definitions.** [Minnesota Statutes 124D.59](https://www.revisor.mn.gov/statutes/cite/124D.59) defines an English learner using both the parent's language declaration and an assessment of English skills. Primary language means the one the child normally uses or the one spoken at home.
- **State reporting.** [Minnesota Statutes 120B.35](https://www.revisor.mn.gov/statutes/cite/120B.35) requires analysis by more detailed race and ethnic groups chosen by population size, by the Karen community, and by home language, unless numbers are too small or would reveal a student. The [2021-22 MDE report](https://www.lrl.mn.gov/docs/2023/Other/231750.pdf) shows Spanish, Somali and Hmong as the top languages other than English.

**How to read it:**

- Home language is not ethnicity. English learner status is not home language. These are three different groups.
- An MDE "immigrant student" is [narrowly defined](https://www.lrl.mn.gov/docs/2023/Other/231750.pdf): born outside the U.S. and in U.S. schools for no more than three full academic years. It does not mean every child of immigrants.
- A federally supported [regional lab](https://ies.ed.gov/use-work/resource-library/resource/other-resource/home-language-survey-data-quality-self-assessment) warns that home language surveys can be inaccurate and can contribute to misidentifying English learners.
- Our reading: families can answer strategically or out of fear, and a child's language can shift within a family. Later generations who speak English at home disappear from these counts while remaining part of the community.

## 6. Qualitative work, life histories and archives

Interviews, focus groups, ethnography (long-term observation in a community) and life histories (a person's account across their life) answer questions numbers cannot, such as what a term means, why people avoid a service, or how a family changed. They do not estimate how common something is.

**Minnesota and University of Minnesota examples:**

- **Ethnography.** Cawo Abdi's *Elusive Jannah* ([University of Minnesota Press, 2015](https://lebanesestudies.ojs.chass.ncsu.edu/index.php/mashriq/article/download/89/573)) rests on ethnographic research in three Somali diaspora locations, which helps show what is specific to one place.
- **Small interview studies.** [Dini and Solheim (2025)](https://experts.umn.edu/en/publications/making-sense-of-complexity-in-refugee-family-systems-second-gener/) interviewed six second-generation adults, three Hmong and three Somali, about their refugee parents. That depth is valuable, but the sample was chosen for parents' migration trauma and cannot speak for a generation.
- **Parent interviews on disability.** See the [MDH autism report](https://www.leg.mn.gov/docs/2014/mandated/140404.pdf) described above.

**Collections to use:**

| Collection | What it holds |
|---|---|
| [Minnesota Immigrant Oral Histories (MNHS)](https://archives.internetscout.org/r43246/minnesota_immigrant_oral_histories) | Over 360 interviews conducted between 1967 and 2012. A [library guide](https://libraryguides.goshen.edu/c.php?g=1344118) reported it temporarily closed as of September 2023, so check current access. |
| [Hmong collections (MNHS)](https://libguides.mnhs.org/hmong/primary) | The Hmong Oral History Project has 9 interviews. The Hmong Women's Action Team project has 18 interviews with women from three generations of six families, mostly in Hmong and then translated. It is a rare ready-made look at change across generations. |
| [Somali collections](https://libguides.mnhs.org/somali) | The Somali Skyline Tower project (2004), and the [Macalester Somali Oral History Project](https://www.legacy.mn.gov/node/37500) with the Somali Museum of Minnesota, with 57 interviews reported. |
| [Immigration History Research Center Archives](https://www.lib.umn.edu/collections/special/ihrca) (University of Minnesota) | Papers and records, strongest on first and second generations from central, eastern and southern Europe and the eastern Mediterranean, with some late 20th and 21st century material. Many serials are in other languages. |
| [Immigrant Stories](https://cla.umn.edu/ihrc/immigrant-stories) (University of Minnesota) | Over 375 short digital stories from more than 50 communities. Not currently collecting. |
| [Minnesota Immigrants collection](https://mndigital.org/node/417) | Oral histories gathered from organizations across the state, combined with new stories. |

Our reading on archives: they show who was asked, by whom, in what language and for what purpose. People who volunteer stories differ from those who do not. Check permissions before quoting, and remember that a named speaker in a small community can be recognized.

## 7. Translation, interpreters and validity across languages

Validity means a question really measures what you intend. A translated question can read well and still measure something else.

**University of Minnesota evidence.** [Westermeyer (1986)](https://experts.umn.edu/en/publications/two-self-rating-scales-for-depression-in-hmong-refugees-assessmen/) translated two depression scales into Hmong and tested them with Hmong refugees. Among patients, only one scale tracked clinician ratings and treatment, against the author's expectation, and some items did not separate depressed from non-depressed people at all. A faithful translation did not guarantee a working scale.

**Back translation is not enough.** Back translation means translating the text back into English to compare. [Walde and Völlm (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10309006/) note that it has limited ability to find flaws or the need for cultural adaptation. The [Washington Group](https://www.washingtongroup-disability.com/wg-blog/post/translating-the-washington-group-short-set-questions-66/) gives a telling case: a Marathi question about walking around the house returned identical English, yet respondents took it to mean walking around the outside of the building.

**Better practice:**

- **[TRAPD](https://pmc.ncbi.nlm.nih.gov/articles/PMC10309006/).** This stands for Translation, Review, Adjudication, Pretest and Documentation. Several translators work independently, a review group discusses their versions, an adjudicator settles disputes, and the draft is tested with the target population.
- **Cognitive interviews.** Ask people to explain what a question means to them and how they chose an answer.
- **Community involvement.** A [Hmong immunization survey study](https://geriatrics-references.stanford.edu/publications/hmong-american/translation-health-surveys-using-mixed-methods) found that community involvement strengthened translation quality and the survey's reliability and validity.

**Interpreters shape data.** [Temple and Edwards (2002)](https://sites.ualberta.ca/~iiqm/backissues/1_2Final/html/temple.html) argue against treating an interpreter as a neutral channel, since word choices and the interpreter's own background affect what researchers see. They suggest interviewing interpreters as key informants. [Squires (2008)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2697452) advises choosing and evaluating qualified bilingual staff, planning their role in advance, being cautious with family members as interpreters, reporting how they were used, and listing translation as a limitation.

**Oral languages and small communities.** Our reading: a written translation may not help people who read another language or do not read at all, so plan for spoken formats. In a small community, the interpreter may know the participant, so discuss confidentiality and offer a choice.

## 8. Measuring generations

**The usual categories:**

- **First generation:** born abroad, came as an adult.
- **1.5 generation:** born abroad, came as a child. [Rumbaut](https://www.socsci.uci.edu/newsevents/news/2012/2012-03-22-gen-1-5-where-an-immigrant-generation-fits-in.php) splits this by arrival age: 1.75 (age 5 or younger), 1.5 (ages 6 to 12) and 1.25 (ages 13 to 17). Not all scholars accept this scale.
- **Second generation:** born in the U.S. with an immigrant parent. Whether one or two parents, and which parent, varies by study.
- **Third generation and later:** born in the U.S. to U.S.-born parents.

**The data problem.** The [2024 ACS questionnaire](https://www2.census.gov/programs-surveys/acs/methodology/questionnaires/2024/quest24.pdf) asks birthplace but not parents' birthplace. The [National Academies](https://www.nationalacademies.org/read/23550/chapter/15) note that the Current Population Survey has asked both parents' birth countries since 1994, but its sample is too small for many groups and places. So:

- In the ACS, researchers can link children to parents only when they live together. Minnesota's two main sources use this kind of linking for children ([Compass](https://mncompass.org/demographics/cultural-communities/methodology), [State Demographic Center](https://mn.gov/admin/assets/The%20Economic%20Status%20of%20Minnesotans%202026_tcm36-717691.pdf)).
- Our reading: adult children living apart can be found only if they report ancestry or race, and a mixed-heritage third generation may not be found at all. Those who stop reporting a heritage vanish from the count, which can make a group look more or less successful than it is.
- For a Minnesota community, the "second generation" often cannot be measured directly from public data. If it matters to your question, you will likely need a purpose-built survey.

**Do not confuse generation with age or time.** A second-generation teenager and a first-generation elder differ in age, historical period and generation all at once. Group history also matters: [fewer than half of Hmong Minnesotans were born abroad, while other Asian groups are more likely to be foreign-born](https://mn.gov/capm/assets/SusanBrower_StateOfAsianPacificMinnesotans_June2026_tcm1051-759113.pdf).

**Segmented assimilation.** This theory argues that the children of immigrants do not follow one path upward. [Portes and colleagues (2009)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3634592) describe outcomes shaped by parents' education and resources, how government and society receive a group, and family structure, along with barriers such as racism. The paths run from upward mobility to stagnation to downward mobility. Their [2005 paper](https://collaborate.princeton.edu/en/publications/segmented-assimilation-on-the-ground-the-new-second-generation-in/) finds most youth moving ahead, with a significant minority left behind. It rests mainly on the two metro areas of one study and is written by the theory's originators, so test it before applying it here.

**Background studies, neither from Minnesota:**

- **[Children of Immigrants Longitudinal Study (CILS)](https://www.russellsage.org/node/10103).** It followed 5,262 eighth and ninth graders from 77 nationalities in San Diego and South Florida, starting in 1992, with a final wave in 2001 to 2003. Sources give the third wave as 3,613 or [3,564](https://pmc.ncbi.nlm.nih.gov/articles/PMC3634592). Those lost over time were more often disadvantaged, a warning for any long-term study.
- **[Immigrant Second Generation in Metropolitan New York](https://revista.drclas.harvard.edu/a-review-of-inheriting-the-city-the-children-of-immigrants-come-of-age).** It surveyed 3,415 adults aged 18 to 32 from Chinese, Dominican, South American, Russian Jewish and West Indian backgrounds, plus native-born comparison groups, with in-depth interviews and fieldwork. The authors stress that the second generation can draw on both worlds.

Our reading: these studies drew on large, mixed-origin metro populations. Their findings may not carry over to groups shaped by forced migration and resettlement in Minnesota.

**Critiques of acculturation.** Acculturation means cultural change after contact between groups. [Hunt and colleagues (2004)](https://ideas.repec.org/a/eee/socmed/v59y2004i5p973-986.html) reviewed U.S. health research on Hispanics and concluded that using acculturation as a variable may rest more on ethnic stereotyping than on real cultural differences. [Schwartz and colleagues (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3700543/) argue that it has several dimensions (practices, values, identities) that move at different rates, that it varies by migrant type and age at arrival, and that the receiving society limits the options open to migrants.

Practical advice from our reading: do not use years in the U.S. or English ability as a stand-in for culture. When a health or service gap appears, look first at discrimination, income, access and policy before explaining it through culture.

## 9. Measuring disability across cultures

**The ACS six questions.** The [ACS](https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html) asks about hearing, vision, cognition, walking or climbing stairs, self-care and independent living, and counts anyone reporting at least one. The [Washington Group Short Set](https://www.washingtongroup-disability.com/fileadmin/uploads/wg/Washington_Group_Questionnaire__1_-_WG_Short_Set_on_Functioning__October_2022_.pdf) asks about seeing, hearing, walking or climbing steps, remembering or concentrating, self-care and communicating in one's usual language, each with four answer choices from no difficulty to cannot do at all. The two overlap but are not the same, so do not treat their counts as interchangeable. The questions ask about difficulty rather than whether someone has a disability, which sidesteps the label but not all of the meaning.

**What they miss:**

- **Some people, by design.** The Washington Group [says its set](https://www.washingtongroup-disability.com/question-sets/wg-short-set-on-functioning-wg-ss/) covers most but not all people with limitations in basic actions, and does not directly capture impairments, participation limits or environmental barriers.
- **Mental health and developmental disability.** An [advocacy letter from 2011](https://dredf.org/proposed-aca-data-collection-standards/), citing a national health survey analysis, reported that the ACS questions caught 70% of people with mental health disabilities and 57% with developmental disabilities other than intellectual disability. These figures are old and from an advocate, so treat them as a signal.
- **Measurement choices.** The Census Bureau [backed off a proposed change](https://www.thenationshealth.org/content/54/2/1.2) in February 2024 that could have cut the ACS disability count by 40%. A question's wording can move the count more than real change does.

**Why culture and language matter.** The [MDH autism report](https://www.leg.mn.gov/docs/2014/mandated/140404.pdf) says the term "autism" does not exist in the Hmong and Somali languages, and describes medical, vaccine-related and spiritual beliefs about causes. It also reports key informants warning that individuals within a community hold many different beliefs. Our reading: a person can have real functional difficulty and not report it, because of how a question was translated, what they think is expected at a given age, or who is asking.

**A Minnesota example of careful counting.** The University of Minnesota's [Somali autism prevalence project](https://ici.umn.edu/products/583) grew out of [concerns raised by Somali parents](https://research.umn.edu/inquiry-blog/post/study-somali-children-among-top-20-autism-research). It reviewed more than 5,000 clinical and educational records of Minneapolis children aged 7 to 9. It found about 1 in 32 Somali and 1 in 36 White children identified, with no meaningful statistical difference between the two, and lower identification among non-Somali Black (1 in 62) and Hispanic (1 in 80) children. It was not designed to explain why. Records only show children who reached services, so differences can reflect access as well as occurrence (our reading).

**In practice (our reading):** treat survey disability rates for small groups as a floor. Test translated questions with cognitive interviews. Pair survey counts with records and with family interviews. Keep functional difficulty, diagnosis, service eligibility and personal identity as separate ideas.

## 10. Small-number privacy

**Deductive disclosure** means working out something about a person by combining published facts. Removing names is not enough. In a small community, "Somali woman, 70, Stearns County, receiving a service" may identify one person, and others may know exactly who it is.

**Minnesota rules:**

- [Summary data](https://www.revisor.mn.gov/statutes/cite/13.02) under state law must not let anyone identify an individual or a unique characteristic.
- [Educational data](https://www.revisor.mn.gov/statutes/cite/13.32) are generally private.
- ECLDS and SLEDS [suppress cells under 10](https://dcyf.mn.gov/sites/default/files/2026-04/eclds-damp-data-guide.pdf) in public reporting.
- MDE's [report card notes](https://rc.education.mn.gov/js/plugins/templates/table_graduationMoreInfo.html) describe primary and secondary suppression for foster care data.

**Technique.** The federal [NCES brief](https://nces.ed.gov/pubs2011/2011603.pdf) explains that hiding a small cell is not enough if a total lets someone subtract to find it, so a related cell must also be hidden. This is called complementary suppression. It found that state minimums ranged from 5 to 30 as of 2010, most often 10. Other options in the brief include reporting values as ranges and limiting the detail published. Pooling more years is another option (our reading).

**The other side of the risk.** Suppression can erase the people you most need to see. A [coalition of researchers and civil rights advocates](https://www.aclu.org/wp-content/uploads/document/coalition_comments_on_data_suppression_in_nces_technical_brief.pdf) objected that the NCES recommendations would hide key civil rights data, and the [ECLDS guide](https://dcyf.mn.gov/sites/default/files/2026-04/eclds-damp-data-guide.pdf) itself concedes that suppression may leave very little data on small populations. Our reading: when a group is suppressed, pool years, widen the area, or work under a data agreement before giving up, and tell readers the group exists but could not be shown.

**Community risk.** Harm can reach a whole community even when no individual is identified. Our reading of common risks:

- A finding about a stigmatized condition or a benefit can attach to everyone in a small group.
- A map of a small community can show where to find its people.
- Comparisons with other groups can be misused in public debate.
- A rate based on a handful of events can swing widely and make headlines.

This risk is current. Compass notes that [fear of persecution](https://mncompass.org/demographics/cultural-communities/methodology) can keep people from reporting their community. A [Center for Health Law and Policy Innovation brief](https://chlpi.org/wp-content/uploads/2026/04/Medicaid-ICE-data-sharing-FINAL.pdf) from April 2026 reports federal sharing of Medicaid data for immigration enforcement, under ongoing court disputes, and says the government admitted improperly sharing data on Minnesota residents with immigration enforcement, then said the data had been deleted. It is a policy analysis, and the status may have changed.

**Before you share (our reading):**

- Ask who could be identified, and by whom, from this table combined with what is already public.
- Collect only what the question needs, and avoid immigration status unless it is essential and legally reviewed.
- Tell participants honestly what data protection can and cannot promise.
- Share sensitive findings with community partners before release, and agree how they will be framed. That means a chance to correct and prepare. It does not mean hiding inconvenient results.
- Never name a small community's location at fine detail with a sensitive measure.

## 11. Not generalizing from a group to a person

**The ecological fallacy** is assuming that a pattern among groups holds for individuals. [Freedman](https://www.stat.berkeley.edu/~census/549.pdf) retells Robinson's classic case. Across U.S. states in 1930, those with more foreign-born residents had higher literacy, but among individuals the link ran the other way, because immigrants tended to live in states where native-born residents were more literate. Even a correct group fact can mislead.

**Kleinman and Benson** warn against treating culture as a fixed set of traits. They propose a rule for clinics serving immigrant and refugee patients: ["First do no harm by stereotyping."](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0030294) They advise asking people what matters most to them and what they call the problem.

**In your writing:**

- Say "in this survey, 22% (±7.6) reported," not "Burmese families are poor."
- Do not turn a group average into a statement about what a family believes, needs or will do.
- Name variation within the group: generation, arrival age, faith, clan, gender, region, education, legal status, disability.
- Say who was asked. Six interviews, or 38 parents, describe those people, and can suggest but not prove a wider pattern.
- Name strengths with the same care as gaps, and do not assume a gap is cultural.
- Use a group finding only to prepare better questions. Then ask the person.

## What could not be established

1. **State Demographic Center web pages.** Its topic pages on immigration, language, age, race and ethnicity would not open. Only its 2026 chartbook and the State Demographer's June 2026 slides were read, so its other tables and tools were not checked. The 2019-2023 pooled data in the chartbook are older than the 2020-2024 data in Compass.
2. **MDE's own pages.** MDE's English learner and Minnesota Language Survey pages would not open. Details rest on statute, an older copy of the form held by a district, one district's procedure, and an MDE report from 2021-22. MDE's general public suppression threshold was not confirmed, and the 2021-22 home-language counts were not extracted.
3. **The future of the ancestry question.** Press and search results suggested possible removal, but no opened Census source confirmed that. The final content of the 2027 ACS was also not confirmed.
4. **Next Selected Population Tables.** The Census page lists 2017-2021 as the latest and gives no next date.
5. **Specific group coverage in the Census detail files.** Whether Somali and other groups appear in the Detailed DHC-A and Selected Population Tables, and with what Minnesota results, was not checked.
6. **The original theory and study files.** The 1993 Portes and Zhou article, Rumbaut's own generational paper, and the ICPSR study pages for CILS and the New York study would not open. Those sections rest on later papers, a university news item, a publisher's page and a book review.
7. **A Minnesota generational study on a population scale.** No opened source used a representative Minnesota sample to compare generations in one community. Whether one exists is unknown.
8. **Minnesota use of RDS or venue sampling.** No opened source showed either method used with a Minnesota immigrant community, and no Minnesota comparison of these methods was found.
9. **Hmong and Somali name methods.** A Hmong name-algorithm validation study would not open, and no opened source tested a surname method for Somali Minnesotans. The comments here on names are judgment.
10. **Linked data results for immigrant communities.** No opened source reported linkage error by ethnic group in Minnesota, or a Minnesota linked-data study focused on an immigrant or refugee community. Minn-LInK's method and ethnicity fields were not described in the opened abstract.
11. **Washington Group details.** The recommended cut-off for counting disability, and any cognitive testing in Somali, Hmong or Karen, were not confirmed.
12. **Current disability critiques.** Recent critiques of the ACS and the Washington Group would not open, so this note relies on a 2011 letter and a 2024 news article. The prevalence project's full report would not open, so its counts and confidence intervals are not given.
13. **Interview counts and access.** The MNHS oral history site would not open, so the count of over 360 comes from a third-party description. Its present access status is unknown.
14. **Why some refugee counts look inconsistent.** The 2024 MDH report gives 719 Ukrainian parolees and 739 arrivals from Ukraine. It does not explain the gap; other statuses may account for it. The 2025 report and fiscal year-end federal totals were not read.
15. **Current status of the Medicaid data dispute.** The latest opened source is dated April 2026.
16. **Abdi's method in detail.** A review confirms ethnographic research in three locations. The number of interviews was not confirmed from an opened page.
17. **Some figures have no year label.** Compass's Hmong and Burmese total-population rows do not show a year on the page.
18. **IPUMS's home.** The opened IPUMS page did not itself state its University of Minnesota base, so this note does not rely on that connection.

## Sources

All sources were checked October 30, 2026.

1. U.S. Census Bureau. [Understanding and Using ACS Data: When to Use 1-year or 5-year Estimates](https://www.census.gov/programs-surveys/acs/guidance/estimates.html).
2. U.S. Census Bureau. [Table IDs Explained](https://www.census.gov/programs-surveys/acs/data/data-tables/table-ids-explained.html).
3. U.S. Census Bureau. [2017-2021 ACS Selected Population Tables](https://www.census.gov/programs-surveys/acs/data/race-aian/2021.html).
4. U.S. Census Bureau. [Race, Ethnicity, Ancestry Tables](https://www.census.gov/programs-surveys/acs/data/race-aian.html).
5. U.S. Census Bureau. [ACS General Handbook, Chapter 8](https://www.census.gov/content/dam/Census/library/publications/2018/acs/acs_general_handbook_2018_ch08.pdf).
6. U.S. Census Bureau. [Comparing Race and Ethnicity Data from the ACS and the 2020 Census (May 2024)](https://www.census.gov/content/dam/Census/programs-surveys/acs/guidance/training-presentations/ACS_and_%202020_Census_Race_and_Ethnicity_Data.pdf).
7. U.S. Census Bureau. [Overlapping Race and Ancestry Estimates](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2025-01.html).
8. U.S. Census Bureau. [Improvements to the Race Question](https://www.census.gov/programs-surveys/acs/technical-documentation/user-notes/2021-03.html).
9. U.S. Census Bureau. [2024 ACS Questionnaire](https://www2.census.gov/programs-surveys/acs/methodology/questionnaires/2024/quest24.pdf).
10. U.S. Census Bureau. [Federal Register notice on the ACS, document 2025-23329](https://public-inspection.federalregister.gov/2025-23329.pdf).
11. U.S. Census Bureau. [Note for Language Spoken at Home, 2016 ACS](https://census.gov/content/dam/Census/programs-surveys/acs/tech-doc/user-notes/2016_Language_User_Note.pdf).
12. U.S. Census Bureau. [B16001 variable, 2024 ACS 5-year](https://api.census.gov/data/2024/acs/acs5/variables/B16001_111EA.html).
13. U.S. Census Bureau. [2020 Census Detailed DHC-A overview](https://census.gov/library/stories/2023/09/2020-census-dhc-a-race-overview.html).
14. U.S. Census Bureau. [What You Should Know About the Detailed DHC-A](https://census.gov/newsroom/blogs/random-samplings/2023/09/what-you-should-know-detailed-dhc-a.html).
15. Minnesota Compass. [Cultural communities](https://www.mncompass.org/topics/demographics/cultural-communities).
16. Minnesota Compass. [Cultural communities methodology](https://mncompass.org/demographics/cultural-communities/methodology).
17. Minnesota Compass. [Somali profile](https://www.mncompass.org/topics/demographics/cultural-communities/somali).
18. Minnesota Compass. [Hmong profile](https://www.mncompass.org/topics/demographics/cultural-communities/hmong).
19. Minnesota Compass. [Burmese profile](https://www.mncompass.org/topics/demographics/cultural-communities/burmese).
20. Liuzzi and Li, Minnesota Compass (2024). [The importance of data disaggregation in Minnesota's Asian communities](https://www.mncompass.org/data-insights/articles/importance-data-disaggregation-minnesotas-asian-communities).
21. Minnesota State Demographic Center (2026). [The Economic Status of Minnesotans 2026](https://mn.gov/admin/assets/The%20Economic%20Status%20of%20Minnesotans%202026_tcm36-717691.pdf).
22. Brower, Minnesota State Demographer (2026). [The State of Asian Pacific Minnesotans](https://mn.gov/capm/assets/SusanBrower_StateOfAsianPacificMinnesotans_June2026_tcm1051-759113.pdf).
23. IPUMS. [IPUMS home page](https://www.ipums.org/).
24. Minnesota Department of Health. [Refugee Health Statistics](https://www.health.state.mn.us/communities/rih/stats/index.html).
25. Minnesota Department of Health. [Minnesota Refugee Health Report 2024](https://www.web.health.state.mn.us/communities/rih/stats/24rhrpt.pdf).
26. Refugee Processing Center. [Admissions and Arrivals](https://www.rpc.state.gov/admissions-and-arrivals/).
27. Congressional Research Service (2026). [U.S. Refugee Admissions Program in FY2025 and FY2026](https://www.everycrsreport.com/reports/IF13277.html).
28. Community-University Health Care Center. [SoLaHmo](https://cuhcc.umn.edu/research/solahmo).
29. Culhane-Pera, Allen and colleagues (2010). [Improving Health through Community-Based Participatory Action Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC5484585).
30. Minnesota Department of Health (2014). [A Qualitative Study of Families of Children with Autism in the Somali Community](https://www.leg.mn.gov/docs/2014/mandated/140404.pdf).
31. Spring and colleagues (2003). [Sampling in Difficult to Access Refugee and Immigrant Communities](https://experts.umn.edu/en/publications/sampling-in-difficult-to-access-refugee-and-immigrant-communities/).
32. Wilder Research. [Speaking for Ourselves data book](https://www.wilder.org/wilder_research/speaking-for-ourselves-a-study-with-immigrant-and-refugee-communities-in-the-twin-cities-data-book/).
33. Rudolph, Fuller and Latkin (2013). [The importance of measuring and accounting for potential biases in respondent-driven samples](https://pmc.ncbi.nlm.nih.gov/articles/PMC3674117).
34. Gile, Johnston and Salganik. [Diagnostics for Respondent-driven Sampling](https://pmc.ncbi.nlm.nih.gov/articles/PMC4877136).
35. Crow, BMC Series blog (2012). [Post on snowball sampling with refugee groups](https://blogs.biomedcentral.com/bmcseriesblog/?p=41).
36. Reichel and Morales (2017). [Surveying immigrants without sampling frames](https://research-portal.najah.edu/migrant/35331/).
37. Davern and colleagues (2007). [Are surname telephone oversamples an efficient way](https://experts.umn.edu/en/publications/are-surname-telephone-oversamples-an-efficient-way-to-better-unde/).
38. Johnson, Hoffmeister and Piescher (2026). [The Minn-LInK Project](https://ijpds.org/index.php/ijpds/article/view/3721).
39. Minnesota P-20 partners. [SLEDS](https://sleds.mn.gov/).
40. Minnesota ECLDS Governing Body (2023). [ECLDS Data Access Management Policy and Data Guide](https://dcyf.mn.gov/sites/default/files/2026-04/eclds-damp-data-guide.pdf).
41. Lariscy (2011). [Differential record linkage by Hispanic ethnicity and age](https://pmc.ncbi.nlm.nih.gov/articles/PMC4598042).
42. Lam and colleagues (2026). [Mitigating Ethnoracial-Based Linkage Bias](https://ijpds.org/index.php/ijpds/article/view/3618).
43. Minnesota Language Survey form, [copy held by Winona Area Public Schools](https://www.winonaschools.org/uploaded/Documents/Learning_Teaching/MN_Language_Survey_Aug_2017_fillable_-_English.pdf).
44. Intermediate District 287. [Identification of Potential English Learners procedure](https://www.district287.org/our-district/policies-procedures/board/~board/600-education-programs/post/6001-procedure-identification-of-potential-english-learners-enrollment).
45. Minnesota Statutes. [Section 124D.59](https://www.revisor.mn.gov/statutes/cite/124D.59).
46. Minnesota Statutes. [Section 120B.35](https://www.revisor.mn.gov/statutes/cite/120B.35).
47. Minnesota Department of Education. [English Learner Education in Minnesota, 2021-22 Report](https://www.lrl.mn.gov/docs/2023/Other/231750.pdf).
48. REL Northeast and Islands (2017). [Home Language Survey Data Quality Self-Assessment](https://ies.ed.gov/use-work/resource-library/resource/other-resource/home-language-survey-data-quality-self-assessment).
49. Carrier, review in *Mashriq & Mahjar* (2016). [Elusive Jannah by Cawo M. Abdi](https://lebanesestudies.ojs.chass.ncsu.edu/index.php/mashriq/article/download/89/573). The reviewer's name is inferred from a contact address on the page.
50. Dini and Solheim (2025). [Making sense of complexity in refugee family systems](https://experts.umn.edu/en/publications/making-sense-of-complexity-in-refugee-family-systems-second-gener/).
51. Internet Scout. [Minnesota Immigrant Oral Histories](https://archives.internetscout.org/r43246/minnesota_immigrant_oral_histories).
52. Goshen College Libraries. [Immigrant Oral Histories from Minnesota](https://libraryguides.goshen.edu/c.php?g=1344118).
53. Minnesota Historical Society. [Hmong in Minnesota: primary sources](https://libguides.mnhs.org/hmong/primary).
54. Minnesota Historical Society. [Somali in Minnesota guide](https://libguides.mnhs.org/somali).
55. Minnesota Legacy Amendment. [Macalester Somali Oral History Project](https://www.legacy.mn.gov/node/37500).
56. University of Minnesota Libraries. [Immigration History Research Center Archives](https://www.lib.umn.edu/collections/special/ihrca).
57. University of Minnesota. [Immigrant Stories](https://cla.umn.edu/ihrc/immigrant-stories).
58. Minnesota Digital Library. [Minnesota Immigrants collection project](https://mndigital.org/node/417).
59. Westermeyer (1986). [Two self-rating scales for depression in Hmong refugees](https://experts.umn.edu/en/publications/two-self-rating-scales-for-depression-in-hmong-refugees-assessmen/).
60. Walde and Völlm (2023). [The TRAPD approach](https://pmc.ncbi.nlm.nih.gov/articles/PMC10309006/).
61. Washington Group on Disability Statistics. [Translating the Short Set Questions](https://www.washingtongroup-disability.com/wg-blog/post/translating-the-washington-group-short-set-questions-66/).
62. Baker and colleagues (2010). [Translation of health surveys using mixed methods](https://geriatrics-references.stanford.edu/publications/hmong-american/translation-health-surveys-using-mixed-methods).
63. Temple and Edwards (2002). [Interpreters/Translators and Cross-Language Research](https://sites.ualberta.ca/~iiqm/backissues/1_2Final/html/temple.html).
64. Squires (2008). [Language barriers and qualitative nursing research](https://pmc.ncbi.nlm.nih.gov/articles/PMC2697452).
65. UC Irvine School of Social Sciences (2012). [Gen 1.5: Where an immigrant generation fits in](https://www.socsci.uci.edu/newsevents/news/2012/2012-03-22-gen-1-5-where-an-immigrant-generation-fits-in.php).
66. National Academies (2017). [The Economic and Fiscal Consequences of Immigration, data chapter](https://www.nationalacademies.org/read/23550/chapter/15).
67. Portes, Fernández-Kelly and Haller (2009). [The Adaptation of the Immigrant Second Generation in America](https://pmc.ncbi.nlm.nih.gov/articles/PMC3634592).
68. Portes, Fernández-Kelly and Haller (2005). [Segmented assimilation on the ground](https://collaborate.princeton.edu/en/publications/segmented-assimilation-on-the-ground-the-new-second-generation-in/).
69. Russell Sage Foundation. [Children of Immigrants Longitudinal Study](https://www.russellsage.org/node/10103).
70. Tran, *ReVista* (2009). [A Review of Inheriting the City](https://revista.drclas.harvard.edu/a-review-of-inheriting-the-city-the-children-of-immigrants-come-of-age).
71. Hunt, Schneider and Comer (2004). [Should "acculturation" be a variable in health research?](https://ideas.repec.org/a/eee/socmed/v59y2004i5p973-986.html)
72. Schwartz, Unger, Zamboanga and Szapocznik (2010). [Rethinking the Concept of Acculturation](https://pmc.ncbi.nlm.nih.gov/articles/PMC3700543/).
73. U.S. Census Bureau. [How Disability Data are Collected from the ACS](https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html).
74. Washington Group on Disability Statistics. [WG Short Set on Functioning page](https://www.washingtongroup-disability.com/question-sets/wg-short-set-on-functioning-wg-ss/).
75. Washington Group on Disability Statistics (2022). [WG Short Set questionnaire](https://www.washingtongroup-disability.com/fileadmin/uploads/wg/Washington_Group_Questionnaire__1_-_WG_Short_Set_on_Functioning__October_2022_.pdf).
76. Disability Rights Education and Defense Fund (2011). [Comment on proposed data collection standards](https://dredf.org/proposed-aca-data-collection-standards/).
77. *The Nation's Health* (2024). [Article on ACS disability questions](https://www.thenationshealth.org/content/54/2/1.2).
78. Hewitt and colleagues (2013). [Minneapolis Somali Autism Spectrum Disorder Prevalence Project: Community Report](https://ici.umn.edu/products/583).
79. University of Minnesota Research (2014). [Study of Somali Children Among Top 20 in Autism Research](https://research.umn.edu/inquiry-blog/post/study-somali-children-among-top-20-autism-research).
80. Minnesota Statutes. [Section 13.02](https://www.revisor.mn.gov/statutes/cite/13.02).
81. Minnesota Statutes. [Section 13.32](https://www.revisor.mn.gov/statutes/cite/13.32).
82. Minnesota Department of Education. [Report card graduation data notes](https://rc.education.mn.gov/js/plugins/templates/table_graduationMoreInfo.html).
83. National Center for Education Statistics (2010). [SLDS Technical Brief 3](https://nces.ed.gov/pubs2011/2011603.pdf).
84. Coalition of researchers and civil rights advocates (2011). [Comments on data suppression in the NCES brief](https://www.aclu.org/wp-content/uploads/document/coalition_comments_on_data_suppression_in_nces_technical_brief.pdf).
85. Center for Health Law and Policy Innovation (2026). [Medicaid Data Sharing with ICE](https://chlpi.org/wp-content/uploads/2026/04/Medicaid-ICE-data-sharing-FINAL.pdf).
86. Freedman (1999). [Ecological Inference and the Ecological Fallacy](https://www.stat.berkeley.edu/~census/549.pdf).
87. Kleinman and Benson (2006). [Anthropology in the Clinic](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0030294).
