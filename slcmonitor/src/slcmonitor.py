from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from org.netmelody.slcmonitor.controllers.mappings import controller_map 

application = webapp.WSGIApplication(controller_map, debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()