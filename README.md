# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/robot.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/> MQTT for MycroftAI
This is a skill written for mycroft to publish commands over an mqtt broker for home automation or any other purpose.

## About
Currently it will publish the action to a topic built from the commands said, for example
- say `hey mycroft, turn the light on` and mycroft will publish `on` to `/mycroft/turn/light/on`.
- say `hey mycroft, switch the tv on` and mycroft will publish `on` to `/mycroft/switch/tv/on`.

## Examples
* "Turn the light on."
* "Switch the tv on."

## Credits
@jamiehoward430

## Notes
### Setup mycroft.conf
Add the following lines to your config file and adjust to your needs, if you ar not using SSL or authentication
just change them to no.
If you are using SSL and a self signed certificate you will need to change mqtt-ca-cert to the location of your cerftificate,
Or you can add it the default trusted certificates.

- Copy your certificate to directory:```sudo cp yourcert.crt /usr/local/share/ca-certificates/yourcert.crt```
- Update the CA store:```sudo update-ca-certificates```

```
  "mymqttskill": {
    "protocol": "mqtt",
    "mqtt-ssl": "yes",
    "mqtt-ca-cert": "/etc/ssl/certs/ca-certificates.crt",
    "mqtt-host": "example.com",
    "mqtt-port": 8883,
    "mqtt-auth": "yes",
    "mqtt-user": "user",
    "mqtt-pass": "pass"
  }
```
Thas it, now start mycroft and start turning your light on and off.

## Supported Devices
platform_picroft platform_plasmoid 

## Category
IoT

## Tags
#mqtt

