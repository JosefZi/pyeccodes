import pyeccodes.accessors as _


def load(h):

    h.add(_.Codetable('parameterCategory', 1, "4.1.[discipline:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable('parameterNumber', 1, "4.2.[discipline:l].[parameterCategory:l].table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Codetable_units('parameterUnits', _.Get('parameterNumber')))
    h.add(_.Codetable_title('parameterName', _.Get('parameterNumber')))
    h.add(_.Codetable('constituentType', 2, "4.230.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfModeOfDistribution', 2))
    h.add(_.Unsigned('modeNumber', 2))
    h.add(_.Codetable('typeOfDistributionFunction', 2, "4.240.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('numberOfDistributionFunctionParameters', 1))
    h.alias('NP', 'numberOfDistributionFunctionParameters')

    with h.list('listOfDistributionFunctionParameter'):
        for i in range(0, h.get_l('numberOfDistributionFunctionParameters')):
            h.add(_.Signed('scaleFactorOfDistributionFunctionParameter', 1))
            h.add(_.Unsigned('scaledValueOfDistributionFunctionParameter', 4))
    h.add(_.Codetable('typeOfGeneratingProcess', 1, "4.3.table", _.Get('masterDir'), _.Get('localDir')))
    h.add(_.Unsigned('backgroundProcess', 1))
    h.alias('backgroundGeneratingProcessIdentifier', 'backgroundProcess')
    h.add(_.Unsigned('generatingProcessIdentifier', 1))
    h.add(_.Unsigned('hoursAfterDataCutoff', 2))
    h.alias('hoursAfterReferenceTimeOfDataCutoff', 'hoursAfterDataCutoff')
    h.add(_.Unsigned('minutesAfterDataCutoff', 1))
    h.alias('minutesAfterReferenceTimeOfDataCutoff', 'minutesAfterDataCutoff')
    h.add(_.Codetable('indicatorOfUnitOfTimeRange', 1, "4.4.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('defaultStepUnits', 'one')
    _.Template('grib2/localConcepts/[centre:s]/default_step_units.def', True).load(h)
    h.add(_.StringTransientCodetable('stepUnits', 1, "stepUnits.table"))
    h.add(_.Signed('forecastTime', 4))