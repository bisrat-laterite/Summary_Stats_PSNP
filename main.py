import requests
import os
import pandas as pd
import gspread
import numpy as np
from collections import Counter
from geopy.distance import geodesic


### Reading the data
# break
# #### 
gc=gspread.service_account(filename='credentials.json')
key_='1lnQ9R9i1RS9IBl_9QPzmrMHXAHRZjr751UMKSB_k13E'
### Reading in the specific googles sheets file
sh=gc.open_by_key(key_)

df=sh.worksheet('Data').get_all_records()

# data_gs_=sh.worksheet('Data').get_all_records()
# _all=sh.worksheet('Data').get_all_values()

# working on the gsheets returned
data = pd.DataFrame(df)


print(data.head())

# break
# #### 
gc=gspread.service_account(filename='credentials.json')
key_='1iJ_GDl0FqZxEr2vvi469zUlsVfg3F9AA-Gaw3SmqEt4'
### Reading in the specific googles sheets file
sh=gc.open_by_key(key_)

surveyp=sh.worksheet('survey').get_all_records()
choicesp=sh.worksheet('choices').get_all_records()
# data_gs_=sh.worksheet('Data').get_all_records()
# _all=sh.worksheet('Data').get_all_values()

# working on the gsheets returned
survey = pd.DataFrame(surveyp)
survey_choice = pd.DataFrame(choicesp)
# data_gs = pd.DataFrame(data_gs_)
#reading in data
data_csv=data
# data_csv=data_gs

