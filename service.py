# -*- coding: utf-8 -*-

import xbmc

from resources.lib.misc import *


class Monitor(xbmc.Monitor):
    pass


if __name__ == '__main__':
    monitor = Monitor()
    try:
        monitor.waitForAbort()
    except AttributeError:
        # Below for Gotham support
        while not xbmc.abortRequested:
            xbmc.sleep(500)
    xbmc.log("Watchlist Service done!", level=xbmc.LOGNOTICE)
