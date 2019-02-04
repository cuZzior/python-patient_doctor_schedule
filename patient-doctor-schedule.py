"""
Patient / Doctor Scheduling system by cuZz
"""

from datetime import time
from random import randint


class Doctor:
    patients = []

    def __init__(self, first_name, last_name, profession, calendar):
        self.first_name = first_name
        self.last_name = last_name
        self.name = first_name + ' ' + last_name
        self.profession = profession
        self.calendar = calendar

    def add_patient(self, patient):
        self.patients.append(patient)

    def show_details(self):
        str_return = "Name: " + self.name + "\nProfession: " + self.profession + "\n\nPatients:"
        for patient in self.patients:
            str_return += "\n" + patient.name + ' ' + str(patient.pesel)
        str_return += '\n' + self.calendar.show_calendar()
        return str_return


class Patient:

    def __init__(self, first_name, last_name, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.name = first_name + ' ' + last_name
        self.pesel = pesel

    def show_details(self):
        return "Name: " + self.name + "\n" + "PESEL: " + str(self.pesel)


class DailyCalendar:
    hours = {}
    appointments = []

    def __init__(self):
        for hour in range(8, 17):
            self.hours[time(hour).strftime('%H:%M')] = time(hour).strftime('%H:%M')
            self.hours[time(hour, 30).strftime('%H:%M')] = time(hour, 30).strftime('%H:%M')

    def show_calendar(self):
        str_return = '\nToday appointments:'
        for appointment in self.appointments:
            str_return += '\n' + appointment['Hour'] + ' with ' + appointment['Patient']
        return str_return


def schedule(patient, doctor, hour, calendar):
    if hour in calendar.hours:
        calendar.appointments.append({'Patient': patient.name, 'Doctor': doctor.name, 'Hour': hour})
        del calendar.hours[hour]

        if patient not in doctor.patients:
            doctor.add_patient(patient)
    else:
        print('That hour is unavailable.')


P1 = Patient('John', 'Wick', randint(90000000000, 99999999999))
P2 = Patient('Adam', 'Malysz', randint(90000000000, 99999999999))
C1 = DailyCalendar()
D1 = Doctor('Robert', 'Wieckiewicz', 'Neurochirurg', C1)

schedule(P1, D1, '09:30', C1)
schedule(P2, D1, '10:30', C1)
schedule(P2, D1, '15:30', C1)

print(D1.show_details())
