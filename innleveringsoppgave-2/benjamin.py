print("\n=== Prosjektledelse og konflikthåndtering ===\n")

print("Erling leder et team bestående av: Sivert, Silje, Hamdi, Hallgeir, Noa og Jabir.")
print("Det er tre uker igjen til første prototype, og trykket øker.\n")

print("En konflikt har oppstått mellom Silje og Sivert.")
print("Det som startet som faglig uenighet, har utviklet seg til en mer personlig konflikt.\n")

# -------------------------
# Valgpunkt 1
# -------------------------

svar1 = input(
    "1) Hvordan bør Erling løse konflikten mellom Silje og Sivert?"
    "\nA) Ta konflikten opp i plenum foran hele teamet"
    "\nB) Ta individuelle samtaler med begge to"
    "\nDitt valg (A/B): "
).strip().upper()

if svar1 == "A":
    print("\nErling tar konflikten i plenum. Det skaper åpenhet, men øker også spenningen i teamet.\n")
elif svar1 == "B":
    print("\nErling tar individuelle samtaler. Begge føler seg hørt, og situasjonen roer seg litt.\n")
else:
    print("\nUgyldig valg – husk å skrive A eller B.\n")
# -------------------------
# Valgpunkt 2
# -------------------------

svar2 = input(
    "2) Hvordan bør Erling håndtere uenigheten mellom Hamdi og Jabir?"
    "\nA) Arrangere et møte der begge får snakke ut"
    "\nB) Overlate til dem selv å løse uenigheten"
    "\nDitt valg (A/B): "
).strip().upper()

if svar2 == "A":
    print("\nErling samler begge til et møte. De får forklart synspunktene sine og finner en løsning.\n")
elif svar2 == "B":
    print("\nErling lar dem ordne opp selv. Dette kan føre til at spenningen øker.\n")
else:
    print("\nUgyldig valg – kun A eller B er gyldige.\n")

# -------------------------
# Valgpunkt 3
# -------------------------

svar3 = input(
    "3) Hvordan bør Erling avslutte konflikten?"
    "\nA) Lage en felles avtale for hele teamet"
    "\nB) Gi hver deltaker individuelle utviklingspunkter"
    "\nDitt valg (A/B): "
).strip().upper()

if svar3 == "A":
    print("\nErling lager en felles avtale som hele teamet skal følge videre.\n")
elif svar3 == "B":
    print("\nErling gir individuelle tilbakemeldinger og mål til hver deltaker.\n")
else:
    print("\nUgyldig valg – husk A eller B.\n")

print("=== Konfliktene er håndtert, og teamet kan gå videre i prosessen ===")
