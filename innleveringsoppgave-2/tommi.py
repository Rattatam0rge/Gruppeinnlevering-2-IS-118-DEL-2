print("\nErling er prosjektleder for et team med seks personer: Sivert, Silje, Hamdi, Hallgeir, Noa og Jabir.")
print("Det er kun tre uker igjen til første prototype, så må jobbe effektift.\n")

print("Til nå har samarbeidet gått relativt bra, men nå har det oppstått en konflikt mellom to av teammedlemmene.\n")

print(
    "Silje og Sivert er uenige om design og teknologivalg. Konflikten har gått fra saklig uenighet til en mer personlig spenning."
    " Erling må nå bestemme hvordan han vil håndtere situasjonen."
)
# Beslutningspunkt 1
valg1 = input(
    "1) Hvordan bør Erling håndtere konflikten mellom Silje og Sivert?"
    "\nA) Ta konflikten opp i plenum"
    "\nB) Ha individuelle samtaler\nVelg A eller B: "
).upper()

if valg1 == "A":
    print("Erling velger å ta konflikten opp i plenum. Dette skaper åpenhet, men stemningen blir mer anspent.\n")
elif valg1 == "B":
    print("Erling velger individuelle samtaler. Konflikten dempes, og begge føler seg hørt.\n")
else:
    print("Ugyldig valg! Kun A eller B er gyldige alternativer.\n")
# Beslutningspunkt 2
valg2 = input(
    "2) Hvordan bør Erling følge opp den ulmende konflikten mellom Hamdi og Jabir?"
    "\nA) Avholde et felles møte for å avklare uenigheter"
    "\nB) La partene finne ut av det selv\nVelg A eller B: "
).upper()
if valg2 == "A":
    print("Erling holder et felles møte. Begge får forklart sine synspunkter, og en løsning nås.\n")
elif valg2 == "B":
    print("Erling lar partene løse konflikten selv. Spenningen kan fortsatt vokse.\n")
else:
    print("Ugyldig valg! Kun A eller B er gyldige alternativer.\n")
# Beslutningspunkt 3
valg3 = input(
    "3) Hvordan skal prosessen avsluttes?"
    "\nA) Lage en felles avtale for alle"
    "\nB) Gi individuelle utviklingspunkter til hver deltaker\nVelg A eller B: "
).upper()
if valg3 == "A":
    print("Erling lager en felles avtale som alle kan følge.\n")
elif valg3 == "B":
    print("Erling gir hver deltaker individuelle mål og oppgaver.\n")
else:
    print("Ugyldig valg! Kun A eller B er gyldige alternativer.\n")

print("=== Konfliktene er håndtert, og teamet kan fortsette arbeidet ===")

