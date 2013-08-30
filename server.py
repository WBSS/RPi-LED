#!/usr/bin/python
from flask import Flask, render_template, request
import RPi.GPIO as GPIO

server = Flask("LED Server")

@server.route('/control')
def show_form():
    return render_template('control.html')


@server.route('/toggle_led', methods=['GET'])
def do_toggle():
    val = request.args.get('led_state', '')
    if val != '1' and val != '-1':
        return "error"
    else:
        led = True if val == '1' else False
        GPIO.output(led_port, led)
        return "ok"


if __name__ == '__main__':
    led_port = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_port, GPIO.OUT)
    try:
        #server.debug = True
        server.run(host='0.0.0.0')
    except KeyboardInterrupt:
        GPIO.cleanup()
