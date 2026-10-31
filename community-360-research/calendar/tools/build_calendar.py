import sys, json, datetime as dt

import holidays
from dateutil.easter import easter, EASTER_WESTERN, EASTER_ORTHODOX
from hijridate import Hijri
from lunardate import LunarDate

OUT = sys.argv[1]
YEARS = [2026, 2027, 2028]
HV = 'python-holidays 0.107'

def hol(country, match, label):
    def f(y):
        h = holidays.country_holidays(country, years=y, language='en_US') if country in ('ET','KR','CN','LA','TH','KH','MM','VN','JP','LB','BA','MX','CO','EC','GT','SV','CU','FR','RU') else holidays.country_holidays(country, years=y)
        hits = sorted(d for d, n in h.items() if match(n))
        return (hits[0], f'Calculated with {HV}, {label} module (country {country}); first matching holiday entry') if hits else (None, None)
    return f

def fixed(m, d, note='Fixed Gregorian date'):
    return lambda y: (dt.date(y, m, d), note)

def nth_weekday(m, wd, n, note):
    def f(y):
        d = dt.date(y, m, 1); c = 0
        while True:
            if d.weekday() == wd:
                c += 1
                if c == n: return d, note
            d += dt.timedelta(days=1)
    return f

def western_easter(offset=0, label='Western Easter'):
    return lambda y: (easter(y, EASTER_WESTERN) + dt.timedelta(days=offset), f'Calculated: Gregorian Easter computus (python-dateutil 2.9), {label}')

def orthodox_easter(offset=0, label='Orthodox Easter'):
    return lambda y: (easter(y, EASTER_ORTHODOX) + dt.timedelta(days=offset), f'Calculated: Julian Easter computus converted to Gregorian (python-dateutil 2.9), {label}')

HIJRI_NOTE = ('Estimated with the Umm al-Qura tabular calendar (hijridate 2.6). Minnesota mosques decide the day by local or global moon sighting or by an astronomical calculation they adopt, so the observed day can differ by one day; the date is confirmed close to the time.')
def hijri(month, day):
    def f(y):
        # find the Hijri year whose month/day falls in Gregorian year y
        for hy in range(1446, 1453):
            try:
                g = Hijri(hy, month, day).to_gregorian()
            except Exception:
                continue
            gd = dt.date(g.year, g.month, g.day)
            if gd.year == y: return gd, HIJRI_NOTE
        return None, None
    return f

LUNAR_NOTE = 'Calculated from the Chinese lunisolar calendar (lunardate 0.3, tables for 1900-2099)'
def lunar(m, d, label):
    return lambda y: (LunarDate(y, m, d).toSolarDate(), f'{LUNAR_NOTE}: lunar month {m}, day {d} ({label})')

def julian_fixed(m, d, label):
    # Julian calendar date -> Gregorian (+13 days for 1900-2099)
    return lambda y: (dt.date(y, m, d) + dt.timedelta(days=13), f'Calculated: {label} on the Julian calendar, 13 days after the same Gregorian date in 1900-2099')

def us(match):
    return hol('US', match, 'United States (federal)')

E = []
def add(name, aka, comms, kind, rule, fn, certainty, marks):
    E.append(dict(name=name, alsoKnownAs=aka, communities=comms, kind=kind, dateRule=rule, _fn=fn, dateCertainty=certainty, whatItMarks=marks))

# Lunisolar new years and festivals
add('Lunar New Year', ['Spring Festival', 'Chunjie'], ['chinese'], 'cultural', 'First day of the first month of the Chinese lunisolar calendar, falling between January 21 and February 20.', lunar(1,1,'Spring Festival'), 'calculated', 'Start of the lunisolar year.')
add('Tết Nguyên Đán', ['Tết', 'Vietnamese Lunar New Year'], ['vietnamese'], 'cultural', 'First day of the first month of the Vietnamese lunisolar calendar (usually the same day as Chinese New Year; rare one-day differences come from the time zone used).', hol('VN', lambda n: n == 'Lunar New Year', 'Vietnam'), 'calculated', 'Start of the lunisolar year.')
add('Seollal', ['Korean Lunar New Year'], ['korean'], 'cultural', 'First day of the first month of the Korean lunisolar calendar.', hol('KR', lambda n: n == 'Korean New Year', 'South Korea'), 'calculated', 'Start of the lunisolar year.')
add('Chuseok', ['Hangawi'], ['korean'], 'cultural', 'Fifteenth day of the eighth month of the Korean lunisolar calendar.', hol('KR', lambda n: n.startswith('Chuseok'), 'South Korea'), 'calculated', 'Autumn harvest festival.')
add('Mid-Autumn Festival', ['Zhongqiu Jie', 'Tết Trung Thu'], ['chinese', 'vietnamese'], 'cultural', 'Fifteenth day of the eighth month of the Chinese lunisolar calendar.', lunar(8,15,'Mid-Autumn'), 'calculated', 'Harvest moon festival.')
add('Dragon Boat Festival', ['Duanwu Jie'], ['chinese'], 'cultural', 'Fifth day of the fifth month of the Chinese lunisolar calendar.', lunar(5,5,'Duanwu'), 'calculated', 'Traditional early-summer festival.')
add('Qingming', ['Tomb-Sweeping Day'], ['chinese'], 'cultural', 'Solar term beginning about April 4 or 5.', hol('CN', lambda n: 'Tomb' in n or 'Qingming' in n, 'China'), 'calculated', 'Day for tending family graves and honoring ancestors.')

