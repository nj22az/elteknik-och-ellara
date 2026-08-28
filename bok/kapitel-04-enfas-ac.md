# 4 Enfas AC: mätning och beräkning

Kapitel 3 var resistiv DC. Det här kapitlet är enfas AC: rms mot topp, räkna slingan, läs DMM i AC-läge. Inte trefas. Inte 440 V. Inte en ny labbdag. Isolation på avställd fartygsgrupp är kapitel 2.

---

## 4.0 Innan du tar i något

«230 V» är rms. Toppen på sinus ligger runt 325 V. DC-läge på AC kan visa nära noll. Det är inte bevisad spänningslöshet.

**Varning.** Tror du att det är av för att DC-läget visade noll, tar du i en spänningssatt krets. Det är stöt- och kortslutningsrisk. Den här övningen är papper, ELV eller död/isolerad tränare. Inte live huvudtavla.

**Stopp.** Ingen mätning på MSB. Ingen 440 V. Ingen ampere över källan. Ingen «24 V tål allt» mot 230 V.

---

## 4.1 Föreslagen regel

Mät enfas så att mätningen inte blir stöt eller kort. AC-spänning läses som rms i AC-läge. Räkna slingan. Inte DC-område på AC. Inte live huvudtavla.

**Källnivå: skall.** TSFS 2017:26 5 kap. 5 §, parafras. Minimera elchock och kortslutning. Inte avskrift. Här: DC-läge på AC som visar noll, och du tror det är av, *är* den stötrisk 5 § vill att du minimerar. Det är inte Ohms lag som lagtext.

**Utförande.** Fackmässigt, 2 kap. 6 §. Isolation på avställd fartygsgrupp är kapitel 2. Den här lektionen mäter på papper, ELV eller död/isolerad tränare. Inte 440 V.

**Inte skall i den här rutan**

- rms, topp, \(U_{\mathrm{topp}} \approx U_{\mathrm{rms}}\sqrt{2}\) på sinus är ellära, inte TSFS-paragraf.
- Klenspänning runt 50 V AC är upplysning / allmänna råd, inte 5 §-skall-siffra.
- 1 MΩ är upplysning i kapitel 2. Inte AC-labbgräns här.
- Trefas och fasföljd är kapitel 5.

**Elektrikerspår.** 230 V ombord är inte lägenhetens TN. Referens kan vara skrov, inte PE-nolla hemma. Isolation först. Inte «det sitter JFB».

**Maskinspår.** rms innan du klämmer på. AC-läge är ett val, inte «den visar något». Uttaget i hytten är inte 24 V i maskin.

---

## 4.2 Vad det betyder i jobbet

**Var.** Resistiv enfas. ELV-tränare eller död övningstavla. Inredningsuttag som begrepp, inte live fartygsuttag i den här övningen.

**Vem.** Den som mäter väljer AC-läge. På varvsdagen äger värd-elektrikern tränaren.

**Räkna.** Resistiv last: \(I = U_{\mathrm{rms}}/R\). Topp är högre än det DMM visar i AC-läge. «230 V» är rms. Toppen ligger runt 325 V på sinus. Därför är «24 V tål allt» fel när du möter 230 V.

**Mät**

- DMM AC V parallellt över last.
- Ström: AC-ström i serie, eller tång kring *en* ledare. Inte som volt.
- Inte DC-läge på AC. Visningen ljuger, eller mätaren far illa.
- Polaritet på AC: inte batteriplus. Probes i volt-läge. Inte «hitta nollan som PE».

**Landreflex som är fel.** 230 V plus JFB som hemma.

**Maskinreflex som är fel.** Uttaget i hytt är ofarligt som 24 V.

**Grind.** Kapitel 2 om det är avställd fartygsgrupp. Kapitel 3 polaritet och område på DC. Här: AC-läge plus rms.

**Figur 4.1.** Vänster: sinus, rms 230 V mot topp cirka 325 V. Höger: samma krets, DMM i AC-läge mot DMM i DC-läge. DC-läget nära noll är inte bevisad död. Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in.

---

