# Sledenje SLO COVID-19

Projekt sledenja COVID zbira podatke o širjenju koronavirusa SARS-CoV-2
oz. virusa, ki povzroča COVID-19. Vključeni so podatki o številu
opravljenih testov, številu pozitivnih (okuženih) ter šteivlu in stanju
pacientov po posameznih regijah,sproti pa se trudimo dodajati tudi nove,
relevantne kategorije. 

Projekt je začel Luka Renko (@lukarenko), sedaj pa na njem aktivno dela
od N do M ljudi; gre za množican projekt, kjer lahko **vsak pomaga**
tako, da prispeva kakšen nov vir ali informacijo iz svojega okolja.
**Dodate jo kot komentar na katerokoli polje v dokumentu.**

Pokaži podatke ([*GDocs
preglednica*](https://docs.google.com/spreadsheets/d/1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY/edit#gid=702553602))
ali me pelji do APIja (CSV). 

Podatke že uporabljajo: 

Better Care - [*Covid 19 nadzorna
plošča*](https://app.powerbi.com/view?r=eyJrIjoiMWE2NGNmZWMtMjcxZC00MzkxLWIyMTUtYjExYjI2YTg4NzA0IiwidCI6IjkxMGYyNzY0LWEyZGItNGM2Mi04OGM0LWE1ZTcwYzMzNjVjNCIsImMiOjl9&nbsp;)
([*API*](https://bettercare365-my.sharepoint.com/:x:/g/personal/emilp_better_care/EeZA7U_tdFpPjftMy3X2_koBrgpHfQKQvtQMRXPmQakFNw?rtime=eJWxRL3J10g))

Razmerja okužbe/testi ([*Matjaž Lipuš - GDocs
preglednica*](https://docs.google.com/spreadsheets/d/1o9DE8PEXvEOZ0yz02JsUGNhWGx2Q11Ncq2uaY-rE-QY/edit#gid=0))

Pokažite mi surove podatke (preglednico) ali me povežite z API-jem (JSON
in CSV).

**Zakaj? **

Pravilno zbrani podatki in transparentnost sta ključna dela vsakega
odziva v javnem zdravju, zato je transparentna objava podatkov ključnega
pomena za razumevanje tega izbruha ter nujnosti ukrepov.  
NIJZ trenutno ne objavlja popolnih in dovolj strukturiranih podatkov o
številu okužb, zato jih zbiramo in dopolnjujemo iz različnih javnih
virov in jih posredujemo javnosti. 

Informacije v medijih in uradnih virih, iz katerih črpamo, so pogosto
delne, nejasne in nedosledne, zaradi tega preglednica vključuje tudi
opombe o virih in spremembah podatkov. 

**Kako urejamo statistiko:**

Statistiko urejamo praviloma ob 14:00 s podatki iz NIJZ. Če so
objavljeni vmesni podatki, začasno vnesemo te. Podatki po regijah in
starosti se včasih ne ujemajo s tistimi ob 14h (ker niso objavljeni
istočasno); dopolnjujemo in preverjamo tudi z podatki, objavljenimi v
medijih. 

**Kako urejamo posamezne primere:**

Posamezne primere spremljamo iz podatkov iz tiskovne konference in objav
medijev (link na vir).

Zabeležimo predvsem identifikacijske podatke in sledimo izvor in žarišča
(kjer je možno).

Naredimo placeholderje z minimalno informacij (Izvor - na podlagi
podatka po regijah), ki jih v naslednjih dneh dopolnjujemo.

Žarišča vodimo iz podatkov o direktnih okužbah in sumarnih podatkov NIJZ
(takrat dodamo žarišče na placeholderje).

K:žarišče, K:regija in K:kraj so kontrolne pivot tabele za validacijo
posameznih primerov.

Tukaj si lahko ogledate tudi naše [*vire
*](https://docs.google.com/spreadsheets/d/1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY/edit#gid=328677411)**[*podatkov*](https://docs.google.com/spreadsheets/d/1N1qLMoWyi3WFGhIpPFzKsFmVE0IwNP3elb_c18t2DwY/edit#gid=328677411),
ter zbirko [*povezav na ostale statistike, podatkovne vizualizacije in
zanimive objave*](#4geu807pkmre) o metodah in ukrepih, ki se nanašajo na
COVID-10 pri nas in po svetu. 

<span id="anchor"></span>Dobre prakse objave podatkov

Priporočila, katere podatke bi morali objavljati državni organi za javno
zdravje in kako.

<span id="anchor-1"></span>Pogoji uporabe

Podatki so zbrani iz virov v javni domeni in jih lahko prosto
uporabljate, urejate, predelujete ali vključujete v vse nekomercialne
vsebine ob navedbi vira - "tinyurl.com/slo-covid-19".  
Za izvoz podatkov v drugih formatih ali uporabo za vizualizacije nas
kontaktirajte na...\_\_\_\_\_???  
<span id="anchor-2"></span>

<span id="anchor-3"></span>Druge statistike, vizualizacije, simulacije

<table>
<tbody>
<tr class="odd">
<td><strong>Druge statistike, vizualizacije, simulacije</strong></td>
<td></td>
</tr>
<tr class="even">
<td>Alpaka: primerjave SLO z drugimi državami</td>
<td><a href="http://www.alpaka.si/koronavirus/"><em>http://www.alpaka.si/koronavirus/</em></a></td>
</tr>
<tr class="odd">
<td>Zemljevid okužb &amp; nadzorna plošča - SLO</td>
<td><a href="https://mediastream.si/korona.php"><em>https://mediastream.si/korona.php</em></a></td>
</tr>
<tr class="even">
<td>Zemljevid okužb&amp; nadzorna plošča - SLO (by Alenka Jelen)</td>
<td><a href="https://gdiljubljana.maps.arcgis.com/apps/opsdashboard/index.html#/1cf4f90e05984ae5a365f4838f746138"><em>https://gdiljubljana.maps.arcgis.com/apps/opsdashboard/index.html#/1cf4f90e05984ae5a365f4838f746138</em></a></td>
</tr>
<tr class="odd">
<td>CoVID 19 Worldwide Growth Rates (by Mark Handley, UCL)</td>
<td><a href="http://nrg.cs.ucl.ac.uk/mjh/covid19/"><em>http://nrg.cs.ucl.ac.uk/mjh/covid19/</em></a></td>
</tr>
<tr class="even">
<td>WHO Covid-19 World Situation Dashboard</td>
<td><a href="https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd"><em>https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd</em></a></td>
</tr>
<tr class="odd">
<td>Udomačena statistika (do 14.4.).</td>
<td><a href="https://udomacenastatistika.wordpress.com/2020/03/13/rast-koronavirusa-v-sloveniji-do-12-3-2020/"><em>https://udomacenastatistika.wordpress.com/2020/03/13/rast-koronavirusa-v-sloveniji-do-12-3-2020/</em></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Projekcija/primerjava št. primerov za SLO (Andraž Stalec)</td>
<td><a href="https://www.facebook.com/andraz.stalec/posts/10157326285444205"><em>https://www.facebook.com/andraz.stalec/posts/10157326285444205</em></a></td>
</tr>
<tr class="even">
<td>Covid-19 World Dashboard by Center for Systems Science and Engineering</td>
<td><a href="https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"><em>https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6</em></a></td>
</tr>
<tr class="odd">
<td>Worldometer</td>
<td><a href="https://www.worldometers.info/coronavirus"><em>https://www.worldometers.info/coronavirus</em></a></td>
</tr>
<tr class="even">
<td>Day Zero grafi</td>
<td><a href="https://behroozh.shinyapps.io/COVID19/"><em>https://behroozh.shinyapps.io/COVID19/</em></a></td>
</tr>
<tr class="odd">
<td>Our World in Data (Oxford)</td>
<td><a href="https://ourworldindata.org/coronavirus"><em>https://ourworldindata.org/coronavirus</em></a></td>
</tr>
<tr class="even">
<td>ECDC - European Centre for Disease Prevention and Control dataset</td>
<td><a href="https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data#__sid=js11"><em>https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data#__sid=js11</em></a></td>
</tr>
<tr class="odd">
<td>Welt.de: Alle Karten, Zahlen und Fakten zur Corona-Ausbreitung</td>
<td><a href="https://www.welt.de/vermischtes/article206504969/Coronavirus-8600-Faelle-in-Deutschland-Alle-Karten-zur-Ausbreitung.html?wtrid=socialmedia.socialflow....socialflow_twitter"><em>https://www.welt.de/vermischtes/article206504969/Coronavirus-8600-Faelle-in-Deutschland-Alle-Karten-zur-Ausbreitung.html?wtrid=socialmedia.socialflow....socialflow_twitter</em></a></td>
</tr>
<tr class="even">
<td>OECD AI Coronavirus watch</td>
<td><a href="http://coronaviruswatch.ircai.org/?country=SVN&amp;dashboard=evolution"><em>http://coronaviruswatch.ircai.org/?country=SVN&amp;dashboard=evolution</em></a></td>
</tr>
<tr class="odd">
<td>An interactive map of self-reported COVID-19 cases (by Una Larisa Pecovnik, Jan Likar, Gabrijel Persin</td>
<td><a href="https://www.covid-report.com/"><em>https://www.covid-report.com/</em></a></td>
</tr>
<tr class="even">
<td>COVID-19 Cases in Germany by state (data vs exponential model)</td>
<td><a href="https://observablehq.com/@jheer/covid-19-cases-in-germany"><em>https://observablehq.com/@jheer/covid-19-cases-in-germany</em></a></td>
</tr>
<tr class="odd">
<td>The COVID Tracking Project USA "+&amp;-"results, pending tests, and total people tested</td>
<td><a href="https://covidtracking.com/"><em>https://covidtracking.com/</em></a></td>
</tr>
<tr class="even">
<td>COVID-19 Austria (GoogleSheets by twitter.com/walterra)</td>
<td><a href="https://docs.google.com/spreadsheets/d/1f8cgShmTVmldRcNKvqWW55iLZsgmodlzU_Z8VqL7BWk/edit?ts=5e71e266#gid=0"><em>https://docs.google.com/spreadsheets/d/1f8cgShmTVmldRcNKvqWW55iLZsgmodlzU_Z8VqL7BWk/edit?ts=5e71e266#gid=0</em></a></td>
</tr>
<tr class="odd">
<td>podatki za Italijo, kjer delijo primere na intenzivno negi (terapia intensiva), bolnisnicni negi (ricoverati), ter domaca nega v izolaciji (isolamento domiciliare)</td>
<td><a href="https://lab24.ilsole24ore.com/coronavirus/"><em>https://lab24.ilsole24ore.com/coronavirus/</em></a></td>
</tr>
<tr class="even">
<td>FT: smrtnost COVID-19 po državah (The countries affected, the number of deaths and the economic impact)</td>
<td><a href="https://www.ft.com/content/a26fbf7e-48f8-11ea-aeb3-955839e06441"><em>https://www.ft.com/content/a26fbf7e-48f8-11ea-aeb3-955839e06441</em></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Podatki za Italijo (GitHub)</td>
<td><a href="https://github.com/pcm-dpc/COVID-19"><em>https://github.com/pcm-dpc/COVID-19</em></a></td>
</tr>
<tr class="odd">
<td>Network Graph Visualisation of C19 Outbreak-Singapore</td>
<td><a href="https://co.vid19.sg/cases"><em>https://co.vid19.sg/cases</em></a></td>
</tr>
<tr class="even">
<td>Nadzorna plošča COVID-19 Virus Outbreak in Singapore</td>
<td><a href="https://co.vid19.sg/"><em>https://co.vid19.sg/</em></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Simulacije,projekcije</strong></td>
<td></td>
</tr>
<tr class="odd">
<td><p>Corona transfer simulator</p>
<p>(Washington Post)</p></td>
<td><a href="https://www.washingtonpost.com/graphics/2020/world/corona-simulator/"><em>https://www.washingtonpost.com/graphics/2020/world/corona-simulator/</em></a></td>
</tr>
<tr class="even">
<td>Visualizing the spread of viruses in a population by @swizec</td>
<td><a href="https://corona-simulation.now.sh/"><em>https://corona-simulation.now.sh/</em></a></td>
</tr>
<tr class="odd">
<td>Visualizing how viruses spread in a population (by Swizec Teller)</td>
<td><a href="https://reactfordataviz.com/articles/corona-simulation/"><em>https://reactfordataviz.com/articles/corona-simulation/</em></a></td>
</tr>
<tr class="even">
<td>Outbreak - playable disease simulaton</td>
<td><a href="https://meltingasphalt.com/interactive/outbreak/"><em>https://meltingasphalt.com/interactive/outbreak/</em></a></td>
</tr>
<tr class="odd">
<td>Simulacija karantena/brez karantene za SLO (Žiga Zaplotnik)</td>
<td><a href="https://twitter.com/ZaplotnikZiga/status/1239848814879612928"><em>https://twitter.com/ZaplotnikZiga/status/1239848814879612928</em></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Ostalo</strong></td>
<td></td>
</tr>
<tr class="even">
<td>Coronavirus Tech Handbook for doctors</td>
<td><a href="https://docs.google.com/document/d/111k1L5D9TZNShV5Gr2AJ7grfuXmEx_dYXAZcNwEebQI/edit#heading=h.abb7jnjb11f1"><em>https://docs.google.com/document/d/111k1L5D9TZNShV5Gr2AJ7grfuXmEx_dYXAZcNwEebQI/edit#heading=h.abb7jnjb11f1</em></a></td>
</tr>
<tr class="odd">
<td>Can informal social distancing interventions minimize demand for antiviral treatment during a severe pandemic?</td>
<td><a href="https://bmcpublichealth.biomedcentral.com/articles/10.1186/1471-2458-13-669"><em>https://bmcpublichealth.biomedcentral.com/articles/10.1186/1471-2458-13-669</em></a></td>
</tr>
<tr class="even">
<td><p>Wuhan izkušnje (Epidemiological Characteristics and</p>
<p>Non-Pharmaceutical Intervention Effects)</p></td>
<td><a href="https://drive.google.com/file/d/14tGJF9tdv4osPhY1-fswLcSlWZJ9zx45/view?fbclid=IwAR2OB3WGkqeZ17Ugon6tD5OweGUbJMd3W4TPH5Tsi1-XHziOF6xGCrcS_ro"><em>https://drive.google.com/file/d/14tGJF9tdv4osPhY1-fswLcSlWZJ9zx45/view?fbclid=IwAR2OB3WGkqeZ17Ugon6tD5OweGUbJMd3W4TPH5Tsi1-XHziOF6xGCrcS_ro</em></a></td>
</tr>
<tr class="odd">
<td>Koronavirus v Sloveniji: Zbrani linki (Zemljevidi in statistika, Vladne in javne informacije, Skupnosti, Članki, Delo in izobraževanje, Prosti čas, APIs,..)</td>
<td><a href="https://docs.google.com/document/d/1p3eYS1nExgkZFdPuspOOO5e77N_xJ94wuxyM-lyiDwU/edit?ts=5e6d62c2#"><em>https://docs.google.com/document/d/1p3eYS1nExgkZFdPuspOOO5e77N_xJ94wuxyM-lyiDwU/edit?ts=5e6d62c2#</em></a></td>
</tr>
<tr class="even">
<td>Patient 31-The Korean clusters How coronavirus cases exploded in South Korean churches and hospitals</td>
<td><a href="https://graphics.reuters.com/CHINA-HEALTH-SOUTHKOREA-CLUSTERS/0100B5G33SB/index.html"><em>https://graphics.reuters.com/CHINA-HEALTH-SOUTHKOREA-CLUSTERS/0100B5G33SB/index.html</em></a></td>
</tr>
<tr class="odd">
<td>Chinese Clinical Guidance For COVID-19 Pneumonia Diagnosis and Treatment</td>
<td><a href="https://www.acc.org/latest-in-cardiology/articles/2020/03/17/11/22/chinese-clinical-guidance-for-covid-19-pneumonia-diagnosis-and-treatment?utm_medium=social&amp;utm_source=twitter_post&amp;utm_campaign=twitter_post"><em>https://www.acc.org/latest-in-cardiology/articles/2020/03/17/11/22/chinese-clinical-guidance-for-covid-19-pneumonia-diagnosis-and-treatment?utm_medium=social&amp;utm_source=twitter_post&amp;utm_campaign=twitter_post</em></a></td>
</tr>
<tr class="even">
<td><p>Why Singapore’s coronavirus response worked (Dale Fisher</p>
<p>Chair, Infection Control, National University Hospital, National University of Singapore)</p></td>
<td><a href="https://theconversation.com/why-singapores-coronavirus-response-worked-and-what-we-can-all-learn-134024"><em>https://theconversation.com/why-singapores-coronavirus-response-worked-and-what-we-can-all-learn-134024</em></a></td>
</tr>
<tr class="odd">
<td>Why You Must Act Now (Tomas Pueyo)</td>
<td><a href="https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca"><em>https://medium.com/@tomaspueyo/coronavirus-act-today-or-people-will-die-f4d3d9cd99ca</em></a></td>
</tr>
</tbody>
</table>
