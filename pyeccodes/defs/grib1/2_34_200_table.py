def load(h):
    return ({'abbr': 1, 'code': 1, 'title': 'PRES Pressure', 'units': 'Pa'},
            {'abbr': 2, 'code': 2, 'title': 'MSL Mean sea level pressure', 'units': 'Pa'},
            {'abbr': 3,
             'code': 3,
             'title': 'PTEND Pressure tendency',
             'units': 'Pa s**-1'},
            {'abbr': 4,
             'code': 4,
             'title': 'PV Potential vorticity',
             'units': 'K m**2 kg**-1 s**-1'},
            {'abbr': 5,
             'code': 5,
             'title': 'ICAHT ICAO Standard Atmosphere reference height',
             'units': 'm'},
            {'abbr': 6, 'code': 6, 'title': 'Z Geopotential', 'units': 'm**2 s**-2'},
            {'abbr': 7, 'code': 7, 'title': 'GH Geopotential Height', 'units': 'gpm'},
            {'abbr': 8, 'code': 8, 'title': 'H Geometrical height', 'units': 'm'},
            {'abbr': 9,
             'code': 9,
             'title': 'HSTDV Standard deviation of height',
             'units': 'm'},
            {'abbr': 10, 'code': 10, 'title': 'TOZNE Total ozone', 'units': 'Dobson'},
            {'abbr': 11, 'code': 11, 'title': 'T Temperature', 'units': 'K'},
            {'abbr': 12, 'code': 12, 'title': 'VTMP Virtual temperature', 'units': 'K'},
            {'abbr': 13, 'code': 13, 'title': 'PT Potential temperature', 'units': 'K'},
            {'abbr': 14,
             'code': 14,
             'title': 'PAPT Pseudo-adiabatic potential temperature',
             'units': 'K'},
            {'abbr': 15, 'code': 15, 'title': 'TMAX Maximum temperature', 'units': 'K'},
            {'abbr': 16, 'code': 16, 'title': 'TMIN Minimum temperature', 'units': 'K'},
            {'abbr': 17, 'code': 17, 'title': 'DPT Dew point temperature', 'units': 'K'},
            {'abbr': 18,
             'code': 18,
             'title': 'DEPR Dew point depression or deficit',
             'units': 'K'},
            {'abbr': 19, 'code': 19, 'title': 'LAPR Lapse rate', 'units': 'K m**-1'},
            {'abbr': 20, 'code': 20, 'title': 'VIS Visibility', 'units': 'm'},
            {'abbr': 21, 'code': 21, 'title': 'RDSP1 Radar spectra 1', 'units': '~'},
            {'abbr': 22, 'code': 22, 'title': 'RDSP2 Radar spectra 2', 'units': '~'},
            {'abbr': 23, 'code': 23, 'title': 'RDSP3 Radar spectra 3', 'units': '~'},
            {'abbr': 24,
             'code': 24,
             'title': 'PLI Parcel lifted index to 500 hPa',
             'units': 'K'},
            {'abbr': 25, 'code': 25, 'title': 'TA Temperature anomaly', 'units': 'K'},
            {'abbr': 26, 'code': 26, 'title': 'PRESA Pressure anomaly', 'units': 'Pa'},
            {'abbr': 27,
             'code': 27,
             'title': 'GPA Geopotential height anomaly',
             'units': 'gpm'},
            {'abbr': 28, 'code': 28, 'title': 'WVSP1 Wave spectra 1', 'units': '~'},
            {'abbr': 29, 'code': 29, 'title': 'WVSP2 Wave spectra 2', 'units': '~'},
            {'abbr': 30, 'code': 30, 'title': 'WVSP3 Wave spectra 3', 'units': '~'},
            {'abbr': 31,
             'code': 31,
             'title': 'WDIR Wind direction',
             'units': 'Degree true'},
            {'abbr': 32, 'code': 32, 'title': 'WS Wind speed', 'units': 'm s**-1'},
            {'abbr': 33, 'code': 33, 'title': 'U U component of wind', 'units': 'm s**-1'},
            {'abbr': 34, 'code': 34, 'title': 'V V component of wind', 'units': 'm s**-1'},
            {'abbr': 35,
             'code': 35,
             'title': 'STRF Stream function',
             'units': 'm**2 s**-1'},
            {'abbr': 36,
             'code': 36,
             'title': 'VP Velocity potential',
             'units': 'm**2 s**-1'},
            {'abbr': 37,
             'code': 37,
             'title': 'MNTSF Montgomery stream Function',
             'units': 'm**2 s**-2'},
            {'abbr': 38,
             'code': 38,
             'title': 'SGCVV Sigma coordinate vertical velocity',
             'units': 's**-1'},
            {'abbr': 39, 'code': 39, 'title': 'W Vertical velocity', 'units': 'Pa s**-1'},
            {'abbr': 40,
             'code': 40,
             'title': 'OMG2 Vertical velocity',
             'units': 'm s**-1'},
            {'abbr': 41, 'code': 41, 'title': 'ABSV Absolute vorticity', 'units': 's**-1'},
            {'abbr': 42,
             'code': 42,
             'title': 'ABSD Absolute divergence',
             'units': 's**-1'},
            {'abbr': 43, 'code': 43, 'title': 'VO Vorticity relative', 'units': 's**-1'},
            {'abbr': 44, 'code': 44, 'title': 'D Divergence', 'units': 's**-1'},
            {'abbr': 45,
             'code': 45,
             'title': 'VUCSH Vertical u-component shear',
             'units': 's**-1'},
            {'abbr': 46,
             'code': 46,
             'title': 'VVCSH Vertical v-component shear',
             'units': 's**-1'},
            {'abbr': 47,
             'code': 47,
             'title': 'DIRC Direction of current',
             'units': 'Degree true'},
            {'abbr': 48, 'code': 48, 'title': 'SPC Speed of current', 'units': 'm s**-1'},
            {'abbr': 49,
             'code': 49,
             'title': 'UCURR U-component of current',
             'units': 'm s**-1'},
            {'abbr': 50,
             'code': 50,
             'title': 'VCURR V-component of current',
             'units': 'm s**-1'},
            {'abbr': 51, 'code': 51, 'title': 'Q Specific humidity', 'units': 'kg kg**-1'},
            {'abbr': 52, 'code': 52, 'title': 'R Relative humidity', 'units': '%'},
            {'abbr': 53,
             'code': 53,
             'title': 'MIXR Humidity mixing ratio',
             'units': 'kg kg**-1'},
            {'abbr': 54,
             'code': 54,
             'title': 'PWAT Precipitable water',
             'units': 'kg m**-2'},
            {'abbr': 55, 'code': 55, 'title': 'VP Vapour pressure', 'units': 'Pa'},
            {'abbr': 56, 'code': 56, 'title': 'SATD Saturation deficit', 'units': 'Pa'},
            {'abbr': 57, 'code': 57, 'title': 'EVPSFC Evaporation', 'units': 'mm per day'},
            {'abbr': 58, 'code': 58, 'title': 'CICE Cloud Ice', 'units': 'kg m**-2'},
            {'abbr': 59,
             'code': 59,
             'title': 'PRATE Precipitation rate',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 60,
             'code': 60,
             'title': 'TSTM Thunderstorm probability',
             'units': '%'},
            {'abbr': 61,
             'code': 61,
             'title': 'TPRATSFC Total precipitation',
             'units': 'mm per day'},
            {'abbr': 62,
             'code': 62,
             'title': 'LPRATSFC Large scale precipitation',
             'units': 'mm per day'},
            {'abbr': 63,
             'code': 63,
             'title': 'CPRATSFC Convective precipitation',
             'units': 'mm per day'},
            {'abbr': 64,
             'code': 64,
             'title': 'SRWEQSFC Snowfall rate water equivalent',
             'units': 'mm per day'},
            {'abbr': 65,
             'code': 65,
             'title': 'SF Snow Fall water equivalent',
             'units': 'kg m**-2'},
            {'abbr': 66, 'code': 66, 'title': 'SD Snow depth', 'units': 'm'},
            {'abbr': 67, 'code': 67, 'title': 'MLD Mixed layer depth', 'units': 'm'},
            {'abbr': 68,
             'code': 68,
             'title': 'TTHDP Transient thermocline depth',
             'units': 'm'},
            {'abbr': 69, 'code': 69, 'title': 'MTHD Main thermocline depth', 'units': 'm'},
            {'abbr': 70,
             'code': 70,
             'title': 'MTHA Main thermocline anomaly',
             'units': 'm'},
            {'abbr': 71, 'code': 71, 'title': 'TCC Total Cloud Cover', 'units': '%'},
            {'abbr': 72, 'code': 72, 'title': 'CCC Convective cloud cover', 'units': '%'},
            {'abbr': 73, 'code': 73, 'title': 'LCC Low cloud cover', 'units': '%'},
            {'abbr': 74, 'code': 74, 'title': 'MCC Medium cloud cover', 'units': '%'},
            {'abbr': 75, 'code': 75, 'title': 'HCC High cloud cover', 'units': '%'},
            {'abbr': 76, 'code': 76, 'title': 'CWAT Cloud water', 'units': 'kg m**-2'},
            {'abbr': 77,
             'code': 77,
             'title': 'BLI Best lifted index to 500 hPa',
             'units': 'K'},
            {'abbr': 78, 'code': 78, 'title': 'SNOC Convective snow', 'units': 'kg m**-2'},
            {'abbr': 79,
             'code': 79,
             'title': 'LSSF Large scale snow',
             'units': 'kg m**-2'},
            {'abbr': 80, 'code': 80, 'title': 'WTMP Water temperature', 'units': 'K'},
            {'abbr': 81, 'code': 81, 'title': 'LSM Land-sea mask', 'units': '(0 - 1)'},
            {'abbr': 82,
             'code': 82,
             'title': 'DSLM Deviation of sea-level from mean',
             'units': 'm'},
            {'abbr': 83, 'code': 83, 'title': 'SR Surface roughness', 'units': 'm'},
            {'abbr': 84, 'code': 84, 'title': 'AL Albedo', 'units': '%'},
            {'abbr': 85, 'code': 85, 'title': 'ST Soil Temperature', 'units': 'K'},
            {'abbr': 86,
             'code': 86,
             'title': 'SSW Soil moisture content',
             'units': 'kg m**-2'},
            {'abbr': 87,
             'code': 87,
             'title': 'VEGREA Percentage of vegetation',
             'units': '%'},
            {'abbr': 88, 'code': 88, 'title': 'S Salinity', 'units': 'kg kg**-1'},
            {'abbr': 89, 'code': 89, 'title': 'DEN Density', 'units': 'kg m**-3'},
            {'abbr': 90,
             'code': 90,
             'title': 'ROFSFC Water run-off',
             'units': 'mm per day'},
            {'abbr': 91, 'code': 91, 'title': 'ICEC Ice cover', 'units': '(0 - 1)'},
            {'abbr': 92, 'code': 92, 'title': 'ICETK Ice thickness', 'units': 'm'},
            {'abbr': 93,
             'code': 93,
             'title': 'DICED Direction of ice drift',
             'units': 'Degree true'},
            {'abbr': 94,
             'code': 94,
             'title': 'SICED Speed of ice drift',
             'units': 'm s**-1'},
            {'abbr': 95,
             'code': 95,
             'title': 'UICE U-component of ice drift',
             'units': 'm s**-1'},
            {'abbr': 96,
             'code': 96,
             'title': 'VICE V-component of ice drift',
             'units': 'm s**-1'},
            {'abbr': 97, 'code': 97, 'title': 'ICEG Ice growth rate', 'units': 'm s**-1'},
            {'abbr': 98, 'code': 98, 'title': 'ICED Ice divergence', 'units': 's**-1'},
            {'abbr': 99, 'code': 99, 'title': 'SNOM Snow melt', 'units': 'kg m**-2'},
            {'abbr': 100,
             'code': 100,
             'title': 'SWH Significant height of combined wind waves and swell',
             'units': 'm'},
            {'abbr': 101,
             'code': 101,
             'title': 'MDWW Mean direction of wind waves',
             'units': 'Degree true'},
            {'abbr': 102,
             'code': 102,
             'title': 'SHWW Significant height of wind waves',
             'units': 'm'},
            {'abbr': 103,
             'code': 103,
             'title': 'MPWW Mean period of wind waves',
             'units': 's'},
            {'abbr': 104,
             'code': 104,
             'title': 'SWDIR Direction of swell waves',
             'units': 'Degree true'},
            {'abbr': 105,
             'code': 105,
             'title': 'SWELL Significant height of swell waves',
             'units': 'm'},
            {'abbr': 106,
             'code': 106,
             'title': 'SWPER Mean period of swell waves',
             'units': 's'},
            {'abbr': 107,
             'code': 107,
             'title': 'MDPS Primary wave direction',
             'units': 'Degree true'},
            {'abbr': 108,
             'code': 108,
             'title': 'MPPS Primary wave mean period',
             'units': 's'},
            {'abbr': 109,
             'code': 109,
             'title': 'DIRSW Secondary wave direction',
             'units': 'Degree true'},
            {'abbr': 110,
             'code': 110,
             'title': 'SWP Secondary wave mean period',
             'units': 's'},
            {'abbr': 111,
             'code': 111,
             'title': 'NSWRS Net short-wave radiation flux surface',
             'units': 'W m**-2'},
            {'abbr': 112,
             'code': 112,
             'title': 'NLWRS Net long-wave radiation flux surface',
             'units': 'W m**-2'},
            {'abbr': 113,
             'code': 113,
             'title': 'NLWRT Net short-wave radiation flux top of atmosphere',
             'units': 'W m**-2'},
            {'abbr': 114,
             'code': 114,
             'title': 'NLWRT Net long-wave radiation flux top of atmosphere',
             'units': 'W m**-2'},
            {'abbr': 115,
             'code': 115,
             'title': 'LWAVR Long wave radiation flux',
             'units': 'W m**-2'},
            {'abbr': 116,
             'code': 116,
             'title': 'SWAVR Short wave radiation flux',
             'units': 'W m**-2'},
            {'abbr': 117,
             'code': 117,
             'title': 'GRAD Global radiation flux',
             'units': 'W m**-2'},
            {'abbr': 118,
             'code': 118,
             'title': 'BTMP Brightness temperature',
             'units': 'K'},
            {'abbr': 119,
             'code': 119,
             'title': 'LWRAD Radiance with respect to wave number',
             'units': 'W m**-1 sr**-1'},
            {'abbr': 120,
             'code': 120,
             'title': 'SWRAD Radiance with respect to wave length',
             'units': 'W m**-3 sr**-1'},
            {'abbr': 121,
             'code': 121,
             'title': 'LHF Latent heat flux',
             'units': 'W m**-2'},
            {'abbr': 122,
             'code': 122,
             'title': 'SHF Sensible heat flux',
             'units': 'W m**-2'},
            {'abbr': 123,
             'code': 123,
             'title': 'BLD Boundary layer dissipation',
             'units': 'W m**-2'},
            {'abbr': 124,
             'code': 124,
             'title': 'UFLX Momentum flux, u-component',
             'units': 'N m**-2'},
            {'abbr': 125,
             'code': 125,
             'title': 'VFLX Momentum flux, v-component',
             'units': 'N m**-2'},
            {'abbr': 126, 'code': 126, 'title': 'WMIXE Wind mixing energy', 'units': 'J'},
            {'abbr': 127, 'code': 127, 'title': 'IMGD Image data', 'units': '~'},
            {'abbr': 132,
             'code': 132,
             'title': 'BVF2THT Square of Brunt-Vaisala frequency',
             'units': 's**-2'},
            {'abbr': 144,
             'code': 144,
             'title': 'CTMP Temperature at canopy',
             'units': 'K'},
            {'abbr': 145,
             'code': 145,
             'title': 'TGSC Ground/surface cover temperature',
             'units': 'K'},
            {'abbr': 146,
             'code': 146,
             'title': 'CWORK Cloud work function',
             'units': 'J kg**-1'},
            {'abbr': 147,
             'code': 147,
             'title': 'FGLUSFC Zonal momentum flux by long gravity wave',
             'units': 'N m**-2'},
            {'abbr': 148,
             'code': 148,
             'title': 'FGLVSFC Meridional momentum flux by long gravity wave',
             'units': 'N m**-2'},
            {'abbr': 151,
             'code': 151,
             'title': 'ADUAHBL Adiabatic zonal acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 152,
             'code': 152,
             'title': 'VWVCLM Meridional water vapour flux',
             'units': 'kg m**-1 s**-1'},
            {'abbr': 154,
             'code': 154,
             'title': 'FGSVSFC Meridional momentum flux by short gravity wave',
             'units': 'N m**-2'},
            {'abbr': 155,
             'code': 155,
             'title': 'GFLUX Ground heat flux',
             'units': 'W m**-2'},
            {'abbr': 157,
             'code': 157,
             'title': '~ Vertical integral of eastward water vapour flux',
             'units': 'kg m**-1 s**-1'},
            {'abbr': 159,
             'code': 159,
             'title': 'FGSUSFC Zonal momentum flux by short gravity wave',
             'units': 'N m**-2'},
            {'abbr': 160,
             'code': 160,
             'title': 'CSUSF Clear Sky Upward Solar Flux',
             'units': 'W m**-2'},
            {'abbr': 161,
             'code': 161,
             'title': 'CSDSF Clear Sky Downward Solar Flux',
             'units': 'W m**-2'},
            {'abbr': 162,
             'code': 162,
             'title': 'CSULF Clear Sky Upward Long Wave Flux',
             'units': 'W m**-2'},
            {'abbr': 163,
             'code': 163,
             'title': 'CSDLF Clear Sky Downward Long Wave Flux',
             'units': 'W m**-2'},
            {'abbr': 165,
             'code': 165,
             'title': 'ADVAPRS Adiabatic meridional acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 170,
             'code': 170,
             'title': 'FRCVSFC Frequency of deep convection',
             'units': '%'},
            {'abbr': 171,
             'code': 171,
             'title': 'FRCVSSFC Frequency of shallow convection',
             'units': '%'},
            {'abbr': 172,
             'code': 172,
             'title': 'FRSCSFC Frequency of stratocumulus parameterisation',
             'units': '%'},
            {'abbr': 173,
             'code': 173,
             'title': 'GWDUAHBL Gravity wave zonal acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 174,
             'code': 174,
             'title': 'GWDVAHBL Gravity wave meridional acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 190,
             'code': 190,
             'title': 'UTHECLM Zonal thermal energy flux',
             'units': 'W m**-1'},
            {'abbr': 191,
             'code': 191,
             'title': 'VTHECLM Meridional thermal energy flux',
             'units': 'W m**-1'},
            {'abbr': 202,
             'code': 202,
             'title': 'LTRSSFC Evapotranspiration',
             'units': 'W m**-2'},
            {'abbr': 203,
             'code': 203,
             'title': 'PITP Interception loss',
             'units': 'W m**-2'},
            {'abbr': 204,
             'code': 204,
             'title': 'DSWRF Downward short-wave radiation flux',
             'units': 'W m**-2'},
            {'abbr': 205,
             'code': 205,
             'title': 'DLWRF Downward long-wave radiation flux',
             'units': 'W m**-2'},
            {'abbr': 211,
             'code': 211,
             'title': 'USWRF Upward short-wave radiation flux',
             'units': 'W m**-2'},
            {'abbr': 212,
             'code': 212,
             'title': 'ULWRF Upward long-wave radiation flux',
             'units': 'W m**-2'},
            {'abbr': 219,
             'code': 219,
             'title': 'MAXGUST Maximum wind speed',
             'units': 'm s**-1'},
            {'abbr': 221,
             'code': 221,
             'title': 'QC specific cloud water content',
             'units': 'kg kg**-1'},
            {'abbr': 222,
             'code': 222,
             'title': 'ADHRHBL Adiabatic heating rate',
             'units': 'K per day'},
            {'abbr': 223,
             'code': 223,
             'title': 'MSCSFC Moisture storage on canopy',
             'units': 'm'},
            {'abbr': 224,
             'code': 224,
             'title': 'MSGSFC Moisture storage on ground or cover',
             'units': 'm'},
            {'abbr': 225,
             'code': 225,
             'title': 'USSL Soil wetness of surface',
             'units': '(0 - 1)'},
            {'abbr': 226,
             'code': 226,
             'title': 'SMCUGL Mass concentration of condensed water in soil',
             'units': 'kg m**-3'},
            {'abbr': 227,
             'code': 227,
             'title': 'CWCLM Cloud liquid water',
             'units': 'kg m**-2'},
            {'abbr': 228,
             'code': 228,
             'title': 'CLW Cloud liquid water',
             'units': 'kg kg**-1'},
            {'abbr': 229,
             'code': 229,
             'title': 'CIWC Specific cloud ice water content',
             'units': 'kg kg**-1'},
            {'abbr': 230,
             'code': 230,
             'title': 'MFLXBHBL Upward mass flux at cloud base',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 231,
             'code': 231,
             'title': 'MFLUXHBL Upward mass flux',
             'units': 'kg m**-2 s**-1'},
            {'abbr': 236,
             'code': 236,
             'title': 'ADMRHBL Adiabatic moistening rate',
             'units': 'kg kg**-1 per day'},
            {'abbr': 237,
             'code': 237,
             'title': 'OZONEHBL Ozone mixing ratio',
             'units': 'mg kg**-1'},
            {'abbr': 239,
             'code': 239,
             'title': 'CNVUAHBL Convective zonal acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 240,
             'code': 240,
             'title': 'CNVVAHBL Convective meridional acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 241,
             'code': 241,
             'title': 'LRGHRHBL Large scale condensation heating rate',
             'units': 'K per day'},
            {'abbr': 242,
             'code': 242,
             'title': 'CNVHRHBL Convective heating rate',
             'units': 'K per day'},
            {'abbr': 243,
             'code': 243,
             'title': 'CNVMRHBL Convective moistening rate',
             'units': 'kg kg**-1 per day'},
            {'abbr': 246,
             'code': 246,
             'title': 'VDFHRHBL Vertical diffusion heating rate',
             'units': 'K per day'},
            {'abbr': 247,
             'code': 247,
             'title': 'VDFUAHBL Vertical diffusion zonal acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 248,
             'code': 248,
             'title': 'VDFVAHBL Vertical diffusion meridional acceleration',
             'units': 'm s**-1 per day'},
            {'abbr': 249,
             'code': 249,
             'title': 'VDFMRHBL Vertical diffusion moistening rate',
             'units': 'kg kg**-1 per day'},
            {'abbr': 250,
             'code': 250,
             'title': 'SWHRHBL Solar radiative heating rate',
             'units': 'K per day'},
            {'abbr': 251,
             'code': 251,
             'title': 'LWHRHBL Long wave radiative heating rate',
             'units': 'K per day'},
            {'abbr': 252,
             'code': 252,
             'title': 'Type of vegetation',
             'units': 'Code Table JMA-252'},
            {'abbr': 253,
             'code': 253,
             'title': 'LRGMRHBL Large scale moistening rate',
             'units': 'kg kg**-1 per day'})
