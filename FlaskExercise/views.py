from distutils.log import debug, error, info
from logging import critical, warning
from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log:
        if log == 'debug':
            app.logger.debug('DEBUG button is pressed')
        elif log == 'info':
            app.logger.info('INFO button pressed')
        elif log == 'warning':
            app.logger.warning('WARNING button pressed')
        elif log == 'error':
            app.logger.error('ERROR butoon pressed')
        elif log == 'critical':
            app.logger.critical('CRITICAL button pressed')


    return render_template(
        'index.html',
        log=log
    )
