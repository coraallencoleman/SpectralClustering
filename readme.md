
Monkeying Around with Spectral Clustering

- k means clustering is a form of unsupervised learning

see (https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html)

# Data
[download](http://vlado.fmf.uni-lj.si/pub/networks/data/ucinet/ucidata.htm#wolfe)
WOLFE PRIMATES
DATASET WOLF, WOLFI
DESCRIPTION WOLF: Two 20×20 matrices
WOLFK non-symmetric, binary
WOLFN symmetric, valued.

## BACKGROUND
These data represent 3 months of interactions among a troop of monkeys, observed in the wild by Linda Wolfe as they sported by a river in Ocala, Florida. Joint presence at the river was coded as an interaction and these were summed within all pairs (WOLFN).  

WOLFK indicates the putative kin relationships among the animals: 18 may be the granddaughter of 19.  

## Covariate Information
WOLFI: One 20×4 matrix, valued.
monkeyCov contains four columns of information about the individual animals: (1) ID number of the animal; (2) age in years; (3) sex; (4) rank in the troop.