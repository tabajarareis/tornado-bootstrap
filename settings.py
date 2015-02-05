import tornado
import os

from tornado.options import define, options

define("port", default=8000, help="Run on given port", type=int)
define("debug", default=False, help="Debug mode")
tornado.options.parse_command_line()


if 'ENVIRONMENT' in os.environ:
    ENVIRONMENT = os.environ['ENVIRONMENT'].upper()
else:
    ENVIRONMENT = 'DEV'

settings = {

    # Debug options
    'debug': ENVIRONMENT != 'PROD' or options.debug,

    # Database connection
    'database': {
        'dbdriver': 'mongodb',
        'hostport': 27017,
        'username': '',
        'password': '',
        'hostname': 'localhost',
        'basename': 'test',
    },

    # Security
    'cookie_secret': '98ou19p23749182u3y4p923',
    'xsrf_cookies': True,

    # Application Paths
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),

}
