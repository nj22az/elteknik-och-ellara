# 1 Elsäkerhet, stötar, elens verkningar

Du står vid startskåpet. Det här kapitlet är stötväg. Hur du gör anläggningen spänningslös, och hur du dokumenterar jobbet mot befälhavaren, är senare kapitel. Nödström, EX och landström är appendix.

---

## 1.0 Innan du tar i något

Luckan är inte en arbetsplats förrän du har pekat ut var strömmen går genom dig om du tar fel. Skåpstomme och skrov är metall. Fukt på luckans undersida gör kroppen till en bättre ledare.

**Varning.** Boken ersätter inte fartygets ritning, klass eller flagga. «Jag kan anläggningen» tar inte bort spänningen. En JFB du minns från land sitter ofta inte här.

**Stopp.** Ingen hand mot stomme som första steg. Ingen mätning på misstänkt spänningssatt krets utan bedömd väg. Här räcker: *varför* du inte börjar. Själva frånskiljningen kommer i kapitel 2.

---

## 1.1 Föreslagen regel

El ombord ska vara gjord och monterad så att risken för stöt, brand, kortslutning och explosion blir så liten som det går. Det är ett skall, inte ett tips.

**Källnivå: funktionskrav (skall).** TSFS 2017:26 5 kap. 5 §, parafras. Inte avskrift.

**Inte skall i den här rutan**

- «Så här görs kontroll» är vägledning.
- Allmänna råd under 5 § (jordning av berörbara metalldelar, extra försiktighet med bärbar utrustning i trånga eller fuktiga utrymmen) är råd.
- Klenspänning i upplysningstexten är upplysning, inte 5 §-skall.

**Elektrikerspår.** Elinstallationsreglerna från Elsäkerhetsverket styr i allmänhet inte el ombord. Källa: Transportstyrelsens webb, prop. 2015/16:163 och Elsäkerhetsverkets FAQ. Inte upphävda ELSÄK-FS 2008:1. Undantag: EMC, ELSÄK-FS 2016:3.

**Maskinspår.** Funktionskravet sitter på installationen, inte på att du känner motorn. Du bedömer stötväg innan du gör luckan till din arbetsplats.

---

## 1.2 Vad det betyder i jobbet

**Var.** Pannrum eller maskin. Barlastpump. Magnetventil. Fukt. Inte kaj, inte EX-zon, inte nödgenerator.

**Vem.** Den som ska röra komponenten pekar stötväg först. Befälhavaren bär arbetsmiljön. Rederiet äger SMS. ELSÄK-auktorisation räcker inte ensam.

**Stöt, kort.** Ström genom kroppen. In och ut, ofta skrov. Fukt gör höljet till ledare. Verkningar på G-nivå: kramp, du släpper inte, hjärta. Därför chansar du inte. På höjd: stöten dödar inte alltid. Fallet gör det.

**Två källor, håll isär.** Transportstyrelsens olyckor-sida (2025-01-24) talar om slitage, flexkabel och att rutinerna ska ligga i SMS. Den namnger inte det här fallet. SHK 2024:04 är den namngivna rapporten. Blanda inte ihop dem.

**Landreflex som är fel.** JFB plus PE. Ombord är personskyddet oftast inte JFB. Jordfelsövervakning larmar. Den slår inte ifrån. Den ser bara det nät den sitter på.

**Maskinreflex som är fel.** Det läcker vatten, händerna först. Pumpen går, alltså är ventilen säker. Felen i det genomgångna fallet rörde inte driften. Därför tyst.

**SMS i det här kapitlet** (inte isolationsrutin, den övas i kapitel 2):

1. Räkna inte med JFB i isolerat huvudnät. Räkna med IR-vakt. Källa: olyckor-sidan; allmänna råd till 5 §.
2. Packning och kåpa tillbaka efter öppning. Avledning, ingen TS-rubrik. Källa: olyckor-sidan.
3. Sidokretsar utanför IR-vakt. Källa: SHK 2024:04.
4. Efter stöt: sjukvård iland. Källa: SHK 2024:04.

**Figur 1.1.** Magnetventil. Packning saknas mellan kontakt och spole. Ingen PE. Stötväg: hölje, hand, skrov. IR-vakt på huvudnätet ser inte den lokalt jordade sidokretsen. Märk packning saknas, ingen PE, skrov, IR-vakt, sidokrets. Inte «den röda ledaren». Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in.

Olyckor-sida: https://www.transportstyrelsen.se/sv/sjofart/aktuell-information/olyckor-relaterad-till-elinstallationer-ombord/

---

## 1.3 Genomgånget fel — SHK 2024:04 (STENA GERMANICA)

