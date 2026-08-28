# 6 Maskiner ombord: DC/AC, konstruktion och drift

Kapitel 5 namngav spänningarna. Det här kapitlet är maskinen: motor mot generator, märkskylt, stilla axel är inte död plint. Inte en ny trefaslektion. Inte 440-mätning. Inte landström. Inte en ny labbdag.

---

## 6.0 Innan du tar i något

En elmaskin är spänningssatt tills du visat att den är död. Läs märkskylt och system (24 V DC, 230 V enfas, 400/440 V trefas från 5.1) innan luckan. 440 V-plint: titta, rör inte, utan värdtillstånd.

**Varning.** Stilla axel är inte bevisad spänningslöshet. Öppnad 440-kåpa «för att den står» är stöt- och kortrisk. DMM på MSB för att «hitta motorn» är fel ställe och live tavla.

**Stopp.** Ingen kåpa på 440. Ingen DMM på MSB. Ingen 80005. Ingen IEC-maskintabell. Ingen «motorn står = av».

---

## 6.1 Föreslagen regel

En elmaskin är spänningssatt tills du visat att den är död. Titta på märkskylt och system innan luckan. 440 V-plint = look-not-touch utan värdtillstånd. Felsök inte 440-motor med DMM på MSB.

**Källnivå: skall.** TSFS 2017:26 5 kap. 5 §, parafras. Minimera elchock och kortslutning. Inte avskrift. Här: öppnad 440-plint för att axeln står, och DMM på live MSB, *är* den risk 5 § vill att du minimerar.

**Utförande.** Fackmässigt, 2 kap. 6 §. Isolation är kapitel 2. Spänningstyper är 5.1. Enfas rms är kapitel 4. DC-område är kapitel 3. Labbdag: 440 V är look-not-touch. Elever live-wirar inte fartyg. DMM bara på avsedd tränare.

**Inte skall i den här rutan**

- Stator, rotor och märkskyltsfält är konstruktion, inte TSFS-paragraf.
- Varför trefas till maskin = pek 5.1, inte ny IEC-regel.
- IEC-maskintabell och kapslingsklasser som matris klistras inte in.
- 5 kap. 1–4 och 6–7 § (nöd, batteri, landnät) undervisas inte här.

**Elektrikerspår.** Plint på 440 är inte lägenhetens kopplingsdosa mot PE. Skrov är inte N. 440 V ombord är look-not-touch.

**Maskinspår.** Stilla rotor är inte död plint. Isolation enligt 2.1 innan handen på *el*maskinen. «Jag kan den motorn» räcker inte.

---

## 6.2 Vad det betyder i jobbet

**Var.** Foto av motor eller generator, märkskylt, stängd plintlåda. Inte inne i 440-plint.

**Vem.** Eleven läser skylt och stannar. Värden äger luckan.

**Motor mot generator.** Samma släkt, olika energiriktning. Motor: el till rörelse. Generator: rörelse till el. Inte nödgeneratorprov. Inte blackout.

**Konstruktion, grund.** Stator står. Rotor snurrar. DC-maskin och AC-maskin som namn, inte lindningsformel.

**Drift, grund.** Märkskylt U måste matcha systemet från 5.1. Trefasmaskin har tre ledare (5.1, inte omberättat). 24 V DC-styr är ett annat system. Blanda inte plintarna.

**Märkskylt.** Läs U, I, kW, varv, DC eller AC. Det är vad du tittar på. Inte en IEC-katalog.

**Landreflex som är fel.** Öppna dosa, mät mot PE.

**Maskinreflex som är fel.** Axeln stilla = av.

**Grind.** 2.1 innan plint på avställd fartygsmaskin. 5.1 namnger spänningen. 3.1 och 4.1 DMM-läge bara på tränare.

**Figur 6.1.** Energiriktning motor mot generator. Stängd plint plus märkskylt. MSB överkorsad. Gråskala, 300 DPI, 7 × 10 in, ränna 0,625 in. Ingen IEC-tabell.

