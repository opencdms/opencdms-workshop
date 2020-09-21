import os
from pathlib import Path

from opencdms import MidasOpen

# Instead of using a database connection string, the MIDAS Open
# provider requires the root directory for the MIDAS Open data.
connection = os.path.join(
    Path.home(), 'opencdms-demo', 'git', 'opencdms-test-data')

# All instances of CDMS Providers act as an active session
session = MidasOpen(connection)

filters = {
    'src_id': 838,
    'period': 'hourly',
    'year': 1991,
    'elements': ['wind_speed', 'wind_direction'],
}

# Get observations using filters
obs = session.obs(**filters)

# Save observations to CSV file
obs.to_csv('example_observations.csv')