# Southeast Asian solar new years
add('Songkran', ['Thai New Year'], ['thai'], 'cultural', 'April 13 to 15 as set by the Thai government (traditional solar new year).', hol('TH', lambda n: 'Songkran' in n, 'Thailand'), 'fixed', 'Traditional Thai new year.')
add('Pi Mai Lao', ['Lao New Year', 'Boun Pi Mai'], ['lao'], 'cultural', 'Mid-April, usually April 14 to 16 as set by the Lao government.', hol('LA', lambda n: n.startswith('Lao New Year'), 'Laos'), 'announced each year', 'Traditional Lao new year.')
add('Choul Chnam Thmey', ['Khmer New Year'], ['khmer'], 'cultural', 'Mid-April, usually April 13 or 14 to 16, set each year by the Cambodian government from the traditional astronomical calendar.', hol('KH', lambda n: 'Khmer New Year' in n, 'Cambodia'), 'announced each year', 'Traditional Khmer new year.')
add('Thingyan', ['Burmese New Year', 'Water Festival'], ['burmese'], 'cultural', 'Mid-April, calculated from the traditional Myanmar calendar.', hol('MM', lambda n: 'Myanmar New Year' in n, 'Myanmar'), 'calculated', 'Traditional Burmese new year.')
add('Karen New Year', ['Kaw La Thaw Ni'], ['karen'], 'cultural', 'First day of the Karen month of Thalay (Pyatho waxing moon), usually in late December or January.', hol('MM', lambda n: 'Karen' in n, 'Myanmar'), 'calculated', 'Karen new year.')
add('Visakha Bucha', ['Vesak', 'Buddha Day'], ['thai', 'lao', 'khmer', 'burmese'], 'religious', 'Full moon of the sixth lunar month in the Thai and Cambodian calendars, usually in May; temples may choose a nearby weekend.', hol('TH', lambda n: 'Visakha' in n, 'Thailand'), 'calculated', 'Birth, enlightenment and death of the Buddha in Theravada tradition.')

# Islamic observances
add('Start of Ramadan', ['Ramadan', 'Ramazan', 'Soomaan'], ['somali', 'arabic-speaking', 'oromo', 'bosnian', 'ethiopian', 'lebanese', 'nigerian', 'kenyan', 'indian', 'african-american'], 'religious', 'First day of the ninth month of the Islamic (Hijri) lunar calendar.', hijri(9,1), 'moon-sighted or announced', 'Start of the month of daytime fasting.')
add('Eid al-Fitr', ['Ciid Yare', 'Ramazanski Bajram', 'Id el Fitr'], ['somali', 'arabic-speaking', 'oromo', 'bosnian', 'ethiopian', 'lebanese', 'nigerian', 'kenyan', 'indian', 'african-american'], 'religious', 'First day of the tenth Islamic month (Shawwal), after Ramadan ends.', hijri(10,1), 'moon-sighted or announced', 'End of Ramadan.')
add('Eid al-Adha', ['Ciid Weyn', 'Kurban Bajram', 'Id el Kabir'], ['somali', 'arabic-speaking', 'oromo', 'bosnian', 'ethiopian', 'lebanese', 'nigerian', 'kenyan', 'indian', 'african-american'], 'religious', 'Tenth day of the twelfth Islamic month (Dhu al-Hijjah).', hijri(12,10), 'moon-sighted or announced', 'Festival of sacrifice, during the Hajj season.')
add('Islamic New Year', ['Hijri New Year', 'Muharram'], ['somali', 'arabic-speaking', 'oromo', 'bosnian', 'lebanese', 'nigerian', 'kenyan', 'indian'], 'religious', 'First day of the first Islamic month (Muharram).', hijri(1,1), 'moon-sighted or announced', 'Start of the Hijri year.')
add('Ashura', [], ['arabic-speaking', 'lebanese', 'indian'], 'religious', 'Tenth day of Muharram.', hijri(1,10), 'moon-sighted or announced', 'A day observed differently in Sunni and Shia practice.')
add('Mawlid an-Nabi', ['Mawlid', 'Mawliid'], ['somali', 'arabic-speaking', 'oromo', 'ethiopian', 'nigerian'], 'religious', 'Twelfth day of the third Islamic month (Rabi al-Awwal); not observed by all Muslims.', hijri(3,12), 'moon-sighted or announced', 'Birthday of the Prophet Muhammad.')

