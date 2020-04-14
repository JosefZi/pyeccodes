def load(h):
    return ({'abbr': 'mslp', 'code': 1, 'title': 'MSLP Pressure reduced to MSL Pa'},
            {'abbr': 't', 'code': 11, 'title': 'T Temperature K'},
            {'abbr': 'vis', 'code': 20, 'title': 'VIS Visibility m'},
            {'abbr': 'u', 'code': 33, 'title': 'U u-component of wind m/s'},
            {'abbr': 'v', 'code': 34, 'title': 'V v-component of wind m/s'},
            {'abbr': 'r', 'code': 52, 'title': 'R Relative humidity %'},
            {'abbr': 'fzrapr', 'code': 58, 'title': 'FZRAPR Probability of frozen rain %'},
            {'abbr': 'tstm', 'code': 60, 'title': 'TSTM Probability thunderstorm %'},
            {'abbr': 'tcc', 'code': 71, 'title': 'TCC Total cloud cover fraction'},
            {'abbr': 'ccc', 'code': 72, 'title': 'CCC Convective cloud cover fraction'},
            {'abbr': 'lcc', 'code': 73, 'title': 'LCC Low cloud cover fraction'},
            {'abbr': 'mcc', 'code': 74, 'title': 'MCC Medium cloud cove fraction'},
            {'abbr': 'hcc', 'code': 75, 'title': 'HCC High cloud cover fraction'},
            {'abbr': 'cm', 'code': 77, 'title': 'CM cloud mask fraction'},
            {'abbr': 'epstm', 'code': 110, 'title': 'EPSTM EPS T mean K'},
            {'abbr': 'epststd',
             'code': 111,
             'title': 'EPSTSTD EPS T standard deviation K'},
            {'abbr': 'mxws10min',
             'code': 130,
             'title': 'MXWS10MIN Maximum wind (mean 10 min) M/S'},
            {'abbr': 'gust', 'code': 131, 'title': 'GUST Wind gust M/S'},
            {'abbr': 'cbase_sig',
             'code': 135,
             'title': 'CBASE_SIG Cloud base (significant) m'},
            {'abbr': 'ctop_sig',
             'code': 136,
             'title': 'CTOP_SIG Cloud top (significant) m'},
            {'abbr': 'pit',
             'code': 140,
             'title': 'PIT Precipitation intensity total kg/m2/s'},
            {'abbr': 'pis',
             'code': 141,
             'title': 'PIS Precipitation intensity snow kg/m2/s'},
            {'abbr': 'ptype',
             'code': 145,
             'title': 'PTYPE Precipitation type, conv 0, large scale 1, no prec -9 '
                      'category'},
            {'abbr': 'pcat',
             'code': 146,
             'title': 'PCAT Category of precipitation, 0 no, 1 snow, 2 snow and rain, 3 '
                      'rain, 4 drizzle, 5, freezing rain, 6 freezing drizzle category'},
            {'abbr': 'dswrf',
             'code': 150,
             'title': 'DSWRF Downward short-wave radiation flux W/m2'},
            {'abbr': 'uswrf',
             'code': 151,
             'title': 'USWRF Upward short-wave radiation flux W/m2'},
            {'abbr': 'nswrf',
             'code': 152,
             'title': 'NSWRF Net short wave radiation flux W/m2'},
            {'abbr': 'photar',
             'code': 153,
             'title': 'PHOTAR Photosynthetically active radiation W/m2'},
            {'abbr': 'nswrfcs',
             'code': 154,
             'title': 'NSWRFCS Net short-wave radiation flux, clear sky W/m2'},
            {'abbr': 'dwuvr', 'code': 155, 'title': 'DWUVR Downward UV radiation W/m2'},
            {'abbr': 'uviucs',
             'code': 156,
             'title': 'UVIUCS UV index (under clear sky) Numeric'},
            {'abbr': 'uvi', 'code': 157, 'title': 'UVI UV index Numeric'},
            {'abbr': 'dlwrf',
             'code': 158,
             'title': 'DLWRF Downward long-wave radiation flux W/m2'},
            {'abbr': 'ulwrf',
             'code': 159,
             'title': 'ULWRF Upward long-wave radiation flux W/m2'},
            {'abbr': 'nlwrf',
             'code': 160,
             'title': 'NLWRF Net long wave radiation flux W/m2'},
            {'abbr': 'nlwrfcs',
             'code': 161,
             'title': 'NLWRFCS Net long-wave radiation flux, clear sky W/m2'},
            {'abbr': 'cdca', 'code': 162, 'title': 'CDCA Cloud amount %'},
            {'abbr': 'cdct', 'code': 163, 'title': 'CDCT Cloud type Code'},
            {'abbr': 'tmaxt', 'code': 164, 'title': 'TMAXT Thunderstorm maximum tops m'},
            {'abbr': 'thunc', 'code': 165, 'title': 'THUNC Thunderstorm coverage Code'},
            {'abbr': 'cdcb', 'code': 166, 'title': 'CDCB Cloud base m'},
            {'abbr': 'cdct', 'code': 167, 'title': 'CDCT Cloud top m'},
            {'abbr': 'ceil', 'code': 168, 'title': 'CEIL Ceiling m'},
            {'abbr': 'cdlyr', 'code': 169, 'title': 'CDLYR Non-convective cloud cover %'},
            {'abbr': 'cwork', 'code': 170, 'title': 'CWORK Cloud work function J/kg'},
            {'abbr': 'cuefi',
             'code': 171,
             'title': 'CUEFI Convective cloud efficiency Proportion'},
            {'abbr': 'tcond', 'code': 172, 'title': 'TCOND Total condensate kg/kg'},
            {'abbr': 'tcolw',
             'code': 173,
             'title': 'TCOLW Total column-integrated cloud water kg/m2'},
            {'abbr': 'tcoli',
             'code': 174,
             'title': 'TCOLI Total column-integrated cloud ice kg/m2'},
            {'abbr': 'tcolc',
             'code': 175,
             'title': 'TCOLC Total column-integrated condensate kg/m2'},
            {'abbr': 'fice',
             'code': 176,
             'title': 'FICE Ice fraction of total condensate Proportion'},
            {'abbr': 'cc', 'code': 177, 'title': 'CC Cloud cover %'},
            {'abbr': 'cdcimr',
             'code': 178,
             'title': 'CDCIMR Cloud ice mixing ratio kg/kg'},
            {'abbr': 'suns', 'code': 179, 'title': 'SUNS Sunshine Numeric'},
            {'abbr': 'cbext',
             'code': 180,
             'title': 'CBEXT Horizontal extent of cumulunimbus (CB) %'},
            {'abbr': 'fracc',
             'code': 181,
             'title': 'FRACC Fraction of cloud cover Numeric'},
            {'abbr': 'sund', 'code': 182, 'title': 'SUND Sunshine duration s'},
            {'abbr': 'kx', 'code': 183, 'title': 'KX K index K'},
            {'abbr': 'kox', 'code': 184, 'title': 'KOX KO index K'},
            {'abbr': 'totalx', 'code': 185, 'title': 'TOTALX Total totals index K'},
            {'abbr': 'sx', 'code': 186, 'title': 'SX Sweat index Numeric'},
            {'abbr': 'hlcy', 'code': 187, 'title': 'HLCY Storm relative helicity J/kg'},
            {'abbr': 'ehlx', 'code': 188, 'title': 'EHLX Energy helicity index Numeric'},
            {'abbr': 'lftx', 'code': 189, 'title': 'LFTX Surface lifted index K'},
            {'abbr': '4lftx', 'code': 190, 'title': '4LFTX Best (4-layer) lifted index K'},
            {'abbr': 'ri', 'code': 191, 'title': 'RI Richardson number Numeric'},
            {'abbr': 'aerot', 'code': 192, 'title': 'AEROT Aerosol type Code'},
            {'abbr': 'o3mx', 'code': 193, 'title': 'O3MX Ozone mixing ratio kg/kg'},
            {'abbr': 'tcioz',
             'code': 194,
             'title': 'TCIOZ Total column integrated ozone Dobson'},
            {'abbr': 'bswid', 'code': 200, 'title': 'BSWID Base spectrum width m/s'},
            {'abbr': 'bref', 'code': 201, 'title': 'BREF Base reflectivity dB'},
            {'abbr': 'brvel', 'code': 202, 'title': 'BRVEL Base radial velocity m/s'},
            {'abbr': 'veril',
             'code': 203,
             'title': 'VERIL Vertically integrated liquid kg/m'},
            {'abbr': 'lmaxbr',
             'code': 204,
             'title': 'LMAXBR Layer-maximum base reflectivity dB'},
            {'abbr': 'prrad', 'code': 205, 'title': 'PRRAD Precipitation (radar) kg/m'},
            {'abbr': 'eqrrra',
             'code': 206,
             'title': 'EQRRRA Equivalent radar reflectivity factor for rain mm6/m3'},
            {'abbr': 'eqrrsn',
             'code': 207,
             'title': 'EQRRSN Equivalent radar reflectivity factor for snow mm6/m3'},
            {'abbr': 'eqrfpc',
             'code': 208,
             'title': 'EQRFPC Equivalent radar reflectivity factor for paramterized '
                      'convection mm6/m3'},
            {'abbr': 'ectop_rad', 'code': 209, 'title': 'ECTOP_RAD Echo top (radar) m'},
            {'abbr': 'refl_rad', 'code': 210, 'title': 'REFL_RAD Reflectivity (radar) dB'},
            {'abbr': 'corefl_rad',
             'code': 211,
             'title': 'COREFL_RAD Composite reflectivity (radar) dB'},
            {'abbr': 'icit', 'code': 215, 'title': 'ICIT Icing top m'},
            {'abbr': 'icib', 'code': 216, 'title': 'ICIB Icing base m'},
            {'abbr': 'ici', 'code': 217, 'title': 'ICI Icing Code'},
            {'abbr': 'turbt', 'code': 218, 'title': 'TURBT Turbulence top m'},
            {'abbr': 'turbb', 'code': 219, 'title': 'TURBB Turbulence base m'},
            {'abbr': 'turb', 'code': 220, 'title': 'TURB Turbulence Code'},
            {'abbr': 'pblr',
             'code': 221,
             'title': 'PBLR Planetary boundary-layer regime Code'},
            {'abbr': 'conti', 'code': 222, 'title': 'CONTI Contrail intensity Code'},
            {'abbr': 'contet', 'code': 223, 'title': 'CONTET Contrail engine type Code'},
            {'abbr': 'contt', 'code': 224, 'title': 'CONTT Contrail top m'},
            {'abbr': 'contb', 'code': 225, 'title': 'CONTB Contrail base m'},
            {'abbr': 'snfalb', 'code': 226, 'title': 'SNFALB Snow free albedo %'},
            {'abbr': 'ici_prop', 'code': 227, 'title': 'ICI_PROP Icing %'},
            {'abbr': 'icturb', 'code': 228, 'title': 'ICTURB In-cloud turbulence %'},
            {'abbr': 'cat', 'code': 229, 'title': 'CAT Clear air turbulence (CAT) %'},
            {'abbr': 'scld_prob',
             'code': 230,
             'title': 'SCLD_PROB Supercooled large droplet probability %'},
            {'abbr': 'text', 'code': 235, 'title': 'TEXT Arbitrary text string CCITTIA5'},
            {'abbr': 'secpref',
             'code': 236,
             'title': 'SECPREF Seconds prior to initial reference time (defined in '
                      'section1) (meteorology) s'})