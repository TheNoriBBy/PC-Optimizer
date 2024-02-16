# run as administrator
import os
import psutil

def disable_telemetry():
    os.system('sc delete DiagTrack')
    os.system('sc delete dmwappushservice')
    os.system('echo "" > C:\\ProgramData\\Microsoft\\Diagnosis\\ETLLogs\\AutoLogger\\AutoLogger-Diagtrack-Listener.etl')
    os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')

def disable_office_telemetry():
    os.system('sc delete "OfficeSvc"')


def clean_system():
    os.system('cleanmgr /sagerun:1')

def flush_dns():
    os.system('ipconfig /flushdns')


def inspect_hardware():
    print(psutil.virtual_memory())
    print(psutil.cpu_percent(interval=1))

if __name__ == "__main__":
    print("Starting PC Optimizer Tool...")
    disable_telemetry()
    clean_system()
    flush_dns()
    inspect_hardware()
    print("Optimization complete.")
