#!/usr/bin/env python

import requests
import json
import sys
from flask import render_template_string


class Platform:
    def docs(self):
        documentation = {
            "name":
            "Covid Tracker",
            "author":
            "Blackhippy",
            "author_url":
            "https://github.com/Blackhippy/",
            "version":
            1.0,
            "description":
            "Covid State Tracker",
            "variables": [
                {
                    "variable": "[variable_name]",
                    "description": "Name for the data source.",
                    "default": "",
                    "options": ".ini header",
                },
                {
                    "variable": "platform",
                    "description": "Name of the platform.",
                    "default": "covid",
                    "options": "covid",
                },
                {
                    "variable": "state",
                    "description": "Abbreviation for your state",
                    "default": "TX",
                    "options": "string",
                },
            ],
        }
        return documentation


def __init__(self, *args, **kwargs):
    for key, value in kwargs.items():
        self.__dict__[key] = value

    self.html_template = """
    <div class="row">
        <div class="col s12">
            <div class="center">
                <p>
                <span class="material-icons">bug_report</span>
                Positive: {{positive}}
                </p>
                <p>
                <span class="material-icons">cancel</span>
                Deaths: {{death}}
                </p>
                <p>
                <span class="material-icons">settings_backup_restore</span>
                Recovered: {{recovered}}
                </p>
            </div>
        </div>
    </div>
    """


def process(self):
    api_url = 'https://covidtracking.com/api/v1/states/current.json'
    r = requests.get(api_url)
    r_data = r.json()
    if r.status_code == 200:
        for state in r_data:
            if state['state'] == self.state:
                positive = state['positive']
                negative = state['negative']
                recovered = state['recovered']
                death = state['death']
                print(f'TX: SICK {positive} LIFE {recovered} DEAD {death}')
                return render_template_string(self.html_template,
                                              positive=positive,
                                              recovered=recovered,
                                              death=death)
    else:
        print("Covid tracking api down")
