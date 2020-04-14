def load(h):
    return ({'abbr': 1, 'code': 1, 'title': 'PRES Pressure [hPa]'},
            {'abbr': 2, 'code': 2, 'title': 'psnm Pressure reduced to MSL [hPa]'},
            {'abbr': 3, 'code': 3, 'title': 'tsps Pressure tendency [Pa/s]'},
            {'abbr': 4, 'code': 4, 'title': 'var4 undefined'},
            {'abbr': 5, 'code': 5, 'title': 'var5 undefined'},
            {'abbr': 6, 'code': 6, 'title': 'geop Geopotential [dam]'},
            {'abbr': 7, 'code': 7, 'title': 'zgeo Geopotential height [gpm]'},
            {'abbr': 8, 'code': 8, 'title': 'gzge Geometric height [m]'},
            {'abbr': 9, 'code': 9, 'title': 'var9 undefined'},
            {'abbr': 10, 'code': 10, 'title': 'var10 undefined'},
            {'abbr': 11, 'code': 11, 'title': 'temp ABSOLUTE TEMPERATURE [K]'},
            {'abbr': 12, 'code': 12, 'title': 'vtmp VIRTUAL TEMPERATURE [K]'},
            {'abbr': 13, 'code': 13, 'title': 'ptmp POTENTIAL TEMPERATURE [K]'},
            {'abbr': 14,
             'code': 14,
             'title': 'psat PSEUDO-ADIABATIC POTENTIAL TEMPERATURE [K]'},
            {'abbr': 15, 'code': 15, 'title': 'mxtp MAXIMUM TEMPERATURE [K]'},
            {'abbr': 16, 'code': 16, 'title': 'mntp MINIMUM TEMPERATURE [K]'},
            {'abbr': 17, 'code': 17, 'title': 'tpor DEW POINT TEMPERATURE [K]'},
            {'abbr': 18, 'code': 18, 'title': 'dptd DEW POINT DEPRESSION [K]'},
            {'abbr': 19, 'code': 19, 'title': 'lpsr LAPSE RATE [K/m]'},
            {'abbr': 20, 'code': 20, 'title': 'var20 undefined'},
            {'abbr': 21, 'code': 21, 'title': 'rds1 RADAR SPECTRA(1) [non-dim]'},
            {'abbr': 22, 'code': 22, 'title': 'rds2 RADAR SPECTRA(2) [non-dim]'},
            {'abbr': 23, 'code': 23, 'title': 'rds3 RADAR SPECTRA(3) [non-dim]'},
            {'abbr': 24, 'code': 24, 'title': 'var24 undefined'},
            {'abbr': 25, 'code': 25, 'title': 'tpan TEMPERATURE ANOMALY [K]'},
            {'abbr': 26, 'code': 26, 'title': 'psan PRESSURE ANOMALY [Pa hPa]'},
            {'abbr': 27, 'code': 27, 'title': 'zgan GEOPOT HEIGHT ANOMALY [m]'},
            {'abbr': 28, 'code': 28, 'title': 'wvs1 WAVE SPECTRA(1) [non-dim]'},
            {'abbr': 29, 'code': 29, 'title': 'wvs2 WAVE SPECTRA(2) [non-dim]'},
            {'abbr': 30, 'code': 30, 'title': 'wvs3 WAVE SPECTRA(3) [non-dim]'},
            {'abbr': 31, 'code': 31, 'title': 'wind WIND DIRECTION [deg]'},
            {'abbr': 32, 'code': 32, 'title': 'wins WIND SPEED [m/s]'},
            {'abbr': 33, 'code': 33, 'title': 'uvel ZONAL WIND (U) [m/s]'},
            {'abbr': 34, 'code': 34, 'title': 'vvel MERIDIONAL WIND (V) [m/s]'},
            {'abbr': 35, 'code': 35, 'title': 'fcor STREAM FUNCTION [m2/s]'},
            {'abbr': 36, 'code': 36, 'title': 'potv VELOCITY POTENTIAL [m2/s]'},
            {'abbr': 37, 'code': 37, 'title': 'var37 undefined'},
            {'abbr': 38, 'code': 38, 'title': 'sgvv SIGMA COORD VERT VEL [sec/sec]'},
            {'abbr': 39, 'code': 39, 'title': 'omeg OMEGA [Pa/s]'},
            {'abbr': 40, 'code': 40, 'title': 'omg2 VERTICAL VELOCITY [m/s]'},
            {'abbr': 41, 'code': 41, 'title': 'abvo ABSOLUTE VORTICITY [10**5/sec]'},
            {'abbr': 42, 'code': 42, 'title': 'abdv ABSOLUTE DIVERGENCE [10**5/sec]'},
            {'abbr': 43, 'code': 43, 'title': 'vort VORTICITY [1/s]'},
            {'abbr': 44, 'code': 44, 'title': 'divg DIVERGENCE [1/s]'},
            {'abbr': 45, 'code': 45, 'title': 'vucs VERTICAL U-COMP SHEAR [1/sec]'},
            {'abbr': 46, 'code': 46, 'title': 'vvcs VERT V-COMP SHEAR [1/sec]'},
            {'abbr': 47, 'code': 47, 'title': 'dirc DIRECTION OF CURRENT [deg]'},
            {'abbr': 48, 'code': 48, 'title': 'spdc SPEED OF CURRENT [m/s]'},
            {'abbr': 49, 'code': 49, 'title': 'ucpc U-COMPONENT OF CURRENT [m/s]'},
            {'abbr': 50, 'code': 50, 'title': 'vcpc V-COMPONENT OF CURRENT [m/s]'},
            {'abbr': 51, 'code': 51, 'title': 'umes SPECIFIC HUMIDITY [kg/kg]'},
            {'abbr': 52, 'code': 52, 'title': 'umrl RELATIVE HUMIDITY [no Dim]'},
            {'abbr': 53, 'code': 53, 'title': 'hmxr HUMIDITY MIXING RATIO [kg/kg]'},
            {'abbr': 54, 'code': 54, 'title': 'agpl INST. PRECIPITABLE WATER [Kg/m2]'},
            {'abbr': 55, 'code': 55, 'title': 'vapp VAPOUR PRESSURE [Pa hpa]'},
            {'abbr': 56, 'code': 56, 'title': 'sadf SATURATION DEFICIT [Pa hPa]'},
            {'abbr': 57, 'code': 57, 'title': 'evap EVAPORATION [Kg/m2/day]'},
            {'abbr': 58, 'code': 58, 'title': 'var58 undefined'},
            {'abbr': 59, 'code': 59, 'title': 'prcr PRECIPITATION RATE [kg/m2/day]'},
            {'abbr': 60, 'code': 60, 'title': 'thpb THUNDER PROBABILITY [%]'},
            {'abbr': 61, 'code': 61, 'title': 'prec TOTAL PRECIPITATION [Kg/m2/day]'},
            {'abbr': 62,
             'code': 62,
             'title': 'prge LARGE SCALE PRECIPITATION [Kg/m2/day]'},
            {'abbr': 63, 'code': 63, 'title': 'prcv CONVECTIVE PRECIPITATION [Kg/m2/day]'},
            {'abbr': 64, 'code': 64, 'title': 'neve SNOWFALL [Kg/m2/day]'},
            {'abbr': 65, 'code': 65, 'title': 'wenv WAT EQUIV ACC SNOW DEPTH [kg/m2]'},
            {'abbr': 66, 'code': 66, 'title': 'nvde SNOW DEPTH [cm]'},
            {'abbr': 67, 'code': 67, 'title': 'mxld MIXED LAYER DEPTH [m cm]'},
            {'abbr': 68, 'code': 68, 'title': 'tthd TRANS THERMOCLINE DEPTH [m cm]'},
            {'abbr': 69, 'code': 69, 'title': 'mthd MAIN THERMOCLINE DEPTH [m cm]'},
            {'abbr': 70, 'code': 70, 'title': 'mtha MAIN THERMOCLINE ANOM [m cm]'},
            {'abbr': 71, 'code': 71, 'title': 'cbnv CLOUD COVER [0-1]'},
            {'abbr': 72, 'code': 72, 'title': 'cvnv CONVECTIVE CLOUD COVER [0-1]'},
            {'abbr': 73, 'code': 73, 'title': 'lwnv LOW CLOUD COVER [0-1]'},
            {'abbr': 74, 'code': 74, 'title': 'mdnv MEDIUM CLOUD COVER [0-1]'},
            {'abbr': 75, 'code': 75, 'title': 'hinv HIGH CLOUD COVER [0-1]'},
            {'abbr': 76, 'code': 76, 'title': 'wtnv CLOUD WATER [kg/m2]'},
            {'abbr': 77, 'code': 77, 'title': 'bli BEST LIFTED INDEX (TO 500 HPA) [K]'},
            {'abbr': 78, 'code': 78, 'title': 'var78 undefined'},
            {'abbr': 79, 'code': 79, 'title': 'var79 undefined'},
            {'abbr': 80, 'code': 80, 'title': 'var80 undefined'},
            {'abbr': 81, 'code': 81, 'title': 'lsmk LAND SEA MASK [0,1]'},
            {'abbr': 82, 'code': 82, 'title': 'dslm DEV SEA_LEV FROM MEAN [m]'},
            {'abbr': 83, 'code': 83, 'title': 'zorl ROUGHNESS LENGTH [m]'},
            {'abbr': 84, 'code': 84, 'title': 'albe ALBEDO [%]'},
            {'abbr': 85, 'code': 85, 'title': 'dstp DEEP SOIL TEMPERATURE [K]'},
            {'abbr': 86, 'code': 86, 'title': 'soic SOIL MOISTURE CONTENT [Kg/m2]'},
            {'abbr': 87, 'code': 87, 'title': 'vege VEGETATION [%]'},
            {'abbr': 88, 'code': 88, 'title': 'var88 undefined'},
            {'abbr': 89, 'code': 89, 'title': 'dens DENSITY [kg/m3]'},
            {'abbr': 90, 'code': 90, 'title': 'var90 Undefined'},
            {'abbr': 91, 'code': 91, 'title': 'icec ICE CONCENTRATION [fraction]'},
            {'abbr': 92, 'code': 92, 'title': 'icet ICE THICKNESS [m]'},
            {'abbr': 93, 'code': 93, 'title': 'iced DIRECTION OF ICE DRIFT [deg]'},
            {'abbr': 94, 'code': 94, 'title': 'ices SPEED OF ICE DRIFT [m/s]'},
            {'abbr': 95, 'code': 95, 'title': 'iceu U-COMP OF ICE DRIFT [m/s]'},
            {'abbr': 96, 'code': 96, 'title': 'icev V-COMP OF ICE DRIFT [m/s]'},
            {'abbr': 97, 'code': 97, 'title': 'iceg ICE GROWTH [m]'},
            {'abbr': 98, 'code': 98, 'title': 'icdv ICE DIVERGENCE [sec/sec]'},
            {'abbr': 99, 'code': 99, 'title': 'var99 undefined'},
            {'abbr': 100, 'code': 100, 'title': 'shcw SIG HGT COM WAVE/SWELL [m]'},
            {'abbr': 101, 'code': 101, 'title': 'wwdi DIRECTION OF WIND WAVE [deg]'},
            {'abbr': 102, 'code': 102, 'title': 'wwsh SIG HGHT OF WIND WAVES [m]'},
            {'abbr': 103, 'code': 103, 'title': 'wwmp MEAN PERIOD WIND WAVES [sec]'},
            {'abbr': 104, 'code': 104, 'title': 'swdi DIRECTION OF SWELL WAVE [deg]'},
            {'abbr': 105, 'code': 105, 'title': 'swsh SIG HEIGHT SWELL WAVES [m]'},
            {'abbr': 106, 'code': 106, 'title': 'swmp MEAN PERIOD SWELL WAVES [sec]'},
            {'abbr': 107, 'code': 107, 'title': 'prwd PRIMARY WAVE DIRECTION [deg]'},
            {'abbr': 108, 'code': 108, 'title': 'prmp PRIM WAVE MEAN PERIOD [s]'},
            {'abbr': 109, 'code': 109, 'title': 'swdi SECOND WAVE DIRECTION [deg]'},
            {'abbr': 110, 'code': 110, 'title': 'swmp SECOND WAVE MEAN PERIOD [s]'},
            {'abbr': 111,
             'code': 111,
             'title': 'ocas SHORT WAVE ABSORBED AT GROUND [W/m2]'},
            {'abbr': 112, 'code': 112, 'title': 'slds NET LONG WAVE AT BOTTOM [W/m2]'},
            {'abbr': 113, 'code': 113, 'title': 'nswr NET SHORT-WAV RAD(TOP) [W/m2]'},
            {'abbr': 114, 'code': 114, 'title': 'role OUTGOING LONG WAVE AT TOP [W/m2]'},
            {'abbr': 115, 'code': 115, 'title': 'lwrd LONG-WAV RAD [W/m2]'},
            {'abbr': 116,
             'code': 116,
             'title': 'swea SHORT WAVE ABSORBED BY EARTH/ATMOSPHERE [W/m2]'},
            {'abbr': 117, 'code': 117, 'title': 'glbr GLOBAL RADIATION [W/m2 ]'},
            {'abbr': 118, 'code': 118, 'title': 'var118 undefined'},
            {'abbr': 119, 'code': 119, 'title': 'var119 undefined'},
            {'abbr': 120, 'code': 120, 'title': 'var120 undefined'},
            {'abbr': 121,
             'code': 121,
             'title': 'clsf LATENT HEAT FLUX FROM SURFACE [W/m2]'},
            {'abbr': 122,
             'code': 122,
             'title': 'cssf SENSIBLE HEAT FLUX FROM SURFACE [W/m2]'},
            {'abbr': 123, 'code': 123, 'title': 'blds BOUND LAYER DISSIPATION [W/m2]'},
            {'abbr': 124, 'code': 124, 'title': 'var124 undefined'},
            {'abbr': 125, 'code': 125, 'title': 'var125 undefined'},
            {'abbr': 126, 'code': 126, 'title': 'var126 undefined'},
            {'abbr': 127, 'code': 127, 'title': 'imag IMAGE [image^data]'},
            {'abbr': 128, 'code': 128, 'title': 'tp2m 2 METRE TEMPERATURE [K]'},
            {'abbr': 129, 'code': 129, 'title': 'dp2m 2 METRE DEWPOINT TEMPERATURE [K]'},
            {'abbr': 130, 'code': 130, 'title': 'u10m 10 METRE U-WIND COMPONENT [m/s]'},
            {'abbr': 131, 'code': 131, 'title': 'v10m 10 METRE V-WIND COMPONENT [m/s]'},
            {'abbr': 132, 'code': 132, 'title': 'topo TOPOGRAPHY [m]'},
            {'abbr': 133,
             'code': 133,
             'title': 'gsfp GEOMETRIC MEAN SURFACE PRESSURE [hPa]'},
            {'abbr': 134, 'code': 134, 'title': 'lnsp LN SURFACE PRESSURE [hPa]'},
            {'abbr': 135, 'code': 135, 'title': 'pslc SURFACE PRESSURE [hPa]'},
            {'abbr': 136,
             'code': 136,
             'title': 'pslm M S L PRESSURE (MESINGER METHOD) [hPa]'},
            {'abbr': 137, 'code': 137, 'title': 'mask MASK [-/+]'},
            {'abbr': 138, 'code': 138, 'title': 'mxwu MAXIMUM U-WIND [m/s]'},
            {'abbr': 139, 'code': 139, 'title': 'mxwv MAXIMUM V-WIND [m/s]'},
            {'abbr': 140,
             'code': 140,
             'title': 'cape CONVECTIVE AVAIL. POT.ENERGY [m2/s2]'},
            {'abbr': 141, 'code': 141, 'title': 'cine CONVECTIVE INHIB. ENERGY [m2/s2]'},
            {'abbr': 142, 'code': 142, 'title': 'lhcv CONVECTIVE LATENT HEATING [K/s]'},
            {'abbr': 143, 'code': 143, 'title': 'mscv CONVECTIVE MOISTURE SOURCE [1/s]'},
            {'abbr': 144,
             'code': 144,
             'title': 'scvm SHALLOW CONV. MOISTURE SOURCE [1/s]'},
            {'abbr': 145, 'code': 145, 'title': 'scvh SHALLOW CONVECTIVE HEATING [K/s]'},
            {'abbr': 146, 'code': 146, 'title': 'mxwp MAXIMUM WIND PRESS. LVL [hPa]'},
            {'abbr': 147, 'code': 147, 'title': 'ustr STORM MOTION U-COMPONENT [m/s]'},
            {'abbr': 148, 'code': 148, 'title': 'vstr STORM MOTION V-COMPONENT [m/s]'},
            {'abbr': 149, 'code': 149, 'title': 'cbnt MEAN CLOUD COVER [0-1]'},
            {'abbr': 150, 'code': 150, 'title': 'pcbs PRESSURE AT CLOUD BASE [hPa]'},
            {'abbr': 151, 'code': 151, 'title': 'pctp PRESSURE AT CLOUD TOP [hPa]'},
            {'abbr': 152, 'code': 152, 'title': 'fzht FREEZING LEVEL HEIGHT [m]'},
            {'abbr': 153,
             'code': 153,
             'title': 'fzrh FREEZING LEVEL RELATIVE HUMIDITY [%]'},
            {'abbr': 154, 'code': 154, 'title': 'fdlt FLIGHT LEVELS TEMPERATURE [K]'},
            {'abbr': 155, 'code': 155, 'title': 'fdlu FLIGHT LEVELS U-WIND [m/s]'},
            {'abbr': 156, 'code': 156, 'title': 'fdlv FLIGHT LEVELS V-WIND [m/s]'},
            {'abbr': 157, 'code': 157, 'title': 'tppp TROPOPAUSE PRESSURE [hPa]'},
            {'abbr': 158, 'code': 158, 'title': 'tppt TROPOPAUSE TEMPERATURE [K]'},
            {'abbr': 159, 'code': 159, 'title': 'tppu TROPOPAUSE U-WIND COMPONENT [m/s]'},
            {'abbr': 160, 'code': 160, 'title': 'tppv TROPOPAUSE v-WIND COMPONENT [m/s]'},
            {'abbr': 161, 'code': 161, 'title': 'var161 undefined'},
            {'abbr': 162, 'code': 162, 'title': 'gvdu GRAVITY WAVE DRAG DU/DT [m/s2]'},
            {'abbr': 163, 'code': 163, 'title': 'gvdv GRAVITY WAVE DRAG DV/DT [m/s2]'},
            {'abbr': 164,
             'code': 164,
             'title': 'gvus GRAVITY WAVE DRAG SFC ZONAL STRESS [Pa]'},
            {'abbr': 165,
             'code': 165,
             'title': 'gvvs GRAVITY WAVE DRAG SFC MERIDIONAL STRESS [Pa]'},
            {'abbr': 166, 'code': 166, 'title': 'var166 undefined'},
            {'abbr': 167,
             'code': 167,
             'title': 'dvsh DIVERGENCE OF SPECIFIC HUMIDITY [1/s]'},
            {'abbr': 168, 'code': 168, 'title': 'hmfc HORIZ. MOISTURE FLUX CONV. [1/s]'},
            {'abbr': 169,
             'code': 169,
             'title': 'vmfl VERT. INTEGRATED MOISTURE FLUX CONV. [kg/(m2*s)]'},
            {'abbr': 170,
             'code': 170,
             'title': 'vadv VERTICAL MOISTURE ADVECTION [kg/(kg*s)]'},
            {'abbr': 171,
             'code': 171,
             'title': 'nhcm NEG. HUM. CORR. MOISTURE SOURCE [kg/(kg*s)]'},
            {'abbr': 172, 'code': 172, 'title': 'lglh LARGE SCALE LATENT HEATING [K/s]'},
            {'abbr': 173, 'code': 173, 'title': 'lgms LARGE SCALE MOISTURE SOURCE [1/s]'},
            {'abbr': 174, 'code': 174, 'title': 'smav SOIL MOISTURE AVAILABILITY [0-1]'},
            {'abbr': 175, 'code': 175, 'title': 'tgrz SOIL TEMPERATURE OF ROOT ZONE [K]'},
            {'abbr': 176, 'code': 176, 'title': 'bslh BARE SOIL LATENT HEAT [Ws/m2]'},
            {'abbr': 177, 'code': 177, 'title': 'evpp POTENTIAL SFC EVAPORATION [m]'},
            {'abbr': 178, 'code': 178, 'title': 'rnof RUNOFF [kg/m2/s)]'},
            {'abbr': 179, 'code': 179, 'title': 'pitp INTERCEPTION LOSS [W/m2]'},
            {'abbr': 180,
             'code': 180,
             'title': 'vpca VAPOR PRESSURE OF CANOPY AIR SPACE [mb]'},
            {'abbr': 181, 'code': 181, 'title': 'qsfc SURFACE SPEC HUMIDITY [kg/kg]'},
            {'abbr': 182, 'code': 182, 'title': 'ussl SOIL WETNESS OF SURFACE [0-1]'},
            {'abbr': 183, 'code': 183, 'title': 'uzrs SOIL WETNESS OF ROOT ZONE [0-1]'},
            {'abbr': 184,
             'code': 184,
             'title': 'uzds SOIL WETNESS OF DRAINAGE ZONE [0-1]'},
            {'abbr': 185, 'code': 185, 'title': 'amdl STORAGE ON CANOPY [m]'},
            {'abbr': 186, 'code': 186, 'title': 'amsl STORAGE ON GROUND [m]'},
            {'abbr': 187, 'code': 187, 'title': 'tsfc SURFACE TEMPERATURE [K]'},
            {'abbr': 188, 'code': 188, 'title': 'tems SURFACE ABSOLUTE TEMPERATURE [K]'},
            {'abbr': 189,
             'code': 189,
             'title': 'tcas TEMPERATURE OF CANOPY AIR SPACE [K]'},
            {'abbr': 190, 'code': 190, 'title': 'ctmp TEMPERATURE AT CANOPY [K]'},
            {'abbr': 191,
             'code': 191,
             'title': 'tgsc GROUND/SURFACE COVER TEMPERATURE [K]'},
            {'abbr': 192, 'code': 192, 'title': 'uves SURFACE ZONAL WIND (U) [m/s]'},
            {'abbr': 193, 'code': 193, 'title': 'usst SURFACE ZONAL WIND STRESS [Pa]'},
            {'abbr': 194, 'code': 194, 'title': 'vves SURFACE MERIDIONAL WIND (V) [m/s]'},
            {'abbr': 195,
             'code': 195,
             'title': 'vsst SURFACE MERIDIONAL WIND STRESS [Pa]'},
            {'abbr': 196, 'code': 196, 'title': 'suvf SURFACE MOMENTUM FLUX [W/m2]'},
            {'abbr': 197, 'code': 197, 'title': 'iswf INCIDENT SHORT WAVE FLUX [W/m2]'},
            {'abbr': 198, 'code': 198, 'title': 'ghfl TIME AVE GROUND HT FLX [W/m2]'},
            {'abbr': 199, 'code': 199, 'title': 'var199 undefined'},
            {'abbr': 200,
             'code': 200,
             'title': 'lwbc NET LONG WAVE AT BOTTOM (CLEAR) [W/m2]'},
            {'abbr': 201,
             'code': 201,
             'title': 'lwtc OUTGOING LONG WAVE AT TOP (CLEAR) [W/m2]'},
            {'abbr': 202,
             'code': 202,
             'title': 'swec SHORT WV ABSRBD BY EARTH/ATMOS (CLEAR) [W/m2]'},
            {'abbr': 203,
             'code': 203,
             'title': 'ocac SHORT WAVE ABSORBED AT GROUND (CLEAR) [W/m2]'},
            {'abbr': 204, 'code': 204, 'title': 'var204 undefined'},
            {'abbr': 205, 'code': 205, 'title': 'lwrh LONG WAVE RADIATIVE HEATING [K/s]'},
            {'abbr': 206, 'code': 206, 'title': 'swrh SHORT WAVE RADIATIVE HEATING [K/s]'},
            {'abbr': 207,
             'code': 207,
             'title': 'olis DOWNWARD LONG WAVE AT BOTTOM [W/m2]'},
            {'abbr': 208,
             'code': 208,
             'title': 'olic DOWNWARD LONG WAVE AT BOTTOM (CLEAR) [W/m2]'},
            {'abbr': 209,
             'code': 209,
             'title': 'ocis DOWNWARD SHORT WAVE AT GROUND [W/m2]'},
            {'abbr': 210,
             'code': 210,
             'title': 'ocic DOWNWARD SHORT WAVE AT GROUND (CLEAR) [W/m2]'},
            {'abbr': 211, 'code': 211, 'title': 'oles UPWARD LONG WAVE AT BOTTOM [W/m2]'},
            {'abbr': 212, 'code': 212, 'title': 'oces UPWARD SHORT WAVE AT GROUND [W/m2]'},
            {'abbr': 213,
             'code': 213,
             'title': 'swgc UPWARD SHORT WAVE AT GROUND (CLEAR) [W/m2]'},
            {'abbr': 214, 'code': 214, 'title': 'roce UPWARD SHORT WAVE AT TOP [W/m2]'},
            {'abbr': 215,
             'code': 215,
             'title': 'swtc UPWARD SHORT WAVE AT TOP (CLEAR) [W/m2]'},
            {'abbr': 216, 'code': 216, 'title': 'var216 undefined'},
            {'abbr': 217, 'code': 217, 'title': 'var217 undefined'},
            {'abbr': 218, 'code': 218, 'title': 'hhdf HORIZONTAL HEATING DIFFUSION [K/s]'},
            {'abbr': 219,
             'code': 219,
             'title': 'hmdf HORIZONTAL MOISTURE DIFFUSION [1/s]'},
            {'abbr': 220,
             'code': 220,
             'title': 'hddf HORIZONTAL DIVERGENCE DIFFUSION [1/s2]'},
            {'abbr': 221,
             'code': 221,
             'title': 'hvdf HORIZONTAL VORTICITY DIFFUSION [1/s2]'},
            {'abbr': 222,
             'code': 222,
             'title': 'vdms VERTICAL DIFF. MOISTURE SOURCE [1/s]'},
            {'abbr': 223, 'code': 223, 'title': 'vdfu VERTICAL DIFFUSION DU/DT [m/s2]'},
            {'abbr': 224, 'code': 224, 'title': 'vdfv VERTICAL DIFFUSION DV/DT [m/s2]'},
            {'abbr': 225, 'code': 225, 'title': 'vdfh VERTICAL DIFFUSION HEATING [K/s]'},
            {'abbr': 226, 'code': 226, 'title': 'umrs SURFACE RELATIVE HUMIDITY [no Dim]'},
            {'abbr': 227,
             'code': 227,
             'title': 'vdcc VERTICAL DIST TOTAL CLOUD COVER [no Dim]'},
            {'abbr': 228, 'code': 228, 'title': 'var228 undefined'},
            {'abbr': 229, 'code': 229, 'title': 'var229 undefined'},
            {'abbr': 230,
             'code': 230,
             'title': 'usmt TIME MEAN SURFACE ZONAL WIND (U) [m/s]'},
            {'abbr': 231,
             'code': 231,
             'title': 'vsmt TIME MEAN SURFACE MERIDIONAL WIND (V) [m/s]'},
            {'abbr': 232,
             'code': 232,
             'title': 'tsmt TIME MEAN SURFACE ABSOLUTE TEMPERATURE [K]'},
            {'abbr': 233,
             'code': 233,
             'title': 'rsmt TIME MEAN SURFACE RELATIVE HUMIDITY [no Dim]'},
            {'abbr': 234, 'code': 234, 'title': 'atmt TIME MEAN ABSOLUTE TEMPERATURE [K]'},
            {'abbr': 235,
             'code': 235,
             'title': 'stmt TIME MEAN DEEP SOIL TEMPERATURE [K]'},
            {'abbr': 236, 'code': 236, 'title': 'ommt TIME MEAN DERIVED OMEGA [Pa/s]'},
            {'abbr': 237, 'code': 237, 'title': 'dvmt TIME MEAN DIVERGENCE [1/s]'},
            {'abbr': 238, 'code': 238, 'title': 'zhmt TIME MEAN GEOPOTENTIAL HEIGHT [m]'},
            {'abbr': 239,
             'code': 239,
             'title': 'lnmt TIME MEAN LOG SURFACE PRESSURE [ln(cbar)]'},
            {'abbr': 240, 'code': 240, 'title': 'mkmt TIME MEAN MASK [-/+]'},
            {'abbr': 241,
             'code': 241,
             'title': 'vvmt TIME MEAN MERIDIONAL WIND (V) [m/s]'},
            {'abbr': 242, 'code': 242, 'title': 'omtm TIME MEAN OMEGA [cbar/s]'},
            {'abbr': 243,
             'code': 243,
             'title': 'ptmt TIME MEAN POTENTIAL TEMPERATURE [K]'},
            {'abbr': 244, 'code': 244, 'title': 'pcmt TIME MEAN PRECIP. WATER [kg/m2]'},
            {'abbr': 245, 'code': 245, 'title': 'rhmt TIME MEAN RELATIVE HUMIDITY [%]'},
            {'abbr': 246, 'code': 246, 'title': 'mpmt TIME MEAN SEA LEVEL PRESSURE [hPa]'},
            {'abbr': 247, 'code': 247, 'title': 'simt TIME MEAN SIGMADOT [1/s]'},
            {'abbr': 248,
             'code': 248,
             'title': 'uemt TIME MEAN SPECIFIC HUMIDITY [kg/kg]'},
            {'abbr': 249, 'code': 249, 'title': 'fcmt TIME MEAN STREAM FUNCTION| m2/s]'},
            {'abbr': 250, 'code': 250, 'title': 'psmt TIME MEAN SURFACE PRESSURE [hPa]'},
            {'abbr': 251, 'code': 251, 'title': 'tmmt TIME MEAN SURFACE TEMPERATURE [K]'},
            {'abbr': 252,
             'code': 252,
             'title': 'pvmt TIME MEAN VELOCITY POTENTIAL [m2/s]'},
            {'abbr': 253, 'code': 253, 'title': 'tvmt TIME MEAN VIRTUAL TEMPERATURE [K]'},
            {'abbr': 254, 'code': 254, 'title': 'vtmt TIME MEAN VORTICITY [1/s]'},
            {'abbr': None, 'code': 255, 'title': 'uvmt TIME MEAN ZONAL WIND (U) [m/s]'})