### creating a lookup dictionary
dict_={1: 'A',
 2: 'B',
 3: 'C',
 4: 'D',
 5: 'E',
 6: 'F',
 7: 'G',
 8: 'H',
 9: 'I',
 10: 'J',
 11: 'K',
 12: 'L',
 13: 'M',
 14: 'N',
 15: 'O',
 16: 'P',
 17: 'Q',
 18: 'R',
 19: 'S',
 20: 'T',
 21: 'U',
 22: 'V',
 23: 'W',
 24: 'X',
 25: 'Y',
 26: 'Z',
 27: 'AA',
 28: 'AB',
 29: 'AC',
 30: 'AD',
 31: 'AE',
 32: 'AF',
 33: 'AG',
 34: 'AH',
 35: 'AI',
 36: 'AJ',
 37: 'AK',
 38: 'AL',
 39: 'AM',
 40: 'AN',
 41: 'AO',
 42: 'AP',
 43: 'AQ',
 44: 'AR',
 45: 'AS',
 46: 'AT',
 47: 'AU',
 48: 'AV',
 49: 'AW',
 50: 'AX',
 51: 'AY',
 52: 'AZ',
 53: 'BA',
 54: 'BB',
 55: 'BC',
 56: 'BD',
 57: 'BE',
 58: 'BF',
 59: 'BG',
 60: 'BH',
 61: 'BI',
 62: 'BJ',
 63: 'BK',
 64: 'BL',
 65: 'BM',
 66: 'BN',
 67: 'BO',
 68: 'BP',
 69: 'BQ',
 70: 'BR',
 71: 'BS',
 72: 'BT',
 73: 'BU',
 74: 'BV',
 75: 'BW',
 76: 'BX',
 77: 'BY',
 78: 'BZ',
 79: 'CA',
 80: 'CB',
 81: 'CC',
 82: 'CD',
 83: 'CE',
 84: 'CF',
 85: 'CG',
 86: 'CH',
 87: 'CI',
 88: 'CJ',
 89: 'CK',
 90: 'CL',
 91: 'CM',
 92: 'CN',
 93: 'CO',
 94: 'CP',
 95: 'CQ',
 96: 'CR',
 97: 'CS',
 98: 'CT',
 99: 'CU',
 100: 'CV',
 101: 'CW',
 102: 'CX',
 103: 'CY',
 104: 'CZ',
 105: 'DA',
 106: 'DB',
 107: 'DC',
 108: 'DD',
 109: 'DE',
 110: 'DF',
 111: 'DG',
 112: 'DH',
 113: 'DI',
 114: 'DJ',
 115: 'DK',
 116: 'DL',
 117: 'DM',
 118: 'DN',
 119: 'DO',
 120: 'DP',
 121: 'DQ',
 122: 'DR',
 123: 'DS',
 124: 'DT',
 125: 'DU',
 126: 'DV',
 127: 'DW',
 128: 'DX',
 129: 'DY',
 130: 'DZ',
 131: 'EA',
 132: 'EB',
 133: 'EC',
 134: 'ED',
 135: 'EE',
 136: 'EF',
 137: 'EG',
 138: 'EH',
 139: 'EI',
 140: 'EJ',
 141: 'EK',
 142: 'EL',
 143: 'EM',
 144: 'EN',
 145: 'EO',
 146: 'EP',
 147: 'EQ',
 148: 'ER',
 149: 'ES',
 150: 'ET',
 151: 'EU',
 152: 'EV',
 153: 'EW',
 154: 'EX',
 155: 'EY',
 156: 'EZ',
 157: 'FA',
 158: 'FB',
 159: 'FC',
 160: 'FD',
 161: 'FE',
 162: 'FF',
 163: 'FG',
 164: 'FH',
 165: 'FI',
 166: 'FJ',
 167: 'FK',
 168: 'FL',
 169: 'FM',
 170: 'FN',
 171: 'FO',
 172: 'FP',
 173: 'FQ',
 174: 'FR',
 175: 'FS',
 176: 'FT',
 177: 'FU',
 178: 'FV',
 179: 'FW',
 180: 'FX',
 181: 'FY',
 182: 'FZ',
 183: 'GA',
 184: 'GB',
 185: 'GC',
 186: 'GD',
 187: 'GE',
 188: 'GF',
 189: 'GG',
 190: 'GH',
 191: 'GI',
 192: 'GJ',
 193: 'GK',
 194: 'GL',
 195: 'GM',
 196: 'GN',
 197: 'GO',
 198: 'GP',
 199: 'GQ',
 200: 'GR',
 201: 'GS',
 202: 'GT',
 203: 'GU',
 204: 'GV',
 205: 'GW',
 206: 'GX',
 207: 'GY',
 208: 'GZ',
 209: 'HA',
 210: 'HB',
 211: 'HC',
 212: 'HD',
 213: 'HE',
 214: 'HF',
 215: 'HG',
 216: 'HH',
 217: 'HI',
 218: 'HJ',
 219: 'HK',
 220: 'HL',
 221: 'HM',
 222: 'HN',
 223: 'HO',
 224: 'HP',
 225: 'HQ',
 226: 'HR',
 227: 'HS',
 228: 'HT',
 229: 'HU',
 230: 'HV',
 231: 'HW',
 232: 'HX',
 233: 'HY',
 234: 'HZ',
 235: 'IA',
 236: 'IB',
 237: 'IC',
 238: 'ID',
 239: 'IE',
 240: 'IF',
 241: 'IG',
 242: 'IH',
 243: 'II',
 244: 'IJ',
 245: 'IK',
 246: 'IL',
 247: 'IM',
 248: 'IN',
 249: 'IO',
 250: 'IP',
 251: 'IQ',
 252: 'IR',
 253: 'IS',
 254: 'IT',
 255: 'IU',
 256: 'IV',
 257: 'IW',
 258: 'IX',
 259: 'IY',
 260: 'IZ',
 261: 'JA',
 262: 'JB',
 263: 'JC',
 264: 'JD',
 265: 'JE',
 266: 'JF',
 267: 'JG',
 268: 'JH',
 269: 'JI',
 270: 'JJ',
 271: 'JK',
 272: 'JL',
 273: 'JM',
 274: 'JN',
 275: 'JO',
 276: 'JP',
 277: 'JQ',
 278: 'JR',
 279: 'JS',
 280: 'JT',
 281: 'JU',
 282: 'JV',
 283: 'JW',
 284: 'JX',
 285: 'JY',
 286: 'JZ',
 287: 'KA',
 288: 'KB',
 289: 'KC',
 290: 'KD',
 291: 'KE',
 292: 'KF',
 293: 'KG',
 294: 'KH',
 295: 'KI',
 296: 'KJ',
 297: 'KK',
 298: 'KL',
 299: 'KM',
 300: 'KN',
 301: 'KO',
 302: 'KP',
 303: 'KQ',
 304: 'KR',
 305: 'KS',
 306: 'KT',
 307: 'KU',
 308: 'KV',
 309: 'KW',
 310: 'KX',
 311: 'KY',
 312: 'KZ',
 313: 'LA',
 314: 'LB',
 315: 'LC',
 316: 'LD',
 317: 'LE',
 318: 'LF',
 319: 'LG',
 320: 'LH',
 321: 'LI',
 322: 'LJ',
 323: 'LK',
 324: 'LL',
 325: 'LM',
 326: 'LN',
 327: 'LO',
 328: 'LP',
 329: 'LQ',
 330: 'LR',
 331: 'LS',
 332: 'LT',
 333: 'LU',
 334: 'LV',
 335: 'LW',
 336: 'LX',
 337: 'LY',
 338: 'LZ',
 339: 'MA',
 340: 'MB',
 341: 'MC',
 342: 'MD',
 343: 'ME',
 344: 'MF',
 345: 'MG',
 346: 'MH',
 347: 'MI',
 348: 'MJ',
 349: 'MK',
 350: 'ML',
 351: 'MM',
 352: 'MN',
 353: 'MO',
 354: 'MP',
 355: 'MQ',
 356: 'MR',
 357: 'MS',
 358: 'MT',
 359: 'MU',
 360: 'MV',
 361: 'MW',
 362: 'MX',
 363: 'MY',
 364: 'MZ',
 365: 'NA',
 366: 'NB',
 367: 'NC',
 368: 'ND',
 369: 'NE',
 370: 'NF',
 371: 'NG',
 372: 'NH',
 373: 'NI',
 374: 'NJ',
 375: 'NK',
 376: 'NL',
 377: 'NM',
 378: 'NN',
 379: 'NO',
 380: 'NP',
 381: 'NQ',
 382: 'NR',
 383: 'NS',
 384: 'NT',
 385: 'NU',
 386: 'NV',
 387: 'NW',
 388: 'NX',
 389: 'NY',
 390: 'NZ',
 391: 'OA',
 392: 'OB',
 393: 'OC',
 394: 'OD',
 395: 'OE',
 396: 'OF',
 397: 'OG',
 398: 'OH',
 399: 'OI',
 400: 'OJ',
 401: 'OK',
 402: 'OL',
 403: 'OM',
 404: 'ON',
 405: 'OO',
 406: 'OP',
 407: 'OQ',
 408: 'OR',
 409: 'OS',
 410: 'OT',
 411: 'OU',
 412: 'OV',
 413: 'OW',
 414: 'OX',
 415: 'OY',
 416: 'OZ',
 417: 'PA',
 418: 'PB',
 419: 'PC',
 420: 'PD',
 421: 'PE',
 422: 'PF',
 423: 'PG',
 424: 'PH',
 425: 'PI',
 426: 'PJ',
 427: 'PK',
 428: 'PL',
 429: 'PM',
 430: 'PN',
 431: 'PO',
 432: 'PP',
 433: 'PQ',
 434: 'PR',
 435: 'PS',
 436: 'PT',
 437: 'PU',
 438: 'PV',
 439: 'PW',
 440: 'PX',
 441: 'PY',
 442: 'PZ',
 443: 'QA',
 444: 'QB',
 445: 'QC',
 446: 'QD',
 447: 'QE',
 448: 'QF',
 449: 'QG',
 450: 'QH',
 451: 'QI',
 452: 'QJ',
 453: 'QK',
 454: 'QL',
 455: 'QM',
 456: 'QN',
 457: 'QO',
 458: 'QP',
 459: 'QQ',
 460: 'QR',
 461: 'QS',
 462: 'QT',
 463: 'QU',
 464: 'QV',
 465: 'QW',
 466: 'QX',
 467: 'QY',
 468: 'QZ',
 469: 'RA',
 470: 'RB',
 471: 'RC',
 472: 'RD',
 473: 'RE',
 474: 'RF',
 475: 'RG',
 476: 'RH',
 477: 'RI',
 478: 'RJ',
 479: 'RK',
 480: 'RL',
 481: 'RM',
 482: 'RN',
 483: 'RO',
 484: 'RP',
 485: 'RQ',
 486: 'RR',
 487: 'RS',
 488: 'RT',
 489: 'RU',
 490: 'RV',
 491: 'RW',
 492: 'RX',
 493: 'RY',
 494: 'RZ',
 495: 'SA',
 496: 'SB',
 497: 'SC',
 498: 'SD',
 499: 'SE',
 500: 'SF',
 501: 'SG',
 502: 'SH',
 503: 'SI',
 504: 'SJ',
 505: 'SK',
 506: 'SL',
 507: 'SM',
 508: 'SN',
 509: 'SO',
 510: 'SP',
 511: 'SQ',
 512: 'SR',
 513: 'SS',
 514: 'ST',
 515: 'SU',
 516: 'SV',
 517: 'SW',
 518: 'SX',
 519: 'SY',
 520: 'SZ',
 521: 'TA',
 522: 'TB',
 523: 'TC',
 524: 'TD',
 525: 'TE',
 526: 'TF',
 527: 'TG',
 528: 'TH',
 529: 'TI',
 530: 'TJ',
 531: 'TK',
 532: 'TL',
 533: 'TM',
 534: 'TN',
 535: 'TO',
 536: 'TP',
 537: 'TQ',
 538: 'TR',
 539: 'TS',
 540: 'TT',
 541: 'TU',
 542: 'TV',
 543: 'TW',
 544: 'TX',
 545: 'TY',
 546: 'TZ',
 547: 'UA',
 548: 'UB',
 549: 'UC',
 550: 'UD',
 551: 'UE',
 552: 'UF',
 553: 'UG',
 554: 'UH',
 555: 'UI',
 556: 'UJ',
 557: 'UK',
 558: 'UL',
 559: 'UM',
 560: 'UN',
 561: 'UO',
 562: 'UP',
 563: 'UQ',
 564: 'UR',
 565: 'US',
 566: 'UT',
 567: 'UU',
 568: 'UV',
 569: 'UW',
 570: 'UX',
 571: 'UY',
 572: 'UZ',
 573: 'VA',
 574: 'VB',
 575: 'VC',
 576: 'VD',
 577: 'VE',
 578: 'VF',
 579: 'VG',
 580: 'VH',
 581: 'VI',
 582: 'VJ',
 583: 'VK',
 584: 'VL',
 585: 'VM',
 586: 'VN',
 587: 'VO',
 588: 'VP',
 589: 'VQ',
 590: 'VR',
 591: 'VS',
 592: 'VT',
 593: 'VU',
 594: 'VV',
 595: 'VW',
 596: 'VX',
 597: 'VY',
 598: 'VZ',
 599: 'WA',
 600: 'WB',
 601: 'WC',
 602: 'WD',
 603: 'WE',
 604: 'WF',
 605: 'WG',
 606: 'WH',
 607: 'WI',
 608: 'WJ',
 609: 'WK',
 610: 'WL',
 611: 'WM',
 612: 'WN',
 613: 'WO',
 614: 'WP',
 615: 'WQ',
 616: 'WR',
 617: 'WS',
 618: 'WT',
 619: 'WU',
 620: 'WV',
 621: 'WW',
 622: 'WX',
 623: 'WY',
 624: 'WZ',
 625: 'XA',
 626: 'XB',
 627: 'XC',
 628: 'XD',
 629: 'XE',
 630: 'XF',
 631: 'XG',
 632: 'XH',
 633: 'XI',
 634: 'XJ',
 635: 'XK',
 636: 'XL',
 637: 'XM',
 638: 'XN',
 639: 'XO',
 640: 'XP',
 641: 'XQ',
 642: 'XR',
 643: 'XS',
 644: 'XT',
 645: 'XU',
 646: 'XV',
 647: 'XW',
 648: 'XX',
 649: 'XY',
 650: 'XZ',
 651: 'YA',
 652: 'YB',
 653: 'YC',
 654: 'YD',
 655: 'YE',
 656: 'YF',
 657: 'YG',
 658: 'YH',
 659: 'YI',
 660: 'YJ',
 661: 'YK',
 662: 'YL',
 663: 'YM',
 664: 'YN',
 665: 'YO',
 666: 'YP',
 667: 'YQ',
 668: 'YR',
 669: 'YS',
 670: 'YT',
 671: 'YU',
 672: 'YV',
 673: 'YW',
 674: 'YX',
 675: 'YY',
 676: 'YZ',
 677: 'ZA',
 678: 'ZB',
 679: 'ZC',
 680: 'ZD',
 681: 'ZE',
 682: 'ZF',
 683: 'ZG',
 684: 'ZH',
 685: 'ZI',
 686: 'ZJ',
 687: 'ZK',
 688: 'ZL',
 689: 'ZM',
 690: 'ZN',
 691: 'ZO',
 692: 'ZP',
 693: 'ZQ',
 694: 'ZR',
 695: 'ZS',
 696: 'ZT',
 697: 'ZU',
 698: 'ZV',
 699: 'ZW',
 700: 'ZX',
 701: 'ZY',
 702: 'ZZ'}
