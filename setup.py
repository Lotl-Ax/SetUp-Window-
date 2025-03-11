from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QLabel
import json

import sys


def open_setup():
    window.show()


class Map(QMainWindow):

    def __init__(self, crime_id: list):

        super(Map, self).__init__()
        uic.loadUi("Wireframe.ui", self, crime_id)

        self.crime_id = crime_id

        self.map_graphics = self.findChild(QLabel, 'Image')
        self.placeholder1 = self.findChild(QPushButton, 'marker_placeHolder1')
        self.placeholder2 = self.findChild(QPushButton, 'marker_placeHolder2')
        self.placeholder3 = self.findChild(QPushButton, 'marker_placeHolder3')
        self.placeholder4 = self.findChild(QPushButton, 'marker_placeHolder4')
        self.placeholder5 = self.findChild(QPushButton, 'marker_placeHolder5')
        self.placeholder6 = self.findChild(QPushButton, 'marker_placeHolder6')
        self.placeholder7 = self.findChild(QPushButton, 'marker_placeHolder7')
        self.placeholder8 = self.findChild(QPushButton, 'marker_placeHolder8')
        self.placeholder9 = self.findChild(QPushButton, 'marker_placeHolder9')
        self.placeholder10 = self.findChild(QPushButton, 'marker_placeHolder10')
        self.placeholder11 = self.findChild(QPushButton, 'marker_placeHolder11')
        self.placeholder12 = self.findChild(QPushButton, 'marker_placeHolder12')
        self.edit_setup_button = self.findChild(QPushButton, 'Edit_Setup_Button')

        # Define regions lists
        self.region_1 = self.region_2 = self.region_3 = self.region_4 = self.region_5 = self.region_6 = self.region_7 = self.region_8 = self.region_9 = self.region_10 = self.region_11 = self.region_12 = []
        self.region_boundaries = []

        self.edit_setup_button.clicked.connect(open_setup)

        # Check that the provided list of crime ID's is not empty.
        if len(self.crime_id) != 0:
            self.get_region_boundaries()
            self.set_region()
            self.display_region_vals()
        self.show()

        # Set of processes that use the data to assign each Crime to a Region

    def get_region_boundaries(self):
        """
        Assign the region boundaries and the values for the region.
        :return:
        """

        # latitude and longitude boundaries
        lower_latitude = 50.86193
        higher_latitude = 54.951083
        lower_longitude = -0.000358
        higher_longitude = 1.269397

        # Get the distance between the two points.
        latitude_difference = higher_latitude - lower_latitude
        longitude_difference = higher_longitude - lower_longitude

        # Splitting differences into the differences for the grid. 3 rows 4 columns.
        latitude_split = latitude_difference / 3
        longitude_split = longitude_difference / 4

        # Defining the boundaries
        # (0top, 1bottom, 2left, 3right)
        self.region_boundaries = [
            (higher_latitude, higher_latitude - latitude_split, lower_longitude, lower_longitude + longitude_split),
            # Region 1
            (higher_latitude - latitude_split, higher_latitude - latitude_split * 2,
             higher_longitude + longitude_split),  # Region 2
            (higher_latitude - latitude_split * 2, lower_latitude, lower_longitude,
             lower_longitude + longitude_split),  # Region 3
            (higher_latitude, higher_latitude - latitude_split, lower_longitude + longitude_split,
             lower_longitude + longitude_split * 2),  # Region 4
            (higher_latitude - latitude_split, higher_latitude - latitude_split * 2,
             lower_longitude + longitude_split, lower_longitude + longitude_split * 2),  # Region 5
            (higher_latitude - latitude_split * 2, lower_latitude, lower_longitude + longitude_split,
             lower_longitude + longitude_split * 2),  # Region 6
            (higher_latitude, higher_latitude - latitude_split, lower_longitude + longitude_split * 2,
             lower_longitude + longitude_split * 3),  # Region 7
            (higher_latitude - latitude_split, higher_latitude - latitude_split * 2,
             lower_longitude + longitude_split * 2, lower_longitude + longitude_split * 3),  # Region 8
            (higher_latitude - latitude_split * 2, lower_latitude, lower_longitude + longitude_split * 2,
             lower_longitude + longitude_split * 3),  # Region 9
            (higher_latitude, higher_latitude - latitude_split, lower_longitude + longitude_split * 3,
             higher_longitude),  # Region 10
            (higher_latitude - longitude_split, higher_latitude - longitude_split * 2,
             lower_longitude + longitude_split * 3, higher_longitude + longitude_split * 2),  # Region 11
            (higher_latitude - longitude_split * 2, lower_latitude, lower_longitude + longitude_split * 3,
             higher_longitude)  # Region 12
        ]
        # test = {
        #     'Region_1_boundaries': {
        #         'top': higher_latitude,
        #         'bottom': (higher_latitude - latitude_split),
        #         'left': lower_longitude,
        #         'right': (lower_longitude + longitude_split)
        #     },
        #
        #     'Region_2_boundaries': {
        #         'top': (higher_latitude - latitude_split),
        #         'bottom': (lower_latitude + latitude_split),
        #         'left': lower_longitude,
        #         'right': (lower_longitude + longitude_split)
        #     },
        #
        #     'Region_3_boundaries': {
        #         'top': (lower_latitude + latitude_split),
        #         'bottom': lower_latitude,
        #         'left': lower_longitude,
        #         'right': (lower_longitude + longitude_split)
        #     },
        #
        #     'Region_4_boundaries': {
        #         'top': higher_latitude,
        #         'bottom': (higher_latitude - latitude_split),
        #         'left': (lower_longitude + longitude_split),
        #         'right': (lower_longitude + longitude_split + longitude_split)
        #     },
        #
        #     'Region_5_boundaries': {
        #         'top': (higher_latitude - latitude_split),
        #         'bottom': (lower_latitude + latitude_split),
        #         'left': (lower_longitude + longitude_split),
        #         'right': (lower_longitude + longitude_split + longitude_split)
        #     },
        #
        #     'Region_6_boundaries': {
        #         'top': (lower_latitude + latitude_split),
        #         'bottom': lower_latitude,
        #         'left': (lower_longitude + longitude_split),
        #         'right': (lower_longitude + longitude_split + longitude_split)
        #     },
        #
        #     'Region_7_boundaries': {
        #         'top': higher_latitude,
        #         'bottom': (higher_latitude - latitude_split),
        #         'left': (higher_longitude - longitude_split - longitude_split),
        #         'right': (higher_longitude - longitude_split)
        #     },
        #
        #     'Region_8_boundaries': {
        #         'top': (higher_latitude - latitude_split),
        #         'bottom': (lower_latitude + latitude_split),
        #         'left': (higher_longitude - longitude_split - longitude_split),
        #         'right': (higher_longitude - longitude_split)
        #     },
        #
        #     'Region_9_boundaries': {
        #         'top': (lower_latitude + latitude_split),
        #         'bottom': lower_latitude,
        #         'left': (higher_longitude - longitude_split - longitude_split),
        #         'right': (higher_longitude - longitude_split)
        #     },
        #
        #     'Region_10_boundaries': {
        #         'top': higher_latitude,
        #         'bottom': (higher_latitude - latitude_split),
        #         'left': (higher_longitude - longitude_split),
        #         'right': higher_longitude
        #     },
        #
        #     'Region_11_boundaries': {
        #         'top': (higher_latitude - latitude_split),
        #         'bottom': (lower_latitude + latitude_split),
        #         'left': (higher_longitude - longitude_split),
        #         'right': higher_longitude
        #     },
        #
        #     'Region_12_boundaries': {
        #         'top': (lower_latitude + latitude_split),
        #         'bottom': lower_latitude,
        #         'left': (higher_longitude - longitude_split),
        #         'right': higher_longitude
        #     }
        # }

    def set_region(self):
        with open("output.json", 'r') as of:
            output_json = json.load(of)
            for crime in output_json['crimes']:
                # Check that the latitude and longitude exist
                if crime['latitude'] == '' or crime['longitude'] == '': continue

                if crime['crimeId'] in self.crime_id:
                    latitude_of_crime = float(crime['latitude'])
                    longitude_of_crime = float(crime['longitude'])

                    region_list = [self.region_1, self.region_2, self.region_3, self.region_4, self.region_5,
                                   self.region_6, self.region_7, self.region_8, self.region_9, self.region_10,
                                   self.region_11, self.region_12]

                    for i in range(len(self.region_boundaries)):
                        region = self.region_boundaries[i]
                        top = region[0]
                        bottom = region[1]
                        left = region[2]
                        right = region[3]

                        if latitude_of_crime <= top & latitude_of_crime >= bottom:
                            if longitude_of_crime >= left & longitude_of_crime <= right:
                                region_list[i].append(crime['crimeId'])

    def assign_boundaries(self):
        with open("output.json", "r") as cf:  # loading JSON file
            output_json = json.load(cf)

            for crime in output_json['crimes']:
                # Check that there is a provided latitude or longitude
                if crime['latitude'] == '' or crime['longitude'] == '': continue

                if crime['crimeId'] in self.crime_id:
                    lat = crime['latitude']
                    long = crime['longitude']

                    ## TODO: Check that the crime falls in these regions. This is where the bug is.
                    self.check_Region1(crime, lat, long)
                    self.check_Region2(crime, lat, long)
                    self.check_Region3(crime, lat, long)
                    self.check_Region4(crime, lat, long)
                    self.check_Region5(crime, lat, long)
                    self.check_Region6(crime, lat, long)
                    self.check_Region7(crime, lat, long)
                    self.check_Region8(crime, lat, long)
                    self.check_Region9(crime, lat, long)
                    self.check_Region10(crime, lat, long)
                    self.check_Region11(crime, lat, long)
                    self.check_Region12(crime, lat, long)

    def display_region_vals(self):
        regions = [self.region_1, self.region_2, self.region_3, self.region_4, self.region_5, self.region_6,
                   self.region_7, self.region_8, self.region_9, self.region_10, self.region_11, self.region_12]
        for region in regions:
            index = regions.index(region)
            print(f"Number of items in Region{index}: {len(region)}")

        r1 = str(len(self.region_1))
        r2 = str(len(self.region_2))
        r3 = str(len(self.region_3))
        r4 = str(len(self.region_4))
        r5 = str(len(self.region_5))
        r6 = str(len(self.region_6))
        r7 = str(len(self.region_7))
        r8 = str(len(self.region_8))
        r9 = str(len(self.region_9))
        r10 = str(len(self.region_10))
        r11 = str(len(self.region_11))
        r12 = str(len(self.region_12))

        self.placeholder1.setText(r1)
        self.placeholder2.setText(r2)
        self.placeholder3.setText(r3)
        self.placeholder4.setText(r4)
        self.placeholder5.setText(r5)
        self.placeholder6.setText(r6)
        self.placeholder7.setText(r7)
        self.placeholder8.setText(r8)
        self.placeholder9.setText(r9)
        self.placeholder10.setText(r10)
        self.placeholder11.setText(r11)
        self.placeholder12.setText(r12)

    # enddef

    def check_Region1(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_1_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_1.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region2(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_2_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_2.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region3(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_3_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_3.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region4(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_4_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_4.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region5(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_5_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_5.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region6(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_6_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_6.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region7(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_7_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_7.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region8(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_8_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_8.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region9(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_9_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_9.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region10(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_10_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_10.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region11(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_11_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_11.append(item['crimeId'])
            # endif
        # endif

    # enddef

    def check_Region12(self, item, latitude, longitude):
        r = self.Region_boundaries['Region_12_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                self.region_12.append(item['crimeId'])
            # endif
        # endif

    # enddef

    # enddef


class SetUP(QWidget):

    def __init__(self):

        super(SetUP, self).__init__()
        uic.loadUi("SetUP_widget.ui", self)

        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setGeometry(750, 300, 760, 410)  # sets window position (750, 300) and its size w=600, h= 450
        self.setFixedSize(760, 410)  # fixes the window proportions so size cant be changed

        self.month_select = self.findChild(QComboBox, 'Month_picker')
        self.month_change: bool = False
        self.year_select = self.findChild(QComboBox, 'Year_Picker')
        self.year_change: bool = False

        self.chosen_month = None
        self.chosen_year = None

        self.AntiSocial = self.findChild(QCheckBox, 'AntiSoc_Check')
        self.BikeTheft = self.findChild(QCheckBox, 'BikeTheft_Check')
        self.Drugs = self.findChild(QCheckBox, 'Drugs_Check')
        self.ShopLift = self.findChild(QCheckBox, 'Shoplift_Check')
        self.Robbery = self.findChild(QCheckBox, 'Robbery_Check')
        self.PublicOrder = self.findChild(QCheckBox, 'PubOrder_Check')
        self.CrimDmgArson = self.findChild(QCheckBox, 'CrimDmgArs_Check')
        self.VehicleCrim = self.findChild(QCheckBox, 'Vehicle_Check')
        self.Vio_SexualOffs = self.findChild(QCheckBox, 'Vio_SexOff_Check')
        self.PersonTheft = self.findChild(QCheckBox, 'PersonTheft_Check')
        self.Weapons = self.findChild(QCheckBox, 'WeaponPossess_Check')
        self.Burglary = self.findChild(QCheckBox, 'Burglary_Check')
        self.select_all_crimes = self.findChild(QCheckBox, 'SelectAL_Check')
        self.save_button = self.findChild(QPushButton, 'Save_Button')
        self.Safe = False  # setting changes as unsaved, here as it's connected to Save_btn
        self.continue_button = self.findChild(QPushButton, 'Continue_Button')
        self.cancel_button = self.findChild(QPushButton, 'Cancel_Button')

        self.crime_list = []
        self.num_crime_selected = len(self.crime_list)

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December']
        self.year = {
            0: 2024,
            1: 2023,
            2: 2022,
            3: 2021,
            4: 2020
        }
        self.crimeCounter = {
            'Anti-social behaviour': 0,
            'Bicycle theft': 0,
            'Burglary': 0,
            'Criminal damage and arson': 0,
            'Drugs': 0,
            'Possession of weapons': 0,
            'Public order': 0,
            'Robbery': 0,
            'Shoplifting': 0,
            'Theft from the person': 0,
            'Vehicle crime': 0,
            'Violence and sexual offences': 0
        }
        self.crime_id = []

        # setting event handlers
        self.month_select.currentIndexChanged.connect(self.month_change_handler)
        self.year_select.currentIndexChanged.connect(self.year_change_handler)
        self.select_all_crimes.clicked.connect(self.select_all_crimes_handler)
        self.Robbery.stateChanged.connect(self.robbery_select_handler)
        self.CrimDmgArson.stateChanged.connect(self.criminal_damage_and_arson_select_handler)
        self.Weapons.stateChanged.connect(self.weapons_select_handler)
        self.Vio_SexualOffs.stateChanged.connect(self.violent_and_sexual_offences_select_handler)
        self.Burglary.stateChanged.connect(self.burglary_select_handler)
        self.PublicOrder.stateChanged.connect(self.public_order_select_handler)
        self.VehicleCrim.stateChanged.connect(self.vehicle_crime_select_handler)
        self.Drugs.stateChanged.connect(self.drug_select_handler)
        self.PersonTheft.stateChanged.connect(self.person_theft_select_handler)
        self.ShopLift.stateChanged.connect(self.shoplifting_select_handler)
        self.BikeTheft.stateChanged.connect(self.bike_theft_select_handler)
        self.AntiSocial.stateChanged.connect(self.antisocial_behaviour_select_handler)
        self.save_button.clicked.connect(self.save_button_handler)
        self.continue_button.clicked.connect(self.continue_button_handler)
        self.cancel_button.clicked.connect(self.cancel_button_handler)

        self.show()

    def month_change_handler(self):
        self.month_change = True
        month_index = self.month_select.currentIndex()
        self.chosen_month = self.months[month_index]
        print(self.chosen_month)

    def year_change_handler(self):
        self.year_change = True
        year_index = self.year_select.currentIndex()
        self.chosen_year = self.year[year_index]
        print(self.chosen_year)

    def select_all_crimes_handler(self):
        if self.select_all_crimes.checkState() == 2:
            self.Robbery.setChecked(True)
            self.CrimDmgArson.setChecked(True)
            self.VehicleCrim.setChecked(True)
            self.Vio_SexualOffs.setChecked(True)
            self.Burglary.setChecked(True)
            self.BikeTheft.setChecked(True)
            self.Weapons.setChecked(True)
            self.Drugs.setChecked(True)
            self.PersonTheft.setChecked(True)
            self.PublicOrder.setChecked(True)
            self.AntiSocial.setChecked(True)
            self.ShopLift.setChecked(True)
        else:
            self.Robbery.setChecked(False)
            self.CrimDmgArson.setChecked(False)
            self.VehicleCrim.setChecked(False)
            self.Vio_SexualOffs.setChecked(False)
            self.Burglary.setChecked(False)
            self.BikeTheft.setChecked(False)
            self.Weapons.setChecked(False)
            self.Drugs.setChecked(False)
            self.PersonTheft.setChecked(False)
            self.PublicOrder.setChecked(False)
            self.AntiSocial.setChecked(False)
            self.ShopLift.setChecked(False)

    def robbery_select_handler(self):
        self.Safe = False
        if self.Robbery.checkState() == 2:
            self.crime_list.append('Robbery')
        else:
            self.crime_list.remove('Robbery')

    def criminal_damage_and_arson_select_handler(self):
        self.Safe = False
        if self.CrimDmgArson.checkState() == 2:
            self.crime_list.append('Criminal damage and arson')
        else:
            self.crime_list.remove('Criminal damage and arson')

    def weapons_select_handler(self):
        self.Safe = False
        if self.Weapons.checkState() == 2:
            self.crime_list.append('Possession of weapons')
        else:
            self.crime_list.remove('Possession of weapons')

    def violent_and_sexual_offences_select_handler(self):
        self.Safe = False
        if self.Vio_SexualOffs.checkState() == 2:
            self.crime_list.append('Violence and sexual offences')
        else:
            self.crime_list.remove('Violence and sexual offences')

    def burglary_select_handler(self):
        self.Safe = False
        if self.Burglary.checkState() == 2:
            self.crime_list.append('Burglary')
        else:
            self.crime_list.remove('Burglary')

    def bike_theft_select_handler(self):
        self.Safe = False
        if self.BikeTheft.checkState() == 2:
            self.crime_list.append('Bicycle theft')
        else:
            self.crime_list.remove('Bicycle theft')

    def public_order_select_handler(self):
        self.Safe = False
        if self.PublicOrder.checkState() == 2:
            self.crime_list.append('Public order')
        else:
            self.crime_list.remove('Public order')

    def drug_select_handler(self):
        self.Safe = False
        if self.Drugs.checkState() == 2:
            self.crime_list.append('Drugs')
        else:
            self.crime_list.remove('Drugs')

    def person_theft_select_handler(self):
        self.Safe = False
        if self.PersonTheft.checkState() == 2:
            self.crime_list.append('Theft from the person')
        else:
            self.crime_list.remove('Theft from the person')

    def vehicle_crime_select_handler(self):
        self.Safe = False
        if self.VehicleCrim.checkState() == 2:
            self.crime_list.append('Vehicle crime')
        else:
            self.crime_list.remove('Vehicle crime')

    def shoplifting_select_handler(self):
        self.Safe = False
        if self.ShopLift.checkState() == 2:
            self.crime_list.append('Shoplifting')
        else:
            self.crime_list.remove('Shoplifting')

    def antisocial_behaviour_select_handler(self):
        self.Safe = False
        if self.AntiSocial.checkState() == 2:
            self.crime_list.append('Anti-social behaviour')
        else:
            self.crime_list.remove('Anti-social behaviour')

    def save_button_handler(self):
        # If dates don't exist then set to default values.
        if not self.month_change:
            self.chosen_month = self.months[0]
        if not self.year_change:
            self.chosen_year = self.year[0]

        self.Safe = True  # sets safe as True, essentially 'Saving' changes

        print('Saved:')
        print(self.crime_list)
        print(self.chosen_month)
        print(self.chosen_year)

    def continue_button_handler(self):
        if self.Safe:
            self.fetch_data()
            self.set_date()
            self.hide()
            Map(self.crime_id).show()  # TODO: Figure out how this is causing issues.
        else:
            # Alert to being unsafe
            msgbox = QMessageBox.warning(
                self,
                'HOLD ON',
                'Changes Are Not Saved! \nAre you sure you want to continue',
                QMessageBox.Yes | QMessageBox.No)
            if msgbox == QMessageBox.Yes:
                self.close()

    def cancel_button_handler(self):
        self.close()

    def set_date(self):
        """
        Converts the dates chosen into the date for the file.
        :return: nothing
        """
        # a dictionary that assigns each month its specific number e.g February = '-02' so that it matches the labelling in the JSON file
        month_to_int = {
            'January': '-01',
            'February': '-02',
            'March': '-03',
            'April': '-04',
            'May': '-05',
            'June': '-06',
            'July': '-07',
            'August': '-08',
            'September': '-09',
            'October': '-10',
            'November': '-11',
            'December': '-12'
        }
        month_chosen = month_to_int[self.chosen_month]
        self.date = str(self.chosen_year) + month_chosen
        print(self.date)

    def fetch_data(self):
        with open("output.json", "r") as cf:
            output_json = json.load(cf)
            for crime in output_json['crimes']:
                if crime['crimeType'] not in self.crime_list: continue
                if crime['location'] == 'No Location':  continue

                self.crimeCounter[crime[
                    'crimeType']] += 1  # increases the number associated with the crimeType of the current item by one
                self.crime_id.append([crime['crimeId']])

        for crime in self.crimeCounter:
            if crime in self.crime_list:
                print(self.crimeCounter[crime])  # printing the count for each chosen crime so that i can check


x = []

app = QApplication(sys.argv)

map = Map(x)
map.show()

window = SetUP()
window.show()

app.exec_()
