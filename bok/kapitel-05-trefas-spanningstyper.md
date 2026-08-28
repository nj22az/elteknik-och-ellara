# 5 Trefas, system och spänningstyper ombord

Kapitel 4 var enfas rms. Det här kapitlet är trefas som begrepp: linje mot fas, tre ledare, tre spänningstyper kursen redan låst. Inte en IEC-matris. Inte 440 V-mätning. Inte landström. Inte en ny labbdag.

---

## 5.0 Innan du tar i något

Känn igen vilken spänning du står vid. 440 V-tavla: titta, rör inte, utan att värden isolerat och gett tillstånd. Skrov är inte nolla hemma.

**Varning.** Fas mot skrov som om det vore PE är fel referens och kan vara stöt. DC-läge på trefas ljuger, samma fel som kapitel 4. Den här övningen är papper, foto och look-not-touch. Inte live-wiring.

**Stopp.** Inga prober på MSB. Ingen 80005. Ingen påhittad spänningstabell. Ingen «440 är bara lite mer än 400, jag mäter».

---

## 5.1 Föreslagen regel

Känn igen vilken spänning du står vid. Trefas är linje mellan faser, inte tre lösa enfas mot skrov. 440 V-tavla rör du inte utan att värden isolerat och gett tillstånd. Mät inte trefas som DC.

**Källnivå: skall.** TSFS 2017:26 5 kap. 5 §, parafras. Minimera elchock och kortslutning. Inte avskrift. Här: fel referens (fas mot skrov som nolla) och fel läge (DC på trefas) *är* den risk 5 § vill att du minimerar.

**Utförande.** Fackmässigt, 2 kap. 6 §. Isolation är kapitel 2. Enfas rms är kapitel 4. DC-område är kapitel 3. Labbdag: 440 V är look-not-touch utan isolerat tillstånd. Elever live-wirar inte fartyg.

**Inte skall i den här rutan**

- Linje \(U_L = U_f\sqrt{3}\) på symmetrisk stjärna är ellära, inte TSFS-paragraf.
- Namnen 24 V DC, 230 V enfas, 400/440 V trefas är kursens låsta begrepp. Inte en IEC-tabell.
- Klenspänning runt 50 V är upplysning / allmänna råd, inte 5 §-skall.
- 5 kap. 1–4 och 6–7 § (nöd, batteri, landnät) undervisas inte här.

**Elektrikerspår.** Skrov är inte N. Inte lägenhetens tre faser mot nolla. Inte JFB som bevis. 440 V ombord är look-not-touch.

**Maskinspår.** 440 V är inte ett rum. Det är tre spänningar. Linje mot fas innan handen. DMM-läge från kapitel 3 och 4 gäller fortfarande.

---

## 5.2 Vad det betyder i jobbet

**Var.** Foto av tavla. Enlinje. Skrov som referensbegrepp. Inte inne i 440 V-fält utan värd.

**Vem.** Eleven namnger systemet. Värden äger luckan.

**Tre spänningstyper** (låsta begrepp, ingen IEC-matris)

- **24 V DC** — styr och håll, batteri. Kapitel 3.
- **230 V enfas** — inredning, rms. Kapitel 4. Inte lägenhetens TN bara för att talet är 230.
- **400/440 V trefas** — maskiner. Linje mellan faser. 440 V på tavlan: look-not-touch.

**Linje mot fas.** Linje = mellan två faser. Fas = en fas mot systemets nolla *om den finns*. Ombord saknas ofta den nolla du är van vid. Skrov är inte N. Tre ledare till motorn räcker för trefasmaskin.

**Varför trefas till maskiner.** Jämnare effekt. Motor som begrepp, utan att göra kapitel 6. Inte «tre enfas i samma rör».

**Landreflex som är fel.** Mät fas mot PE eller N.

**Maskinreflex som är fel.** 440 är rummet. DMM på DC. En fas mot skrov.

