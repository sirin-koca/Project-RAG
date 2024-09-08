# GitHub Arbeidsflyt for Teamet

## 1. Opprette og Bruke Branches
For å sikre at hovedbranchen (`main`) forblir stabil, skal hvert teammedlem opprette og jobbe på egne branches.

### Opprette en ny branch
- Naviger til din lokale kopi av repositoryet i terminalen (eller PyCharm).
- For å opprette og bytte til en ny branch, kjør:
  ``` git checkout -b <branch-name>  ```
  
## 2. Navngivning av Branches
Navngi branches på en beskrivende måte basert på funksjonen eller oppgaven. Eksempler inkluderer:

feature-login
bugfix-header
update-readme

## 3. Arbeide med Kode og Gjøre Commits
Lag endringer lokalt og gjør commits ofte med beskrivende meldinger.

Lage en commit
Legg til endrede filer:
bash
Kopier kode
git add .
Lag en commit med en beskrivende melding:
bash
Kopier kode
git commit -m "Beskriv hva endringene innebærer og hvorfor de er gjort"

## 4. Synkronisere med GitHub (Remote)
Push dine lokale endringer til GitHub for å sikre at teamet har tilgang til din nyeste kode.

Push til GitHub
For å push din branch til GitHub, kjør:
bash
Kopier kode
git push origin <branch-name>

## 5. Opprette Pull Requests (PR)
En PR brukes for å foreslå og diskutere endringer før de merges inn i hovedbranchen.

### Opprette en Pull Request
* Gå til GitHub-repoet ditt.
* GitHub vil foreslå å opprette en PR hvis en ny branch nylig har blitt pushet.
* Følg instruksjonene på skjermen for å opprette en PR, inkludert en tittel og en detaljert beskrivelse.

## 6. Gjennomgang og Godkjenning av PR
Teammedlemmer bør gjennomgå hverandres PRs, gi tilbakemeldinger og godkjenne endringer.

### Review prosess
* Les gjennom endringene og legg igjen kommentarer om nødvendig.
* Juster koden basert på tilbakemeldinger og push oppdateringene.

## 7. Merge PR til Main
Når en PR er godkjent, kan den merges inn i main.

### Merge en PR
* Bruk "Merge pull request"-knappen på GitHub.
* Det anbefales å slette branchen etter merge for å holde repoet ryddig.

## Beste Praksis
* Kommuniser tydelig og effektivt i commits og PRs.
* Oppdater regelmessig din branch med main for å unngå merge-konflikter.
```
git checkout main
git pull
git checkout <your-branch>
git merge main
```

Dette dokumentet er ment som en oversikt over standard arbeidsflyt og beste praksiser for GitHub-bruk i prosjektet.

[sirin-koca](https://github.com/sirin-koca)

