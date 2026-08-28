# 3 DC-kretsar: mätning och beräkning

Kapitel 1 var stötväg. Kapitel 2 var frånskiljning. Det här kapitlet är resistiv DC: räkna slingan, sedan mät på 24 V / klenspänning. Inte trefas. Inte 440 V. Inte en ny labbdag. Isolation på avställd *fartygs*grupp är kapitel 2, inte den här övningens plats.

---

## 3.0 Innan du tar i något

Räkna I innan du klämmer på. Välj volt eller ampere medvetet. Ström i serie. Spänning parallellt. Ohm bara spänningslöst.

**Varning.** En DMM på fel område *är* en kortslutning. Amperemeter över last eller batteri tar säkring och mätare. Den här övningen är ELV-tränare. Inte live huvudtavla.

**Stopp.** Ingen mätning på MSB. Ingen ohm på spänningssatt. Ingen «det går väl» med polaritet. Ingen tång runt en ledare som om den visade volt.

---

## 3.1 Föreslagen regel

Mät så att du inte gör kortslutning eller stöt av mätningen. Rätt funktion på mätaren, rätt polaritet, ström i serie, spänning över. Räkna slingan innan du kopplar.

**Källnivå: skall (funktionskrav).** TSFS 2017:26 5 kap. 5 §, parafras. El ska vara gjord så att kortslutning och elchock minimeras. Inte avskrift. Här: fel område på DMM *är* kortslutningen 5 § vill att du minimerar. Det är inte Ohms lag som lagtext.

**Utförande.** Fackmässigt, 2 kap. 6 §. Isolation före arbete på avställd grupp är kapitel 2. Den här lektionen mäter på avsedd ELV-tränare, inte på live huvudtavla.

**Inte skall i den här rutan**

- Ohm, serie, parallell som formler är ellära, inte TSFS-paragraf.
- 1 MΩ är upplysning i kapitel 2. Inte DC-labbgräns här.
- Mätning på MSB / 440 V är förbjuden i kursen utan värdtillstånd. Inte ett labb.
- Allmänna råd: varje krets skydd mot kortslutning och överlast. Bakgrund, inte Ohm-tal.

**Elektrikerspår.** Minus är inte PE. Skrov som retur är inte PE-skenan hemma. Mätning på fartygstavla utan isolation är kapitel 2-fel, inte den här övningen.

**Maskinspår.** Räkna I innan du klämmer på. Polaritet och område är ett val, inte «den visar något».

---

## 3.2 Vad det betyder i jobbet

**Var.** 24 V / klenspänning. Övningskort. Batteri. Inte 440 V, inte kaj, inte trefas.

**Vem.** Den som mäter väljer område och polaritet. På varvsdagen äger värd-elektrikern vilken tränare som får mätas.

**Räkna först.** Serie: samma I, U delas. Parallell: samma U, I delas. \(R = U/I\). Avläsning mot räkning. Stämmer de inte: mätfel eller fel krets. Inte «ungefär».

**Mät**

- Spänning: parallellt över komponenten, volt-område, rätt polaritet. Röd mot plus på DC.
- Ström: bryt slingan, mätare i serie, ström-område. Tångamperemeter är inte voltmeter.
- Resistans: spänningslöst, ohm-område. Inte ohm på spänningssatt.

**Landreflex som är fel.** Tång runt plus «som ström hemma» och läsa det som volt. Minus mot PE.

**Maskinreflex som är fel.** Koppla på och se vad som händer. Ingen slinga räknad. «24 V tål allt.»

**Grind från kapitel 2.** Den här övningen är ELV-tränare. Avställd fartygsgrupp: isolation först. Inte DC-räkning på spänningssatt tavla.

**Figur 3.1.** Vänster: serie mot parallell, 24 V. Höger: DMM rätt volt parallellt över last, mot fel ampere över last (kortslutning). Märk serie, parallell, volt parallellt, ampere i serie. Inte «den röda ledaren» som färgkod. Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in.

---

## 3.3 Genomgånget fel: ampere över last, polaritet mot skrov

