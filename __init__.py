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

        if ( not self.settings.get('protocol') ):
           self.settings['protocol'] = 'mqtt'
        if ( not self.settings.get('mqtthost') ):
           self.settings['mqtthost'] = 'localhost'
        if ( not self.settings.get('mqttport') ):
           self.settings['mqttport'] = '1883'
    
    def initialize(self):
        self.__build_single_command()
        
    def __build_single_command(self):
        intent = IntentBuilder("mymqttIntent").require("CommandKeyword").require("ModuleKeyword").require("ActionKeyword").build()
        self.register_intent(intent, self.handle_single_command)
        
    def handle_single_command(self, message):
        cmd_name = message.data.get("CommandKeyword")
        mdl_name = message.data.get("ModuleKeyword")
        act_name = message.data.get("ActionKeyword")
        dev_name = mdl_name.replace(' ', '_')
        
        if act_name:
            cmd_name += '_' + act_name

        if (self.settings['protocol'] == "mqtt"):
            mqttc = mqtt.Client("MycroftAI")
            if (self.settings.get('mqttuser')):
                mqttc.username_pw_set(self.settings['mqttuser'],self.setting['mqttpass'])
            if (self.settings.get('mqttca')):
                mqttc.tls_set(self.settings['mqttca']) #/etc/ssl/certs/ca-certificates.crt
            LOGGER.info( "MQTT Connect: " + self.settings['mqtthost'] + ':' + str(self.settings['mqttport']) )
            mqttc.connect(self.settings['mqtthost'], self.settings['mqttport'])
            mqttc.publish(cmd_name + "/" + dev_name + "/" + act_name, act_name)
            mqttc.disconnect()
            self.speak_dialog("cmd.sent")
            LOGGER.info("MQTT Publish: " + cmd_name + "/" + dev_name + "/" + act_name)

        else:
            self.speak_dialog("not.found", {"command": cmd_name, "action": act_name, "module": dev_name})
            LOGGER.error("Error: {0}".format(e))
        
    def stop(self):
        pass
        
def create_skill():
    return mymqttskill()
