#Score for sluttresultatet
score = 0

# Funksjon for å hente valg med input
def hent_valg(tekst):
    valg = ""
    while valg not in ["A", "B"]:
        valg = input(tekst).upper()
        if valg not in ["A", "B"]:
            print("Feil input! Du må skrive A eller B.\n")
    return valg


print("\nHistorien om Erling og prosjektteamet\n")


#  intro / Historien

print("Erling er prosjektleder for kommunens nye digitale medborgerportal.")
print("Prosjektet er inne i sin sjette uke, og teamet har begynt å møte utfordringer.\n")

print("Konflikten mellom Silje og Sivert har utviklet seg fra faglig uenighet til en mer personlig konflikt.")
print("Erling må ta viktige valg for å håndtere situasjonen.\n")



# beslbeslutning 1: Silje og Sivert

print("--- SITUASJON 1: Konflikt mellom Silje og Sivert ---")
print("A: Ta konflikten i plenum")
print("B: Ha individuelle samtaler")

valg1 = hent_valg("Valg (A/B): ")

if valg1 == "A":
    print("\nErling tar opp konflikten i plenum.")
    print("Det skaper åpenhet, men stemningen blir mer anspent.\n")
    score -= 1

elif valg1 == "B":
    print("\nErling tar individuelle samtaler.")
    print("Han får bedre innsikt i begge parters perspektiver og demper temperaturen.\n")
    score += 1


# besluting 2: Hamdi og Jabir

print("--- SITUASJON 2: Den ulmende saken ---")
print("Hamdi og Jabir er uenige om hvordan innbyggerne skal delta i digitale folkemøter.")
print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform.")
print("Jabir ønsker et mer åpent dialogbasert system med rom for spontane innspill.\n")

print("A: Holde et felles møte for å avklare uenigheter")
print("B: Avvente og håpe konflikten løser seg selv")

valg2 = hent_valg("Valg (A/B): ")

if valg2 == "A":
    print("\nErling samler alle til et felles møte.")
    print("Alle får forklare sine behov og en kompromissløsning oppnås.")
    print("Teamet får trygghet og felles retning.\n")
    score += 1

elif valg2 == "B":
    print("\nErling avventer og håper konflikten løser seg selv.")
    print("Uenigheten eskalerer, frustrasjonen øker og samarbeidet svekkes.\n")
    score -= 1


# beslutning 3: Lav motivasjon i teamet

print("--- SITUASJON 3: Lav motivasjon ---")
print("A: Prioritere relasjonsbygging")
print("B: Fokusere på leveranser")

valg3 = hent_valg("Valg (A/B): ")

if valg3 == "A":
    print("\nErling prioriterer relasjonsbygging.")
    print("Teamet opplever større trygghet. Bedre samarbeid og økt motivasjon.\n")
    score += 1

elif valg3 == "B":
    print("\nErling fokuserer på leveranser.")
    print("Teamet får retning og fremdrift, men konflikter og stress kan øke.\n")
    score -= 1


# utfallet

print("--- SLUTTRESULTAT ---\n")

if score >= 2:
    print("Teamet klarer å gjenopprette samarbeidet.")
    print("Prototypen leveres med god kvalitet.\n")

elif score >= 0:
    print("Teamet leverer prototypen, men det er fortsatt spenninger.")
    print("Samarbeidet kunne vært bedre.\n")

else:
    print("Konfliktene fortsetter og samarbeidet svekkes.")
    print("Prototypen blir forsinket og kvaliteten er dårligere enn forventet.\n")

print("Takk for at du hjalp Erling.")
