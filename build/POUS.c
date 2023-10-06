void LOGGER_init__(LOGGER *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->MSG,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->LEVEL,LOGLEVEL__INFO,retain)
  __INIT_VAR(data__->TRIG0,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void LOGGER_body__(LOGGER *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  if ((__GET_VAR(data__->TRIG,) && !(__GET_VAR(data__->TRIG0,)))) {
    #define GetFbVar(var,...) __GET_VAR(data__->var,__VA_ARGS__)
    #define SetFbVar(var,val,...) __SET_VAR(data__->,var,__VA_ARGS__,val)

   LogMessage(GetFbVar(LEVEL),(char*)GetFbVar(MSG, .body),GetFbVar(MSG, .len));
  
    #undef GetFbVar
    #undef SetFbVar
;
  };
  __SET_VAR(data__->,TRIG0,,__GET_VAR(data__->TRIG,));

  goto __end;

__end:
  return;
} // LOGGER_body__() 





void PYTHON_EVAL_init__(PYTHON_EVAL *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->CODE,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->ACK,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RESULT,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->STATE,0,retain)
  __INIT_VAR(data__->BUFFER,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->PREBUFFER,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->TRIGM1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->TRIGGED,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void PYTHON_EVAL_body__(PYTHON_EVAL *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  __IL_DEFVAR_T __IL_DEFVAR;
  __IL_DEFVAR_T __IL_DEFVAR_BACK;
  #define GetFbVar(var,...) __GET_VAR(data__->var,__VA_ARGS__)
  #define SetFbVar(var,val,...) __SET_VAR(data__->,var,__VA_ARGS__,val)
extern void __PythonEvalFB(int, PYTHON_EVAL*);__PythonEvalFB(0, data__);
  #undef GetFbVar
  #undef SetFbVar
;

  goto __end;

__end:
  return;
} // PYTHON_EVAL_body__() 





void PYTHON_POLL_init__(PYTHON_POLL *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->CODE,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->ACK,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RESULT,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->STATE,0,retain)
  __INIT_VAR(data__->BUFFER,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->PREBUFFER,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->TRIGM1,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->TRIGGED,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void PYTHON_POLL_body__(PYTHON_POLL *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  __IL_DEFVAR_T __IL_DEFVAR;
  __IL_DEFVAR_T __IL_DEFVAR_BACK;
  #define GetFbVar(var,...) __GET_VAR(data__->var,__VA_ARGS__)
  #define SetFbVar(var,val,...) __SET_VAR(data__->,var,__VA_ARGS__,val)
extern void __PythonEvalFB(int, PYTHON_EVAL*);__PythonEvalFB(1,(PYTHON_EVAL*)(void*)data__);
  #undef GetFbVar
  #undef SetFbVar
;

  goto __end;

__end:
  return;
} // PYTHON_POLL_body__() 





void PYTHON_GEAR_init__(PYTHON_GEAR *data__, BOOL retain) {
  __INIT_VAR(data__->EN,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->ENO,__BOOL_LITERAL(TRUE),retain)
  __INIT_VAR(data__->N,0,retain)
  __INIT_VAR(data__->TRIG,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->CODE,__STRING_LITERAL(0,""),retain)
  __INIT_VAR(data__->ACK,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->RESULT,__STRING_LITERAL(0,""),retain)
  PYTHON_EVAL_init__(&data__->PY_EVAL,retain);
  __INIT_VAR(data__->COUNTER,0,retain)
  __INIT_VAR(data__->_TMP_ADD10_OUT,0,retain)
  __INIT_VAR(data__->_TMP_EQ13_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_SEL15_OUT,0,retain)
  __INIT_VAR(data__->_TMP_AND7_OUT,__BOOL_LITERAL(FALSE),retain)
}

// Code part
void PYTHON_GEAR_body__(PYTHON_GEAR *data__) {
  // Control execution
  if (!__GET_VAR(data__->EN)) {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(FALSE));
    return;
  }
  else {
    __SET_VAR(data__->,ENO,,__BOOL_LITERAL(TRUE));
  }
  // Initialise TEMP variables

  __SET_VAR(data__->,_TMP_ADD10_OUT,,ADD__UINT__UINT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (UINT)__GET_VAR(data__->COUNTER,),
    (UINT)1));
  __SET_VAR(data__->,_TMP_EQ13_OUT,,EQ__BOOL__UINT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (UINT)__GET_VAR(data__->N,),
    (UINT)__GET_VAR(data__->_TMP_ADD10_OUT,)));
  __SET_VAR(data__->,_TMP_SEL15_OUT,,SEL__UINT__BOOL__UINT__UINT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (BOOL)__GET_VAR(data__->_TMP_EQ13_OUT,),
    (UINT)__GET_VAR(data__->_TMP_ADD10_OUT,),
    (UINT)0));
  __SET_VAR(data__->,COUNTER,,__GET_VAR(data__->_TMP_SEL15_OUT,));
  __SET_VAR(data__->,_TMP_AND7_OUT,,AND__BOOL__BOOL(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (BOOL)__GET_VAR(data__->_TMP_EQ13_OUT,),
    (BOOL)__GET_VAR(data__->TRIG,)));
  __SET_VAR(data__->PY_EVAL.,TRIG,,__GET_VAR(data__->_TMP_AND7_OUT,));
  __SET_VAR(data__->PY_EVAL.,CODE,,__GET_VAR(data__->CODE,));
  PYTHON_EVAL_body__(&data__->PY_EVAL);
  __SET_VAR(data__->,ACK,,__GET_VAR(data__->PY_EVAL.ACK,));
  __SET_VAR(data__->,RESULT,,__GET_VAR(data__->PY_EVAL.RESULT,));

  goto __end;

