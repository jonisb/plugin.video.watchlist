#! python3
from Kodi_testing import CreateKodiVersionSpecificTests, addonid, base as testbase


class base(testbase):
    def test_showPlugin(self):
        self.jsonrpc("Addons.ExecuteAddon", addonid)
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.PluginName']])
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.FolderPath']])
        self.assertEqual(result["Container.FolderPath"], addonid)

    def test_test(self):
        result = self.jsonrpc("Addons.GetAddonDetails", [addonid, ["extrainfo"]])
        print(result)

        self.jsonrpc("Addons.ExecuteAddon", addonid)
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.PluginName']])
        self.assertEqual(result["Container.PluginName"], addonid)
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.Content']])
        self.assertEqual(result["Container.Content"], addonid)
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.FolderPath']])
        self.assertEqual(result["Container.FolderPath"], addonid)
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.FolderName']])
        self.assertEqual(result["Container.FolderName"], addonid)
        result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.PluginCategory']])
        self.assertEqual(result["Container.PluginCategory"], addonid)
        #result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.Property(addoncategory)']])
        #self.assertEqual(result["Container.PluginName"], addonid)
        #result = self.jsonrpc("XBMC.GetInfoLabels", [['Container.Property(reponame)']])
        #self.assertEqual(result["Container.PluginName"], addonid)


CreateKodiVersionSpecificTests(base, globals())

if __name__ == '__main__':
    pass
