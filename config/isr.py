# Config override for lsst.ip.isr.IsrTask

# This dataset contains CP calibs, not regular ones
config.connections.bias = "cpBias"
config.connections.flat = "cpFlat"
# For Gen 2 support
config.biasDataProductName = config.connections.bias
config.flatDataProductName = config.connections.flat
