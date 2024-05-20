import curses
import logging
import os
from pyrace.config import configuration
import sentry_sdk

from pyrace.shared.encryption import verifyLegacyCipherSupport

def main(win):
    corelogger = logging.getLogger(__name__)
    corelogger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    corelogger.addHandler(logging.StreamHandler())
    
    print("Starting core server")

    try:
        verifyLegacyCipherSupport()
    except Exception as e:
        corelogger.error("Error in core sever: %s", e)
        return 1

    sentry_sdk.init(
        dsn="https://67febaa0a5343792fce8a0750fc12152@o1413557.ingest.us.sentry.io/4507288238358528",
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
    
    corelogger.info(
        "Starting core server with the following configuration: %s", configuration
    )
    
    appLogger = logging.getLogger("pyrace")
    
    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    win.clear()                
    win.addstr("Detected key:")
    
    while 1:          
        try:                 
           key = win.getkey()         
           win.addstr(str(key)) 
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass 

    return 0


if __name__ == "__main__":
    curses.wrapper(main)
