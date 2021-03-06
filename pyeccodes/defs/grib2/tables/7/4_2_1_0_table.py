def load(h):
    return ({'abbr': 0,
             'code': 0,
             'title': 'Flash flood guidance (Encoded as an accumulation over a floating '
                      'subinterval of time between the reference time and valid time)',
             'units': 'kg m-2'},
            {'abbr': 1,
             'code': 1,
             'title': 'Flash flood runoff (Encoded as an accumulation over a floating '
                      'subinterval of time)',
             'units': 'kg m-2'},
            {'abbr': 2,
             'code': 2,
             'title': 'Remotely sensed snow cover',
             'units': 'code table 4.215'},
            {'abbr': 3,
             'code': 3,
             'title': 'Elevation of snow covered terrain',
             'units': 'code table 4.216'},
            {'abbr': 4,
             'code': 4,
             'title': 'Snow water equivalent percent of normal',
             'units': '%'},
            {'abbr': 5,
             'code': 5,
             'title': 'Baseflow-groundwater runoff',
             'units': 'kg m-2'},
            {'abbr': 6, 'code': 6, 'title': 'Storm surface runoff', 'units': 'kg m-2'},
            {'abbr': None, 'code': 255, 'title': 'Missing', 'units': '-'})
