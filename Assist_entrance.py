# -*- coding: utf-8 -*-

"""
Module implementing FetchWindow.
"""
from datetime import datetime
import threading
import requests
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMenu, QMessageBox

from Ui_Assist_entrance import Ui_MainWindow
from ProxyInfoContainer import ProxyInfoContainer
from ExportUtil import ExportUtil

class FetchWindow(QMainWindow, Ui_MainWindow):
    #max page count for retrieving
    MAX_PAGE = 100

    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(FetchWindow, self).__init__(parent)
        self.setupUi(self)
        
        #context menu
        self.proxyTable.customContextMenuRequested.connect(self.handleTableMenu)

        #init table widget
        self._createTable()
        
        self.container = ProxyInfoContainer()
        self.container.fetchCountryInfo()

        #initialize combobox
        for i in self.container.countries:
            self.countrySelector.addItem(i[0], i[1])
        #print(self.countrySelector.itemData(self.countrySelector.currentIndex()))
        

    def handleTableMenu(self, pos):

        cmenu = QMenu(self)
        
        cmenu.addAction(self.actionExportJSON_SR)
        cmenu.addAction(self.actionExport_Proxychains)
        action = cmenu.exec_(self.mapToGlobal(pos))

        if action == self.actionExportJSON_SR:
            if self.proxyTable.rowCount() == 0:
                QMessageBox.information(self, "Please fetch first",  "No information to export", QMessageBox.Yes)
                return
            ExportUtil().exportShadowrocketJSON(self.proxyTable)
            QMessageBox.information(self, "Completed",  "Export completed", QMessageBox.Yes)
        elif action == self.actionExport_Proxychains:
            if self.proxyTable.rowCount() == 0:
                QMessageBox.information(self, "Please fetch first",  "No information to export", QMessageBox.Yes)
                return
            ExportUtil().exportProxychains(self.proxyTable)
            QMessageBox.information(self, "Completed",  "Export completed", QMessageBox.Yes)

    def _createTable(self):
        #self.proxyTable = QTableWidget()
        self.proxyTable.setColumnCount(6)
        self.proxyTable.setHorizontalHeaderLabels(["IP:Port", "Country", "City", "Type", "Speed", "HTTPS/SSL"])
        
        #adjust width of each cell
        header = self.proxyTable.horizontalHeader()   
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        #self.proxyTable.move(0,0)
        
    def _fetchDataThread(self):
        print("Start Fetching")
        self.status_label.setText("Fetching ...")
        self.proxyTable.clearContents()
        self.proxyTable.setRowCount(0)
        self.container.proxyItems.clear()
        for i in range(1, self.MAX_PAGE):
            result = self.container.fetchInfoForCountryByPage(self.countrySelector.itemData(self.countrySelector.currentIndex()), str(i))
            if not result:
                break
                
            currentRowCount = self.proxyTable.rowCount()
            self.proxyTable.setRowCount(len(self.container.proxyItems))
            for j in range(currentRowCount, len(self.container.proxyItems)):
                self.proxyTable.setItem(j,0, QTableWidgetItem(self.container.proxyItems[j].ip_port))
                self.proxyTable.setItem(j,1, QTableWidgetItem(self.container.proxyItems[j].country))
                self.proxyTable.setItem(j,2, QTableWidgetItem(self.container.proxyItems[j].city))
                self.proxyTable.setItem(j,3, QTableWidgetItem(self.container.proxyItems[j].type))
                self.proxyTable.setItem(j,4, QTableWidgetItem(self.container.proxyItems[j].speed))
                self.proxyTable.setItem(j,5, QTableWidgetItem(self.container.proxyItems[j].protocol))
                
        print("Fetching Finished")
        self.status_label.setText("Fetching Finished.")
        
        #Speed recheck
        for i in range(self.proxyTable.rowCount()):
            t =threading.Thread(target=self._speedCheckThread,  args=(i, ))
            t.start()
        
    def _speedCheckThread(self, rowNum):
        span = "-"
        startTime = datetime.now()
        try:
            requests.get(self.testURL.text(), proxies={"http":self.proxyTable.item(rowNum, 5).text()+"://" + self.proxyTable.item(rowNum, 0).text()}, timeout=10)
        except Exception:
            pass
        else:
            endTime = datetime.now()
            span = (endTime-startTime).total_seconds()*1000
            span = str(int(span))
        #self.proxyTable.setItem(rowNum, 4, QTableWidgetItem(self.proxyTable.item(rowNum, 4).text() + " (" + span + "ms)"))
        self.proxyTable.item(rowNum, 4).setText(self.proxyTable.item(rowNum, 4).text() + " (" + span + "ms)")
        
        #resize column
        #resizeColumnToContents is for only one coumn
        #setStretchLastSection will set stretch property for all sections
        #resizeSections will resize all section by their own resize modes
#        for i in range(6):
#            self.proxyTable.resizeColumnToContents(i)
        self.proxyTable.horizontalHeader().resizeSections()
        #self.proxyTable.horizontalHeader().setStretchLastSection(True)
        
    def _updatetableData(self):
        
        pass
    
    @pyqtSlot(bool)
    def on_btnStartFetch_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        t =threading.Thread(target=self._fetchDataThread)
        t.start()
        #raise NotImplementedError

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FetchWindow()
    ui.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