### Survey preprocessing functions
def survey_preprocessing(survey, column):
    """preprocessing like lowering and stripping white space and converting to string type"""
    # variable names are alwasy in lower case doing that
    survey[column]=survey[column].str.lower()
    survey[column]=survey[column].str.lower()
    #striping unnecessary white space
    survey[column]=survey[column].str.strip()
    survey[column]=survey[column].str.strip()
    #converting to the appropriate types
    survey[column]=survey[column].apply(str)
    survey[column]=survey[column].apply(str)
    return survey

def survey_columns(survey):
    """Lowecasing the columns and replacing  :: with : for the column names"""
    survey.rename(columns=str.lower, inplace=True)
    survey_columnz=[x.replace('::', ':') for  x in list(survey.columns)]
    survey.rename(columns=dict(zip(survey.columns,survey_columnz)) , inplace=True)
    return survey

def filtering_unnecessary(survey):
    """filtering out disabled and note quesions"""
    #filtering out disabled and label question
    filter_disable=survey['disabled'] !="yes"
    filter_label=survey['appearance'] !="label"
    filter_publish=survey['type']!=""
    #filtering out disabled and variable which are just labels
    survey=survey[filter_disable & filter_label & filter_publish]
    return survey

#getting type and label of a question
def get_type(val):
    """to get the type of the question from the survey"""
    return str(val).split()[0]

