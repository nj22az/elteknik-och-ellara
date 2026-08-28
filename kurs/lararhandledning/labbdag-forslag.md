# Labbdag — lärarkörschema

**Status: FÖRSLAG.** Inte ägarens beslut. Riktat mot Kurs Labbdag v1 (inte låst). Skelett: FM isolation + DMM, EM enklare elarbete + hållkrets. Skollabb, inte fartyg.

När ägaren kryssar v1: den här ryggraden gäller. Tills dess: förslag.

Full 1.1 (Germanica, ELSÄK, SMS utan megger) är redan distans. På dagen: 20 min pekstart, inte egen stötstation.

---

## Dagen (Kurs v1 klockslag — förslag)

| Tid | Du kör | Form |
|---|---|---|
| 08:30–08:50 | Stötväg, foto/tavla Germanica | Plenar |
| 08:50–10:20 | Station 1 Isolation (SMS-kedja + megger) | Par, du går runt |
| 10:20–10:35 | Paus | |
| 10:35–12:00 | Station 2 DMM: resistiv DC + enfas AC | Samma par |
| 12:00–12:45 | Lunch | |
| 12:45–14:15 | Station 3 Strömbrytare/uttag 230 V **eller** reserv lågspänning serie/parallell (ägaren kryssar ett) | Par |
| 14:15–14:25 | Paus | |
| 14:25–15:50 | Station 4 Hållkrets 24 V | Par |
| 15:50–16:00 | Intyg in, packa | Plenar |

Inte parallella stationer. Inte 20 händer i samma skåp. IP = kåpa/packning tillbaka på station 1 och 3, kryss på samma papper. Intyg = ett pedagogiskt papper per par, fylls löpande, lämnas 15:50. Inte TS-blankett.

Kurs v1 räknar 12–16 elever i blandade par. Elon sa 20: samma sekvens, upp till 10 par. Båda i paret ska visa momentet. Ingen åker snålskjuts.

Utrustning: boka listan i Kurs Labbdag v1. Den här handledningen är vad *du säger och rättar*, inte inköpslistan.

---

## 08:30 — vad du säger till rummet

En safety-mening, sen pekövningen:

Ingen in i skåp, ingen megger, ingen DMM på misstänkt spänningssatt, förrän *den här* kretsen är bedömd och (där stationen kräver det) isolerad. Hoppat steg = IG, inte ”vi tar det sen”.

Skolans 230 V-bänk har JFB. Säg högt: det är skola, inte fartygsnät.

**Plenar 20 min, foto/tavla:** packning, jord, krets märkt utanför IR. Felanmälan: ”Det läcker vid pumpen, känn efter var.” Inte megger.

**Till elektriker:** Leta inte JFB.
**Till ingenjör:** Läckagesökning är elarbete när komponenten kan vara spänningssatt.

**G på starten:** pekar stötväg in/ut; minst två av packning / saknad jord / krets utanför IR; ELSÄK-JFB är inte skyddet här.
**VG på starten:** en mening varför IR-vakten var tyst. (Full fyraraders 1.1-text är redan distans — jaga den inte här.)
**IG:** handen mot ventil först; ”pumpen går ju”; ”JFB tar det.”

---

## Station 1 — isolation

Kedja: från, lås/skylt, prova spänningslös, megger, protokoll. Megger mot tavlans skyddsjord *och* säg att ombord är referensen skrov/IT. **1 MΩ är upplysning, inte skall.** Under givet värde: inte spänningssätt, skriv avvikelse.

**Till elektriker:** Megga inte mot PE som hemma.
**Till ingenjör:** ”Den gick ju” är inte isolation. Du megger också. Inte titta.

**G:** följer kedjan, rätt referens, protokoll. Med handledning OK.
**VG:** kedjan själv, motiverar varje steg mot risk (fukt, sidokrets, ”den gick ju”). Mata inte orden. Hinner du inte höra båda = G, inte VG på spekulation.
**IG / stopp:** skippar från/lås/prova; megger på misstänkt spänningssatt; vill spänningssätta vid dålig isolation. Stationen stannar. Ingen station 3 utan G här.

IP-rad på papperet: kåpa/packning tillbaka.

---

## Station 2 — DMM

Resistiv DC + enfas AC. Samma par.

