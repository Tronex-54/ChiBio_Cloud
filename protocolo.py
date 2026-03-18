    elif (program == "C8"):
        # --- MOTOR DE GENERACIONES BIOLÓGICAS ---
        if 'Generations' not in sysData[M]['Custom']:
            sysData[M]['Custom']['Generations'] = 0.0
        _gr = sysData[M]['GrowthRate']['current']
        if _gr > 0:
            sysData[M]['Custom']['Generations'] += max(0, (_gr / 0.693147) / 60.0)

        current_status = sysData[M]['Custom']['Status']

        if current_status == 0.0:
            sysData[M]['Thermostat']['target'] = 32
            SetOutputOn(M, 'Thermostat', 1)
            sysData[M]['Stir']['target'] = 0.5
            SetOutputOn(M, 'Stir', 1)
            sysData[M]['OD']['target'] = 0.1
            SetOutputOn(M, 'OD', 1)
            sysData[M]['Custom']['Status'] = 1.0

        elif current_status == 1.0:
            sysData[M]['Custom']['param2'] = sysData[M]['Custom'].get('Generations', 0.0)
            sysData[M]['Custom']['Status'] = 3.0
        elif current_status == 3.0:
            if (sysData[M]['Custom'].get('Generations', 0.0) - sysData[M]['Custom']['param2']) >= 3:
                sysData[M]['Custom']['Status'] = 4.0
        elif current_status == 4.0:
            sysData[M]['Custom']['loop_nn6'] = 0
            sysData[M]['Custom']['Status'] = 5.0
        elif current_status == 5.0:
            if sysData[M]['OD']['current'] >= 0.6:
                sysData[M]['Custom']['Status'] = 8.0
        elif current_status == 6.0:
            sysData[M]['Custom']['param1'] = sysData[M]['Experiment']['cycles']
            sysData[M]['Custom']['Status'] = 9.0
        elif current_status == 7.0:
            sysData[M]['Custom']['loop_nn6'] += 1
            if sysData[M]['Custom']['loop_nn6'] < 5:
                sysData[M]['Custom']['Status'] = 5.0
            else:
                sysData[M]['Custom']['Status'] = 6.0
        elif current_status == 8.0:
            sysData[M]['Pump2']['target'] = 1
            SetOutputOn(M, 'Pump2', 1)
            time.sleep(10)
            SetOutputOn(M, 'Pump2', 0)
            sysData[M]['UV']['target'] = 0.2
            SetOutputOn(M, 'UV', 1)
            time.sleep(5)
            SetOutputOn(M, 'UV', 0)
            addTerminal(M, 'limpiando tubo')
            sysData[M]['Custom']['Status'] = 7.0
        elif current_status == 9.0:
            _elapsed = sysData[M]['Experiment']['cycles'] - sysData[M]['Custom']['param1']
            if _elapsed <= 45:
                _target_t = 32 + (25 - 32) * (_elapsed / 45)
                sysData[M]['Thermostat']['target'] = _target_t
                SetOutputOn(M, 'Thermostat', 1)
            else:
                sysData[M]['Thermostat']['target'] = 25
                SetOutputOn(M, 'Thermostat', 1)
                sysData[M]['Custom']['Status'] = 10.0
        elif current_status == 10.0:
            if sysData[M]['FP1']['Emit1'] >= 100:
                sysData[M]['Custom']['Status'] = 11.0
        elif current_status == 11.0:
            sysData[M]['LEDF']['target'] = 0.5
            SetOutputOn(M, 'LEDF', 1)
            sysData[M]['Custom']['param1'] = sysData[M]['Experiment']['cycles']
            sysData[M]['Custom']['Status'] = 12.0
        elif current_status == 12.0:
            if (sysData[M]['Experiment']['cycles'] - sysData[M]['Custom']['param1']) >= 2:
                SetOutputOn(M, 'LEDF', 0)
                sysData[M]['Custom']['Status'] = 13.0
        elif current_status == 2.0:
            addTerminal(M, 'Protocolo Finalizado')
            sysData[M]['Custom']['Status'] = 99.0
        elif current_status == 99.0:
            pass  # Reposo eterno