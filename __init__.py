from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

import paho.mqtt.client as mqtt

__author__ = 'jamiehoward430/JonStratton'

LOGGER = getLogger(__name__)

class mymqttskill(MycroftSkill):

    def __init__(self):
        super(mymqttskill, self).__init__(name="mymqttskill")
        if ( not self.settings.get('mqtthost') ):
           self.settings['mqtthost'] = 'localhost'
        if ( not self.settings.get('mqttport') ):
           self.settings['mqttport'] = 1883
        self.mqttc = mqtt.Client("MycroftAI")

    def shutdown(self):
        self.mqttc.disconnect()
    
    def initialize(self):
        self.__build_single_command()
        
    def __build_single_command(self):
        intent = IntentBuilder("mymqttIntent").require("CommandKeyword").require("ModuleKeyword").require("ActionKeyword").build()
        self.register_intent(intent, self.handle_single_command)
        
    def handle_single_command(self, message):
        cmd_name = message.data.get("CommandKeyword").replace(' ', '_')
        dev_name = message.data.get("ModuleKeyword").replace(' ', '_')
        act_name = message.data.get("ActionKeyword").replace(' ', '_')
        
        try:
            if (self.settings.get('mqttuser')):
                self.mqttc.username_pw_set(self.settings['mqttuser'],self.setting['mqttpass'])
            if (self.settings.get('mqttca')):
                self.mqttc.tls_set(self.settings['mqttca']) #/etc/ssl/certs/ca-certificates.crt
            LOGGER.info( "MQTT Connect: " + self.settings['mqtthost'] + ':' + str(self.settings['mqttport']) )
            self.mqttc.connect(self.settings['mqtthost'], int(self.settings['mqttport']))

            self.mqttc.publish(dev_name + "/" + cmd_name, act_name)
            self.mqttc.disconnect()
            self.speak_dialog("cmd.sent")
            LOGGER.info("MQTT Publish: " + dev_name + "/" + cmd_name + "/" + act_name)
        except Exception as e:
            LOGGER.info("MQTT Exception: %s" % e)
            self.speak_dialog("not.found", {"command": cmd_name, "action": act_name, "module": dev_name})
        
    def stop(self):
        pass
        
def create_skill():
    return mymqttskill()
