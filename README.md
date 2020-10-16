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
cd ~/work/opencdms-dev/git
git clone https://github.com/opencdms/opencdms-demo.git
pip3 install -r ~/work/opencdms-dev/git/opencdms-demo/requirements.txt

# You can run the jupyter notebook server by typing:
jupyter notebook

```

### The following section gives an example of a Jupyter notebook session

```python
import os
from pathlib import Path
from opencdms import MidasOpen
```

```python
connection = os.path.join(
    Path.home(), 'work', 'opencdms-dev', 'git', 'opencdms-test-data')
```

```python
session = MidasOpen(connection)
```

```python
filters = {
    'src_id': 838,
    'period': 'hourly',
    'year': 1991,
    'elements': ['wind_speed', 'wind_direction'],
}
```

```python
obs = session.obs(**filters)
```

```python
obs

```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ob_time</th>
      <th>src_id</th>
      <th>wind_direction</th>
      <th>wind_speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1991-01-01 00:00:00</td>
      <td>838</td>
      <td>230.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1991-01-01 01:00:00</td>
      <td>838</td>
      <td>230.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1991-01-01 02:00:00</td>
      <td>838</td>
      <td>210.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1991-01-01 03:00:00</td>
      <td>838</td>
      <td>200.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1991-01-01 04:00:00</td>
      <td>838</td>
      <td>220.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>16212</th>
      <td>1991-12-31 19:00:00</td>
      <td>838</td>
      <td>190.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>16213</th>
      <td>1991-12-31 20:00:00</td>
      <td>838</td>
      <td>220.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>16214</th>
      <td>1991-12-31 21:00:00</td>
      <td>838</td>
      <td>210.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>16215</th>
      <td>1991-12-31 22:00:00</td>
      <td>838</td>
      <td>200.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>16216</th>
      <td>1991-12-31 23:00:00</td>
      <td>838</td>
      <td>220.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
<p>16217 rows × 4 columns</p>
</div>

```python
type(obs)

```
>    pandas.core.frame.DataFrame

```python
from opencdms.process.climatol import windrose
```

```python
windrose(obs)
```

### Setting up database servers

|            | Postgres | MySQL | Oracle | File-based |
|------------|:--------:|:-----:|:------:|:----------:|
| CliDE      | :white_check_mark: ||     |            |
| Climsoft   |          | :white_check_mark: ||       |
| MCH        |          | :white_check_mark: ||       |
| Midas Open |          |       |        | :white_check_mark: |

#### Installing PostgreSQL

In this demo we'll install PostgreSQL 12 by using a [docker image](https://docs.timescale.com/latest/getting-started/installation/docker/installation-docker) that also contains the TimescaleDB (time series) and the PostGIS (spatial) extensions.

When the container is running, the database server will be available on port `5432`

```
sudo docker pull timescale/timescaledb-postgis:latest-pg12
# Note: change `password` below to a suitable password
sudo docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb:latest-pg12
```