**Figur 5.1.** Tre ledare till motor, linje mellan L1 och L2, skrov inte N. Tre rutor: 24 V DC, 230 V enfas, 400/440 V trefas. Stängd 440 V-tavla, look-not-touch. Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in. Ingen IEC-matris.

---

## 5.3 Genomgånget fel: fas mot skrov, DC-läge, tre enfas

**Symptom.** Elektriker ska «kolla 440». Mäter en fas mot skrov som hemma mot PE. Får ett tal som inte är linje, utgår från nolla. Ingenjör: «tre faser, tre enfas, mät en.» DMM i DC-läge kvar från 24 V.

**Räkning som saknades.** Linje är inte fas. Tre ledare. rms från kapitel 4. DC-läge ljuger på AC.

**Fel landreflex.** Skrov = N/PE. **Fel maskinreflex.** Trefas = tre uttag.

**Rätt kedja**

1. Namnge systemet: 24 V DC, 230 V enfas, eller 400/440 V trefas.
2. Linje mellan faser. Inte mot skrov som nolla.
3. AC-läge.
4. 440 V-tavla: titta.
5. Mätning bara på isolerad tränare eller död tavla, enligt labbdagen som redan finns.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| Fas mot skrov, «nolla hemma» | Linje mellan två faser | Skrov är inte N | PE-tänk |
| «Tre faser, tre enfas» | Tre ledare, en maskin | Fel modell | Mäta en fas som uttag |
| DMM i DC på 440-begrepp | AC-läge, sedan titta | Kvar från 24 V | Tro på noll |
| «Bara lite mer än 400, jag mäter» | Look-not-touch | Ingen isolation | Prober på MSB |
| Lucka upp för att se | Värden äger luckan | Rumstänk | Live-wiring |

---

## 5.4 Distansövning — papper och foto

Inte ny labbdag. Classroom vecka 5.

**Ticket.** Enlinje med 24 V DC, 230 V enfas, 400/440 V trefas märkta. Foto: 440 V-tavla, lucka stängd. Schema: tre ledare till motor.

**G, godkänt**

1. Pekar linje mot fas på schemat.
2. Namnger de tre låsta spänningstyperna på enlinjen.
3. En mening varför maskinen har tre ledare.
4. Foto av 440 V: look-not-touch.

**VG, godkänt.** Varför fas mot skrov inte är nolla hemma. Varför DC-läge på trefas är fel. Kopplar till 5 §: elchock eller kort.

**IG.** «Tre enfas.» Mätplan fas mot skrov. «Bara lite mer än 400, jag mäter.»

**Varvsdag.** Samma look-not-touch som redan ligger i labbdagen. 440 V-tavla: visning bakom värden, lucka stängd om värden inte öppnar och står kvar. Ingen live-wiring. Ingen DMM på MSB. G: pekar rätt tavla och spänningstyp från däck utan att röra. VG: motiverar varför proberna stannar i fickan.

**Elektrikerspår i övningen.** Skrov är inte N.

**Maskinspår i övningen.** 440 V är tre spänningar, inte ett rum.

---

## 5.5 Dokumentation

Inte TS-blankett. Inte IEC-tabell. Inte intyg till befälhavaren.

```
PROTOKOLL — spänningstyper ombord
Namn:
Datum:
24 V DC pekad: ja / nej
230 V enfas pekad: ja / nej
400/440 V trefas pekad: ja / nej
Linje vs fas (en mening):
440 V = look-not-touch: ja
Skrov är inte N: ja
VG — fas–skrov:
VG — DC-läge på trefas:
Varvsdag: pekade tavla, rörde inte:
```

G: namn, tre spänningstyper, linje mot fas i en mening, 440 = look-not-touch. VG: plus riskmening fas–skrov och DC på trefas. Varvsdag: samma lapp, ingen mätning på 440.

---

## Produktionsnot, kap. 5

Fem rutor, sen stopp. Figur 5.1: tre ledare plus linje mot fas; tre spänningsrutor; stängd 440-tavla. 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. Ingen IEC-matris. Inte 2024:58. Inte 80005. Inte Germanica. Inte ny labbdag. Kap. 4 orörd.
