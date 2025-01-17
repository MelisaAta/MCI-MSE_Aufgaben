## Project background

### Purpose of project

Eine Software, die für die diagnostizierung der Leistung anhand eines Ergometers entwickelt wurde.
Die zu erbringende Leistung der Probanden:innen kann vom Ergometer eingestellt werden und auch die erbrachte Leistung und Elektrodiagramm werden zunächst als Daten abgespeichert. Diese Daten werden dann anhand der Software ausgewertet und visualisiert.

### Scope of project

Die Software erleichtert hiermit die Datenaufnahme und -verabeitung bei der Durchführung einer Leistungsdiagnostik. Im Großen und Ganzen beeinflusst dies den Prabanden in keiner hinsicht. 

### Other background information

Grundsätzlich ist nur der Name, die technische ID, und das Geburtsdatum der Probanden:innen erforderlich.

## Perspectives
### Who will use the system?

Die Software wird grundsätzlich nur vom Auftraggeber, der Hersteller von Ergometern ist, genutzt und dient zur Aufzeichnung und Darstellung der erbrachten Leistung der Probanden.

### Who can provide input about the system?

Der Inout für die Daten die die Software zum Verarbeiten benötigt, wird vom Probanden zu Verfügung gestellt. Anhand eines 3 minütigen Testes wird der Puls und die erbrachte Leistung als Zeitreihe erfasst und gespeichert.


## Project Objectives
### Known business rules

Im Lastenheft sind alle vom Auftraggeber gegebenen Regeln für die Entwicklung von der Software im Detail beschrieben.

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

(Programmierabgabe Nr.1: Annahmen gelten als gewisses Risiko, das es gilt zu erkennen und zu minimieren. Eine Annahme ist in diesem Fall die Feststellung, dass die Kriterien des Auftraggebers im Lastenheft erfüllt sind.)

Die vorhandenen Dateien unterteilen sich grundsätzlich in 3 Informationsgruppen: (1) perönliche Daten zu den Probanden, (2) erbrachte Leistung während Test und die (3)aufgezeichneten EKG-Daten.
Zur ersten Gruppe zählen die Dateien "subject_1", "subject_2" und "subject_3". In Ihnen steht die jeweilige ID-Nummer, das Geburtsjahr, die vorgesehene Leistung. Zudem wird auch die Testdauer mit 180 Sekunden, also 3 Minuten, angegeben.
Die Dateien der zweiten sind Gruppe sind : "power_data_1", "power_data_2" und "power_data_3". Sie beinhalten die tatsächlich, pro Sekunde erfasste, erbrachte Leistung des jeweiligen Probanden.
Die dritte Gruppe wird durch die Dateien "ecg_data_subject_1", "ecg_data_subject_2" und "ecg_data_subject_3" repräsentiert. Aus der Zeilenanzahl lässt sich schließen, dass es sich um ein EKG mit einer 1000Hz Aufzeichnung handelt.

### Design and implementation constraints

Bis auf Weiteres soll das Tool mittels Kommandozeile bedient werden. Also wird es kein Nutzerinterface geben, da es anfänglich sehr einfach geschrieben werden soll.

## Risks

Es kann immer wieder dazu kommen, dass die Durchläufe als ungültig gelten. Es kann mehrere Gründe zum Abbruch geben, die von den Diagnostikern nach Begutachtung der Daten manuell vermerken können. Erfolgreiche und abgebrochene Daten sollen dann in seperaten Ordnern gespeichert werden.

## Known future enhancements

Der Auftraggeber will zunächst eine sehr einfach geschrieben Software haben, die die Daten auswertet und visualisiert. Dies kann in Zukunft natürlich weiter ausgarbeitet und verbessert werden. Beispielsweise kann das Tool in Zukunft ein Kundenfreundliches Nutzerinterace verfügen und mehr Funktionen bieten.

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

Im Abschnitt "Risks" wurde erwähnt, dass es teilst zu ungültigen Durchläufen kommen kann. Dieser Fehler sollte in Zukunft, wenn möglich, behoben werden.