# Ethiopian calendar and Orthodox
add('Enkutatash', ['Ethiopian New Year', 'Meskerem 1'], ['ethiopian', 'amharic', 'oromo'], 'cultural', 'Meskerem 1 on the Ethiopian calendar: September 11, or September 12 in the Gregorian year before a Gregorian leap year.', hol('ET', lambda n: 'New Year' in n, 'Ethiopia'), 'calculated', 'Start of the Ethiopian year.')
add('Meskel', ['Finding of the True Cross', 'Demera'], ['ethiopian', 'amharic'], 'religious', 'Meskerem 17 on the Ethiopian calendar: September 27, or September 28 in leap-adjacent years.', hol('ET', lambda n: 'Finding' in n or 'Meskel' in n or 'Cross' in n, 'Ethiopia'), 'calculated', 'Ethiopian Orthodox feast of the finding of the True Cross.')
add('Genna', ['Ethiopian Christmas', 'Ledet'], ['ethiopian', 'amharic', 'oromo'], 'religious', 'Tahsas 29 on the Ethiopian calendar, usually January 7.', hol('ET', lambda n: 'Christmas' in n, 'Ethiopia'), 'calculated', 'Christmas in the Ethiopian Orthodox Tewahedo Church.')
add('Timkat', ['Ethiopian Epiphany', 'Timket'], ['ethiopian', 'amharic', 'oromo'], 'religious', 'Tir 11 on the Ethiopian calendar, usually January 19 (January 20 in some years).', hol('ET', lambda n: 'Epiphany' in n, 'Ethiopia'), 'calculated', 'Baptism of Jesus in the Ethiopian Orthodox tradition.')
add('Fasika', ['Ethiopian Easter'], ['ethiopian', 'amharic', 'oromo'], 'religious', 'Same date as Eastern Orthodox Easter.', orthodox_easter(0, 'Fasika'), 'calculated', 'Easter in the Ethiopian Orthodox tradition.')
add('Adwa Victory Day', [], ['ethiopian', 'amharic', 'oromo'], 'national', 'March 2 (Yekatit 23).', hol('ET', lambda n: 'Adwa' in n, 'Ethiopia'), 'fixed', 'The 1896 Ethiopian victory at Adwa.')
add('Orthodox Christmas (Julian calendar)', ['Rizdvo', 'Rozhdestvo', 'Božić (Pravoslavni)'], ['ukrainian', 'russian-speaking', 'bosnian'], 'religious', 'December 25 on the Julian calendar, which is January 7 on the Gregorian calendar in 1900-2099. Since 2023 the Orthodox Church of Ukraine also uses December 25 on the Revised Julian calendar.', julian_fixed(12, 25, 'December 25'), 'calculated', 'Christmas for churches on the Julian calendar.')
add('Orthodox Easter', ['Pascha', 'Velykden', 'Paskha'], ['ukrainian', 'russian-speaking', 'bosnian', 'arabic-speaking', 'lebanese'], 'religious', 'First Sunday after the first full moon on or after the spring equinox, calculated on the Julian calendar.', orthodox_easter(0), 'calculated', 'Resurrection of Jesus in Eastern Christian tradition.')

# Western Christian moving feasts
add('Easter', ['Pascua', 'Pâques', 'Pasko ng Pagkabuhay'], ['american', 'european-american', 'minnesota', 'filipino', 'mexican', 'latino', 'guatemalan', 'salvadoran', 'colombian', 'ecuadorian', 'cuban', 'puerto-rican', 'french', 'african-american', 'liberian', 'nigerian', 'kenyan', 'lebanese', 'korean', 'karen', 'ukrainian'], 'religious', 'First Sunday after the first ecclesiastical full moon on or after March 21 (Gregorian).', western_easter(0), 'calculated', 'Resurrection of Jesus in Western Christian tradition.')
add('Good Friday', ['Viernes Santo', 'Biyernes Santo'], ['filipino', 'mexican', 'latino', 'guatemalan', 'salvadoran', 'colombian', 'ecuadorian', 'puerto-rican', 'liberian', 'nigerian', 'kenyan', 'european-american'], 'religious', 'The Friday before Western Easter.', western_easter(-2, 'Good Friday'), 'calculated', 'The crucifixion of Jesus.')
add('Ash Wednesday', ['Miércoles de Ceniza'], ['latino', 'mexican', 'filipino', 'european-american', 'guatemalan', 'salvadoran'], 'religious', '46 days before Western Easter.', western_easter(-46, 'Ash Wednesday'), 'calculated', 'Start of Lent.')

