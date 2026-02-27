    elif (program == "C8"):
        current_status = sysData[M]['Custom']['Status']

        if current_status == 0.0:
            sysData[M]['Thermostat']['target'] = 37
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['Stir']['target'] = 0.5
            SetOutputOn(M, 'Stir', 1)
            sysData[M]['OD']['target'] = 0.3
            sysData[M]['Custom']['Status'] = 1.0

        elif current_status == 1.0:
            if sysData[M]['ThermometerIR']['current'] == 37:
                sysData[M]['Custom']['Status'] = 3.0
        elif current_status == 3.0:
            sysData[M]['LEDA']['target'] = 0.7
            SetOutputOn(M, 'LEDA', 1)
            time.sleep(2)
            SetOutputOn(M, 'LEDA', 0)
            sysData[M]['Pump1']['target'] = 0.5
            SetOutputOn(M, 'Pump1', 1)
            time.sleep(5)
            SetOutputOn(M, 'Pump1', 0)
            sysData[M]['Custom']['Status'] = 2.0
        elif current_status == 2.0:
            addTerminal(M, 'Protocolo Finalizado')
            sysData[M]['Custom']['Status'] = 99.0
        elif current_status == 99.0:
            pass  # Reposo eterno