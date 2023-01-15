library(reticulate)
library(usethis)
usethis::use_git_config(user.name = "mattiascson", user.email = "mattiascson@gmail.com")
gitcreds::gitcreds_set()
#Use either use_python()
#use_python("/home/mattias/anaconda3/envs/tutorial/bin/python")
#or use_condaenv()
use_condaenv("tutorial")
#conda_install("tutorial","cupy") #GPU Array calculation as NumPy