# Indian
add('Diwali', ['Deepavali'], ['indian'], 'religious', 'New moon (Amavasya) of the Hindu lunar month Kartika (Ashvin in the amanta reckoning), usually October or November.', hol('IN', lambda n: 'Diwali' in n, 'India'), 'calculated', 'Festival of lights.')
add('Holi', [], ['indian'], 'religious', 'Day after the full moon of the Hindu month Phalguna, usually March.', hol('IN', lambda n: n == 'Holi', 'India'), 'calculated', 'Spring festival of colors.')
add('Republic Day (India)', [], ['indian'], 'national', 'January 26.', fixed(1, 26), 'fixed', 'Adoption of the Constitution of India in 1950.')
add('Independence Day (India)', [], ['indian'], 'national', 'August 15.', fixed(8, 15), 'fixed', 'Indian independence in 1947.')

# Japanese
add('Shōgatsu', ['Japanese New Year', 'Oshōgatsu'], ['japanese'], 'cultural', 'January 1, with celebrations through the first days of January.', fixed(1, 1), 'fixed', 'Japanese new year.')

# National days, fixed
NAT = [
 ('Mexican Independence Day', ['Grito de Dolores', 'Día de la Independencia'], ['mexican', 'latino'], 9, 16, 'Start of the 1810 war of independence.'),
 ('Central American Independence Day', ['Día de la Independencia'], ['guatemalan', 'salvadoran', 'latino'], 9, 15, 'Independence of Central America from Spain in 1821.'),
 ('Colombian Independence Day', ['Día de la Independencia'], ['colombian', 'latino'], 7, 20, 'The 1810 declaration in Bogotá.'),
 ('Ecuadorian Independence Day', ['Primer Grito de Independencia'], ['ecuadorian', 'latino'], 8, 10, 'The 1809 Quito uprising.'),
 ('Philippine Independence Day', ['Araw ng Kalayaan'], ['filipino'], 6, 12, 'The 1898 declaration of independence.'),
 ('Nigerian Independence Day', [], ['nigerian'], 10, 1, 'Independence in 1960.'),
 ('Jamhuri Day', [], ['kenyan'], 12, 12, 'Independence (1963) and republic (1964).'),
 ('Liberian Independence Day', [], ['liberian'], 7, 26, 'Independence in 1847.'),
 ('Somali Independence Day', ['1 Luulyo'], ['somali'], 7, 1, 'Union of the former British and Italian territories as the Somali Republic in 1960.'),
 ('Lebanese Independence Day', [], ['lebanese', 'arabic-speaking'], 11, 22, 'Independence in 1943.'),
 ('Ukrainian Independence Day', [], ['ukrainian'], 8, 24, 'Independence in 1991.'),
 ('Bosnia and Herzegovina Independence Day', ['Dan nezavisnosti'], ['bosnian'], 3, 1, 'The 1992 independence referendum.'),
 ('Korean Independence Movement Day', ['Samiljeol'], ['korean'], 3, 1, 'The 1919 March First Movement.'),
 ('Korean Liberation Day', ['Gwangbokjeol'], ['korean'], 8, 15, 'Liberation from Japanese rule in 1945.'),
 ('Puerto Rico Constitution Day', ['Día de la Constitución'], ['puerto-rican'], 7, 25, 'The 1952 Commonwealth constitution.'),
 ('Lao National Day', [], ['lao'], 12, 2, 'Founding of the Lao PDR in 1975.'),
 ('Union Day (Myanmar)', [], ['burmese', 'karen'], 2, 12, 'The 1947 Panglong Agreement.'),
 ('Día de la Virgen de Guadalupe', ['Our Lady of Guadalupe'], ['mexican', 'latino'], 12, 12, 'Feast of Our Lady of Guadalupe.'),
 ('Día de los Muertos', ['Day of the Dead'], ['mexican', 'latino', 'guatemalan'], 11, 2, 'Remembrance of the dead (observed November 1 and 2).'),
 ('St. Patrick\'s Day', [], ['european-american', 'american'], 3, 17, 'Feast of Saint Patrick.'),
 ('Syttende Mai', ['Norwegian Constitution Day'], ['european-american', 'minnesota'], 5, 17, 'The 1814 Norwegian constitution.'),
 ('St. Lucia Day', ['Luciadagen'], ['european-american'], 12, 13, 'Feast of Saint Lucy, kept in Swedish tradition.'),
 ('Minnesota Statehood Day', [], ['minnesota'], 5, 11, 'Minnesota became a state on May 11, 1858.'),
 ('International Day of Sign Languages', [], ['deaf-deafblind-hard-of-hearing'], 9, 23, 'United Nations day for sign languages.'),
 ('Christmas', ['Navidad', 'Noël', 'Pasko'], ['american', 'european-american', 'minnesota', 'filipino', 'mexican', 'latino', 'guatemalan', 'salvadoran', 'colombian', 'ecuadorian', 'cuban', 'puerto-rican', 'french', 'african-american', 'liberian', 'nigerian', 'kenyan', 'lebanese', 'korean', 'karen'], 12, 25, 'Birth of Jesus (Gregorian calendar).'),
 ('Kwanzaa (first day)', [], ['african-american'], 12, 26, 'First of seven days (December 26 to January 1) honoring African heritage, created in 1966.'),
]
for n, aka, c, m, d, w in NAT:
    add(n, aka, c, 'religious' if n in ('Christmas', 'Día de la Virgen de Guadalupe') else ('heritage' if 'Sign' in n or 'Kwanzaa' in n or 'Muertos' in n or 'Patrick' in n or 'Lucia' in n else 'national'), f'{dt.date(2026, m, d):%B} {d}.', fixed(m, d), 'fixed', w)

