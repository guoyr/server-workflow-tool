# -*- coding: utf-8 -*-
import re
import sys

from mongodb_cmdline_tool import __main__

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(__main__.main())
