# Anleitung zur Einrichtung des Sprachassistenten "Talk to Chat GPT": # 

**System- und Hardware-Anforderungen:** 

Mini-PC mit  Windows 10 64Bit- Betriebssystem oder höher, 1,5 GHz CPU und 4 GB RAM, mindestens 30 GB SSD- (HDD-) Speicher, sowie einer Bluetooth- Schnittstelle. 

**Zubehör:** 

Du benötigst eine Bluetooth-Anbindung sowie eine Bluetooth-Lautsprecherbox mit integriertem Mikrofon. 

Verbinde die Bluetooth-Lautsprecherbox mit dem Mini-PC und stelle sicher, dass Audioeingang und Audioausgang über Bluetooth funktionieren. 

###Installation:###  

**Schritt 1:** Voraussetzungen überprüfen. Stelle sicher, dass dein Betriebssystem mindestens Windows 10  ist, da der Task Scheduler (zu deutsch Aufgabenplanung genannt) benötigt wird. Stelle außerdem sicher, dass der Google Chrome Browser auf deinem System installiert ist. 

**Schritt 2:** Die "Talk to Chat GPT"-Erweiterung installieren. Öffne den Google Chrome Browser und gehe zum Web Store. Suche nach der "Talk to Chat GPT"-Erweiterung und installiere sie. 

**Schritt 3:** Die “AutostartGPT.bat”-Datei und das Python-Skript (GPTAssistent.exe) vorbereiten.  

Stelle sicher, dass du die zur Verfügung gestellte AutostartGPT.bat-Datei und das Python-Skript (GPTAssistent.exe) bereits heruntergeladen hast.   

Diese Dateien findest du in einem Ordner mit dem Namen “dist”, welcher als dist.zip-Datei (bzw. als dist.rar) zum Download für dich bereitsteht.  

###Wichtig!###  

Entpacke die Dateien und kopiere den Ordner “dist” nach dem Entpacken unbedingt in folgendes Verzeichnis:  

C:\Program Files (x86) 

So dass der benötigte Dateipfad nun lautet:  

C:\Program Files (x86)\dist\ 

In dem Ordner mit dem Namen “dist” befindet sich die zuvor erwähnte “AutostartGPT.bat”- Datei, welche in den nächsten Schritten benötigt wird, um eine automatisierte Aufgabe zu erstellen.  

*Hinweis:* (Die AutostartGPT.bat-Datei sollte auf das Python-Skript (GPTAssistent.exe) verweisen, während das Python-Skript den Browserpfad, den Link zum automatischen Öffnen der Chat GPT-Internetseite und das automatische Starten der "Talk to Chat GPT"-Erweiterung enthält). 

**Schritt 4:** (dieser Schritt wird nur benötigt, falls es Probleme bei der Automatisierung gibt. Ansonsten geht es für dich an dieser Stelle weiter mit Schritt 5)  

Anpassung der “AutostartGPT.bat”-Datei. Öffne die AutostartGPT.bat-Datei in einem Texteditor deiner Wahl und überprüfe den Inhalt. Stelle sicher, dass der Pfad zur “GPTAssistent.exe”-Datei, welche das benötigte Python-Skript enthält, korrekt angegeben ist.  

Normalerweise sollte der in der AutostartGPT.bat- Datei angegebene Pfad bereits korrekt eingetragen sein.  

Der in der AutostartGPT.bat- Datei hinterlegte Pfad sollte wie folgt aussehen:  

######################################## 

*@echo off 

cd "C:\Program Files (x86)\dist\ChromeAutotstart2.4\" 

start GPTAssistent.exe* 

######################################## 

Falls es nötig sein sollte, den Pfad zu ändern, dann ändere den Pfad entsprechend und speichere die AutostartGPT.bat-Datei erneut im Verzeichnis  

C:\Program Files (x86)\dist\ChromeAutotstart2.4 

 

**Schritt 5:** Einbindung der AutostartGPT.bat-Datei in die Aufgabenplanung.  

Öffne den "Task Scheduler" (Aufgabenplanung) auf deinem Windows-System, in dem du über die, in der Taskleiste unten links integrierte Windows- Suchfunktion, die sogenannte “Aufgabenplanung” aufrufst.  

Öffne die “Aufgabenplanung” (Task Scheduler) und erstelle dort nun eine neue Aufgabe.   

Benenne die von dir erstellten Aufgabe mit einem passenden Namen, wie zum Beispiel "Autostart Assistent". 

Navigiere zur Registerkarte "Trigger" und klicke auf "Neu". Wähle "Bei der Anmeldung" als Trigger aus und bestätige die Einstellungen. 

Gehe zur Registerkarte "Aktionen" und klicke auf "Neu". Wähle "Programm starten" als Aktion aus und gib den Pfad zur zuvor mehrfach erwähnten “AutostartGPT.bat”-Datei an. 

Navigiere zu den weiteren Registerkarten, um weitere Anpassungen vorzunehmen, falls erforderlich. Klicke dann auf "OK", um die Aufgabe zu speichern. 

**Schritt 6:** Systemneustart durchführen. Um sicherzustellen, dass der Sprachassistent automatisch gestartet wird, wenn das System hochfährt, solltest du einen Neustart durchführen. 

(Tipp: Stelle die Windows-Anmeldung so ein, dass der Benutzer nach dem Systemstart automatisch angemeldet wird.) 

*Hinweis:*  

Sollte es entgegen der Erwartung zu Problemen bei der Automatisierung kommen und der Sprachassistent nicht wie gewünscht starten, dann überprüfe nochmals das Vorgehen nach Anleitung aus Schritt 4 

**Schritt 7:** Verwendung des Sprachassistenten. Nach dem Neustart sollte der Sprachassistent nach einer kurzen Wartezeit von *1-2 Minuten* automatisch gestartet werden. Diese Wartezeit ist nötig, um sicherzustellen, dass das System gestartet und vollständig geladen wurde. 

Der Google Chrome Browser sollte sich öffnen und die "Talk to Chat GPT"-Erweiterung sollte geladen und nach einer weiteren Wartezeit von *10 Sekunden* gestartet werden. 

Du kannst nun den Sprachassistenten verwenden, indem du mit der Erweiterung durch Sprache interagierst. Die Erweiterung ermöglicht Sprach-zu-Text- und Text-zu-Sprache-Konvertierung. 

Ich wünsche dir nun viel Freude mit diesem Opensurce- Projekt und deinem persönlichen ChatGPT Sprachassistenten.  

 

 

Liebe Grüße:  Manuel Person  


##Dieses Open- Surce- Projekt schließte alle Weiterentwicklungen unter anderen Betriebssystemen und Browser ein.##