# US federal
add('Martin Luther King Jr. Day', [], ['african-american', 'american', 'minnesota'], 'national', 'Third Monday in January.', nth_weekday(1, 0, 3, 'Calculated: third Monday in January (federal holiday rule)'), 'fixed', 'Life and work of Dr. Martin Luther King Jr.')
add('Juneteenth', ['Juneteenth National Independence Day'], ['african-american', 'american', 'minnesota'], 'national', 'June 19.', fixed(6, 19), 'fixed', 'June 19, 1865, when enslaved people in Galveston, Texas, were told of their freedom.')
add('Independence Day (United States)', ['Fourth of July'], ['american', 'minnesota', 'european-american'], 'national', 'July 4.', fixed(7, 4), 'fixed', 'The 1776 Declaration of Independence.')
add('Thanksgiving', [], ['american', 'minnesota', 'european-american'], 'national', 'Fourth Thursday in November.', nth_weekday(11, 3, 4, 'Calculated: fourth Thursday in November (federal holiday rule)'), 'fixed', 'United States harvest and thanksgiving holiday.')


# Dates named in the community briefs (crosswalk additions)
def last_weekday(m, wd, note):
    def f(y):
        d = dt.date(y, m + 1, 1) - dt.timedelta(days=1) if m < 12 else dt.date(y, 12, 31)
        while d.weekday() != wd: d -= dt.timedelta(days=1)
        return d, note
    return f
