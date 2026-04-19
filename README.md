# 🔐 Keyword Substitution Cipher & Trellis Cipher

Implementim i dy algoritmeve klasike kriptografike në Python, me enkriptim, dekriptim dhe raste testimi të plota.

---

## ▶️ Si të ekzekutohet programi

### Kërkesat paraprake
- Python 3.10 ose më i ri (nuk kërkohen librari të jashtme)

### Ekzekutimi i ndërfaqes interaktive

```bash
python main.py
```

Do të shfaqet menyja kryesore:
```
══════════════════════════════════════════════════════════════
  🔐  SISTEMI I KRIPTOGRAFISË
       Keyword Substitution Cipher & Trellis Cipher
══════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────┐
  │  1. Enkriptim   — Keyword Substitution Cipher       │
  │  2. Dekriptim   — Keyword Substitution Cipher       │
  │  3. Enkriptim   — Trellis Cipher                    │
  │  4. Dekriptim   — Trellis Cipher                    │
  │  5. Enkriptim i dyfishtë  (Keyword + Trellis)       │
  │  6. Dekriptim i dyfishtë  (Trellis + Keyword)       │
  │  7. Shfaq tabelën e shifrit (Keyword)               │
  │  8. Vizualizo trellis-in                            │
  │  9. Demo — shembuj të gatshëm                       │
  │  0. Dil                                             │
  └─────────────────────────────────────────────────────┘
```

---

## 📖 Përshkrimi i algoritmeve

### 1. Keyword Substitution Cipher

**Kategoria:** Shifër zëvendësimi (Substitution Cipher)

**Parimi i funksionimit:**

Ky algoritëm zëvendëson çdo shkronjë të tekstit origjinal me shkronjën korresponduese nga një alfabet i ri, i ndërtuar nga fjala kyçe (*keyword*).

**Ndërtimi i alfabetit kyç:**
1. Merren shkronjat unike nga fjala kyçe, në rendin e paraqitjes.
2. Pas tyre shtohen shkronjat e mbetura të alfabetit standard (A-Z), në rend, duke shmangur dublikatat.
3. Ky alfabet 26-shkronjësh zëvendëson alfabetin standard pozicion pas pozicioni.

**Shembull:**
```
Fjala kyçe   : CRYPTO
Alfabet i ri : C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
Alfabet std  : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

- Enkriptimi: `A → C`, `B → R`, `C → Y`, ...
- Dekriptimi: inversioni i tabelës

**Karakteristikat:**
- Çdo shkronjë ka gjithmonë të njëjtin zëvendësues (shifër monoalfabetike)
- Hapësirat, numrat dhe pikësimi kalojnë pa ndryshim
- Siguria varet nga sekretësia e fjalës kyçe

---

### 2. Trellis Cipher (Rail Fence Cipher)

**Kategoria:** Shifër transpozicioni (Transposition Cipher)

**Parimi i funksionimit:**

Karakteret e tekstit origjinal *nuk ndryshojnë* — ato vetëm *rirenditen* sipas një modeli zigzag (trellis), si vijon:

1. **Enkriptimi:**
   - Karakteret shkruhen në një rrjetë (trellis) diagonale me `N` rreshta, duke ndjekur një lëvizje zigzag (lart-poshtë alternuese).
   - Pastaj lexohen rresht pas rreshti (majtas-djathtas), duke formuar tekstin e enkriptuar.

2. **Dekriptimi:**
   - Llogaritet gjatësia e secilit rresht bazuar në modelin zigzag.
   - Teksti i enkriptuar ndahet sipas atyre gjatësive.
   - Karakteret lexohen sipas rendit zigzag origjinal.

**Shembull vizual me rows=3, "HELLOWORLD":**
```
Rreshti 0: H . . . O . . . L .
Rreshti 1: . E . L . W . R . D
Rreshti 2: . . L . . . O . . .
```
Lexohet rresht pas rreshti: `HOL` + `ELWRD` + `LO` = `HOLELWRDLO`

**Karakteristikat:**
- Karakteret ruhen, vetëm pozicioni ndryshon
- Siguria rritet me numrin e rreshtave
- Mund të kombinohet me shifra zëvendësimi për siguri më të lartë

---

## 🧪 Shembuj të rezultateve

### Keyword Substitution Cipher

```
Fjala kyçe          : CRYPTO
Teksti origjinal    : Hello, World!
Teksti enkriptuar   : Btggj, Vjmgp!
Teksti dekriptuar   : Hello, World!

Tabela e zëvendësimit:
Alfabeti standard : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Alfabeti i shifrit: C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
```

### Trellis Cipher

```
Teksti origjinal    : HELLOWORLD
Rows                : 3
Teksti enkriptuar   : HOLELWRDLO
Teksti dekriptuar   : HELLOWORLD

Vizualizimi:
Rreshti 0: H . . . O . . . L .
Rreshti 1: . E . L . W . R . D
Rreshti 2: . . L . . . O . . .
```

### Enkriptim i dyfishtë (Keyword + Trellis)

```
Teksti origjinal    : ATTACKATDAWN
Fjala kyçe          : SECRET
Rows                : 3
Pas Keyword enc     : SQQSCHSQRSWK
Pas Trellis enc     : SCRQSHQSKQSW
Pas Trellis dec     : SQQSCHSQRSWK
Pas Keyword dec     : ATTACKATDAWN ✅
```

---

## 👥 Contributors

Ky projekt është realizuar në kuadër të lëndës **Siguria e të Dhënave** nga:

- Erjon Ismajli
- Era Popova
- Ermira Zeka
- Ermal Berisha