# opencdms-demo
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

```
# Install R and header files needed to build Python extensions
sudo apt install python3-dev r-base
# curl required for magick library
sudo apt-get install libcurl4-openssl-dev
# At the time of writing (Oct 2020), the imagemagick ppa is not
# available for Unbuntu 20.04
sudo add-apt-repository -y ppa:cran/imagemagick
sudo apt-get update
sudo apt-get install -y libmagick++-dev

# Launch `R` and install `magick`
R
install.packages("magick")

# In Python, rpy2 is not currently a dependency in pyopencdms becase
# R must be installed before pip can install rpy2.
# Therefore install rpy2 (and other dependencies like Jupyter notebook)
pip3 install -r requirements.txt

# You can run the jupyter notebook server by typing:
jupyter notebook

```
