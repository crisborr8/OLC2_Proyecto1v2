
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'initleftANDORleftMENORMAYORMENOR_IGUALMAYOR_IGUALIGUALNOIGUALleftSIMBOLO_SUMASIMBOLO_RESTAleftSIMBOLO_MULTIPLICACIONSIMBOLO_DIVICIONleftSIMBOLO_POTENCIASIMBOLO_MODrightNEGATIVOAND BEGIN BOOL CHAR COMA COS DATO_TIPO_CHAR DATO_TIPO_FLOAT64 DATO_TIPO_INT64 DATO_TIPO_STRING DER_LLAVE DER_PARENTESIS ELSE END FALSE FLOAT FLOAT64 FOR FUNCION ID IF IGUAL IN INT64 IZQ_LLAVE IZQ_PARENTESIS LENGTH LOG LOG10 LOWER MAYOR MAYOR_IGUAL MENOR MENOR_IGUAL NOIGUAL NOT NOTHING OR PARSE POP PRINT PRINTLN PUNTO_COMA PUNTO_PUNTO PUSH RETURN SALTO SIMBOLO_DIVICION SIMBOLO_IGUAL SIMBOLO_MOD SIMBOLO_MULTIPLICACION SIMBOLO_POTENCIA SIMBOLO_RESTA SIMBOLO_SUMA SIN SQRT STRING STRING_FUNC TABULADOR TAN TRUE TRUNC TYPEOF UPPER WHILEinstruccion  : funcion_exp\n                    | funcion_exp_paramexpresion_id    : dato_id array_expinstruccion  : condicioninit   : instruccioninstruccion  : contenidocondicion    : expresion MENOR expresion\n                    | expresion MAYOR expresion\n                    | expresion IGUAL expresion\n                    | expresion NOIGUAL expresion\n                    | expresion MENOR_IGUAL expresion\n                    | expresion MAYOR_IGUAL expresionfuncion_exp    :  dato_id IZQ_PARENTESIS DER_PARENTESIScontenido   : expresionexpresion    : IZQ_PARENTESIS expresion DER_PARENTESISexpresion_id    : dato_idcontenido   : expresion COMA contenidoexpresion    : expresion SIMBOLO_SUMA expresion\n                    | expresion SIMBOLO_RESTA expresion\n                    | expresion SIMBOLO_DIVICION expresion\n                    | expresion SIMBOLO_MULTIPLICACION expresion\n                    | expresion SIMBOLO_POTENCIA expresion\n                    | expresion SIMBOLO_MOD expresionfuncion_exp_param    :  dato_id IZQ_PARENTESIS parametros DER_PARENTESISarray_exp    : IZQ_LLAVE expresion DER_LLAVEcondicion    : condicion OR condicion\n                    | condicion AND condicionarray_exp    : IZQ_LLAVE rango_arr DER_LLAVEparametros   : expresionexpresion    : LOG IZQ_PARENTESIS expresion COMA expresion DER_PARENTESIS\n                    | TRUNC IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS\n                    | PARSE IZQ_PARENTESIS tipo COMA expresion DER_PARENTESISparametros   : expresion COMA parametrosrango_arr    : begin PUNTO_PUNTO endcondicion    : NOT condiciontipo     : INT64\n                | FLOAT64\n                | NOTHING\n                | STRING\n                | CHAR\n                | BOOLbegin    : expresioncondicion    : IZQ_PARENTESIS condicion DER_PARENTESISexpresion    : LOG10 IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | SIN IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | COS IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | TAN IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | SQRT IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | UPPER IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | LOWER IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | STRING_FUNC IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | TYPEOF IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | FLOAT IZQ_PARENTESIS expresion DER_PARENTESIS\n                    | LENGTH IZQ_PARENTESIS expresion DER_PARENTESISbegin    : BEGIN\n                | end  : expresionend  : END\n            | array_exp    : array_exp array_expexpresion    : dato_numerico\n                    | dato_booleano\n                    | funcion_exp\n                    | funcion_exp_param\n                    | expresion_id\n                    | arrayexpresion  : SIMBOLO_RESTA expresion %prec NEGATIVOarray    : IZQ_LLAVE parametros DER_LLAVEdato_booleano    : TRUE\n                        | FALSEdato_numerico    : DATO_TIPO_FLOAT64\n                        | DATO_TIPO_INT64dato_numerico    : DATO_TIPO_STRING\n                        | DATO_TIPO_CHARdato_id    : ID'
    
