# -*- coding: utf-8 -*-
import os
import json

import xbmc
import xbmcaddon

__all__ = ['addonprofile']

addon = xbmcaddon.Addon()
addonprofile = xbmc.translatePath(addon.getAddonInfo('profile')).decode("utf-8")
if not os.path.exists(addonprofile):
    os.makedirs(addonprofile)


def printlog(log, logname=u'service.log'):
    with open(os.path.join(addonprofile, logname), 'a') as f:
        f.write(log+u'\n'.encode('utf-8'))


def jsonrpc(method, params=[], result=True):
    request = {"jsonrpc": "2.0", "method": method, "params": params if isinstance(params, (list, dict)) else [params]}
    if result:
        request["id"] = "result"
    return json.loads(xbmc.executeJSONRPC(json.dumps(request)))['result']


jsonrpcTypes = jsonrpc("JSONRPC.Introspect")["types"]
List_Fields_All = jsonrpcTypes["List.Fields.All"]["items"]["enums"]
Video_Fields_Episode = jsonrpcTypes["Video.Fields.Episode"]["items"]["enums"]
