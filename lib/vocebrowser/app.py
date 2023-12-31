#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWebEngineWidgets import  QWebEngineSettings
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

from vocebrowser.browser import VoceBrowser
from vocebrowser.schemes import VoceUrlSchemeHandler, ResourceUrlSchemeHandler

def main(argv=sys.argv):

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling

    VoceUrlSchemeHandler.registerVoceUrlScheme()
    ResourceUrlSchemeHandler.registerVoceUrlScheme()

    app = QtWidgets.QApplication(argv)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    QtCore.QCoreApplication.setOrganizationName('Cypher Browser Fundation')
    QWebEngineSettings.defaultSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

    browser = VoceBrowser()
    app.setApplicationName(browser.appName)

    voceUrlSchemeHandler = VoceUrlSchemeHandler()
    resourceUrlSchemeHandler = ResourceUrlSchemeHandler()

    QWebEngineProfile.defaultProfile().installUrlSchemeHandler(VoceUrlSchemeHandler.schemeName, voceUrlSchemeHandler)
    QWebEngineProfile.defaultProfile().installUrlSchemeHandler(ResourceUrlSchemeHandler.schemeName, resourceUrlSchemeHandler)


    browser.launch()

    return sys.exit(app.exec())


if __name__ == "__main__":
    main()
