# IS-118 Innleveringsoppgave William

print("\nErling er prosjektleder for et team som jobber med en ny digital medborgerportal.")
print("Teamet består av: Silje, Sivert, Hamdi, Hallgeir og Noa.")
print("Det er tre uker til prototypen skal leveres, og stemningen har begynt å bli litt anspent.\n")

print("Konflikten mellom Silje og Sivert har gått fra faglig uenighet til noe mer personlig.")
print("Erling må nå ta stilling til hvordan han vil håndtere situasjonen.\n")

# --- Beslutningspunkt 1 ---
valg1 = input("1) Skal Erling ta opp konflikten i plenum (A) eller ta individuelle samtaler (B)? ").upper()

if valg1 == "A":
    print("\nErling tar opp konflikten i plenum. Det blir litt opphetet, og stemningen er fortsatt anspent.")
elif valg1 == "B":
    print("\nErling gjennomfører individuelle samtaler. Dette roer situasjonen litt og gir bedre forståelse.")
else:
    print("\nUgyldig valg. Det finnes bare A eller B.")

# --- Beslutningspunkt 2 ---
print("\nHamdi og Jabir begynner også å bli uenige om hvordan innbyggerne skal delta i digitale møter.")
valg2 = input("2) Skal Erling samle dem i et felles møte (A) eller avvente og håpe de løser det selv (B)? ").upper()

if valg2 == "A":
    print("\nErling kaller inn til et møte. Gruppen klarer å bli enige om et kompromiss.")
elif valg2 == "B":
    print("\nErling avventer, men konflikten vokser og påvirker teamet negativt.")
else:
    print("\nUgyldig valg. Det finnes bare A eller B.")

# --- Beslutningspunkt 3 ---
print("\nTeamet begynner å bli slitne, og motivasjonen faller.")
valg3 = input("3) Skal Erling sette av tid til relasjonsbygging (A) eller fokusere på leveranser (B)? ").upper()

if valg3 == "A":
    print("\nTeamet får snakket ut litt og samarbeidet blir bedre.")
elif valg3 == "B":
    print("\nFokus på leveranser gir retning, men også mer stress i teamet.")
else:
    print("\nUgyldig valg. Det finnes bare A eller B.")

print("\n=== Historien er ferdig ===")
print("Basert på valgene dine kunne teamet enten bli sterkere, fungere greit eller streve under press.\n")