BR = [
 ('Somaliland independence (June 26)', [], ['somali'], 'remembrance', 6, 26, 'Independence of British Somaliland in 1960; marked by some families, and its meaning depends on Somaliland politics.'),
 ('May 14 Hmong veterans and General Vang Pao remembrance', [], ['hmong'], 'remembrance', 5, 14, 'The May 14, 1975 departure of General Vang Pao from Laos, remembered by Hmong American and Hmong-Lao veterans.'),
 ('Karen Martyrs\' Day', [], ['karen'], 'remembrance', 8, 12, 'The 1950 killing of Saw Ba U Gyi.'),
 ('Srebrenica Genocide Memorial Day', [], ['bosnian'], 'remembrance', 7, 11, 'The July 1995 genocide at Srebrenica.'),
 ('Victory Day (May 9)', ['Den Pobedy'], ['russian-speaking'], 'remembrance', 5, 9, 'The 1945 end of the Second World War in Europe in Soviet memory; meaningful to some elders and contested by others since 2022.'),
 ('New Year (Novy God)', ['Novy God'], ['russian-speaking', 'ukrainian'], 'cultural', 1, 1, 'The major secular winter holiday from the Soviet era, still central for some families.'),
 ('Haitian Independence Day', ['Jour de l\'Indépendance'], ['french'], 'national', 1, 1, 'Haitian independence in 1804.'),
 ('Haiti earthquake remembrance', [], ['french'], 'remembrance', 1, 12, 'The January 12, 2010 earthquake in Haiti.'),
 ('Cambodian Genocide Remembrance (April 17)', [], ['khmer'], 'remembrance', 4, 17, 'The Khmer Rouge takeover of Phnom Penh on April 17, 1975.'),
 ('Day of Remembrance (Executive Order 9066)', [], ['japanese'], 'remembrance', 2, 19, 'The February 19, 1942 order that led to the incarceration of Japanese Americans.'),
 ('Black April', ['Ngày Quốc Hận', 'Fall of Saigon remembrance'], ['vietnamese'], 'remembrance', 4, 30, 'April 30, 1975, the end of the Republic of Vietnam; grief and politics for many Vietnamese Americans.'),
 ('Día de los Reyes', ['Three Kings Day', 'Epiphany'], ['mexican', 'puerto-rican', 'latino', 'guatemalan', 'salvadoran', 'colombian', 'ecuadorian', 'cuban'], 'religious', 1, 6, 'The visit of the Magi; a major gift day in many Puerto Rican and Mexican families.'),
 ('Las Posadas (first night)', [], ['mexican', 'latino', 'guatemalan'], 'religious', 12, 16, 'Nine nights (December 16 to 24) re-enacting Mary and Joseph\'s search for shelter.'),
 ('Discovery of Puerto Rico Day', [], ['puerto-rican'], 'national', 11, 19, 'Columbus\'s 1493 landing; marked in some public life.'),
 ('Saint Óscar Romero remembrance', [], ['salvadoran'], 'remembrance', 3, 24, 'The assassination of Archbishop Óscar Romero on March 24, 1980.'),
 ('Salvadoran Peace Accords anniversary', [], ['salvadoran'], 'remembrance', 1, 16, 'The January 16, 1992 peace accords ending the civil war.'),
 ('Cuban Revolution / exile anniversary', [], ['cuban'], 'remembrance', 1, 1, 'January 1, 1959; revolution or exile depending on the family, and grief and politics for many.'),
 ('Cuban Independence (May 20)', [], ['cuban'], 'national', 5, 20, 'The 1902 republic; kept in some exile calendars.'),
 ('Grito de Yara (October 10)', [], ['cuban'], 'national', 10, 10, 'The 1868 start of the wars of independence.'),
 ('Madaraka Day', [], ['kenyan'], 'national', 6, 1, 'Self-rule in 1963.'),
 ('Mashujaa Day', ['Heroes\' Day'], ['kenyan'], 'national', 10, 20, 'Day honoring national heroes.'),
 ('EDSA People Power anniversary', [], ['filipino'], 'remembrance', 2, 25, 'The February 1986 People Power movement.'),
 ('Lebanese Independence Day', [], ['lebanese'], 'national', 11, 22, 'Independence in 1943.'),
 ('Watch Night', [], ['african-american', 'liberian'], 'religious', 12, 31, 'New Year\'s Eve church vigil, remembering the 1862 vigil before the Emancipation Proclamation took effect.'),
 ('Malcolm X\'s birthday', [], ['african-american'], 'remembrance', 5, 19, 'Birth of Malcolm X in 1925.'),
 ('Anniversary of Dr. King\'s assassination', [], ['african-american'], 'remembrance', 4, 4, 'April 4, 1968.'),
 ('George Floyd remembrance', [], ['african-american', 'minnesota'], 'remembrance', 5, 25, 'The May 25, 2020 murder of George Floyd in Minneapolis.'),
 ('March on Washington anniversary', [], ['african-american'], 'remembrance', 8, 28, 'The August 28, 1963 March on Washington.'),
 ('Black History Month (begins)', [], ['african-american', 'american', 'minnesota'], 'heritage', 2, 1, 'Month of Black history, February.'),
 ('Hispanic Heritage Month (begins)', [], ['latino', 'mexican', 'guatemalan', 'salvadoran', 'colombian', 'ecuadorian', 'cuban', 'puerto-rican'], 'heritage', 9, 15, 'U.S. heritage month, September 15 to October 15, tied to Central American and Mexican independence days.'),
 ('Thai Mother\'s Day', [], ['thai'], 'national', 8, 12, 'Birthday of Queen Mother Sirikit, kept as Mother\'s Day in Thailand.'),
 ('Thai Father\'s Day', [], ['thai'], 'national', 12, 5, 'Birthday of King Bhumibol, kept as Father\'s Day in Thailand.'),
 ('Ukrainian Independence Day', [], ['ukrainian'], 'national', 8, 24, 'Independence in 1991.'),
]
for n, aka, c, k, m, d, w in BR:
    if any(e['name'] == n for e in E): continue
    add(n, aka, c, k, f'{dt.date(2026, m, d):%B} {d}.', fixed(m, d), 'fixed', w)
