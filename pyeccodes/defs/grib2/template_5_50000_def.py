import pyeccodes.accessors as _


def load(h):

    h.add(_.Ieeefloat('referenceValue', 4))
    h.add(_.Reference_value_error('referenceValueError', _.Get('referenceValue'), _.Get('ieee')))
    h.add(_.Signed('binaryScaleFactor', 2))
    h.add(_.Signed('decimalScaleFactor', 2))
    h.add(_.Transient('optimizeScaleFactor', 0))
    h.add(_.Unsigned('bitsPerValue', 1))
    h.alias('numberOfBits', 'bitsPerValue')
    h.alias('numberOfBitsContainingEachPackedValue', 'bitsPerValue')

    if h._gribex_mode_on():
        h.add(_.Transient('computeLaplacianOperator', 0))
    else:
        h.add(_.Transient('computeLaplacianOperator', 1))

    h.add(_.Spectral_truncation('_numberOfValues', _.Get('J'), _.Get('K'), _.Get('M'), _.Get('numberOfValues')))
    h.add(_.Constant('laplacianScalingFactorUnset', -2147483647))
    h.add(_.Signed('laplacianScalingFactor', 4))
    h.add(_.Scale('laplacianOperator', _.Get('laplacianScalingFactor'), _.Get('one'), _.Get('million'), _.Get('truncateLaplacian')))
    h.alias('data.laplacianOperator', 'laplacianOperator')
    h.add(_.Evaluate('laplacianOperatorIsSet', ((_.Get('laplacianScalingFactor') != _.Get('laplacianScalingFactorUnset')) and not (_.Get('computeLaplacianOperator')))))
    h.add(_.Transient('JS', 20))
    h.add(_.Transient('KS', 20))
    h.add(_.Transient('MS', 20))
    h.add(_.Transient('subSetJ', 0))
    h.add(_.Transient('subSetK', 0))
    h.add(_.Transient('subSetM', 0))
    h.add(_.Unsigned('TS', 4))
    h.add(_.Spectral_truncation('_TS', _.Get('J'), _.Get('K'), _.Get('M'), _.Get('TS')))
    h.add(_.Codetable('unpackedSubsetPrecision', 1, "5.7.table", _.Get('masterDir'), _.Get('localDir')))
    h.alias('precisionOfTheUnpackedSubset', 'unpackedSubsetPrecision')