print("Erling leder et team på fem personer, som har fungert greit ilag frem til nylig.")
print("Silje, Sivert, Jabir, Hamdi, Hallgeir og Noa er teamtes deltakere, og nå har det oppstått konflikt mellom Silje og Sivert.")
print("Silje og Sivert er uenige om fremgangsmåte i arbeidet, og konflikten har blitt mer og mer intens og emosjonell.")
print("Erling er nødt til å gripe inn for å forhindre at konflikten saboterer prosjektet, som de allerede har dårlig tid på å ferdigstille.")
print("Erling må bestemme seg for hvordan han skal gå frem med dette.")

#Beslutningspunkt 1

valg=input("Velg 1 for å snakke med de i plenum, eller 2 for å snakke med dem individuelt.")
if valg == "1":
    print("Erling velger å ta opp konflkten i plenum.")
    print("Han snakker med Silje og Sivert for å oppnå enighet og oppklaring.")

elif valg == "2":
    print("Erling velger å ta samtalene individuelt med Silje og Sivert.")
    print("Han snakker med Silje først, og deretter med Sivert for å forstå begge sitt synspunkt.")

else:
    print("Ugyldig valg, velg mellom 1 og 2.")
              

#Beslutningspunkt 2

valg2=input("Etter samtalene, velg 1 for å mekle mellom dem, eller 2 for. la dem finne en løsning selv.")

if valg2 == "1":
    print("Erling velgr å hjelpe til med å mekle mellom Silje og Sivert, de finner en felles løsning.")
elif valg2 == "2":
    print("Erling lar silje og sivert finne en løsning selv, de kommer ikke frem til en god løsning og konflikten fortsetter.")
else: 
    print("Ugyldig valg, vennligst velg mellom 1 og 2.")


#Beslutningspunkt 3

valg3=input("Velg 1 for å involvere HR, eller 2 for å sette regler for fremtidig arbeid og konsekvenser ved brudd.")

if valg3== "1":
    print("Erling involverer HR ettersom konflikten viser seg å være for stor for ham å handtere alene.")
    print("HR bistår med proffesjonell mekling/konflikthåndtering.")

elif valg3== "2":
    print("Erling setter klare regler for fremtidig arbeid, og hva som skjer ved brudd av avtalen de lager.")
    print("Silje og Sivert blir inforstått med reglene, det er usikkert om konflikten løser seg.")

else: 
    print("Ugyldig valg, du må velge mellom 1 og 2.")

