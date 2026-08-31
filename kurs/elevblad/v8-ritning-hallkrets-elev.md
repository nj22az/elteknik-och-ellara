# Ritning och hållkrets — elevblad

`M09` Ritningar + `M10` Hållkrets · `V8` Vecka 8 · Elteknik och ellära 45 p

Namn: ______________________________  Datum: __________
Spår: [ ] elektriker (land)   [ ] ingenjör (fartyg)   [ ] båda

---

## Arbetsorder

```
┌─ BILJETT ─────────────────────────────────────────┐
│  Läs innan luckan. Pek mot papper, inte live.     │
│  24 V-håll om varvet har. Lås inte 230 här.       │
└───────────────────────────────────────────────────┘
```

```
████ FARA ██████████████████████████████████████████
│  Inte gissa saknad grupp med DMM på MSB.         │
└──────────────────────────────────────────────────┘
```

---

## 1. Enlinje vs krets

Märk: **enlinje** eller **kretsschema**.

```
  MSB ── grupp ── motor 440          start ──( )── stopp
         (lucka stängd)              håll ──[ ]── kontaktor
         Längd kabel: ______ m
              A                            B
```

A = __________________     B = __________________

Peka (skriv): huvudtavla sitter i figur  [ ] A  [ ] B
Motor sitter i figur                     [ ] A  [ ] B

Mått: kabeln är ritad **18 m** i kanten. Fältet ovan är tomt. Skriver du 18 eller mäter live för att kolla?

- [ ] skriver 18 på papper
- [ ] mäter live

Ny grupp saknas på ritningen. STOP eller GO in i tavlan?

- [ ] STOP
- [ ] GO

---

## 2. Hållkrets — numrera 1–3 (start / håll / stopp)

Blandat. Skriv 1 start, 2 håll, 3 stopp.

| Del | Nr |
|---|---|
| NC i serie, bryter allt | ___ |
| NO, tryck för att dra | ___ |
| Parallellt med start, sluts när kontaktor drar | ___ |

Hållkontakten sluter inte. Symptom:  [ ] håller inte   [ ] håller fast
Stopp byglad. Symptom:               [ ] håller inte   [ ] håller fast

Felsök hållkrets på 440-MSB?  [ ] STOP   [ ] GO

---

## 3. Två spår — en rad

Elektriker: styr 24 V är inte last 440. Skrov är inte N på enlinjen.
Ingenjör: schema innan knappen. Huvudet är inte ritningen.