add('Rondo Days', [], ['african-american', 'minnesota'], 'community festival', 'Third Saturday of July in St. Paul, as set by the organizers.', nth_weekday(7, 5, 3, 'Calculated from the usual third-Saturday-of-July pattern; the organizers confirm each year'), 'announced each year', 'The Black St. Paul neighborhood of Rondo, divided by Interstate 94.')
add('Holodomor Remembrance Day', [], ['ukrainian'], 'remembrance', 'Fourth Saturday of November.', nth_weekday(11, 5, 4, 'Calculated: fourth Saturday in November'), 'calculated', 'The 1932-33 famine in Soviet Ukraine.')
add('Vyshyvanka Day', [], ['ukrainian'], 'cultural', 'Third Thursday of May.', nth_weekday(5, 3, 3, 'Calculated: third Thursday in May'), 'calculated', 'A day for wearing embroidered shirts.')
add('Pchum Ben', ['Ancestors\' Day'], ['khmer'], 'religious', 'Last of fifteen days at the end of the Khmer lunar month Photrobot, usually September or October.', hol('KH', lambda n: 'Pchum Ben' in n, 'Cambodia'), 'calculated', 'The fortnight when families make offerings for the dead.')
add('Hùng Kings Commemoration', ['Giỗ Tổ Hùng Vương'], ['vietnamese'], 'cultural', 'Tenth day of the third lunar month.', hol('VN', lambda n: 'Hung Kings' in n, 'Vietnam'), 'calculated', 'Commemoration of the legendary founding kings.')
add('Makha Bucha', ['Magha Puja'], ['thai', 'lao', 'khmer'], 'religious', 'Full moon of the third lunar month, usually February or March.', hol('TH', lambda n: n == 'Makha Bucha', 'Thailand'), 'calculated', 'A Theravada Buddhist holy day.')
add('Asanha Bucha and start of Buddhist Lent', ['Khao Phansa'], ['thai', 'lao', 'khmer', 'burmese'], 'religious', 'Full moon of the eighth lunar month, usually July; the rains retreat starts the next day.', hol('TH', lambda n: n == 'Asarnha Bucha', 'Thailand'), 'calculated', 'The Buddha\'s first sermon, and the start of the three-month rains retreat.')
add('Navaratri and Dussehra', ['Vijayadashami'], ['indian'], 'religious', 'Dussehra is the tenth day of the bright half of the Hindu month Ashvin, usually October; the nine nights of Navaratri come before it.', hol('IN', lambda n: n == 'Dussehra', 'India'), 'calculated', 'Victory of good over evil.')
add('Guru Nanak Gurpurab', [], ['indian'], 'religious', 'Full moon of the Hindu month Kartika, usually November.', hol('IN', lambda n: 'Guru Nanak' in n, 'India'), 'calculated', 'Birth of Guru Nanak, founder of Sikhism.')
add('Obon', ['Bon'], ['japanese'], 'religious', 'Mid-July or mid-August depending on the region and temple; local dates are announced by the organizers.', None, 'announced each year', 'Remembrance of ancestors.')
add('Loy Krathong', [], ['thai'], 'cultural', 'Full moon of the twelfth Thai lunar month, usually November.', None, 'announced each year', 'Floating offerings on water.')
add('Irreecha date note', [], [], 'cultural', '', None, 'announced each year', '')
E[:] = [e for e in E if e['name'] != 'Irreecha date note']

# Announced, no date until published
ANN = [
 ('Hmong New Year (Minnesota)', ['Noj Peb Caug'], ['hmong'], 'community festival', 'Set each year by the organizing groups. Hmong New Year celebrations traditionally follow the harvest; in Minnesota they run from about October to December, and each city or organization picks its own dates and venue.', 'Hmong new year after the harvest.'),
 ('Irreecha', ['Irreessa'], ['oromo'], 'cultural', 'Announced each year; held around the end of the Ethiopian rainy season, usually on a weekend in late September or early October.', 'Oromo thanksgiving at the end of the rainy season.'),
 ('Ramadan night prayers and community iftars', [], ['somali', 'arabic-speaking', 'oromo', 'bosnian'], 'community festival', 'Announced by each mosque and community group during Ramadan.', 'Shared fast-breaking meals and evening prayers during Ramadan.'),
]
for n, aka, c, k, r, w in ANN:
    E.append(dict(name=n, alsoKnownAs=aka, communities=c, kind=k, dateRule=r, _fn=None, dateCertainty='announced each year', whatItMarks=w))

