    elif (program == "C8"):
        current_status = sysData[M]['Custom']['Status']

        if current_status == 0.0:
            sysData[M]['Thermostat']['target'] = 37
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['Custom']['Status'] = 1.0

        elif current_status == 1.0:
            sysData[M]['Thermostat']['target'] = 37
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['Pump1']['target'] = 0.5
            SetOutputOn(M, 'Pump1', 1)
            time.sleep(5)
            SetOutputOn(M, 'Pump1', 0)
            sysData[M]['LEDE']['target'] = 0.1
            SetOutputOn(M, 'LEDE', 1)
            sysData[M]['Custom']['param1'] = sysData[M]['Experiment']['cycles']
            sysData[M]['Custom']['Status'] = 3.0
        elif current_status == 3.0:
            if (sysData[M]['Experiment']['cycles'] - sysData[M]['Custom']['param1']) >= 1:
                SetOutputOn(M, 'LEDE', 0)
                sysData[M]['Custom']['Status'] = 2.0
        elif current_status == 2.0:
            addTerminal(M, 'Protocolo Finalizado')
            sysData[M]['Custom']['Status'] = 99.0
        elif current_status == 99.0:
            pass  # Reposo eterno