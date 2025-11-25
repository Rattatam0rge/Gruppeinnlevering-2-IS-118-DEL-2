#Text farger

RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

#Story Silje og Sivert konfliktløsning

print(
    "\nErling er prosjektleder for et team med 5 medlemmer."

     " Sivert, Silje , Hamdi, Hallgeir og Noa." )
print("Det er tre uker til levering av prototype så det er lite med tid og mye å gjøre fremover.")

print("Det har til nå gått ganske greit og sammarbeidet har fungert bra. Men nå har det oppstått en konflikt mellom to av Erlings prosjektmedarbeidere."
)

print("\nUenigheten mellom Silje og Sivert har utviklet seg fra sakskonflikt til personkonflikt."\
      "Erling må nå velge hvordan han skal løse denne konflikten.")

#Beslutningspunkt 1

valg1 = input("1) Skal Erling velge å løse problemet i plenum (A) eller med individuelle samtaler (B)?").upper()

if valg1 == "A":
    print(f"{GREEN}\nErling velger å løse problemet i plenum. Felles møteform er litt mer tidkrevende men gir alle i teamet mulighet til å uttrykke sine synspunkter.{RESET}" )
elif valg1 == "B":
    print(f"{GREEN}\nErling velger individuelle samtaler men dette viser seg å bare være delvis effektivt.{RESET}")
else:
     print(f"{RED}Prøv på nytt. Det er kun to gyldige valgmuligheter.{RESET}")

#Beslutnings punkt 2

valg2 = input("\n2) Skal han følge opp med et felles møte (A) Eller prøve individuell oppfølging (B)?").upper()

if valg2 == "A":
    print(f"{GREEN}\nErling velger et felles oppklaringsmøte.{RESET}" )
elif valg2 == "B":
    print(f"{GREEN}\nErling prøver videre individuelle samtaler.{RESET}")
else:
    print(f"{RED}\nPrøv på nytt. Det er kun to gyldige valgmuligheter.{RESET}")

#Besluttnings punkt 3

valg3 = input("\n3)Skal prosessen avsluttes med felles avtale (A) eller individuelle mål (B)? ").upper()

if valg3 == "A":
    print(f"{GREEN}\nErling lager en felles avtale for begge.{RESET}" )
elif valg3 == "B":
    print(f"{GREEN}\nErling gir Silje og Sivert individuelle utviklingspunkter.{RESET}")
else:
    print(f"{RED}Prøv på nytt. Det er kun to gyldige valgmuligheter.{RESET}")

# Sluttutfall basert på valg

print(f"{RED}\n--- Sluttvurdering ---{RESET}")

# Beste scenario: åpent møte, videre felles oppfølging, felles avtale

if valg1 == "A" and valg2 == "A" and valg3 == "A":
    print(f"{GREEN}Beste resultat: Konflikten ble håndtert åpent og samlet. En klar felles avtale gjenoppretter tillit og teamet kan jobbe videre med prototypen.{RESET}")

# Alternativt godt scenario: individuelle samtaler, individuell oppfølging og individuelle mål

elif valg1 == "B" and valg2 == "B" and valg3 == "B":
    print(f"{BLUE}Godt resultat, men kostbart i tid: Personlig oppfølging hjelper partene til forbedring, men prosjektet kan bli noe forsinket.{RESET}")

# Felles avtale gir ofte bedre stabilitet uavhengig av møteform

elif valg3 == "A":
    print(f"{BLUE}Stabiliserende resultat: En felles avtale skaper forventninger og reduserer framtidige konflikter, selv om fremgang kan være gradvis.{RESET}")

# Alle andre kombinasjoner: mellomutfall med behov for videre oppfølging

else:
    print(f"{RED}Usikkert/middels resultat: Enkelte problemer ble løst, men spenninger kan vedvare. Anbefalt videre oppfølging og nye sjekkpunkter.{RESET}")