TITLES = {x['id']: x['title'] for x in json.load(open('C:/Users/garyb/Projects/one-dsd-web-consult/lib/content/community-design-data.json', encoding='utf-8'))}
entries = []
for e in E:
    fn = e.pop('_fn')
    dates = []
    for y in YEARS:
        if fn is None:
            dates.append(dict(year=y, date=None, source='Not yet announced or not yet checked against an opened announcement'))
            continue
        d, src = fn(y)
        dates.append(dict(year=y, date=d.isoformat() if d else None, source=src or 'No date found by the calculation'))
    e['dates'] = dates
    e['howCelebratedInMinnesota'] = None
    e['minnesotaEvents'] = []
    e['workplaceNote'] = None
    e['sources'] = sorted({x['source'] for x in dates})
    e['briefLinks'] = [dict(community=c, title=TITLES.get(c, c), url=f'https://one-dsd-people-access-culture-production.up.railway.app/minnesota-communities/{c}') for c in e['communities']]
    e['id'] = '-'.join(''.join(ch for ch in e['name'].lower() if ch.isalnum() or ch == ' ').split())
    entries.append(e)

order = ['id','name','alsoKnownAs','communities','briefLinks','kind','dateRule','dates','dateCertainty','whatItMarks','howCelebratedInMinnesota','minnesotaEvents','workplaceNote','sources']
entries = [{k: e[k] for k in order} for e in entries]
json.dump(dict(generated='2026-10-30', note='Dates calculated locally; Minnesota celebration details, events and workplace notes are not yet researched.', entries=entries), open(OUT + '/cultural-calendar.json', 'w'), ensure_ascii=False, indent=2)

# ICS: only fixed or calculated dates
def esc(s): return s.replace('\\','\\\\').replace(';', chr(92)+';').replace(',','\\,').replace('\n','\\n')
lines = ['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//community-360-research//cultural-calendar//EN','CALSCALE:GREGORIAN','X-WR-CALNAME:Cultural calendar (calculated dates)']
for e in entries:
    if e['dateCertainty'] not in ('fixed', 'calculated'): continue
    for d in e['dates']:
        if not d['date']: continue
        day = dt.date.fromisoformat(d['date'])
        lines += ['BEGIN:VEVENT', f"UID:{e['id']}-{d['year']}@community-360-research", 'DTSTAMP:20261030T000000Z',
                  f"DTSTART;VALUE=DATE:{day:%Y%m%d}", f"DTEND;VALUE=DATE:{day + dt.timedelta(days=1):%Y%m%d}",
                  f"SUMMARY:{esc(e['name'])}", f"DESCRIPTION:{esc(e['whatItMarks'] + ' Date rule: ' + e['dateRule'] + ' Source: ' + d['source'])}",
                  f"CATEGORIES:{esc(e['kind'])}", 'TRANSP:TRANSPARENT', 'END:VEVENT']
lines.append('END:VCALENDAR')
open(OUT + '/cultural-calendar.ics', 'w').write('\r\n'.join(lines) + '\r\n')

# Month view
md = ['# Cultural calendar by month, 2026 to 2028', '',
      'Dates below are calculated. Where an Islamic date depends on the moon, it is marked "about": the actual day is set by each mosque from moon sighting or its chosen calculation, and can be a day later or earlier. Celebrations whose dates are announced each year are listed at the end.', '']
rows = []
for e in entries:
    for d in e['dates']:
        if d['date']: rows.append((d['date'], e))
rows.sort(key=lambda r: (r[0], r[1]['name']))
cur = None
for date, e in rows:
    day = dt.date.fromisoformat(date)
    key = f'{day:%B %Y}'
    if key != cur:
        md += ['', f'## {key}', '']; cur = key
    approx = 'about ' if e['dateCertainty'] not in ('fixed', 'calculated', 'announced each year') else ''
    links = ', '.join(f"[{b['title']}]({b['url']})" for b in e['briefLinks'])
    md.append(f"- {approx}{day:%A, %B} {day.day}: **{e['name']}**. {e['whatItMarks']} Briefs: {links}")
md += ['', '## Dates announced each year', '']
for e in entries:
    if all(not d['date'] for d in e['dates']):
        md.append(f"- **{e['name']}** ({', '.join(e['communities'])}): {e['dateRule']}")
open(OUT + '/calendar-by-month.md', 'w').write('\n'.join(md) + '\n')
print(len(entries), 'entries;', sum(1 for l in lines if l == 'BEGIN:VEVENT'), 'ics events')
for e in entries:
    miss = [d['year'] for d in e['dates'] if not d['date']]
    if miss and e['dateCertainty'] != 'announced each year': print('MISSING', e['name'], miss)
