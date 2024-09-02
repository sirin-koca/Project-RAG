# DATA3710 & DATA3750 
## Applied AI - RAG PROJECT 🤖
Bruk av Retrieval Augmented Generation (RAG- modeller) i Utviklingen av en LLM-basert Chatbot for helserelaterte spørsmål.

## Intro :.
### Bakgrunn og målsettinger:
- Prosjektet er relevant for andre prosjekter innenfor CIM (https://www.oslomet.no/cim)
- Målet er å trene en lokal språkmodell slik at den kan svare på helserelaterte problemer.

### Project description
Prosjektet vil starte med å utforske hvordan man både kjører og trener lokale språkmodeller på GPU-servere ved OsloMet. At modellene er lokale er avgjørende med tanke på sensitive data. Et viktig aspekt er såkalte "hallusinisasjoner" hvor språkmodeller som ChatGPT kommer med svar som er fullstendig gale. Et av målene med RAG-modeller er å begrense hallusinasjoner så mye som mulig. Et viktig mål med prosjektet er å redusere mengden hallusinasjoner så mye som mulig.

### Final deliverable
Det forventes at prosjektet resulterer både i en fungerende chatbot og i en rapport som
beskriver resultater fra testkjøringer, spesielt med tanke på hallusinasjoner.

## Fase1: DATA PREPROCESSING

## Grunnleggende Dataforberedelsesoperasjoner i et Data Science-prosjekt

### 1. **Datavask**
   - **Håndtering av Manglende Data:** Identifisere og håndtere manglende data ved enten å fylle ut, interpolere, eller fjerne rader/kolonner.
   - **Outlier Deteksjon:** Identifisere og potensielt fjerne avvik som kan påvirke modellens ytelse negativt.
   - **Datakonvertering:** Sikre at all data har riktig format (f.eks. konvertering av strenger til datoer eller tall).
   - **Tekstnormalisering:** For tekstdata, kan normalisering innebære å endre til små bokstaver, fjerne tegnsetting, og stemming/lemmatisering.

### 2. **Datatransformasjon**
   - **Funksjonsutvikling:** Skap nye funksjoner som kan forbedre modellens ytelse, som å trekke ut nøkkelord, oppsummere tekst, eller lage dummyvariabler fra kategoriske data.
   - **Skalering/Normalisering:** Anvend skalering (f.eks. Min-Max Scaling, Standard Scaling) på numerisk data for å sikre at den passer innenfor et standardområde, noe som er avgjørende for mange maskinlæringsalgoritmer.
   - **Vektorisering:** For tekstdata, konverter teksten til numeriske vektorer ved hjelp av teknikker som TF-IDF, Word2Vec, eller BERT-innbygginger.

### 3. **Dataintegrasjon**
   - **Sammenslåing av Datasett:** Kombiner ulike datasett (f.eks. slå sammen akademiske artikler med emnetagger) basert på en felles nøkkel eller indeks.
   - **Dataaggregering:** Aggreger data på forskjellige nivåer (f.eks. månedlige gjennomsnitt) for å forstå trender eller for tidsserieanalyse.

### 4. **Datafiltrering og Sampling**
   - **Filtrering av Relevant Data:** Behold kun data som er relevant for prosjektets omfang, som å velge spesifikke AI-emner eller papirkategorier.
   - **Datasampling:** I tilfelle av store datasett kan sampling være nødvendig for å gjøre beregninger mer håndterbare under innledende eksperimenter.

### 5. **Dataannotasjon**
   - **Tagging:** Annoter data med etiketter eller tagger, spesielt i prosjekter der tagging av akademiske artikler med AI-emner er nødvendig. Dette trinnet er avgjørende for oppgaver som likhetssøk.

### 6. **Utforskende Dataanalyse (EDA)**
   - **Grunnleggende Statistikk:** Beregn beskrivende statistikk som gjennomsnitt, median, modus, og standardavvik.
   - **Visualiseringer:** Lag grunnleggende diagrammer (f.eks. histogrammer, boksdiagrammer) for å forstå datadistribusjoner og forhold mellom variabler.
   - **Korrelasjonsanalyse:** Analyser korrelasjoner mellom ulike variabler for å identifisere potensielle sammenhenger som kan være nyttige for modellering.



---

Sirin Koca | Gruppe Project | OsloMet 2024
