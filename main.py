"""
Program Kryesor - Keyword Substitution & Trellis Cipher
=========================================================
Ndërfaqe interaktive për enkriptim dhe dekriptim.
"""

from keyword_cipher import encrypt_keyword, decrypt_keyword, show_cipher_table
from trellis_cipher import encrypt_trellis, decrypt_trellis, visualize_trellis


def print_header():
    print("\n" + "═"*60)
    print("  🔐  SISTEMI I KRIPTOGRAFISË")
    print("       Keyword Substitution Cipher & Trellis Cipher")
    print("═"*60)


def print_menu():
    print("""
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
  Zgjedh opsionin (0-9): """, end="")


def get_rows() -> int:
    while True:
        try:
            r = int(input("  Numri i rreshtave (>=2): "))
            if r >= 2:
                return r
            print("  ⚠  Duhet të jetë >= 2")
        except ValueError:
            print("  ⚠  Ju lutem shkruani një numër të plotë.")


def demo():
    """Shfaq demonstrime të gatshme për të dyja shifrat."""
    print("\n" + "─"*60)
    print("  DEMO 1: Keyword Substitution Cipher")
    print("─"*60)
    kw  = "CRYPTO"
    msg = "Hello, World!"
    enc = encrypt_keyword(msg, kw)
    dec = decrypt_keyword(enc, kw)
    show_cipher_table(kw)
    print(f"\n  Teksti origjinal : {msg}")
    print(f"  Fjala kyçe       : {kw}")
    print(f"  Teksti i enkriptuar : {enc}")
    print(f"  Teksti i dekriptuar : {dec}")

    print("\n" + "─"*60)
    print("  DEMO 2: Trellis Cipher")
    print("─"*60)
    rows = 3
    msg2 = "HELLOWORLD"
    enc2 = encrypt_trellis(msg2, rows)
    dec2 = decrypt_trellis(enc2, rows)
    visualize_trellis(msg2, rows, "Plaintext")
    print(f"\n  Teksti origjinal : {msg2}")
    print(f"  Rreshtat (rows)  : {rows}")
    print(f"  Teksti i enkriptuar : {enc2}")
    print(f"  Teksti i dekriptuar : {dec2}")

    print("\n" + "─"*60)
    print("  DEMO 3: Enkriptim i dyfishtë (Keyword + Trellis)")
    print("─"*60)
    kw3, rows3, msg3 = "SECRET", 3, "ATTACKATDAWN"
    e1 = encrypt_keyword(msg3, kw3)
    e2 = encrypt_trellis(e1, rows3)
    d2 = decrypt_trellis(e2, rows3)
    d1 = decrypt_keyword(d2, kw3)
    print(f"\n  Teksti origjinal    : {msg3}")
    print(f"  Pas Keyword enc     : {e1}")
    print(f"  Pas Trellis enc     : {e2}")
    print(f"  Pas Trellis dec     : {d2}")
    print(f"  Pas Keyword dec     : {d1}")
    print(f"  Suksesi             : {'✅' if d1 == msg3 else '❌'}")


def main():
    print_header()

    while True:
        print_menu()
        choice = input().strip()

        if choice == "0":
            print("\n  👋 Mirupafshim!\n")
            break

        elif choice == "1":
            msg = input("\n  Teksti origjinal : ")
            kw  = input("  Fjala kyçe       : ")
            enc = encrypt_keyword(msg, kw)
            print(f"\n  ✅ Enkriptuar : {enc}")

        elif choice == "2":
            msg = input("\n  Teksti i enkriptuar : ")
            kw  = input("  Fjala kyçe          : ")
            dec = decrypt_keyword(msg, kw)
            print(f"\n  ✅ Dekriptuar : {dec}")

        elif choice == "3":
            msg  = input("\n  Teksti origjinal : ")
            rows = get_rows()
            enc  = encrypt_trellis(msg, rows)
            visualize_trellis(msg, rows, "Plaintext")
            print(f"\n  ✅ Enkriptuar : {enc}")

        elif choice == "4":
            msg  = input("\n  Teksti i enkriptuar : ")
            rows = get_rows()
            dec  = decrypt_trellis(msg, rows)
            print(f"\n  ✅ Dekriptuar : {dec}")

        elif choice == "5":
            msg  = input("\n  Teksti origjinal : ")
            kw   = input("  Fjala kyçe       : ")
            rows = get_rows()
            e1   = encrypt_keyword(msg, kw)
            e2   = encrypt_trellis(e1, rows)
            print(f"\n  Pas Keyword  : {e1}")
            print(f"  ✅ Pas Trellis : {e2}")

        elif choice == "6":
            msg  = input("\n  Teksti i enkriptuar dyfish : ")
            rows = get_rows()
            kw   = input("  Fjala kyçe                 : ")
            d2   = decrypt_trellis(msg, rows)
            d1   = decrypt_keyword(d2, kw)
            print(f"\n  Pas Trellis dec : {d2}")
            print(f"  ✅ Pas Keyword dec : {d1}")

        elif choice == "7":
            kw = input("\n  Fjala kyçe : ")
            show_cipher_table(kw)

        elif choice == "8":
            msg  = input("\n  Teksti : ")
            rows = get_rows()
            visualize_trellis(msg, rows, "Vizualizim")

        elif choice == "9":
            demo()

        else:
            print("  ⚠  Opsion i pavlefshëm. Ju lutem zgjedh 0-9.")


if __name__ == "__main__":
    main()
