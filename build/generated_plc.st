PROGRAM program0
  VAR
    sensor AT %IX0.0 : BOOL := 0;
    led_sensor AT %QX0.2 : BOOL := 0;
    led_red AT %QX0.1 : BOOL := 0;
    led_green AT %QX0.0 : BOOL := 0;
    relay AT %QX0.3 : BOOL := 0;
  END_VAR
  VAR
    temporizador : TIME := T#30000ms;
    tiempo_sensor : TIME := T#500ms;
    TOF1 : TOF;
    TP1 : TP;
    _TMP_NOT26_OUT : BOOL;
    _TMP_NOT3_OUT : BOOL;
  END_VAR

  _TMP_NOT26_OUT := NOT(sensor);
  TP1(IN := _TMP_NOT26_OUT, PT := tiempo_sensor);
  TOF1(IN := TP1.Q, PT := temporizador);
  _TMP_NOT3_OUT := NOT(TOF1.Q);
  led_red := _TMP_NOT3_OUT;
  led_sensor := _TMP_NOT26_OUT;
  led_green := TOF1.Q;
  relay := TOF1.Q;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : program0;
  END_RESOURCE
END_CONFIGURATION
