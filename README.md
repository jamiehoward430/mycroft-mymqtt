# MQTT for MycroftAI

This is a skill written for mycroft to publish commands over an mqtt broker for home automation or any other purpose.

# Commands

Currently it will publish the action to a topic built from the commands said, for example
- say `hey mycroft, turn the light on` and mycroft will publish `on` to `/mycroft/turn/light/on`.
- say `hey mycroft, switch the tv on` and mycroft will publish `on` to `/mycroft/switch/tv/on`.

# Installing the skill

This skill requires paho-mqtt to be installed in your mycroft virtual enviroment.

If you already have mycroft running stop it and enter the following commands,
- to enter the virtual enviroment `workon mycroft`.
- now to install paho-mqtt `pip install paho-mqtt`.
- now you can exit the virtual enviroment by entering `deactivate`

If you have not yet setup mycroft then simply add `paho-mqtt==1.1` to the requirments.txt file before running dev_setup.sh

Now you have paho-mqtt installed move the mycroft skills directory and download the skill.
- Move into the directory `cd ~/mycroft-core/mycroft/skills`
- Clone the repository `git clone https://github.com/jamiehoward430/mycroft-mymqtt.git`
- Rename it `mv mycroft-mymqtt MyMQTT`

# Setup mycroft.conf
Add the following lines to your config file and adjust to your needs. currently tls is not supported, coming soon!

  `"MyMQTTSkill": {`
    `"protocol": "mqtt",`
    `"mqtt-host": "test.mosquitto.org",`
    `"mqtt-port": "1883",`
    `"mqtt-auth": "yes",`
    `"mqtt-user": "youruser",`
    `"mqtt-pass": "yourpass"`
  `}`


Thas it, now start mycroft and start turning your light on and off.