**Till elektriker:** Du kan mätaren. Visa att värdet hör ihop med kretsen. Dra, men låt ingenjören mäta också.
**Till ingenjör:** Kännedom om rummet är inte ett mätvärde. Välj instrument, skriv siffran, jämför med beräkning.

**G:** rätt instrument, rimligt DC, rimligt enfas-AC, enkel beräkning stämmer.
**VG:** samband serie/parallell, hittar eget mätfel, motiverar instrumentval.
**IG / stopp:** mätning på krets som inte är bedömd när labbet kräver det.

---

## Station 3 — enklare elarbete

Ägaren har kryssat **ett:** 230 V strömbrytare/uttag i befintlig gruppledning, eller reserv lågspänning serie/parallell. Inte båda som fulla pass. Isolation först (grind station 1).

**Till elektriker:** Landreflexen räcker inte. Peka FM-isolationen, hoppa inte luckan.
**Till ingenjör:** Det här är händerna. Inte ”jag vet hur den startar”.

**G (230 V):** isolation först, losskoppling/anslutning korrekt, funktionsprov, kåpa/packning tillbaka.
**VG:** självständigt, noggrant, skriftlig riskmening innan spänning.
**G (reserv lågspänning):** rätt koppling och mätning.
**VG (reserv):** förklarar samband utan hjälp.
**IG / stopp:** kopplar utan G på station 1; spänning in innan du vinkat.

---

## Station 4 — hållkrets

24 V-tränare. Schema till tavlan. Inte PLC. Inte Arduino.

**Till elektriker:** Från ritningen, inte från minnet av en landcentral.
**Till ingenjör:** Ritningen först. Inte pumplogiken.

**G:** bygger efter schema, start håller, stopp släpper.
**VG:** felsöker ett lagt fel själv från ritning och motiverar.
**IG / stopp:** spänning på öppen koppling du inte godkänt.

---

## Rättning när klockan går

Kryss på stationskortet innan paret lämnar. Inte på kvällen ur minnet. Par får G bara om *båda* visat momentet.

| Block | G | VG | IG |
|---|---|---|---|
| Start 20 min | stötväg + två fel + inte ELSÄK-JFB | en mening: varför IR var tyst | handen först / JFB / ”pumpen går” |
| 1 Isolation | kedja + värde + protokoll, med hjälp | kedjan själv från risk | hoppad isolation / megger på spänning |
| 2 DMM | rätt instrument, DC+AC, beräkning | samband + eget mätfel | mätning utan bedömd krets |
| 3 Elarbete | isolation först, korrekt, kåpa tillbaka | självständig riskmening | kopplar utan station 1 |
| 4 Hållkrets | funktion från schema | felsöker lagt fel från ritning | spänning du inte godkänt |
| Intyg (papper) | namn, vad, när, värde, packning | utomstående förstår utan att fråga | tomt / bara ena namnet |

Vid 20 personer: du matar inte VG-orden. Ett par i taget på 230 V. De andra tittar eller förbereder papper.

---

## Safety stop, hela rummet

Säg den 08:30. Upprepa före station 1 och 3.

- Hoppat säkerhetssteg = IG på den stationen.
- Dålig isolation → inte spänningssätt.
- Megger, DMM, 230 V: du vinkar. Eleven gissar inte att det är dött.
- En i paret kör, den andra tittar, sen byter ni. Inte fyra händer i skåpet.
- Vatten/fukt i 20-minutersstarten är foto, inte ström på elev.

---

## Inte den här dagen

Nödström, blackout, EX, landström/80005, TSFS 2024:58, Arduino, PLC, IP-tabell som övning (peka URL), fysisk Germanica-uppställning utöver foto, megger som egen station, SMS-blankett från rederi. LIA är separat.

Kursen ger G på labbdagen bara för blocken ovan. Resten examineras distans + LIA.

---

## LIA, en mening till klassen

Samma isolation och samma mätning under handledare ombord. Megger och losskoppling själv på LIA först när station 1 är G.

---

Ägaren ska fortfarande säga ja/nej till Kurs v1: klockslag, station 3 = 230 V eller lågspänning, megger i isolation, blandade par, att skolan kan boka utrustningen. Inte låst förrän det krysset.
