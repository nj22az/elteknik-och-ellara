# 10 Enklare styrkrets och hållkrets

Kapitel 9 var ritningen. Det här kapitlet är slingan: start, håll, stopp. 24 V-styr är inte 440-last. Inte Arduino. Inte låst 230. Inte omberättad ritning. Inte en ny labbdag.

---

## 10.0 Innan du tar i något

Läs kretsen innan du trycker. Hållkrets är start, håll och stopp, inte «håll inne start». Felsök inte styret på spänningssatt 440-tavla.

**Varning.** Håll inne start är inte en krets. DMM på 440-MSB «för styret» är stöt- och kortrisk. Styr 24 V är inte last 440.

**Stopp.** Ingen live 440. Ingen Arduino. Ingen PLC. Inte lås 230 för den här kretsen. Ingen IEC-styrtabell.

---

## 10.1 Föreslagen regel

Läs kretsen innan du trycker. Hållkrets är start, håll och stopp. Inte «håll inne start». Felsök inte styret på spänningssatt 440-tavla.

**Källnivå: skall.** TSFS 2017:26 5 kap. 5 §, parafras. Minimera elchock och kortslutning. Inte avskrift. Här: live 440 «för styret» och gissa utan schema *är* den risk 5 § vill att du minimerar.

**Utförande.** Fackmässigt, 2 kap. 6 §. Ritning innan luckan är 1 kap. 27/29 § (pek 9.1, inte omberättat). Isolation är kapitel 2. 440 look-not-touch är 5.1 och 7.1. Labbdag: antingen död 230 V-övningstavla *eller* 24 V-hållkrets. Varvet väljer. Inte låst 230 här. Finns 24 V-tränare: ticket dit. Finns den inte: papper räcker för G.

**Inte skall i den här rutan**

- NO, NC och hållkontakt som symboler är ellära, inte TSFS-paragraf.
- 24 V-styr mot 440-last är kursbegrepp från 5.1, inte IEC-tabell.
- PLC, Arduino och IEC-styrtabell hör inte hit.
- 5 kap. 1–4 och 6–7 § undervisas inte här.

**Elektrikerspår.** Styr 24 V är inte last 440. Två system. 440 look-not-touch även när du «bara felsöker styr». Inte samma 230 TN som hemma.

**Maskinspår.** Schema innan startknapp. Håll är en slinga, inte vilja. Knappen på durk är inte ritningen.

---

## 10.2 Vad det betyder i jobbet

**Var.** Papper. Eventuellt 24 V-tränare på varvet. Inte 440-tavla.

**Vem.** Den som trycker har läst slingan. Värden äger 440.

**Slingan.** Stopp i serie (NC). Start NO. Hållkontakt parallellt med start, sluts när kontaktorn drar. Släpp start: den håller via håll. Stopp bryter, allt släpper.

**Två felbilder.** Håller inte: hållkontakt sluter inte, eller tråd loss. Håller fast: stopp byglad, svetsad kontaktor. Stoppknapp gör inget.

**Landreflex som är fel.** 230 styr = 230 last.

**Maskinreflex som är fel.** Håll inne start.

**Grind.** 24 V-träning är ELV. 440-lastsida = look-not-touch. Inte blanda proberna.

**Figur 10.1.** Start–håll–stopp. Håller inte mot håller fast. 24 V-styr och 440-last som två rutor. Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in. Inte Arduino.

---

## 10.3 Genomgånget fel: håll inne start, DMM på 440-MSB

**Symptom.** Pump ska hålla. Ingenjör håller inne start. Elektriker går till 440-MSB med DMM: «det är ju styret.»

**Fel maskinreflex.** Startknapp = gas.

**Fel landreflex.** Felsök på lasttavlan.

**Rätt kedja**

1. Kretsschema (9.1).
2. Peka start, håll, stopp.
3. Felbild: håller inte mot håller fast.
4. 24 V-styr skilt från 440-last.
5. Inte live 440.
6. Varv: 24 V-tränare om de har, annars papper.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| Håller inne start | Läs slingan | Startknapp = gas | Tryck tills den går |
| DMM på 440-MSB «för styret» | Look-not-touch | Lasttavla som felsök | Live 440 |
| Håller inte | Peka hållkontakt | Öppen håll / tråd loss | Gissa med prober |
| Håller fast | Peka stopp NC | Byglad stopp / svets | Arduino |
| 230 styr = 230 last | Namnge två system | Landreflex | Lås 230 här |

---

## 10.4 Distansövning — papper

Inte ny labbdag. Classroom vecka 8, efter 9.1. Inte omberättad ritning. Inte Arduino.

**Ticket.** Ett komplett hållkretschema. Två felbilder: öppen håll, byglad stopp.

**G, godkänt**

1. Pekar start, håll, stopp.
2. Pekar var slingan håller.
3. Märker de två felbilderna: håller inte / håller fast.
4. En mening: 440-tavla är inte felsökstället.

**VG, godkänt.** Varför live 440 är 5 §-fel även «bara för styret». 24 V-styr skilt från 440-last.

**IG.** «Tryck tills den går.» Live-mätplan. Arduino.

**Varvsdag.** Inte nytt schema. Inte lås 230 för hållkrets. Har varvet 24 V-kontaktortränare: bygg eller prova start-håll-stopp. Har de den inte: G redan på papper. Ingen live-wiring. Ingen 440-mätning. G: funktion efter schema (om tränare) eller papper (om inte). VG: felsök ett lagt fel från ritning, inte från MSB.

**Elektrikerspår i övningen.** Styr 24 V är inte last 440.

**Maskinspår i övningen.** Schema innan startknapp.

---

## 10.5 Dokumentation

Inte TS-blankett. Inte IEC-tabell. Inte intyg till befälhavaren.

```
PROTOKOLL — hållkrets
Namn:
Datum:
Start NO pekad: ja / nej
Håll parallellt pekad: ja / nej
Stopp NC pekad: ja / nej
Felbild (håller inte / håller fast):
440-tavla är inte felsökstället: ja
24 V-styr ≠ 440-last: ja
VG — varför inte live 440 för styret:
Varvsdag, 24 V-tränare fanns: ja / nej
```

G: namn, pek start/håll/stopp, en felbild namngiven. VG: plus 440-riskmening. Varvsdag: 24 V ja eller nej (varvets svar). Inte påhittad 230-hållkrets.

---

## Produktionsnot, kap. 10

Fem rutor, sen stopp. Figur 10.1: start–håll–stopp; håller inte mot håller fast; 24 V-styr / 440-last som två rutor. 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. Inte Arduino. Inte lås 230. Inte omberättad 9.1. Inte 2024:58. Inte 80005. Inte Germanica. Inte ny labbdag. Kap. 9 orörd.