def get_val_label(val):
    """to get the value label of the question from survey"""
    length=len(str(val).split())
    if length < 2:
        return " "
    return str(val).split()[1]


### Preprocessing of survey and choices tab
#variables are always in lower case and stripped of white space
survey=survey_preprocessing(survey, 'type')
survey=survey_preprocessing(survey, 'name')
survey=survey_columns(survey)
survey=filtering_unnecessary(survey)

#keeping only the relevant columns
columns=['type', 'name', 'label:english', 'appearance', 'disabled']
# keeping only important columns
survey=survey[columns]
#augumenting the survey table with a column from the type of the question and the value label for that question
survey['type_new']=survey['type'].apply(lambda x:get_type(x))
survey['val_label']=survey['type'].apply(lambda x:get_val_label(x))
# keeping only the right type columns in survey
survey=survey[survey['type_new'].isin(['select_one', 'select_multiple', 'decimal', 'integer'])]

#preprocessing the columns
survey_choice=survey_columns(survey_choice)
#keeping only the relevant columns
columns_choice=['list_name', 'value', 'label:english']
# keeping only important columns
survey_choice=survey_choice[columns_choice]
#preprocessing steps
survey_choice=survey_preprocessing(survey_choice, 'list_name')


### Important Functions
def variables_handler(old_var):
    """Handling variables as in variables in a repeat group or not"""
    if old_var in data_csv.columns:
        return [old_var]
    return [f"{old_var}_{i}" for i in range(100) if f"{old_var}_{i}" in data_csv.columns]