Rapport: SHK 2024:04 (S-150/22), STENA GERMANICA. Händelse 27 juni 2022, ny stöt 14 juli. Fartygsingenjör livlös vid barlastpump i pannrum. Kollega söker senare vattenläckage vid samma pump, böjer sig, kraftig stöt från våt magnetventil.

**Flera fel samtidigt** (parafras av rapporten, inte bilaga):

- Packning mellan kontakt och spole saknades.
- Ingen skyddsjordning.
- Inkommande kablar skiftade. Ventilen spänningssatt så länge pumpen gick.
- Kretsen lokalt jordad (TT), utanför det isolationsövervakade nätet. IR-vakten var tyst. Lokalt jordat mot skrov kan ge höga felströmmar.
- Felen påverkade inte driften. Ingen indikation.

Bakom: elarbete utan tillräcklig kunskap om fartygets el. Brister kan ha funnits redan vid nybygge. SHK till Transportstyrelsen: bara den med kunskap om el *och* fartygets elsystem ska göra elarbetet.

**Fel landreflex.** JFB hade löst. IR-vakten på huvudnätet hade visat. **Fel maskinreflex.** Läckage är mekanik. Ventilen är bara en slang.

**Rätt kedja**

1. Peka stötväg: hölje, våt hand, skrov.
2. Tre fel som måste samverka: packning, jord, sidokrets utanför IR.
3. SMS hade velat: packning åter, jord, och att sidokretsen antingen övervakas eller behandlas som spänningssatt.
4. Efter stöt: sjukvård iland. Inte «skaka av det».

Här räcker att du *ser* varför IR-vakten inte räddade dem. Frånskiljning är kapitel 2.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| Läckage vid pumpen | Peka stötväg hölje, hand, skrov | Våt magnetventil kan vara spänningssatt | Känn efter med händerna |
| Pumpen går, IR tyst | Fråga vilket nät ventilen sitter på | Sidokrets utanför IR, lokalt jordad | «Huvudnätets IR tar det» |
| Packning saknas vid spolen | Stopp. Behandla höljet som spänningssatt | Öppen kapsling, ingen täthet | «Den har alltid sett ut så» |
| Ingen PE på ventilen | Stopp | Ingen skyddsjord | Lita på JFB |

---

## 1.4 Lab B — arbetsorder

**Fartygstyp.** Lastfartyg, stål. Inte namngivet fartyg på biljetten.

**Utrymme.** Pannrum. Barlastpump. Magnetventil. Foto eller uppställning med tydlig packning, jord, och en krets märkt «utanför IR».

**Felanmälan.** «Det läcker vid pumpen, känn efter var.»

**Förutsättning.** Bedömning på papper eller foto. Inte losskoppling. Ingen landkabel. Ingen nödstart. Vatten i scenariot är demo, inte ström på elev.

**Verktyg.** Ögon, penna, ritning eller foto. Spänningsprovare bara om läraren sagt att uppställningen är iordning.

**G, godkänt**

1. Pekar stötväg in och ut: hölje, kropp, skrov.
2. Namnger minst två av: saknad packning, saknad skyddsjord, krets utanför IR-vakt.
3. Säger att ELSÄK och JFB inte är skyddet här.

**VG, godkänt.** G plus skriftligt: varför IR-vakten var tyst; vad du gör innan beröring och varför; stöt ger sjukvård iland. Själv. Utan att någon matar orden.

**IG.** Handen mot ventil först. «Pumpen går ju.» «Huvudnätets IR tar det.» «JFB tar det.» «ELSÄK räcker.»

**Elektrikerspår i labbet.** Tvinga fram skrov som utväg, inte PE. Tvinga fram att IR inte ser sidokretsen.

**Maskinspår i labbet.** Läckagesökning är elarbete när komponenten kan vara spänningssatt. Inte slangarbete.

---

## 1.5 Dokumentation

Inte intyg mot befälhavaren. Inte TS-blankett.

```
LABBPROTOKOLL B — stötväg
Namn:
Datum:
Utrymme / komponent:
Utpekad stötväg (hölje / kropp / skrov):
Två fel (packning / jord / utanför IR):
ELSÄK/JFB är inte skyddet här: ja
VG — varför IR var tyst:
VG — åtgärd innan beröring, och varför:
VG — efter stöt:
```

G: namn, stötväg, två fel, ELSÄK/JFB-punkten. VG: samma plus de tre raderna, i kursmappen.

LIA: samma pekövning på riktig utrustning under handledare. Du frånskiljer inte själv förrän kapitel 2 är gjort.

---

## Produktionsnot, kap. 1

1.0–1.1 står (stopp före luckan, 5 kap. 5 § parafras, ELSÄK-hål). 1.2–1.5 mot SHK 2024:04. Figur 1.1: ventil, saknad packning, stötväg mot skrov, IR blind för sidokrets. 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. Olyckor-sida och SHK hålls isär. Ingen meggerprocedur. Sen stopp.