_lr_action_items = {'NOT':([0,8,10,38,39,],[10,10,10,10,10,]),'IZQ_PARENTESIS':([0,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[8,40,8,8,-75,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,63,8,8,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'ID':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'LOG':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'TRUNC':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'PARSE':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'LOG10':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'SIN':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'COS':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'TAN':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'SQRT':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'UPPER':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'LOWER':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'STRING_FUNC':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'TYPEOF':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'FLOAT':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'LENGTH':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'SIMBOLO_RESTA':([0,3,4,7,8,9,10,11,12,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,67,68,69,70,71,72,73,74,75,76,77,79,82,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,],[12,-63,-64,-16,12,55,12,-75,12,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,12,12,12,12,-3,12,55,-63,-64,12,12,12,12,12,12,12,12,12,12,12,12,12,55,-67,12,12,12,12,12,12,12,12,12,12,12,12,12,55,-13,-60,55,-15,55,55,55,55,55,55,55,-18,-19,-20,-21,-22,-23,55,55,55,55,55,55,55,55,55,55,55,55,55,-68,12,-24,-25,-28,12,12,12,12,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,55,55,55,55,-30,-31,-32,]),'DATO_TIPO_FLOAT64':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'DATO_TIPO_INT64':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'DATO_TIPO_STRING':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'DATO_TIPO_CHAR':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'TRUE':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'FALSE':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'IZQ_LLAVE':([0,7,8,10,11,12,37,38,39,40,41,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,84,127,129,130,131,132,133,134,],[37,42,37,37,-75,37,37,37,37,37,42,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,42,37,-25,-28,37,37,37,37,]),'$end':([1,2,3,4,5,6,7,9,11,27,28,29,30,31,32,33,34,35,36,41,45,46,60,62,80,81,82,84,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[0,-5,-1,-2,-4,-6,-16,-14,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,-63,-64,-35,-67,-26,-27,-13,-60,-43,-15,-7,-8,-9,-10,-11,-12,-14,-17,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'MENOR':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,82,84,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,47,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,47,-63,-64,47,-67,-13,-60,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'MAYOR':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,82,84,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,48,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,48,-63,-64,48,-67,-13,-60,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'IGUAL':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,82,84,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,49,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,49,-63,-64,49,-67,-13,-60,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'NOIGUAL':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,82,84,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,50,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,50,-63,-64,50,-67,-13,-60,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'MENOR_IGUAL':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,82,84,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,51,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,51,-63,-64,51,-67,-13,-60,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'MAYOR_IGUAL':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,82,84,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,52,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,52,-63,-64,52,-67,-13,-60,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'COMA':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,45,46,62,79,82,84,90,97,99,100,101,102,103,104,106,107,108,109,110,111,112,113,114,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-63,-64,-16,53,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,-63,-64,-67,127,-13,-60,-15,53,-18,-19,-20,-21,-22,-23,132,133,-36,-37,-38,-39,-40,-41,134,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'SIMBOLO_SUMA':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,79,82,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,],[-63,-64,-16,54,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,54,-63,-64,54,-67,54,-13,-60,54,-15,54,54,54,54,54,54,54,-18,-19,-20,-21,-22,-23,54,54,54,54,54,54,54,54,54,54,54,54,54,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,54,54,54,54,-30,-31,-32,]),'SIMBOLO_DIVICION':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,79,82,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,],[-63,-64,-16,56,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,56,-63,-64,56,-67,56,-13,-60,56,-15,56,56,56,56,56,56,56,56,56,-20,-21,-22,-23,56,56,56,56,56,56,56,56,56,56,56,56,56,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,56,56,56,56,-30,-31,-32,]),'SIMBOLO_MULTIPLICACION':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,79,82,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,],[-63,-64,-16,57,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,57,-63,-64,57,-67,57,-13,-60,57,-15,57,57,57,57,57,57,57,57,57,-20,-21,-22,-23,57,57,57,57,57,57,57,57,57,57,57,57,57,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,57,57,57,57,-30,-31,-32,]),'SIMBOLO_POTENCIA':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,79,82,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,],[-63,-64,-16,58,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,58,-63,-64,58,-67,58,-13,-60,58,-15,58,58,58,58,58,58,58,58,58,58,58,-22,-23,58,58,58,58,58,58,58,58,58,58,58,58,58,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,58,58,58,58,-30,-31,-32,]),'SIMBOLO_MOD':([3,4,7,9,11,27,28,29,30,31,32,33,34,35,36,41,44,45,46,61,62,79,82,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,148,150,151,152,153,154,155,],[-63,-64,-16,59,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,59,-63,-64,59,-67,59,-13,-60,59,-15,59,59,59,59,59,59,59,59,59,59,59,-22,-23,59,59,59,59,59,59,59,59,59,59,59,59,59,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,59,59,59,59,-30,-31,-32,]),'OR':([5,7,11,27,28,29,30,31,32,33,34,35,36,41,43,45,46,60,62,80,81,82,84,89,90,91,92,93,94,95,96,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[38,-16,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,38,-63,-64,38,-67,-26,-27,-13,-60,-43,-15,-7,-8,-9,-10,-11,-12,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'AND':([5,7,11,27,28,29,30,31,32,33,34,35,36,41,43,45,46,60,62,80,81,82,84,89,90,91,92,93,94,95,96,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[39,-16,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,39,-63,-64,39,-67,-26,-27,-13,-60,-43,-15,-7,-8,-9,-10,-11,-12,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'DER_PARENTESIS':([7,11,27,28,29,30,31,32,33,34,35,36,40,41,43,44,45,46,60,62,79,80,81,82,83,84,89,90,91,92,93,94,95,96,99,100,101,102,103,104,105,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,146,150,151,152,153,154,155,],[-16,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,82,-3,89,90,-63,-64,-35,-67,-29,-26,-27,-13,128,-60,-43,-15,-7,-8,-9,-10,-11,-12,-18,-19,-20,-21,-22,-23,90,135,136,137,138,139,140,141,142,143,144,145,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-33,153,154,155,-30,-31,-32,]),'DER_LLAVE':([7,11,27,28,29,30,31,32,33,34,35,36,41,45,46,62,78,79,82,84,85,86,90,99,100,101,102,103,104,126,128,129,130,131,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,153,154,155,],[-16,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,-63,-64,-67,126,-29,-13,-60,129,130,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-59,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-33,-34,-57,-58,-30,-31,-32,]),'PUNTO_PUNTO':([7,11,27,28,29,30,31,32,33,34,35,36,41,42,45,46,62,82,84,85,87,88,90,99,100,101,102,103,104,126,128,129,130,135,136,137,138,139,140,141,142,143,144,145,153,154,155,],[-16,-75,-61,-62,-65,-66,-71,-72,-73,-74,-69,-70,-3,-56,-63,-64,-67,-13,-60,-42,131,-55,-15,-18,-19,-20,-21,-22,-23,-68,-24,-25,-28,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-30,-31,-32,]),'BEGIN':([42,],[88,]),'INT64':([65,66,],[108,108,]),'FLOAT64':([65,66,],[109,109,]),'NOTHING':([65,66,],[110,110,]),'STRING':([65,66,],[111,111,]),'CHAR':([65,66,],[112,112,]),'BOOL':([65,66,],[113,113,]),'END':([131,],[149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instruccion':([0,],[2,]),'funcion_exp':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[3,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'funcion_exp_param':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[4,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'condicion':([0,8,10,38,39,],[5,43,60,80,81,]),'contenido':([0,53,],[6,98,]),'dato_id':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'expresion':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[9,44,61,62,79,61,61,79,85,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,115,116,117,118,119,120,121,122,123,124,125,79,148,150,151,152,]),'dato_numerico':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'dato_booleano':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'expresion_id':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'array':([0,8,10,12,37,38,39,40,42,47,48,49,50,51,52,53,54,55,56,57,58,59,63,64,67,68,69,70,71,72,73,74,75,76,77,127,131,132,133,134,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'array_exp':([7,41,84,],[41,84,84,]),'parametros':([37,40,127,],[78,83,146,]),'rango_arr':([42,],[86,]),'begin':([42,],[87,]),'tipo':([65,66,],[107,114,]),'end':([131,],[147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('instruccion -> funcion_exp','instruccion',1,'p_instruccion_funcion','funcion.py',6),
  ('instruccion -> funcion_exp_param','instruccion',1,'p_instruccion_funcion','funcion.py',7),
  ('expresion_id -> dato_id array_exp','expresion_id',2,'p_expresion_dato_id_arr','arreglos.py',7),
  ('instruccion -> condicion','instruccion',1,'p_instruccion_condicion','condicion.py',7),
  ('init -> instruccion','init',1,'p_init','init.py',7),
  ('instruccion -> contenido','instruccion',1,'p_instruccion_expresion','print.py',7),
  ('condicion -> expresion MENOR expresion','condicion',3,'p_condicion_arit','condicion.py',13),
  ('condicion -> expresion MAYOR expresion','condicion',3,'p_condicion_arit','condicion.py',14),
  ('condicion -> expresion IGUAL expresion','condicion',3,'p_condicion_arit','condicion.py',15),
  ('condicion -> expresion NOIGUAL expresion','condicion',3,'p_condicion_arit','condicion.py',16),
  ('condicion -> expresion MENOR_IGUAL expresion','condicion',3,'p_condicion_arit','condicion.py',17),
  ('condicion -> expresion MAYOR_IGUAL expresion','condicion',3,'p_condicion_arit','condicion.py',18),
  ('funcion_exp -> dato_id IZQ_PARENTESIS DER_PARENTESIS','funcion_exp',3,'p_funcion_dato','funcion.py',13),
  ('contenido -> expresion','contenido',1,'p_imprimir_contenido','print.py',13),
  ('expresion -> IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',3,'p_expresion_par','expresion.py',14),
  ('expresion_id -> dato_id','expresion_id',1,'p_expresion_dato','arreglos.py',16),
  ('contenido -> expresion COMA contenido','contenido',3,'p_imprimir_contenido_coma','print.py',19),
  ('expresion -> expresion SIMBOLO_SUMA expresion','expresion',3,'p_expresion_binario','expresion.py',20),
  ('expresion -> expresion SIMBOLO_RESTA expresion','expresion',3,'p_expresion_binario','expresion.py',21),
  ('expresion -> expresion SIMBOLO_DIVICION expresion','expresion',3,'p_expresion_binario','expresion.py',22),
  ('expresion -> expresion SIMBOLO_MULTIPLICACION expresion','expresion',3,'p_expresion_binario','expresion.py',23),
  ('expresion -> expresion SIMBOLO_POTENCIA expresion','expresion',3,'p_expresion_binario','expresion.py',24),
  ('expresion -> expresion SIMBOLO_MOD expresion','expresion',3,'p_expresion_binario','expresion.py',25),
  ('funcion_exp_param -> dato_id IZQ_PARENTESIS parametros DER_PARENTESIS','funcion_exp_param',4,'p_funcion_dato_param','funcion.py',22),
  ('array_exp -> IZQ_LLAVE expresion DER_LLAVE','array_exp',3,'p_expresion_arrayExp','arreglos.py',25),
  ('condicion -> condicion OR condicion','condicion',3,'p_condicion_logic','condicion.py',32),
  ('condicion -> condicion AND condicion','condicion',3,'p_condicion_logic','condicion.py',33),
  ('array_exp -> IZQ_LLAVE rango_arr DER_LLAVE','array_exp',3,'p_expresion_arrayExp_BE','arreglos.py',35),
  ('parametros -> expresion','parametros',1,'p_parametros','funcion.py',36),
  ('expresion -> LOG IZQ_PARENTESIS expresion COMA expresion DER_PARENTESIS','expresion',6,'p_expresion_nativa_binaria','expresion.py',39),
  ('expresion -> TRUNC IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS','expresion',6,'p_expresion_nativa_binaria','expresion.py',40),
  ('expresion -> PARSE IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS','expresion',6,'p_expresion_nativa_binaria','expresion.py',41),
  ('parametros -> expresion COMA parametros','parametros',3,'p_parametros_coma','funcion.py',44),
  ('rango_arr -> begin PUNTO_PUNTO end','rango_arr',3,'p_rango_array','arreglos.py',45),
  ('condicion -> NOT condicion','condicion',2,'p_condicion_not','condicion.py',47),
  ('tipo -> INT64','tipo',1,'p_expresion_tipo','expresion.py',54),
  ('tipo -> FLOAT64','tipo',1,'p_expresion_tipo','expresion.py',55),
  ('tipo -> NOTHING','tipo',1,'p_expresion_tipo','expresion.py',56),
  ('tipo -> STRING','tipo',1,'p_expresion_tipo','expresion.py',57),
  ('tipo -> CHAR','tipo',1,'p_expresion_tipo','expresion.py',58),
  ('tipo -> BOOL','tipo',1,'p_expresion_tipo','expresion.py',59),
  ('begin -> expresion','begin',1,'p_rango_begin','arreglos.py',57),
  ('condicion -> IZQ_PARENTESIS condicion DER_PARENTESIS','condicion',3,'p_condicion_par','condicion.py',59),
  ('expresion -> LOG10 IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',65),
  ('expresion -> SIN IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',66),
  ('expresion -> COS IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',67),
  ('expresion -> TAN IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',68),
  ('expresion -> SQRT IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',69),
  ('expresion -> UPPER IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',70),
  ('expresion -> LOWER IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',71),
  ('expresion -> STRING_FUNC IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',72),
  ('expresion -> TYPEOF IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',73),
  ('expresion -> FLOAT IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',74),
  ('expresion -> LENGTH IZQ_PARENTESIS expresion DER_PARENTESIS','expresion',4,'p_expresion_nativa','expresion.py',75),
  ('begin -> BEGIN','begin',1,'p_rango_beginEmpty','arreglos.py',66),
  ('begin -> <empty>','begin',0,'p_rango_beginEmpty','arreglos.py',67),
  ('end -> expresion','end',1,'p_rango_end','arreglos.py',72),
  ('end -> END','end',1,'p_rango_endEmpty','arreglos.py',81),
  ('end -> <empty>','end',0,'p_rango_endEmpty','arreglos.py',82),
  ('array_exp -> array_exp array_exp','array_exp',2,'p_expresion_arrayExp2','arreglos.py',87),
  ('expresion -> dato_numerico','expresion',1,'p_expresion_numerico','expresion.py',87),
  ('expresion -> dato_booleano','expresion',1,'p_expresion_numerico','expresion.py',88),
  ('expresion -> funcion_exp','expresion',1,'p_expresion_numerico','expresion.py',89),
  ('expresion -> funcion_exp_param','expresion',1,'p_expresion_numerico','expresion.py',90),
  ('expresion -> expresion_id','expresion',1,'p_expresion_numerico','expresion.py',91),
  ('expresion -> array','expresion',1,'p_expresion_numerico','expresion.py',92),
  ('expresion -> SIMBOLO_RESTA expresion','expresion',2,'p_expresion_negativo','expresion.py',97),
  ('array -> IZQ_LLAVE parametros DER_LLAVE','array',3,'p_expresion_array_param','arreglos.py',100),
  ('dato_booleano -> TRUE','dato_booleano',1,'p_expresion_dato_booleano','expresion.py',109),
  ('dato_booleano -> FALSE','dato_booleano',1,'p_expresion_dato_booleano','expresion.py',110),
  ('dato_numerico -> DATO_TIPO_FLOAT64','dato_numerico',1,'p_expresion_dato_numerico','expresion.py',119),
  ('dato_numerico -> DATO_TIPO_INT64','dato_numerico',1,'p_expresion_dato_numerico','expresion.py',120),
  ('dato_numerico -> DATO_TIPO_STRING','dato_numerico',1,'p_expresion_dato_string','expresion.py',126),
  ('dato_numerico -> DATO_TIPO_CHAR','dato_numerico',1,'p_expresion_dato_string','expresion.py',127),
  ('dato_id -> ID','dato_id',1,'p_expresion_dato_id','expresion.py',135),
]
