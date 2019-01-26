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
Add the following lines to your settings.json and adjust to your needs.
If you are using SSL and a self signed certificate you will need to change mqttca to the location of your cerftificate,
Or you can add it the default trusted certificates.

- Copy your certificate to directory:```sudo cp yourcert.crt /usr/local/share/ca-certificates/yourcert.crt```
- Update the CA store:```sudo update-ca-certificates```

```
    "mqttca": "/etc/ssl/certs/ca-certificates.crt",
    "mqtthost": "example.com",
    "mqttport": 8883,
    "mqttuser": "user",
    "mqttpass": "pass"
```
Thats it, now start mycroft and start turning your light on and off.

## Supported Devices
platform_picroft platform_plasmoid 

## Category
IoT

## Tags
#mqtt