def main_handler(row, var):
    """function to handle everything and call the relevant functions """
    type_=row['type_new']
    if type_=='select_one' or type_=='select_multiple':
        select_=counter_object(type_, var)
        dataframe_pre=value_label_retrieving(row, select_)
        dataframe_pre=adding_question_variable(dataframe_pre, row, var)
        dataframe=relevant_columns(dataframe_pre, var, row)
        dataframe=keeping_first_row(dataframe)
        return dataframe
    data_csv[var]=pd.to_numeric(data_csv[var], downcast="float")
    # dataframe[var]=dataframe[var].astype('int32', coerce=True)
    dataframe=pd.DataFrame(data_csv[var].describe()).T.reset_index(drop=True)
    dataframe=adding_question_variable(dataframe, row, var)
    return dataframe


def counter_object(type_, var):
    """Creating a count from how many times a given option was selected"""
    if type_!='select_multiple':
        # data_csv[var] = data_csv[var][~data_csv[var].isnull()]
        # data_csv[var]=pd.to_numeric(data_csv[var])
        # data_csv[var]=data_csv[var].fillna(99999)
        # data_csv[var]=data_csv[var].replace([np.nan, -np.inf,np.inf], 99999)
        # data_csv[var] = data_csv[var][~data_csv[var]==99999]
        data_csv[var]=data_csv[var].astype(str)
        df_=pd.DataFrame(data_csv[var])
        df_=df_[~df_[var].isin(['nan', ''])]
        counts=[x for x in list(df_[var])]
    # counts=list(data_csv[var].astype('int',errors='raise').astype(str))
    if type_=='select_multiple':
        data_csv[var]=data_csv[var].astype(str)
        select_multiple_split=list(data_csv[var].str.split(' '))
        counts=[str(round(float(val))) for sublist in select_multiple_split for val in sublist if val!='nan' and val!='']
        total=len(counts)
    return Counter(counts)

