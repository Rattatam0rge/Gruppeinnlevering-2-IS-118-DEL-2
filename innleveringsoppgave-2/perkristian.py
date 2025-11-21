#Story

print(
    "\nErling er prosjektleder for et team med 5 medlemmer."

     " Sivert, Silje , Hamdi, Hallgeir og Noa." )
print("Det er tre uker til levering av prototype så det er lite med tid og mye å gjøre fremover.")

print("Det har til nå gått ganske greit og sammarbeidet har fungert bra. Men nå har det oppstått en konflikt mellom to av Erlings prosjektmedarbeidere."
)

print("\nUenigheten mellom Silje og Sivert har utviklet seg fra sakskonflikt til personkonflikt."\
      "Erling må nå velge hvordan han skal løse denne konflikten")

#Beslutningspunkt 1

valg1 = input("1) Skal Erling velge å løse problemet i plenum (A) eller med individuelle samtaler (B)?").upper()

if valg1 == "A":
    print("Erling velger å løse problemet i plenum." )
elif valg1 == "B":
    print("Erling velger individuelle samtaler.")
else:
     print("Prøv på nytt. Det er kun to gyldige valgmuligheter.")

#Beslutnings punkt 2
valg2 = input("\n2) Skal han videre følge opp med felles møte (A) eller prøve individuell oppfølging (B)?").upper()

if valg2 == "A":
    print("Erling velger et felles oppklaringsmøte." )
elif valg2 == "B":
    print("Erling velger flere individuelle samtaler.")
else:
    print("Prøv på nytt. Det er kun to gyldige valgmuligheter.")

#Besluttningspumkt 3

valg3 = input("\n3)Skal prosessen avsluttes med felles avtale (A) eller individuelle mål (B)? ").upper()

if valg3 == "A":
    print("Erling lager en felles avtale for begge." )
elif valg3 == "B":
    print("Erling gir hver enkelt utviklingspunkter.")
else:
    print("Prøv på nytt. Det er kun to gyldige valgmuligheter.")

print("\n=== Saken regnes som løst ===")
