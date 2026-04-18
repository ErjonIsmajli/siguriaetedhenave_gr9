"""
Keyword Substitution Cipher
============================
Implementimi i Keyword Substitution Cipher për enkriptim dhe dekriptim.
"""

def build_keyword_alphabet(keyword: str) -> str:
    """
    Ndërton alfabetin e ri bazuar në fjalën kyçe.
    Hiqen duplikatet nga fjala kyçe dhe shtohen shkronjat e mbetura
    të alfabetit standard në rend.
    
    Args:
        keyword: Fjala kyçe për ndërtimin e alfabetit
        
    Returns:
        Alfabeti i ri i ndërtuar nga fjala kyçe (26 shkronja)
    """
    keyword = keyword.upper().replace(" ", "")
    seen = set()
    cipher_alphabet = []

    # Shto shkronjat unike nga fjala kyçe
    for char in keyword:
        if char.isalpha() and char not in seen:
            seen.add(char)
            cipher_alphabet.append(char)

    # Shto shkronjat e mbetura të alfabetit
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            cipher_alphabet.append(char)

    return "".join(cipher_alphabet)


def encrypt_keyword(plaintext: str, keyword: str) -> str:
    """
    Enkrypton tekstin me Keyword Substitution Cipher.
    
    Args:
        plaintext: Teksti origjinal për enkriptim
        keyword: Fjala kyçe
        
    Returns:
        Teksti i enkriptuar
    """
    standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alpha = build_keyword_alphabet(keyword)
    table = str.maketrans(standard + standard.lower(),
                          cipher_alpha + cipher_alpha.lower())
    return plaintext.translate(table)


def decrypt_keyword(ciphertext: str, keyword: str) -> str:
    """
    Dekrypton tekstin e enkriptuar me Keyword Substitution Cipher.
    
    Args:
        ciphertext: Teksti i enkriptuar
        keyword: Fjala kyçe
        
    Returns:
        Teksti origjinal
    """
    standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alpha = build_keyword_alphabet(keyword)
    # Inverso: shifri → standard
    table = str.maketrans(cipher_alpha + cipher_alpha.lower(),
                          standard + standard.lower())
    return ciphertext.translate(table)


def show_cipher_table(keyword: str) -> None:
    """
    Shfaq tabelën e zëvendësimit për analizë vizuale.
    
    Args:
        keyword: Fjala kyçe
    """
    standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_alpha = build_keyword_alphabet(keyword)
    
    print(f"\n{'='*60}")
    print(f"  Keyword Substitution Cipher - Fjala kyçe: '{keyword}'")
    print(f"{'='*60}")
    print(f"  Alfabeti standard : {' '.join(standard)}")
    print(f"  Alfabeti i shifrit: {' '.join(cipher_alpha)}")
    print(f"{'='*60}")