__end:
  return;
} // PYTHON_GEAR_body__() 





void PROGRAM0_init__(PROGRAM0 *data__, BOOL retain) {
  __INIT_VAR(data__->SENSOR,0,retain)
  __INIT_VAR(data__->LED_R,0,retain)
  __INIT_VAR(data__->LED_G,0,retain)
  __INIT_VAR(data__->LED_B,0,retain)
  __INIT_VAR(data__->LED_SENSOR,0,retain)
  __INIT_VAR(data__->LED_RED,0,retain)
  __INIT_VAR(data__->LED_GREEN,0,retain)
  __INIT_VAR(data__->RELAY,0,retain)
  __INIT_VAR(data__->TEMPORIZADOR,__time_to_timespec(1, 0, 30, 0, 0, 0),retain)
  __INIT_VAR(data__->INTENSIDAD,30000,retain)
  __INIT_VAR(data__->TIEMPO_SUPERIOR,30,retain)
  __INIT_VAR(data__->TRU,1,retain)
  __INIT_VAR(data__->TIEMPO_INFERIOR,20,retain)
  __INIT_VAR(data__->TIME_BLINK,__time_to_timespec(1, 500, 0, 0, 0, 0),retain)
  __INIT_VAR(data__->TIEMPO_SENSOR,__time_to_timespec(1, 500, 0, 0, 0, 0),retain)
  TOF_init__(&data__->TOF1,retain);
  TP_init__(&data__->TP2,retain);
  TP_init__(&data__->TP4,retain);
  TP_init__(&data__->TP5,retain);
  TP_init__(&data__->TP6,retain);
  TP_init__(&data__->TP7,retain);
  __INIT_VAR(data__->_TMP_NOT3_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_NOT4_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_TIME_TO_INT51_OUT,0,retain)
  __INIT_VAR(data__->_TMP_LT74_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_GT5_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_AND75_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_NOT29_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_AND2_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_NOT25_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_AND23_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_NOT24_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_NOT1_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_AND79_OUT,__BOOL_LITERAL(FALSE),retain)
  __INIT_VAR(data__->_TMP_BOOL_TO_INT43_OUT,0,retain)
  __INIT_VAR(data__->_TMP_MUL22_OUT,0,retain)
  __INIT_VAR(data__->_TMP_INT_TO_UINT42_OUT,0,retain)
  __INIT_VAR(data__->_TMP_BOOL_TO_INT37_OUT,0,retain)
  __INIT_VAR(data__->_TMP_MUL35_OUT,0,retain)
  __INIT_VAR(data__->_TMP_INT_TO_UINT36_OUT,0,retain)
  __INIT_VAR(data__->_TMP_BOOL_TO_INT39_OUT,0,retain)
  __INIT_VAR(data__->_TMP_MUL41_OUT,0,retain)
  __INIT_VAR(data__->_TMP_INT_TO_UINT38_OUT,0,retain)
}