---

## 6.3 Genomgånget fel: stilla axel, öppnad 440, DMM på MSB

**Symptom.** Motor står. Ingenjör öppnar 440-plint: «den snurrar ju inte.» Elektriker går till huvudtavlan och mäter på MSB för att felsöka motorn.

**Fel maskinreflex.** Stilla = död.

**Fel landreflex.** Felet sitter i tavlan, mät live.

**Rätt kedja**

1. Läs skylt. U = 440 V trefas (begrepp från 5.1).
2. Look-not-touch.
3. Isolation enligt 2.1 *innan* plint, av värd.
4. Felsök inte 440-motor från spänningssatt MSB.
5. DMM bara på isolerad tränare, enligt labbdagen som redan finns.

| Symptom | Första sak du gör | Trolig orsak | Gör inte |
|---|---|---|---|
| «Motorn står = av» | Läs skylt, stanna | Stilla axel ≠ död plint | Öppna 440-kåpa |
| Öppnar plint «för att se» | Look-not-touch | Ingen isolation | Live-wiring |
| DMM på MSB «för att hitta motorn» | Fel ställe | Live tavla | Megga/volta på MSB |
| Tre ledare, «varför trefas?» | Pek 5.1 | Inte ny lektion | Omberätta linje mot fas |
| Blandar 24 V-styr och 440-plint | Namnge system | Två system | Samma dosa |

---

## 6.4 Distansövning — papper och foto

Inte ny labbdag. Classroom vecka 6.

**Ticket.** Foto märkskylt (U, I, kW, rpm, AC 3~). Foto stängd plintlåda. Foto MSB märkt «inte här».

**G, godkänt**

1. Motor eller generator? Energiriktning i en mening.
2. Pek 5.1: varför tre ledare.
3. En mening: stopp innan lucka (2.1).
4. MSB-fotot: inte felsökstället för 440-plint.

**VG, godkänt.** Varför DMM på MSB inte felsöker motorn: live tavla, fel ställe, 5 §. Motiverar look-not-touch.

**IG.** «Står = av.» Plan att öppna 440-kåpa. Mätplan på MSB.

**Varvsdag.** Samma look-not-touch som redan ligger i labbdagen. Peka motor från durk, läs skylt om synlig, lucka stängd. DMM bara på avsedd tränare. Ingen 440-mätning. Ingen live-wiring. G: pekar maskin och spänningstyp utan att röra plint. VG: motiverar varför proberna inte går mot MSB.

**Elektrikerspår i övningen.** Plint på 440 är inte PE-dosa.

**Maskinspår i övningen.** Stilla rotor är inte död plint.

---

## 6.5 Dokumentation

Inte TS-blankett. Inte IEC-tabell. Inte intyg till befälhavaren.

```
PROTOKOLL — maskiner ombord
Namn:
Datum:
Motor eller generator (energiriktning):
Märkskylt U:
Märkskylt I:
Märkskylt kW:
DC eller AC:
440 V-plint = look-not-touch: ja
Stilla axel ≠ död plint: ja
MSB är inte felsökstället: ja
VG — varför inte DMM på MSB:
Varvsdag: pekade maskin, rörde inte plint:
```

G: namn, motor mot generator, skyltdata avläst, 440 = look-not-touch. VG: plus varför inte MSB-DMM. Varvsdag: samma lapp, ingen plint öppnad utan värd.

---

## Produktionsnot, kap. 6

Fem rutor, sen stopp. Figur 6.1: energiriktning motor/generator; stängd plint + märkskylt; MSB överkorsad. 7,00 × 10,00 in, ränna 0,625 in, gråskala 300 DPI, hårstreck ≥0,75 pt. Pek 5.1, ingen ny trefaslektion. Inte 2024:58. Inte 80005. Inte IEC-tabell. Inte Germanica. Inte ny labbdag. Kap. 5 orörd.
