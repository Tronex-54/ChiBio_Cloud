    elif (program == "C8"):
        current_status = sysData[M]['Custom']['Status']

        if current_status == 0.0:
            sysData[M]['Thermostat']['target'] = 30
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['Custom']['Status'] = 1.0

        elif current_status == 1.0:
            sysData[M]['LEDG']['target'] = 0.1
            SetOutputOn(M, 'LEDG', 1)
            time.sleep(5)
            SetOutputOn(M, 'LEDG', 0)
            sysData[M]['Pump3']['target'] = 0.5
            SetOutputOn(M, 'Pump3', 1)
            time.sleep(3)
            SetOutputOn(M, 'Pump3', 0)
            sysData[M]['Custom']['Status'] = 2.0
        elif current_status == 2.0:
            addTerminal(M, 'Protocolo Finalizado')
            sysData[M]['Custom']['Status'] = 99.0
        elif current_status == 99.0:
            pass  # Reposo eterno