def value_label_retrieving(row, counter):
    """Creates a dataframe with the counts for select_multiple and select_one type questions"""
    filter_x=survey_choice['list_name']==row['val_label']
    dataframe=survey_choice[filter_x].copy()
    # if row['type_new']=='select_multiple':
    dataframe['value']=dataframe['value'].astype(str)
    dataframe['pop']= dataframe['value'].map(counter)
    return dataframe
    
def adding_question_variable(dataframe, row, var):
    """Function for adding the Question and variable name"""
    Question=row['label:english']
    dataframe['Question']=Question
    dataframe['variable name']=var
    return dataframe    

def relevant_columns(dataframe, var, row):
    """Adding all the relevant columns from preexisting columns for 
    select_one and select_multiple types"""     
    dataframe['count']=non_empty_rows(var, row)
    dataframe['proportion']=dataframe['pop']/dataframe['count']
    return dataframe


def non_empty_rows(var, row):
    """Function for counting the number of times the given question was asked(non null)"""
    if row['type_new']=='select_multiple':
        data_csv[var]=data_csv[var].astype(str)
        filter_1=data_csv[var]=='nan'
        filter_2=data_csv[var]==''
        size=len(list(data_csv[~(filter_1 | filter_2)][var]))
        return size
    data_csv[var] = data_csv[var][~data_csv[var].isnull()]
    # data_csv[var]=pd.to_numeric(data_csv[var])
    # data_csv[var]=data_csv[var].fillna(99999)
    # data_csv[var]=data_csv[var].replace([np.nan, -np.inf,np.inf], 99999)
    # data_csv[var] = data_csv[var][~data_csv[var]==99999]
    # data_csv[var]=data_csv[var].astype(str)
    df_=pd.DataFrame(data_csv[var])
    df_=df_[~df_[var].isin(['nan', ''])]
    # data_csv[var]=data_csv[var][~ (data_csv[var]=='nan' | data_csv[var]=='')]
    size=len(list(df_[var]))
    return size


def keeping_first_row(dataframe):
    """Function for taking care of the where 
    questions and variable names appear"""
    dataframe.reset_index(drop=True, inplace=True)
    dataframe.loc[ dataframe.index > 0, "Question"] = np.nan
    dataframe.loc[ dataframe.index > 0, "count"] = np.nan
    dataframe.loc[ dataframe.index > 0, "variable name"] = np.nan  
    return dataframe

keys=[]
for value, data_csv in data_csv.groupby('reg_name'):
    _all=[]
    for index, row in survey.iterrows():
        variable=variables_handler(row['name'])
        for var in variable:
            _all.append(main_handler(row, var))
    ### Creating the dataframe
    df=pd.concat(_all)
    df.rename(columns={'count':'Total', 'label:english':'Options', 'pop':'Count', 'proportion':'Proportion'}, inplace=True)
    df=df[["variable name",	"Question",	"Total",	"Options",	"Count",	"Proportion",	"mean",	"std",	"min",	"25%",	"50%",	"75%",	"max"]]
    df=df.astype('str')
    df.replace('nan', '', inplace=True)
    # Get the number of rows and columns in the DataFrame
    num_rows, num_cols = df.shape
    
    # For example, updating from cell A2 (row 2, column 1)
    start_cell = 'A1'
    # Construct the range string
    end_cell_column=num_cols +1
    row_key=dict_[end_cell_column]
    end_cell_row=1 + num_rows
    end_cell=row_key+str(end_cell_row)
    print(end_cell)
    # break
    # end_cell = chr(ord('A') + num_cols - 1) + str(2 + num_rows - 1)
    range_ = f"{start_cell}:{end_cell}"
    
    ### converting the data to a list of list
    # Convert DataFrame to list of lists
    data = [df.columns.tolist()]+df.values.tolist()
    
    ### updating the dataframe
    sheet=sh
    print(value)
    sheet=sh.worksheet(f'summary_stats_{value}')

    sheet.update(data,range_)




