print("\nErling er prosjektleder for et team med fem personer:")
print("Silje, Sivert, Hamdi, Hallgeir og Noa.")
print("Det er tre uker igjen til levering av en prototype, og det er mye som må bli ferdig.")
print("Til nå har samarbeidet fungert greit, men nå har det oppstått en konflikt.\n")

print(
    "Uenigheten mellom Silje og Sivert har gått fra å være en saklig diskusjon "
    "til å bli mer personlig. Erling må ta noen valg for å få samarbeidet på rett spor.\n"
)

score = 0

valg1 = input(
    "1) Skal Erling ta opp konflikten i plenum (A) eller starte med individuelle samtaler (B)? "
).strip().upper()

if valg1 == "A":
    print("\nErling tar opp konflikten i plenum foran hele gruppa.")
    print("Det skaper åpenhet, men stemningen blir ganske trykket.")
    score -= 1
elif valg1 == "B":
    print("\nErling tar først individuelle samtaler med Silje og Sivert.")
    print("De får forklare sitt syn, og konflikten blir litt mer saklig igjen.")
    score += 1
else:
    print("\nUgyldig valg. Du skrev ikke A eller B.")
    print("Erling blir usikker og gjør ikke noe helt tydelig i første runde.")

valg2 = input(
    "\n2) Etter første runde, skal han følge opp med et felles møte (A) "
    "eller fortsette med individuell oppfølging (B)? "
).strip().upper()

if valg2 == "A":
    print("\nErling samler alle til et felles møte om samarbeidet.")
    print("Det blir en ryddig runde der alle får si noe, og noen misforståelser blir avklart.")
    score += 1
elif valg2 == "B":
    print("\nErling velger å fortsette med individuelle samtaler.")
    print("Det hjelper noe, men felles forståelse i teamet mangler fortsatt.")
    score -= 1
else:
    print("\nUgyldig valg. Du skrev ikke A eller B.")
    print("Erling blir stående litt på sidelinjen, og ting går sin gang uten klar avklaring.")

valg3 = input(
    "\n3) Mot slutten av prosessen, skal de avslutte med en felles avtale (A) "
    "eller individuelle mål for hver person (B)? "
).strip().upper()

if valg3 == "A":
    print("\nErling får til en felles avtale som begge kan leve med.")
    print("Det gir en felles retning for videre samarbeid.")
    score += 1
elif valg3 == "B":
    print("\nErling lager individuelle mål for hver av dem.")
    print("De får tydelige forventninger, men det blir mindre fokus på selve samarbeidet.")
    score -= 1
else:
    print("\nUgyldig valg. Du skrev ikke A eller B.")
    print("Avslutningen blir litt uklar, uten en tydelig felles plan.")

print("\n=== SLUTT PÅ HISTORIEN ===\n")

if score >= 2:
    print("Utfallsalternativ 1: Godt samarbeid")
    print(
        "Erling har tatt aktive grep, og Silje og Sivert klarer å jobbe sammen igjen. "
        "Teamet opplever høyere trygghet, og de rekker å levere en god prototype."
    )
elif score >= 0:
    print("Utfallsalternativ 2: Ok, men ikke helt bra")
    print(
        "Konflikten er delvis ryddet opp i. De klarer å jobbe sammen, "
        "men det er fortsatt litt spent stemning. Prototypen blir levert, "
        "men samarbeidet kunne vært bedre."
    )
else:
    print("Utfallsalternativ 3: Dårlig samarbeid")
    print(
        "Konflikten henger igjen gjennom hele perioden. Det dannes litt fronter i gruppa, "
        "og motivasjonen synker. Prototypen blir så vidt ferdig, og kvaliteten blir preget av konfliktene."
    )

print("\nTakk for at du spilte historien om Erling.")

