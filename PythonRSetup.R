library(reticulate)
use_python("/home/mattias/anaconda3/envs/tutorial/bin/python")
use_condaenv("tutorial")
conda_install("tutorial","cupy") #GPU Array calculation as NumPy
conda_install("tutorial","pandas")
conda_install("tutorial","plotnine")