## 4.3 Genomgånget fel: DMM kvar i DC efter 24 V

**Symptom.** Ingenjör ska kolla 230 V-enfas till värmare. Lämnar DMM i DC-läge, kvar från 24 V-batteri. Visar nära noll eller skräp. «Det är av.» Elektriker mäter mot skrov som om det vore PE och utgår från JFB.

**Räkning som saknades.** 230 V rms. Last till exempel 1 kΩ. \(I \approx 230/1000 = 0{,}23\,\mathrm{A}\). Topp \(\approx 230\sqrt{2} \approx 325\,\mathrm{V}\). Isolation och område ska tåla det. Inte 24 V-tänk.

**Fel landreflex.** DC-läge «funkar ju på allt». **Fel maskinreflex.** «230 i hytten är som 24 i maskin.»

**Rätt kedja**

1. AC-läge.
2. rms i räkningen.
3. Volt över. Ström i serie.
4. Jämför avläsning.
5. Noll i DC-läge på AC är inte bevisad spänningslöshet. Tvåpol i rätt läge, kapitel 2.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| DMM i DC, visar ~0 på 230 V-enfas | Byt till AC V | Fel område, inte dött | «Det är av» |
| Kvar i DC efter 24 V-jobb | Kolla läget innan du mäter AC | Vane från batteri | Samma läge «på allt» |
| «24 V tål allt» mot 230 V | rms 230 V, topp ~325 V | Fel spänningstänk | Klämma på |
| Mäter mot skrov som PE | AC V över last | TN-vana | JFB som bevis |
| Ampere över källan | Ström i serie | Samma fel som kapitel 3 | Kort via mätaren |

---

## 4.4 Distansövning — papper och foto

Inte ny labbdag. Classroom vecka 4. Händer på DMM ligger på den varvsdag som redan finns.

**Ticket.** Sinusfigur rms mot topp. Resistiv enfas med \(U_{\mathrm{rms}}\) och R. Foto: DMM AC V med avläsning. Foto: DMM DC V på samma AC-övning, märkt fel.

**G, godkänt**

1. Anger rms och ungefär topp.
2. Räknar I på resistiv enfas.
3. Väljer AC-bilden som rätt mätning.
4. En mening: DC-bilden är fel läge.

**VG, godkänt.** Risk: DC-läge på AC ger falskt «av» eller skadar. Kopplar till 5 §: elchock eller kort om du tror det är dött.

**IG.** «24 V tål allt.» Läser AC som DC. Ingen skillnad rms/topp.

**Varvsdag.** Samma DMM-station / död tavla som redan ligger i labbdagen. Isolerad tränare eller död tavla. Enfas AC om värden spänningssatt övningstavlan. Annars papper plus ELV och AC som begrepp. Inte live MSB. Inte 440 V. G: rätt AC-avläsning plus enkel beräkning. VG: DC-läge som medvetet underkänt exempel. Läraren visar. Eleven gör det inte på spänningssatt.

**Elektrikerspår i övningen.** 230 V ombord är inte lägenhet.

**Maskinspår i övningen.** rms innan du klämmer på.

---

## 4.5 Dokumentation

Inte TS-blankett. Inte intyg till befälhavaren.

```
MÄTPROTOKOLL AC — resistiv enfas
Namn:
Datum:
U_rms:
U_topp (sinus, ca):
R:
Räknat I:
Avläsning DMM:
Område (AC V, inte DC):
DC-läge utpekat som fel: ja
VG — riskmening (noll i DC ≠ av):
Varvsdag tränare: AC-värde / beräkning:
```

G: namn, rms, topp, I-räkning, AC-avläsning, område AC. VG: plus riskmening DC-läge på AC. Varvsdag: samma lapp på tränaren.

---

## Produktionsnot, kap. 4

Fem rutor, sen stopp. Figur 4.1: sinus rms mot topp; DMM AC-läge mot DC-läge på samma krets. 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. 5 kap. 5 § som risk när DC-läge på AC visar noll och du tror det är av. Inte trefas. Inte 2024:58. Inte Germanica. Inte ny labbdag.