**Symptom.** Ingenjör ska kolla 24 V-matning till en magnetventil. Sätter DMM på strömområde och mäter *över* polerna. Säkring och mätare dör. Elektrikern i rummet har polaritet baklänges och skyller på «skrovet som nolla».

**Första räkning som skulle gjorts.** Matning 24 V, last till exempel 48 Ω. \(I = U/R = 24/48 = 0{,}5\,\mathrm{A}\). Ström mäts i serie, inte som volt över.

**Fel landreflex.** Tång eller strömområde «det är ju bara att mäta». Minus mot PE. **Fel maskinreflex.** «24 V tål allt.» Ingen I räknad.

**Rätt kedja**

1. Räkna I.
2. Välj volt eller ampere medvetet.
3. Polaritet. Röd mot plus. Minus är inte skrov-som-nolla.
4. Spänning parallellt. Ström i serie.
5. Jämför med räkning.
6. Fel område är kortslutningsrisk. Det är 5 § i jobbet, inte Ohms lag som lag.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| DMM på A, pinnar över 24 V | Räkna I. Byt till volt eller bryt slingan | Ampere över last = kort | «Bara mäta» |
| Polaritet baklänges, skyller på skrov | Röd mot plus | Minus är inte nolla mot skrov | PE-tänk |
| Tång runt ledare, läser «volt» | Volt parallellt, tång är ström | Fel storhet | Tång som voltmeter |
| «Provar bara», ingen räkning | Räkna U, I, R först | Ingen slinga | Koppla och se |
| Avläsning stämmer inte med räkning | Kolla område, polaritet, krets | Mätfel | «Ungefär» |

---

## 3.4 Distansövning — papper och foto

Inte ny labbdag. Classroom vecka 3. Händer på DMM ligger på den varvsdag som redan finns, isolerad ELV-tränare.

**Ticket.** Schema serie (två R) och parallell (två R), U given. Foto: DMM i volt-läge, avläsning. Foto: DMM i ampere-läge, felkopplad över last, märkt övning.

**G, godkänt**

1. Räknar I och U-delar i serie, I-delar i parallell.
2. Säger vilken bild som är rätt voltmätning.
3. Pekar ut den felkopplade strömbilden och varför den är kortslutning.
4. Polaritet: röd mot plus på DC.

**VG, godkänt.** En mening risk: fel område, parallell över last. Vad 5 § velat att du minimerade. Instrumentval motiverat.

**IG.** «Tången visar volt.» Polaritet egal. Ingen räkning.

**Varvsdag.** Samma DMM-station som redan ligger i labbdagen. Isolerad ELV-tränare eller förberedd klenspänning. Inte live MSB. Inte 440 V. G: rätt DC-värde plus enkel beräkning. VG: samband, eget mätfel, instrumentval. Underkänt: mätning på huvudtavla.

**Elektrikerspår i övningen.** Minus är inte PE.

**Maskinspår i övningen.** Räkna I innan du klämmer på.

---

## 3.5 Dokumentation

Inte TS-blankett. Inte intyg till befälhavaren.

```
MÄTPROTOKOLL DC — resistiv krets
Namn:
Datum:
Schema (serie / parallell):
Given U:
Räknat I:
Räknat U-delar / I-delar:
Avläsning DMM:
Område (V / A / Ω):
Polaritet (röd mot plus): ja / nej
Volt parallellt / ström i serie: 
Fel ampere över last utpekad: ja
VG — riskmening (fel område / kortslutning):
Varvsdag ELV-tränare: värde / beräkning:
```

G: namn, schema, räknade värden, avläsning, polaritet, område. VG: plus riskmening. Varvsdag: samma lapp på ELV-tränaren.

---

## Produktionsnot, kap. 3

Fem rutor, sen stopp. Figur 3.1: serie mot parallell; DMM rätt volt mot fel ampere över last. 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. 5 kap. 5 § som kortslutningsrisk vid mätfel, inte som Ohms lag. 24 V / ELV. Inte trefas. Inte 2024:58. Inte Germanica. Inte ny labbdag. 1 MΩ är inte DC-gräns.
