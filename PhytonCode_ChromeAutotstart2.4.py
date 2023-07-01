import webbrowser
import pyautogui
import time
import pythoncom
import win32com.client as wincl

def main():
    url = "https://chat.openai.com/"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open(url)

    # Kurze Wartezeit, um sicherzustellen, dass die Seite geladen wurde
    time.sleep(10)

    # Tastenkombination "Alt+Shift+S" ausführen
    pyautogui.hotkey('alt', 'shift', 's')

    # Weitere Schritte ausführen, um mit der Erweiterung zu interagieren
    # ...

def register_in_startup():
    pythoncom.CoInitialize()
    TaskScheduler = wincl.Dispatch('Schedule.Service')
    TaskScheduler.Connect()
    rootFolder = TaskScheduler.GetFolder('\\')
    taskDefinition = TaskScheduler.NewTask(0)
    colTriggers = taskDefinition.Triggers
    trigger = colTriggers.Create(8)  # Trigger bei Systemstart
    trigger.Id = 'StartupTrigger'
    colActions = taskDefinition.Actions
    action = colActions.Create(0)  # Aktionstyp: Ausführen einer Anwendung
    action.Path = 'pythonw.exe'  # Pfad zur Python-Interpreter-Exe
    action.Arguments = 'Pfad\\zu\\deinem\\Skript.py'  # Pfad zu deinem Skript
    action.WorkingDirectory = 'Pfad\\zu\\deinem\\Arbeitsverzeichnis'  # Arbeitsverzeichnis für das Skript
    rootFolder.RegisterTaskDefinition('TaskName', taskDefinition, 6, '', '', 3)  # Task registrieren

if __name__ == "__main__":
    main()
    register_in_startup()