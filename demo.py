import os
from pathlib import Path

from opencdms import MidasOpen
from opencdms.process.climatol import windrose


# Instead of using a database connection string, the MIDAS Open
# provider requires the root directory for the MIDAS Open data.
CONNECTION = os.path.join(
    Path.home(), 'opencdms-dev', 'git', 'opencdms-test-data')


def main(connection=None, write_csv=False):
    if connection is None:
        connection = CONNECTION

    # All instances of CDMS Providers act as an active session
    session = MidasOpen(connection)

    filters = {
        'src_id': 838,
        'period': 'hourly',
        'year': 1991,
        'elements': ['wind_speed', 'wind_direction'],
    }

    # Get observations DataFrame using filters
    obs = session.obs(**filters)

    if write_csv:
        # Save observations to CSV file
        obs.to_csv('example_observations.csv')

    windrose(obs)


if __name__ == '__main__':
    main()
