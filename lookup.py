#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create time @ 2016-03-27 15:03:56

import sys
from workflow import Workflow, ICON_WEB, web

API = "http://ip-api.com/json"

def main(wf):
    data = web.get(API).json()
    if data['status'] == 'success':
        wf.add_item(title=data['query'],
                     subtitle=data['timezone'],
                     icon=ICON_WEB)
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow` object
    wf = Workflow()
    # Call your entry function via `Workflow.run()` to enable its helper
    # functions, like exception catching, ARGV normalization, magic
    # arguments etc.
    sys.exit(wf.run(main))
