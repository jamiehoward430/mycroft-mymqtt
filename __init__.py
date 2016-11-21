# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from urllib2 import urlopen
import paho.mqtt.client as mqtt

__author__ = 'jamiehoward430'

LOGGER = getLogger(__name__)

class MyMQTTSkill(MycroftSkill):

    def __init__(self):
        super(MyMQTTSkill, self).__init__(name="MyMQTTSkill")
       
        self.protocol = self.config["protocol"]
	self.mqtthost = self.config["mqtt-host"]
	self.mqttport = self.config["mqtt-port"]
	self.mqttauth = self.config["mqtt-auth"]
	self.mqttuser = self.config["mqtt-user"]
	self.mqttpass = self.config["mqtt-pass"]
 
    
    def initialize(self):
        self.load_data_files(dirname(__file__))
        self. __build_single_command()
        
        
    def __build_single_command(self):
        intent = IntentBuilder("MyMQTTCmdIntent").require("CommandKeyword").require("ModuleKeyword").optionally("ActionKeyword").build()
        self.register_intent(intent, self.handle_single_command)
        
    def handle_single_command(self, message):
        cmd_name = message.metadata.get("CommandKeyword")
        mdl_name = message.metadata.get("ModuleKeyword")
        act_name = message.metadata.get("ActionKeyword")
        dev_name = mdl_name.replace(' ', '_')
        
        if act_name:
            cmd_name += '_' + act_name

        if (self.protocol == "mqtt"):
	    mqttc = mqtt.Client("MycroftAI")
	    if (self.mqttauth == "yes"):
	        mqttc.username_pw_set(self.mqttuser,self.mqttpass) 
            mqttc.connect(self.mqtthost,self.mqttport)
	    mqttc.publish("/mycroft/" + cmd_name + "/" + dev_name + "/" + act_name, act_name)
	    mqttc.disconnect()
	    self.speak_dialog("cmd.sent")
            LOGGER.info(dev_name + "-" + cmd_name)

	else:
            self.speak_dialog("not.found", {"command": cmd_name, "action": act_name, "module": dev_name})
            LOGGER.error("Error: {0}".format(e))
        
    def stop(self):
        pass
        
def create_skill():
    return MyMQTTSkill()
