PROGRAM program0
  VAR
    sensor AT %IX0.0 : BOOL := 0;
    led_R AT %QW0 : UINT := 0;
    led_G AT %QW1 : UINT := 0;
    led_B AT %QW2 : UINT := 0;
    led_sensor AT %QX0.2 : BOOL := 0;
    led_red AT %QX0.1 : BOOL := 0;
    led_green AT %QX0.0 : BOOL := 0;
    relay AT %QX0.3 : BOOL := 0;
  END_VAR
  VAR
    temporizador : TIME := T#30s;
    intensidad : INT := 30000;
    tiempo_superior : INT := 30;
    tru : BOOL := 1;
    tiempo_inferior : INT := 20;
    time_blink : TIME := T#500ms;
    tiempo_sensor : TIME := T#500ms;
    TOF1 : TOF;
    TP2 : TP;
    TP4 : TP;
    TP5 : TP;
    TP6 : TP;
    TP7 : TP;
    _TMP_NOT3_OUT : BOOL;
    _TMP_NOT4_OUT : BOOL;
    _TMP_TIME_TO_INT51_OUT : INT;
    _TMP_LT74_OUT : BOOL;
    _TMP_GT5_OUT : BOOL;
    _TMP_AND75_OUT : BOOL;
    _TMP_NOT29_OUT : BOOL;
    _TMP_AND2_OUT : BOOL;
    _TMP_NOT25_OUT : BOOL;
    _TMP_AND23_OUT : BOOL;
    _TMP_NOT24_OUT : BOOL;
    _TMP_NOT1_OUT : BOOL;
    _TMP_AND79_OUT : BOOL;
    _TMP_BOOL_TO_INT43_OUT : INT;
    _TMP_MUL22_OUT : INT;
    _TMP_INT_TO_UINT42_OUT : UINT;
    _TMP_BOOL_TO_INT37_OUT : INT;
    _TMP_MUL35_OUT : INT;
    _TMP_INT_TO_UINT36_OUT : UINT;
    _TMP_BOOL_TO_INT39_OUT : INT;
    _TMP_MUL41_OUT : INT;
    _TMP_INT_TO_UINT38_OUT : UINT;
  END_VAR

  _TMP_NOT3_OUT := NOT(sensor);
  TP2(IN := _TMP_NOT3_OUT, PT := T#1ms);
  TOF1(IN := TP2.Q, PT := temporizador);
  _TMP_NOT4_OUT := NOT(TOF1.Q);
  led_red := _TMP_NOT4_OUT;
  led_green := TOF1.Q;
  relay := TOF1.Q;
  led_sensor := _TMP_NOT3_OUT;
  _TMP_TIME_TO_INT51_OUT := TIME_TO_INT(TOF1.ET);
  _TMP_LT74_OUT := LT(_TMP_TIME_TO_INT51_OUT, tiempo_superior);
  _TMP_GT5_OUT := GT(_TMP_TIME_TO_INT51_OUT, tiempo_inferior);
  _TMP_AND75_OUT := AND(_TMP_LT74_OUT, _TMP_GT5_OUT);
  _TMP_NOT29_OUT := NOT(TP5.Q);
  _TMP_AND2_OUT := AND(_TMP_NOT29_OUT, _TMP_AND75_OUT);
  TP4(IN := _TMP_AND2_OUT, PT := T#500ms);
  _TMP_NOT25_OUT := NOT(TP4.Q);
  _TMP_AND23_OUT := AND(_TMP_NOT29_OUT, _TMP_NOT25_OUT, _TMP_AND75_OUT);
  TP7(IN := _TMP_AND23_OUT, PT := T#500ms);
  _TMP_NOT24_OUT := NOT(TP7.Q);
  TP6(IN := _TMP_NOT24_OUT, PT := T#1ms);
  _TMP_NOT1_OUT := NOT(TP6.Q);
  _TMP_AND79_OUT := AND(_TMP_AND75_OUT, _TMP_NOT1_OUT);
  TP5(IN := _TMP_AND79_OUT, PT := T#500ms);
  _TMP_BOOL_TO_INT43_OUT := BOOL_TO_INT(TP5.Q);
  _TMP_MUL22_OUT := MUL(_TMP_BOOL_TO_INT43_OUT, intensidad);
  _TMP_INT_TO_UINT42_OUT := INT_TO_UINT(_TMP_MUL22_OUT);
  led_R := _TMP_INT_TO_UINT42_OUT;
  _TMP_BOOL_TO_INT37_OUT := BOOL_TO_INT(TP4.Q);
  _TMP_MUL35_OUT := MUL(_TMP_BOOL_TO_INT37_OUT, intensidad);
  _TMP_INT_TO_UINT36_OUT := INT_TO_UINT(_TMP_MUL35_OUT);
  led_G := _TMP_INT_TO_UINT36_OUT;
  _TMP_BOOL_TO_INT39_OUT := BOOL_TO_INT(TP7.Q);
  _TMP_MUL41_OUT := MUL(_TMP_BOOL_TO_INT39_OUT, intensidad);
  _TMP_INT_TO_UINT38_OUT := INT_TO_UINT(_TMP_MUL41_OUT);
  led_B := _TMP_INT_TO_UINT38_OUT;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : program0;
  END_RESOURCE
END_CONFIGURATION
