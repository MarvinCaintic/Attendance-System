########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

import cv2
import shutil
import numpy as np
from PySide2.QtGui import *
from PySide2.QtCore import QRunnable, Signal, QThreadPool, QObject

#import app functions
from Functions import AppFunctions
import FRfDTR

#####################
## CLASS MAIN VIDEO THREAD
class videoSignals(QObject):
    change_pixmap_signal = Signal(np.ndarray)
    progressValue = Signal(int)
    run_flag = Signal(bool)
    
class VideoThread(QRunnable):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database\\required folder for face recognition'))
    
    face_classifier = cv2.CascadeClassifier(root_dir + "\\imported\\haarcascade_frontalface_default.xml")
    
    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.signals = videoSignals()

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
                faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)
                for(x, y, w, h) in faces:
                    if(FRfDTR.verify(cv_img[y:y+h, x:x+w])):
                        id, confidence = FRfDTR.recognize(gray[y:y+h, x:x+w])
                        
                        if confidence >= 85:
                            cv2.putText(cv_img, str(id), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
                            AppFunctions.present(id)
                        else:
                            cv2.putText(cv_img, "unknown", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
                        cv2.putText(cv_img, str(confidence), (x, y+h+5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
                        
                self.signals.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        
#####################
## CLASS HIRE VIDEO THREAD

class hiringVideoThread(QRunnable):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database\\required folder for face recognition'))
    
    face_classifier = cv2.CascadeClassifier(root_dir + "\\imported\\haarcascade_frontalface_default.xml")
    
    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.signals = videoSignals()

    def run(self):
        # capture from web cam
        goal = 200
        img_id = 0
        images = []
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
                faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)
                for(x,y,w,h) in faces:
                    if(FRfDTR.verify(cv_img[y:y+h, x:x+w])):
                        img1 = cv2.resize(cv_img[y:y+h, x:x+w], (224, 224))
                        self.signals.change_pixmap_signal.emit(img1)
                        images.append(img1)
                        self.signals.progressValue.emit(((img_id+1)*100)/goal)
                        img_id += 1
                    if img_id >= goal:
                        self._run_flag = False
        # shut down capture system
        df = FRfDTR.train()
        self.signals.run_flag.emit(self._run_flag)
        self.signals.progressValue.emit(0)
        cap.release()
    
    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
    
    
#####################################
class deleteSignals(QObject):
    run_flag = Signal(bool) 
    
class deleteThread(QRunnable):
    idToDelete = []
    def __init__(self, idToDelete2):
        super().__init__()
        self.idToDelete = idToDelete2
        self.signals = deleteSignals()

    def run(self):
        data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database\\required folder for face recognition\\KNOWN_FACES'))
        path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        for image in path:
            id = int(os.path.split(image)[1].split(".")[0])
            if str(id) == str(self.idToDelete[0]):
                os.remove(image)
                
        self.signals.run_flag.emit(False)
        
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.disply_width = 640
        self.display_height = 480

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        
        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self) 
        
        # # CHANGE THE THEME NAME IN SETTINGS
        # # Use one of the app themes from your JSON file
        # settings = QSettings()
        
        # settings.setValue("THEME", "Default-Dark")

        # # RE APPLY THE NEW SETINGS
        # # CompileStyleSheet might also work
        # # CompileStyleSheet.applyCompiledSass(self)
        # QAppSettings.updateAppSettings(self)
        AppFunctions.databaseCreation()
        #Database folder and name
        employees = AppFunctions.getAllEmployee()
        AppFunctions.displayEmployee(self, employees)

        from datetime import date
        today = date.today()
        d = QDate(today.year, today.month, today.day)
        self.ui.aDate.setDate(d)
        self.ui.paDate.setDate(d)
        AppFunctions.displayAttendance(self, 1)
        
        
        self.ui.fireBtn.clicked.connect(self.deleteEmployeeById)
        self.ui.editBtn.clicked.connect(lambda:AppFunctions.setEmployee(self, "edit"))
        self.ui.showEmployeeFormBtn.clicked.connect(lambda:AppFunctions.setEmployee(self, "hire"))
        self.ui.aDate.dateChanged.connect(lambda: AppFunctions.displayAttendance(self, 1))   
        self.ui.paDate.dateChanged.connect(lambda: AppFunctions.displayAttendance(self, 2))      
        self.ui.loginBtn.clicked.connect(self.log_In)
        self.ui.logOutBtn.clicked.connect(self.log_Out)
        self.ui.saveAttendanceBtn.clicked.connect(lambda: AppFunctions.displayAttendance(self, 2))
        self.ui.saveBtn.clicked.connect(lambda: AppFunctions.save(self))
        
        #method
        def selectEmployee():
            self.ui.showEmployeeFormBtn.setEnabled(False)
            self.ui.editBtn.setEnabled(True)
            self.ui.fireBtn.setEnabled(True)
            self.ui.saveAttendanceBtn.setEnabled(True)
        def deselectEmployee():
            self.ui.tableWidget.selectionModel().clearSelection()
            self.ui.showEmployeeFormBtn.setEnabled(True)
            self.ui.editBtn.setEnabled(False)
            self.ui.fireBtn.setEnabled(False)
            self.ui.saveAttendanceBtn.setEnabled(False)
            
        self.ui.tableWidget.clicked.connect(lambda:selectEmployee())
        self.ui.deselectBtn.clicked.connect(lambda:deselectEmployee())
        self.ui.showEmployeeFormBtn.clicked.connect(self.addBtn)
        self.ui.editBtn.clicked.connect(self.editBtn)
 
        
        self.ui.addEmployeeBtn.clicked.connect(self.start_webcam2nd)
        self.threadpool = QThreadPool()
        self.threadpool1 = QThreadPool()
        self.action = "HIRE"
        
        self.start_webcam()
        
        self.root_dir = os.path.join(os.path.dirname(__file__), 'Database\\required folder for face recognition')
        
    def editBtn(self):
        self.action = "EDIT"
        self.ui.addEmployeeBtn.setText(self.action)
    def addBtn(self):
        self.action = "HIRE"
        self.ui.addEmployeeBtn.setText(self.action)
        
        
    def start_webcam(self):
        print("starting webcam 1")
        # create the video capture thread
        self.video_thread = VideoThread()
        # connect its signal to the update_image slot
        self.video_thread.signals.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.threadpool.start(self.video_thread)
                    
    def stop_webcam(self):
        print("ending webcam 1")
        self.video_thread.stop()

  
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        self.ui.image.setPixmap(self.convert_cv_qt(cv_img))
        AppFunctions.displayAttendance(self, 1)
        
    def start_webcam2nd(self):
        self.stop_webcam()
        print("starting webcam 2")
        # create the video capture thread
        self.video_thread1 = hiringVideoThread()
        # connect its signal to the update_image slot
        self.video_thread1.signals.change_pixmap_signal.connect(self.update_image2nd)
        self.video_thread1.signals.progressValue.connect(self.update_progressBar)
        self.video_thread1.signals.run_flag.connect(self.stop_webcam2nd)
        # start the thread  
        self.threadpool1.start(self.video_thread1)
    
    def stop_webcam2nd(self, flag):
        if flag == False:
            self.video_thread1.stop()
            self.start_webcam()
            AppFunctions.addEmployee(self)
            
        
    def update_image2nd(self, cv_img):
        """Updates the image_label with a new opencv image"""
        dir_path = self.root_dir + "\\KNOWN_FACES"
        self.ui.imgLbl.setPixmap(self.convert_cv_qt(cv_img))
        count = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
        cv2.imwrite(dir_path + "\\" + self.ui.idNumber.text() + "." + str(count+1) + ".jpg", cv_img)
        
    def update_progressBar(self, progressValue):
        self.ui.progressBar.setValue(progressValue)
        
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QtGui.QPixmap.fromImage(p)

    
    ######################################### Delete Employee Method ###############################################################################
    
    def deleteEmployeeById(self):
        import shutil
        #create db connection
        row = self.ui.tableWidget.currentRow()
        id = (self.ui.tableWidget.item(row, 0).text(), )
        conn = AppFunctions.create_connection()
        mycursor = conn.cursor()
        mycursor.execute("UPDATE employee set stats = 'inactive' WHERE id = %s", id)
        conn.commit()

        # create the delete thread
        self.stop_webcam
        print("start deleting")
        self.dthread = deleteThread(id)
        self.dthread.signals.run_flag.connect(self.deleteTS)
        # start the thread
        self.threadpool.start(self.dthread)
        
    
    
    def deleteTS(self):
        FRfDTR.train()
        AppFunctions.displayEmployee(self, AppFunctions.getAllEmployee())
        print("employee delete successfully")
        self.start_webcam()
    
    
    
    ########################################################################################################################
    
    


    def log_In(self):
        user = self.ui.userName.text()
        passCode = self.ui.passCode.text()
        if user == "Admin" and passCode == "admin":
            self.ui.stackedWidget.setCurrentWidget(self.ui.mainPage)
            self.ui.userName.setText("")
            self.ui.passCode.setText("")
            
    def log_Out(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)
########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