### Meta Data monitoring
### Reading the data
# break
# #### 
gc=gspread.service_account(filename='creds.json')
key_='1PgTLrYdPySmC-NjIH7j5fPlMy8OMFrLu8nMd_eQYXfc'
### Reading in the specific googles sheets file
sh=gc.open_by_key(key_)

df_pre=sh.worksheet('Data').get_all_records()

# data_gs_=sh.worksheet('Data').get_all_records()
# _all=sh.worksheet('Data').get_all_values()

# working on the gsheets returned
df = pd.DataFrame(df_pre)



#### Converting to the right format
df['starttime']=pd.to_datetime(df['starttime'])
df['endtime']=pd.to_datetime(df['endtime'])
df.rename(columns={'enum_name': 'cs_enumname_name'}, inplace=True)

### keeping surveys where we keep gps
df=df[~pd.isna(df['m0s1_q17_1latitude'])]

### Sorting by datetime
df=df.sort_values(by=['cs_enumname_name','starttime'])

### Shifting starttime
df['shifted_starttime']=df.groupby('cs_enumname_name')['starttime'].shift(-1)


df['time_between_two_surveys']=((df['endtime'] - df['shifted_starttime']).dt.total_seconds() / 60)*(-1)

df['time_between_two_surveys'] = df.groupby(['today', 'cs_enumname_name'])['time_between_two_surveys'].transform(lambda x: x.fillna(x.mean()))

### shifting gps
df['lat_lon']=df[['m0s1_q17_1latitude', 'm0s1_q17_1longitude']].values.tolist()
df['shifted_gps']=df.groupby('cs_enumname_name')['lat_lon'].shift(-1)
# df['shifted_gps']=df.groupby('cs_enumname_name')['lat_lon'].shift(-1)


df['distance_m'] = df[df['shifted_gps'].notna()].apply(
    lambda row: geodesic((row['lat_lon'][0], row['lat_lon'][1]), 
                        (row['shifted_gps'][0], row['shifted_gps'][1])).meters, axis=1)


### Intersurvey distance traveled
df['distance_m'] = df.groupby(['today', 'cs_enumname_name'])['distance_m'].transform(lambda x: x.fillna(x.mean()))

## Phone numbers
# df[df['m0s2_q8']=="."]["m0s2_q8"]=-99
# df[df['m0s2_q11']=="."]["m0s2_q11"]=-99
df['m0s2_q8']=df['m0s2_q8'].astype('str')
df['m0s2_q11']=df['m0s2_q11'].astype('str')
df['phone_numbers']=df[['m0s2_q8', 'm0s2_q11']].values.tolist()
df['phone_numbers']=df['phone_numbers'].apply(lambda x:"".join([y[3:] for y in x if not(y.startswith("-"))]))
dummies = pd.get_dummies(df['phone_numbers'].str.split('').explode()).groupby(level=0).sum()
print(df['phone_numbers'].head())
df = pd.concat([df, dummies], axis=1)



### Testing 
df=df[['today','starttime', 'endtime','cs_enumname_name', 'shifted_starttime', 'time_between_two_surveys', 'distance_m','reg_name', 'hhid_confirmed', '0','1','2','3','4','5','6','7','8','9','key']]
df=df.astype('str')
# df.replace('nan', '', inplace=True)
# Get the number of rows and columns in the DataFrame
num_rows, num_cols = df.shape

# For example, updating from cell A2 (row 2, column 1)
start_cell = 'A1'
# Construct the range string
end_cell_column=num_cols +1
row_key=dict_[end_cell_column]
end_cell_row=1 + num_rows
end_cell=row_key+str(end_cell_row)
print(end_cell)
# break
# end_cell = chr(ord('A') + num_cols - 1) + str(2 + num_rows - 1)
range_ = f"{start_cell}:{end_cell}"

### converting the data to a list of list
# Convert DataFrame to list of lists
data = [df.columns.tolist()]+df.values.tolist()

### updating the google sheet
gc=gspread.service_account(filename='creds.json')
key_='1iJ_GDl0FqZxEr2vvi469zUlsVfg3F9AA-Gaw3SmqEt4'
### Reading in the specific googles sheets file
sh=gc.open_by_key(key_)
sheet=sh
sheet=sh.worksheet(f'_meta_monitoring')

sheet.update(data,range_)