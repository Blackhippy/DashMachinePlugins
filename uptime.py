#!/usr/bin/python
#code from http://planzero.org/blog/2012/01/26/#system_uptime_in_python,_a_better_way
#just using it in dashmachine
from datetime import timedelta
from flask import render_template_string


class Platform:
    def docs(self):
        documentation = {
            "name":
            "uptime",
            "author":
            "Blackhippy",
            "author_url":
            "https://github.com/Blackhippy/",
            "version":
            1.0,
            "description":
            "Uptime status",
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
                    "default": "uptime",
                    "options": "uptime.",
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
                    <h5 class="center-align">Uptime</h5>
                    <h5 class="center-align">{{uptime_string}}</h5>
                </div>
            </div>
        """

    def process(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split(".")[0])
            uptime_string = str(timedelta(seconds=uptime_seconds))
            return render_template_string(self.html_template,
                                          uptime_string=uptime_string)
