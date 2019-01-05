from flask import Flask, render_template, request
import persistence

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    defaultHigh = ''
    defaultMedium = ''
    defaultLow = ''

    retrieveInfo = persistence.getInfo('abc')

    if retrieveInfo != None:
        speed = retrieveInfo.speed
        temperature = retrieveInfo.temperature

        if speed == 'high':
            defaultHigh = 'checked'
        elif speed == 'medium':
            defaultMedium = 'checked'
        elif speed == 'low':
            defaultLow = 'checked'

    else:
        defaultLow = 'checked'
        speed = "low"
        temperature = 20

    if request.method == 'POST':

        if 'speed' in request.form:
            defaultHigh = ''
            defaultMedium = ''
            defaultLow = ''

            speed = request.form['speed']
            if speed == 'high':
                defaultHigh = 'checked'
            elif speed == 'medium':
                defaultMedium = 'checked'
            elif speed == 'low':
                defaultLow = 'checked'

            persistence.saveSpeed('abc', speed)

        if 'temperature' in request.form:
            tempInfo = request.form['temperature']
            if tempInfo == 'UP':
                temperature += 1
            elif tempInfo == 'DOWN':
                temperature -= 1
            persistence.saveTemperature('abc', temperature)

    return render_template('index.html', speed=speed, temperature=temperature, defaultHigh=defaultHigh, defaultMedium=defaultMedium, defaultLow=defaultLow)

if __name__ == '__main__':
    app.run()
