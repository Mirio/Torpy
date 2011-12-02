#                                    LICENSE BSD 2 CLAUSE                                       #
#   Copyright 2011 Mirio. All rights reserved.                                             #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        #   

__version__ = "1.0"

import urllib2
import os
import socket
import time
import pygtk_baloon

def get_myip():
    proxy_handler = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
    proxy_basic = urllib2.ProxyBasicAuthHandler()
    proxy_basic.add_password('Localhost', '127.0.0.1:8118', '', '')
    proxy_build = urllib2.build_opener(proxy_handler, proxy_basic)
    myip = proxy_build.open("http://mirio.altervista.org/getmyip.php")
    return myip.read()

def get_resolvename():
    resolvename = socket.getfqdn(get_myip())
    return resolvename

def get_dns_linux():
    get_nslookup = os.popen('nslookup a').read()
    get_dns = get_nslookup.split('\t')[3].split('#')[0]
    return get_dns

def get_dns_win():
    get_nslookup = os.popen('nslookup a').read()
    get_dns = get_nslookup.split('\n')[1].split(' ')[2]
    return get_dns

def check_myip(ip, rescan_time):
    myip_now = ip
    time.sleep(rescan_time)
    myip_check = get_myip()
    if myip_now != myip_check: 
        return 1
    else:
        return 0
def main():
    separator = "=" * 30 + "\n\n"
    if (os.name == 'posix'):
        try:
            print "\n" * 30
            print "Torpy Version: " + __version__
            print "Ip = " + get_myip()
            print "Dns = " + get_dns_linux()
            print "Resolve Host = " + get_resolvename()
            print "\n" * 5
            try:
                rescan_time = int(raw_input("Rescan time (Seconds)\n--> "))
                while 1:
                    if check_myip(get_myip(), rescan_time):
                        print "\n\n\n" + separator + time.strftime("[%H:%M:%S] ") + "\n Your ip is changed!\n Your New Ip: "+ get_myip() + "\n Your New ResolveHost: " + get_resolvename() + "\n\n\n" + separator
                        pygtk_baloon.baloon("Torpy", "Your ip is changed!\n Your New Ip: "+ get_myip() + "\n Your New ResolveHost:\n" + get_resolvename(), 10000, 4)
                    else:
                        print "\n\n\n" + separator + time.strftime("[%H:%M:%S] ") + "Your ip is not changed"
                        pygtk_baloon.baloon("Torpy","Your ip is not changed", 10000, 4)
            except ValueError:
                    print "Time rescan is invalid."
        except urllib2.URLError:
            print "Tor is not enabled or polipo is not running. Torpy requited: Tor+Polipo"
        else:
            try:
                set_title = os.popen('title Torpy')
                print "\n" * 30
                print "Torpy Version: " + __version__
                print "Ip = " + get_myip()
                print "Dns = " + get_dns_win()
                print "Resolve Host = " + get_resolvename()
                print "\n" * 5
                try:
                    rescan_time = int(raw_input("Rescan time (Seconds)\n--> "))
                    while 1:
                        if check_myip(get_myip(), rescan_time):
                            print "\n\n\n" + separator + time.strftime("[%H:%M:%S] ") + "\n Your ip is changed!\n Your New Ip: "+ get_myip() + "\n Your New ResolveHost: " + get_resolvename() + "\n\n\n" + separator
                            pygtk_baloon.baloon("Torpy", "Your ip is changed!\n Your New Ip: "+ get_myip() + "\n Your New ResolveHost:\n" + get_resolvename(), 10000, 6 )
                        else:
                            print "\n\n\n" + separator + time.strftime("[%H:%M:%S] ") + "Your ip is not changed"
                            pygtk_baloon.baloon("Torpy","Your ip is not changed", 10000, 6 )
                except ValueError:
                    print "Time rescan is invalid."
            except urllib2.URLError:
                print "Tor is not enabled or polipo is not running. Torpy requited: Tor+Polipo"
try:
    main()
except KeyboardInterrupt:
    print " Stopped."