// Code part
void PROGRAM0_body__(PROGRAM0 *data__) {
  // Initialise TEMP variables

  __SET_VAR(data__->,_TMP_NOT3_OUT,,!(__GET_VAR(data__->SENSOR,)));
  __SET_VAR(data__->TP2.,IN,,__GET_VAR(data__->_TMP_NOT3_OUT,));
  __SET_VAR(data__->TP2.,PT,,__time_to_timespec(1, 1, 0, 0, 0, 0));
  TP_body__(&data__->TP2);
  __SET_VAR(data__->TOF1.,IN,,__GET_VAR(data__->TP2.Q,));
  __SET_VAR(data__->TOF1.,PT,,__GET_VAR(data__->TEMPORIZADOR,));
  TOF_body__(&data__->TOF1);
  __SET_VAR(data__->,_TMP_NOT4_OUT,,!(__GET_VAR(data__->TOF1.Q,)));
  __SET_VAR(data__->,LED_RED,,__GET_VAR(data__->_TMP_NOT4_OUT,));
  __SET_VAR(data__->,LED_GREEN,,__GET_VAR(data__->TOF1.Q,));
  __SET_VAR(data__->,RELAY,,__GET_VAR(data__->TOF1.Q,));
  __SET_VAR(data__->,LED_SENSOR,,__GET_VAR(data__->_TMP_NOT3_OUT,));
  __SET_VAR(data__->,_TMP_TIME_TO_INT51_OUT,,TIME_TO_INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (TIME)__GET_VAR(data__->TOF1.ET,)));
  __SET_VAR(data__->,_TMP_LT74_OUT,,LT__BOOL__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->_TMP_TIME_TO_INT51_OUT,),
    (INT)__GET_VAR(data__->TIEMPO_SUPERIOR,)));
  __SET_VAR(data__->,_TMP_GT5_OUT,,GT__BOOL__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->_TMP_TIME_TO_INT51_OUT,),
    (INT)__GET_VAR(data__->TIEMPO_INFERIOR,)));
  __SET_VAR(data__->,_TMP_AND75_OUT,,AND__BOOL__BOOL(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (BOOL)__GET_VAR(data__->_TMP_LT74_OUT,),
    (BOOL)__GET_VAR(data__->_TMP_GT5_OUT,)));
  __SET_VAR(data__->,_TMP_NOT29_OUT,,!(__GET_VAR(data__->TP5.Q,)));
  __SET_VAR(data__->,_TMP_AND2_OUT,,AND__BOOL__BOOL(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (BOOL)__GET_VAR(data__->_TMP_NOT29_OUT,),
    (BOOL)__GET_VAR(data__->_TMP_AND75_OUT,)));
  __SET_VAR(data__->TP4.,IN,,__GET_VAR(data__->_TMP_AND2_OUT,));
  __SET_VAR(data__->TP4.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TP_body__(&data__->TP4);
  __SET_VAR(data__->,_TMP_NOT25_OUT,,!(__GET_VAR(data__->TP4.Q,)));
  __SET_VAR(data__->,_TMP_AND23_OUT,,AND__BOOL__BOOL(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)3,
    (BOOL)__GET_VAR(data__->_TMP_NOT29_OUT,),
    (BOOL)__GET_VAR(data__->_TMP_NOT25_OUT,),
    (BOOL)__GET_VAR(data__->_TMP_AND75_OUT,)));
  __SET_VAR(data__->TP7.,IN,,__GET_VAR(data__->_TMP_AND23_OUT,));
  __SET_VAR(data__->TP7.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TP_body__(&data__->TP7);
  __SET_VAR(data__->,_TMP_NOT24_OUT,,!(__GET_VAR(data__->TP7.Q,)));
  __SET_VAR(data__->TP6.,IN,,__GET_VAR(data__->_TMP_NOT24_OUT,));
  __SET_VAR(data__->TP6.,PT,,__time_to_timespec(1, 1, 0, 0, 0, 0));
  TP_body__(&data__->TP6);
  __SET_VAR(data__->,_TMP_NOT1_OUT,,!(__GET_VAR(data__->TP6.Q,)));
  __SET_VAR(data__->,_TMP_AND79_OUT,,AND__BOOL__BOOL(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (BOOL)__GET_VAR(data__->_TMP_AND75_OUT,),
    (BOOL)__GET_VAR(data__->_TMP_NOT1_OUT,)));
  __SET_VAR(data__->TP5.,IN,,__GET_VAR(data__->_TMP_AND79_OUT,));
  __SET_VAR(data__->TP5.,PT,,__time_to_timespec(1, 500, 0, 0, 0, 0));
  TP_body__(&data__->TP5);
  __SET_VAR(data__->,_TMP_BOOL_TO_INT43_OUT,,BOOL_TO_INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (BOOL)__GET_VAR(data__->TP5.Q,)));
  __SET_VAR(data__->,_TMP_MUL22_OUT,,MUL__INT__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->_TMP_BOOL_TO_INT43_OUT,),
    (INT)__GET_VAR(data__->INTENSIDAD,)));
  __SET_VAR(data__->,_TMP_INT_TO_UINT42_OUT,,INT_TO_UINT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (INT)__GET_VAR(data__->_TMP_MUL22_OUT,)));
  __SET_VAR(data__->,LED_R,,__GET_VAR(data__->_TMP_INT_TO_UINT42_OUT,));
  __SET_VAR(data__->,_TMP_BOOL_TO_INT37_OUT,,BOOL_TO_INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (BOOL)__GET_VAR(data__->TP4.Q,)));
  __SET_VAR(data__->,_TMP_MUL35_OUT,,MUL__INT__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->_TMP_BOOL_TO_INT37_OUT,),
    (INT)__GET_VAR(data__->INTENSIDAD,)));
  __SET_VAR(data__->,_TMP_INT_TO_UINT36_OUT,,INT_TO_UINT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (INT)__GET_VAR(data__->_TMP_MUL35_OUT,)));
  __SET_VAR(data__->,LED_G,,__GET_VAR(data__->_TMP_INT_TO_UINT36_OUT,));
  __SET_VAR(data__->,_TMP_BOOL_TO_INT39_OUT,,BOOL_TO_INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (BOOL)__GET_VAR(data__->TP7.Q,)));
  __SET_VAR(data__->,_TMP_MUL41_OUT,,MUL__INT__INT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (UINT)2,
    (INT)__GET_VAR(data__->_TMP_BOOL_TO_INT39_OUT,),
    (INT)__GET_VAR(data__->INTENSIDAD,)));
  __SET_VAR(data__->,_TMP_INT_TO_UINT38_OUT,,INT_TO_UINT(
    (BOOL)__BOOL_LITERAL(TRUE),
    NULL,
    (INT)__GET_VAR(data__->_TMP_MUL41_OUT,)));
  __SET_VAR(data__->,LED_B,,__GET_VAR(data__->_TMP_INT_TO_UINT38_OUT,));

  goto __end;

__end:
  return;
} // PROGRAM0_body__() 





