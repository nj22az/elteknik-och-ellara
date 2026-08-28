# 12 Risk, strukturerad felsökning och självständighet

Kapitel 11 var kåpa och papper. Det här kapitlet är kedjan: hitta felet utan att göra stöt eller kort. Distans först. VG-spåret: skriv kedjan själv. Inte omberättat intyg. Inte Germanica. Inte skriftligt prov. Inte en ny labbdag.

---

## 12.0 Innan du tar i något

Felsök så att du inte gör stöt eller kort av sökandet. Isolation först. Ritning innan luckan. Rätt instrument. Inte live huvudtavla. Inte gissa.

**Varning.** PE-jakt på 440 är fel nyckel och kan vara stöt. «Den gick i går» plus live-prober är 5 §-risk. DMM på MSB är fel ställe.

**Stopp.** Ingen hoppad isolation. Ingen live 440. Ingen DMM på MSB. Ingen villa-PE. Ingen Arduino. Inte lås 230. Inte skriftligt prov i det här kapitlet.

---

## 12.1 Föreslagen regel

Felsök så att du inte gör stöt eller kort av sökandet. Isolation först. Ritning innan luckan. Rätt instrument. Inte live huvudtavla. Inte gissa.

**Källnivå: skall.** TSFS 2017:26 5 kap. 5 §, parafras. Minimera elchock och kortslutning. Inte avskrift. Här: PE-jakt på 440 och live-prober *är* den risk 5 § vill att du minimerar.

**Skall.** 2 kap. 6 §, fackmässigt. Isolation är 2.1. Dokumentation så felsökning är möjlig är 1 kap. 27/29 § (pek 9.1).

**Kedjan är kursmetod, inte TSFS-paragraf.** Sjustegsställningen nedan är hur kursen felsöker. Inte en lagtext.

**Labbdag Lab I.** Död tavla eller 24 V om varvet har. Inte live-wiring. Inte 440-mätning. Inte lås 230.

**Inte skall i den här rutan**

- Felsökningskedjan som pedagogik är kursmetod, inte TSFS-paragraf.
- PE-jakt och JFB-koll som landmetod är fel ombord (pek 1.1 och 5.1).
- Arduino och IEC-felträd hör inte hit.
- 5 kap. 1–4 och 6–7 § undervisas inte här.

**Elektrikerspår.** Inte PE-jakt. Isolation mot skrov/IT (2.1). 440 look-not-touch. PE är inte felsöknyckeln ombord.

**Maskinspår.** Metod innan handen. «Den går» och «jag kan den» är inte kedjan. Stående maskin är inte död krets.

---

## 12.2 Vad det betyder i jobbet

**Var.** Papper med symptom plus enlinje plus kretsschema. Varv: död tavla eller 24 V-tränare.

**Vem.** Eleven väljer kedjan. Värden äger 440 och MSB.

**Ställning.** G får den given. VG skriver den själv.

1. Symptom i en mening. Inte peka prober än.
2. Namnge spänningstyp (5.1). 440 = look-not-touch.
3. Isolation / död-koll (2.1) om du ska in.
4. Ritning: var ska felet sitta, styr eller last (9.1, 10.1 pek).
5. Instrument (8.1): tvåpol, DMM på tränare, inte MSB, inte megger live.
6. Ett test. Inte tre gissningar.
7. Åtgärd plus papper (11.1 pek: kåpa, intyg, inte omberättat).

Inte PE. Inte MSB. Inte live 440.

**Landreflex som är fel.** Jaga PE. Följ nollan.

**Maskinreflex som är fel.** Den går. Jag kan den.

**Figur 12.1.** Sjustegskedja. Förbjudet: PE-jakt, live 440, DMM på MSB. VG: skriv kedjan själv. Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in.

---

## 12.3 Genomgånget fel: PE-jakt, «den gick i går», live-prober

**Symptom.** «Pumpen startar inte.» Elektriker jagar PE på 440-tavlan. Ingenjör: «den gick i går,» prober live.

**Fel landreflex.** PE/JFB.

**Fel maskinreflex.** Gissa med spänning.

**Rätt kedja.** Symptom. 24 V-styr eller 440-last, på papper. Isolation. Schema. Ett test på död eller ELV-sida. Inte MSB. Inte fas mot skrov som nolla.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| PE-jakt på 440 | Namnge system, isolation | Villa-PE | Fas mot skrov |
| «Den gick i går» + live-prober | Symptom på papper | Gissa med spänning | Live 440 |
| DMM på MSB för motorfel | Pek 6.1/7.1, fel ställe | Live tavla | Prober på MSB |
| Hoppar isolation | Tvåpol efter från/lås (2.1) | Handen först | Tre gissningar |
| Arduino / felträd | Kurskedjan, sju steg | Verktygslåda | PLC |

---

## 12.4 Distansövning — papper

Inte ny labbdag. Classroom vecka 9, efter 11.1. Inte skriftligt prov på det här bladet. Inte omberättat intyg.

**Ticket.** Symptomkort «startar inte». Enlinje: 24 V-styr plus 440-motor märkt look-not-touch. Kretsschema med *ett* lagt fel (öppen håll eller lös 24 V). Inte PE-fel som i villa.

**G, godkänt.** Följer den numrerade ställningen. Pekar rätt fel. Skriver «inte 440, inte MSB».

**VG, godkänt.** Skriver kedjan själv. Motiverar åtgärden mot risk: varför inte PE-jakt, varför isolation först, varför inte MSB.

**IG.** Hoppar isolation. Live-plan. PE-jakt.

**Varvsdag.** Lab I, samma död tavla eller 24 V som redan ligger i labbdagen, om de har. Inte lås 230. Ett lagt fel. Inte live-wiring. Inte 440-mätning. Inte DMM på MSB. G: hittar felet med ställning. VG: själv plus riskmening. IG: prober först.

**Elektrikerspår i övningen.** Inte PE-jakt.

**Maskinspår i övningen.** Metod innan handen.

---

## 12.5 Dokumentation

Inte TS-blankett. Inte 11.1 omberättad. Bara: felsök utan papper = inte färdigt.

```
PROTOKOLL — strukturerad felsökning
Namn:
Datum:
Symptom (en mening):
Spänningstyp:
Isolation / död-koll: ja / nej
Styr eller last (ritning):
Instrument:
Ett test:
Funnet fel:
Inte 440 / inte MSB: ja
G — följde given kedja: ja / nej
VG — skrev kedjan själv:
VG — åtgärd mot risk:
Varvsdag, Lab I:
```

G: symptom, kedja (given), funnet fel, «inte 440/MSB». VG: egen kedja plus motiverad åtgärd. Varvsdag: samma lapp.

---

## Produktionsnot, kap. 12

Fem rutor, sen stopp. Figur 12.1: sjustegskedja; förbjudet (PE-jakt, live 440, MSB-DMM). VG-spåret syns som «skriv kedjan själv». 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. Inte omberättad 11.1. Inte 2024:58. Inte 80005. Inte IEC/IP-tabell. Inte Arduino. Inte PE-jakt från villa. Inte lås 230. Inte skriftligt prov i kapitlet. Inte Germanica. Inte ny labbdag. Kap. 11 orörd.
