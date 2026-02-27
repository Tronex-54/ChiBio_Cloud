    elif (program == "C8"):
        current_status = sysData[M]['Custom']['Status']

        if current_status == 0.0:
            sysData[M]['Thermostat']['target'] = 45
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['OD']['target'] = 0.3
            SetOutputOn(M, 'OD', 1)
            sysData[M]['Custom']['Status'] = 1.0

        elif current_status == 1.0:
            sysData[M]['Custom']['param1'] = sysData[M]['Experiment']['cycles']
            sysData[M]['Custom']['Status'] = 3.0
        elif current_status == 3.0:
            if (sysData[M]['Experiment']['cycles'] - sysData[M]['Custom']['param1']) >= 1:
                sysData[M]['Custom']['Status'] = 4.0
        elif current_status == 4.0:
            sysData[M]['Thermostat']['target'] = 25
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['Custom']['Status'] = 2.0
        elif current_status == 2.0:
            addTerminal(M, 'Protocolo Finalizado')
            sysData[M]['Custom']['Status'] = 99.0
        elif current_status == 99.0:
            pass  # Reposo eterno