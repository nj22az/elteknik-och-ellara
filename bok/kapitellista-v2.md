# Fartygselektriker — kapitellista v2

Till Elon, 2026-08-28, Manus. 1:1 mot Kurs karta v2. Inte övergångsryggraden. Inte manuset. Inte TSFS-avskrift.

Arbetstitel tills Elon säger annat: *Fartygselektriker*. Kursen som boss: Elteknik och ellära, 45 YH-poäng, tolv moduler.

**Skrivregel (källpaket v1, låst):** parafras. Citatnivå som packat: skall / allmänna råd / kompletterande upplysningar / avledning / GAP. ELSÄK-undantaget = TS-webb + prop. 2015/16:163 + ELSÄK FAQ. Citera inte upphävda ELSÄK-FS 2008:1 som lag. TSFS 2024:58 = appendix, inte denna boks skall. Inland = TSFS 2026:20 (inte 2018:60). 1 MΩ och fartområde A–E-tider är inte skall. Återställd IP = avledning. Intyg = vår blankett till befälhavaren, ingen TS-mall.

**Prosametod (står):** H1 kapitel, H2  n.0–n.6, H3 steg, spårbox Elektriker / Maskinist, varning, genomgånget fel, labb som arbetsorder, symptomtabell där det bär, intyg-ruta i de kapitel som labbar det. Inga sidhänvisningar. Inga färgnät.

**Kap. 1 skrivs inte** förrän Kurs m1-blad landar.

---

## Tolv kapitel = m1–m12

| Kap. | Titel | p | Lab | Inte |
|---|---|---|---|---|
| 1 | Elsäkerhet, stötar, elens verkningar | 3 | B | Inte ETO, inte nödnät |
| 2 | Isolering, SMS, säkerhetsåtgärder innan arbete | 4 | A, C | Inte 1 MΩ som lag |
| 3 | DC-kretsar: mätning och beräkning | 5 | F (DC) | Inte Arduino |
| 4 | Enfas AC: mätning och beräkning | 4 | F (AC) | Inte 80005 |
| 5 | Trefas, system och komponenter, spänningstyper ombord | 4 | tavla: peka system | Inte blackout, inte anläggningsdesign |
| 6 | DC/AC-utrustning, maskiner, konstruktion och drift | 4 | visning motor/tavla | Inte nödstart, inte batterimodul |
| 7 | Eltavla / elcentral | 3 | J | Inte SOLAS-taveldjup som kärna |
| 8 | Verktyg och mätinstrument | 3 | verktygsprov | Inte RCD-test som huvudverktyg ombord |
| 9 | Ritningar, kopplingsschema, måttsättning | 4 | J + schema till hållkrets | Inte land-relationsritning som mall |
| 10 | Enklare styrkrets / hållkrets | 3 | G | Inte PLC-kurs |
| 11 | Enklare elarbete, funktionsprovning, enkel IP, intyg | 5 | D, E, H | Inte TS-blankett, inte IP-tabell inklistrad |
| 12 | Risk, strukturerad felsökning, självständighet | 3 | I | Inte PE-jakt från villa |

Samma kö för alla. Spårboxar, inte två kartor. Elektriker: komprimera 3, 4, 8, 9, 10; fördjupa 1, 2, 5, 11. Maskinist: komprimera 5-kontext, 6, 7; fördjupa 2, 3, 4, 8, 9, 10, 11, 12.

---

## Kapitel i en mening var

**1 Elsäkerhet, stötar, elens verkningar.** Vad som dödar (stöt, fall från stöt, slitage, flexkabel). Skall: 2017:26 5 kap. 5 § parafras (elchock). ELSÄK-installationsregler styr inte ombord; källa TS-webb + prop + FAQ, inte 2008:1. EMC = ELSÄK-FS 2016:3. Båt på land = bara TS-webb, inte lag. Lab B.

**2 Isolering, SMS, innan arbete.** LOTO, bevisad spänningslöshet, megger som jobb. Skall: 5 kap. 5 §. 1 MΩ = upplysning/väntar, aldrig «lagen kräver». Lab A + C.

**3 DC-kretsar.** Resistiva, serie/parallell, mät och räkna. Ingen TS-kontrollpunkt. Lab F DC. Maskinistens hål.

**4 Enfas AC.** Mätning, beräkning, instrumentval. Lab F AC.

**5 Trefas och spänningstyper ombord.** System och komponenter på grundnivå. IT mot skrov som kontext, inte designkurs. Box: sluta tänka SS 436 40 00 som toppnod. Inte blackoutlabb.

**6 Maskiner, konstruktion och drift.** DC/AC-utrustning som den ser ut. Batteri får nämnas, inte eget kapitel. Inte nödstart.

**7 Eltavla / elcentral.** Märkning, skydd, tillträde. Skall 5 kap. 5 § + AR. Tavla-vägledning = kompletterande upplysningar, inte skall. Lab J.

**8 Verktyg och mätinstrument.** Välja, vårda, kategori. Landprovare med RCD-test är fel huvudverktyg här.

**9 Ritningar, schema, måttsättning.** Skall: 2017:26 1 kap. 27 och 29 § parafras (dokumentation, spårbar ändring). Lab J. SHK-läget: sidokrets som inte finns på ritning.

**10 Hållkrets.** Enkel styrkrets från schema. Lab G. Elektrikern kan den, maskinisten måste bygga den.

**11 Elarbete, funktionsprov, enkel IP, intyg.** Losskoppling/anslutning i *befintlig* gruppledning. Lab D = återställd kapsling, märkt avledning. Lab E = intyg till befälhavaren (regelverk + tillämpad standard), vår blankett. Lab H. IP-tabell = URL, 1–2 exempelceller, inte inklistrad IEC 60529.

**12 Felsökning och VG-spåret.** Strukturerad kedja, motiverad risk. Lab I. Inte byta enhet först.

---

## Främre / bakre matter (produktion, inte prosa)

Främre: halvtitel, titel, kolofon, säkerhetsdisclaimer, två spår (samma kö, boxar), boken och kursen (bok = bänk + arbetsorder A–J; kurs = distans, labb, G/VG, LIA), förkortningar, innehåll.

Bakre: motståndstabell; IP som *verifieringshjälp* med URL; intygsmall (vår, GAP mot TS); levande standardlista som URL; sakregister.

**Appendix / inte denna 45 p-kärna:** nödström och A–E-tider, blackout, nödstart, EX/tank, HV-landström, IEC/IEEE 80005, TSFS 2024:58, EMC-djup, batteri som eget kapitel.

---

## KDP-ark (Elon, officiell spec)

Inlaga-PDF exakt 7,00 × 10,00 in. Inget utfall. Ränna **0,625 in** (301–500) från dag ett. Yttre/topp/botten ≥ 0,25 in. Wrap separat, inte sida 1. Typsnitt inbäddade. Figurer ≥300 DPI gråskala. Hårstreck ≥0,75 pt. Listing hos KDP.

---

## Kö

1. Den här listan — lås eller stryk.
2. Kurs m1-blad.
3. Då kap. 1 prosa mot källpaket v1, kap. 5-metoden, [Regler]-luckor bara där paketet själv märker väntar/GAP.
