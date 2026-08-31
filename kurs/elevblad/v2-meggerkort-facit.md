# Meggerkort — facit

**Till lärare. Inte till elev. Inte på elev-GitHub Pages.**
`M02` Isolering · `V2` Vecka 2 · Elteknik och ellära 45 p

G: kedja i ordning, referens skrov, 2,4 = GO efter kåpa, 0,4 = STOP + avvikelse, 1 MΩ = upplysning.
VG: saknas megger på varvet → tvåpol + gapflagga.
IG: megger på spänning, PE som referens, 1 MΩ som lag, hoppar lås, 0,4 tillslag.
Räkna: 96 µA / 575 µA; 1 MΩ = upplysning.

---

## Arbetsorder

```
┌─ BILJETT ─────────────────────────────────────────┐
│  230 V-grupp i inredningen. Kabel bytt.           │
│  Isolera på papper. Megga inte på spänning.       │
└───────────────────────────────────────────────────┘
```

```
████ FARA ██████████████████████████████████████████
│  Ingen megger på spänningssatt grupp.            │
└──────────────────────────────────────────────────┘
```

---

## Meggerkort — ifyllt

Kedja **i ordning**. Referens **skrov/stomme**, inte PE.

```
┌─ MEGGERKORT ──────────────────────────────────────┐
│  Grupp: 230 V inredning, kabel bytt               │
│  Tid: före arbete, avställd grupp                 │
│                                                    │
│  Kedja:                                            │
│    [1] från                                        │
│    [2] lås / skylt                                 │
│    [3] tvåpol död                                  │
│    [4] megger                                      │
│    [5] protokoll                                   │
│                                                    │
│  Referens:                                         │
│    [x] skrov / stomme                              │
│    [ ] PE-skena                                    │
│                                                    │
│  Avläsning A:  2,4 MΩ                              │
│    Beslut:  [x] GO     [ ] STOP                    │
│    Tillslag: GO — planera tillslag EFTER kåpa på  │
│                                                    │
│  Avläsning B:  0,4 MΩ                              │
│    Beslut:  [ ] GO     [x] STOP                    │
│    Tillslag: STOP — inte spänningssätt, avvikelse │
│                                                    │
│  1 MΩ är:                                          │
│    [ ] skall i 5 §                                 │
│    [x] upplysning                                  │
└────────────────────────────────────────────────────┘
```

**2,4 MΩ** = GO att *planera* tillslag **efter kåpa på**. Inte tillslag med öppen kåpa.
**0,4 MΩ** = STOP. Ingen tillslag. Skriv avvikelse.
**1 MΩ** = upplysning, inte lag. Inte “olagligt enligt 5 §”.

---

## Räkna

I_läck = U / R.

230 V / 2,4 MΩ ≈ **96 µA**.

230 V / 0,4 MΩ ≈ **575 µA**.

1 MΩ = **upplysning**, inte skall.

Beslut är fortfarande GO/STOP från meggerkortet. µA ändrar inte det.

Elektriker: µA är inte JFB-hemma.
Ingenjör: 1 MΩ är upplysning. Kortet styr.

---

## Två spår — en rad

Elektriker = referens är inte PE-skenan hemma.
Ingenjör = bara för att maskinen inte låter betyder det inte att den är avställd.

---

## VG

Saknas megger på varvet → **tvåpol + gapflagga**. Skriv att meggern saknas. Hitta inte på ett tal. Skippa inte isolation.

---

Inte skolessä. Inte 1 MΩ som skall.
