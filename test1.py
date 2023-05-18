# import subprocess
# from pyuac import main_requires_admin

# @main_requires_admin
# def main():
#     def turn_on_bluetooth():
#         subprocess.call('sudo hciconfig hci0 up', shell=True)
#         print("Bluetooth turned on")

#     # Turn off Bluetooth
#     def turn_off_bluetooth():
#         subprocess.call('sudo hciconfig hci0 down', shell=True)
#         print("Bluetooth turned off")

#     # Turn on WiFi
#     def turn_on_wifi():
#         subprocess.call('netsh interface set interface "Wi-Fi" admin=enabled', shell=True)
#         print("WiFi turned on")

#     # Turn off WiFi
#     def turn_off_wifi():
#         subprocess.call('netsh interface set interface "Wi-Fi" admin=disabled', shell=True)
#         print("WiFi turned off")
#         print("Do stuff here that requires being run as an admin.")
#         # The window will disappear as soon as the program exits!

#     x = input("Enter \n")
#     x= int(x)
#     if x==1:
#         subprocess.call('sudo hciconfig hci0 up', shell=True)
#         print('Bluetooth turned on')
#     elif x==2:
#         subprocess.call('sudo hciconfig hci0 down', shell=True)
#         print("Bluetooth turned off")
#     elif x==3:
#         turn_on_wifi()
#     elif x==4:
#         turn_off_wifi()



#     input("Press enter to close the window. >")

# if __name__ == "__main__":
#     main()

# Turn on Bluetooth

# import bluetooth

# nearby_devices = bluetooth.discover_devices(lookup_names=False)
# print("Found {} devices.".format(len(nearby_devices)))

# import os
# cmd = 'ifconfig wlan0 down'
# os.system(cmd)

# import ctypes

# WLAN_API_DLL = ctypes.windll.wlanapi
# WLAN_INTERFACE_STATE = {
#     0: 'Not ready',
#     1: 'Connected',
#     2: 'Ad-hoc network formed',
#     3: 'Disconnecting',
#     4: 'Disconnected',
#     5: 'Associating',
#     6: 'Discovering',
#     7: 'Authenticating'
# }

# def toggle_wifi(state):
#     """Toggle WiFi on/off"""
#     p_interface = ctypes.POINTER(ctypes.c_void_p)()
#     negotiated_version = ctypes.c_ulong()
#     WLAN_API_DLL.WlanOpenHandle(2, None, ctypes.byref(negotiated_version), ctypes.byref(p_interface))
#     WLAN_API_DLL.WlanEnumInterfaces(p_interface, None, ctypes.byref(p_interface))
#     interface_info = ctypes.POINTER(ctypes.c_void_p)()
#     WLAN_API_DLL.WlanQueryInterface(p_interface.contents, ctypes.byref(ctypes.c_ulong(0)), ctypes.byref(interface_info))
#     wlan_interface_state = ctypes.c_ulong()
#     if state:
#         WLAN_API_DLL.WlanSetInterface(p_interface.contents, interface_info.contents, 4, None, None, None)
#         print("Wi-Fi turned ON.")
#     else:
#         WLAN_API_DLL.WlanSetInterface(p_interface.contents, interface_info.contents, 5, None, None, None)
#         print("Wi-Fi turned OFF.")
#     WLAN_API_DLL.WlanCloseHandle(p_interface.contents, None)

# x= int(input("Enter "))

# if x==1:
#     toggle_wifi(True)
#     print("wifi on")
# elif x==2:
#     toggle_wifi(False)
#     print("wifi off")

import wifi

# interface = wifi() # Create a Wifi object

x= int(input("Enter "))

if x==1:
    wifi.Scheme.activate
    print("wifi on")
elif x==2:
    wifi.Scheme
    print("wifi off")
