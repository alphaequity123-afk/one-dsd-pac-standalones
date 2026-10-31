# How cultural calendars work

**Updated:** October 30, 2026. The opened sources behind each calendar system are listed in [calendar-methods-sources.md](calendar-methods-sources.md), which says what each page supports and what could not be opened. Dates for 2026 to 2028 were checked against opened sources where possible, and the results are in `tools/date-checks.json`.

## Why a cultural calendar is hard

Most of the observances on our calendar do not sit on the Gregorian calendar. They move because they follow the moon, the sun and moon together, a different solar calendar, or a decision someone makes each year. A good calendar therefore has to say, for every entry, three things: what rule sets the date, whether the date for a given year is fixed, calculated, or announced, and where the date came from.

## Calendar systems on our calendar

**Gregorian solar calendar.** National days, heritage months, U.S. federal holidays and most remembrance days. These are fixed, or set by a weekday rule (third Monday in January, fourth Thursday in November).

**Islamic (Hijri) lunar calendar.** Twelve lunar months of 29 or 30 days, about 354 days a year, so every observance moves about eleven days earlier each Gregorian year. Ramadan, Eid al-Fitr, Eid al-Adha, Muharram, Ashura and Mawlid follow it. The month starts when the new crescent is seen, or when a calculation says it should be seen. Communities differ: some mosques follow local sighting, some follow sighting in Saudi Arabia or another country, some follow an astronomical calculation agreed in advance. In practice this means two mosques in the same city can hold Eid on different days. Our data uses the Umm al-Qura tabular calendar as an estimate and labels every such date "moon-sighted or announced". The real date is confirmed by each mosque close to the time, and the workplace effect (fasting, prayer, the Eid day itself) can shift by a day.

**Chinese lunisolar calendar.** Months follow the moon, and a leap month is added about every three years to keep the year in step with the seasons. Lunar New Year, Mid-Autumn and Dragon Boat follow it, and so do the Vietnamese Tết and the Korean Seollal and Chuseok, which use the same system but can differ by a day in rare years because the time zone of the calculation differs. These dates are calculable far in advance from published astronomical tables.

**Hindu lunisolar calendars.** Diwali, Holi, Navaratri and Guru Nanak's birthday follow lunar months tied to the solar year. There are regional variants (amanta and purnimanta month reckoning), and temple panchangs set the day locally. Calculated dates are reliable, but a temple in Minnesota may hold its public celebration on a nearby weekend.

**Theravada Buddhist calendars (Thai, Lao, Khmer, Burmese).** Holy days such as Makha Bucha, Visakha Bucha and Asanha Bucha fall on full moons of lunar months. The mid-April new years (Songkran, Pi Mai Lao, Choul Chnam Thmey, Thingyan) are solar, based on the sun entering Aries in traditional astronomy, and the governments of Thailand, Laos and Cambodia publish the official days each year. Temples in Minnesota usually celebrate on the nearest weekend.

**Ethiopian calendar.** Thirteen months (twelve of thirty days and one of five or six), with the new year on Meskerem 1, which is September 11, or September 12 in the year before a Gregorian leap year. Enkutatash, Meskel, Genna and Timkat are fixed on this calendar and so move only by that one day. Fasika (Easter) follows the Orthodox Easter calculation.

**Julian calendar in Orthodox churches.** Russian Orthodox and many Ukrainian and Serbian Orthodox churches keep Christmas on December 25 Julian, which is January 7 Gregorian through 2099. Easter in all Orthodox churches is calculated on the Julian calendar, so it usually falls later than Western Easter, and sometimes on the same day. The Orthodox Church of Ukraine moved Christmas to December 25 Gregorian in 2023; which date a Minnesota parish uses depends on its jurisdiction and should be checked parish by parish.

**Western Christian moving feasts.** Easter is the first Sunday after the first ecclesiastical full moon on or after March 21. Ash Wednesday, Holy Week, Ascension and Pentecost are counted from it.

**Hmong New Year.** There is no single fixed date. The celebration traditionally comes after the harvest, and in the United States each city's organizing group sets its own weekend, typically between October and December. In St. Paul, the large public celebration has been held at the end of November for decades. The right way to carry this on a calendar is to list each organizer's announced dates for the year, with a link to the announcement, and never to present a date as settled before it is announced.

**Karen New Year.** Falls on the first day of the Karen month Thalay (the waxing moon of Pyatho in the Burmese calendar), usually late December or early January, so some Gregorian years have two and some none. Minnesota Karen organizations often hold their public celebration in early January.

**Irreecha, Pchum Ben, Loy Krathong, Obon.** Tied to lunar or seasonal calendars and set each year by the organizing community or temple. These are listed as "announced each year".

**Jewish calendar.** The Russian-speaking brief notes a Jewish stream within that community. Jewish holidays follow a lunisolar calendar with its own rules and are fully calculable. They are not yet on our calendar because no community on the list is defined by that calendar; add them if the owner wants the Russian-speaking page to carry them.

## How public institutions present moving dates

Good practice, as seen in university and public-sector diversity calendars, is to:

1. Show the date and a short note on how it is set ("begins at sundown", "date depends on moon sighting", "set by the organizers").
2. Keep a separate note on what the observance means at work: fasting, prayer times, a day many people take off, or a day of mourning.
3. Link to the community's own announcement rather than restating it.
4. Mark which entries are confirmed for the year and which are projected.
5. Refresh announced dates every autumn for the coming year.

Our data follows this: each entry has `dateCertainty`, each date has its own `source`, and `workplaceNote` is left empty until a source supports it.

## How dates are treated

Calculated dates start from calendar tables and the rule for each observance, then are checked against opened sources:

- An official or religious source that states the date confirms it.
- A commercial calendar site does not confirm a date. It only adds a note.
- Official sources that disagree confirm nothing. Holi 2027 is March 23 on the Government of India's list and March 22 on Drik Panchang, so it stays unconfirmed.
- A moon-sighted date is never shown as certain, however good the projection. The Fiqh Council of North America publishes a calculated calendar, and Saudi Arabia's Supreme Court calls on sighting committees, so two mosques in one city can differ by a day.
- Dates an organizer announces come from the organizer's own page and are added once posted.

The `.ics` file carries confirmed dates only.

## What still needs checking

- How Minnesota mosques decide their dates. No opened source explains it.
- Which calendar each Ukrainian and Russian Orthodox parish in Minnesota uses for Christmas.
- Organizer dates for 2027 and 2028, most of which had not been posted when checked.
- 2027 and 2028 dates that rest only on commercial calendar sites, including several Buddhist and Ethiopian dates.
