# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/teamlaw/ChatLaw')
from botlaw import app as application
application.secret_key = 'anything you wish'
