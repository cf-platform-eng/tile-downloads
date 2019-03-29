# Copyright 2019 Pivotal Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import csv
import click
import json
import datetime

# Library methods for use in other software

def load_data(slug):
    filename = os.path.join('data', slug + '.csv')
    with open(filename, encoding='utf-8-sig') as report:
        reader = csv.reader(report)
        header = next(reader)
        header = [label.strip().lower().replace(' ', '_') for label in header]
        downloads = [dict(zip(header, download), tile_slug=slug) for download in reader]
        return downloads

# methods for counting the number of users

def load_data_customer(slug):
    downloads = load_data(slug)
    count_num = 0
    customers = {}
    for download in downloads:
        organization = download['organization']
        if organization not in customers:
            customers[organization] = {
                'first_download': download['updated_at']
                'last_download': download['updated_at']
            }
        else:
            customers[organization]{'first_download'}


        # if not download['email'].endswith("pivotal.io"):
        #     customers.append(download['email'])

        return customers


# Command Line Interface implementation (using click module for parsing)

@click.group()
def cli():
	pass

@cli.command('dump')
@click.argument('slug')
def dump(slug):
    downloads = load_data(slug)
    print(json.dumps(downloads, indent = 4))

@cli.command('list')
@click.argument('slug')
def customerlist(slug):
    clist = load_data_customer(slug)
    clist.sort()
    print(json.dumps(clist, indent = 4))


if __name__ == '__main__':
    cli()
