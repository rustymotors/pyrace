import logging
import sentry_sdk

from pyrace.shared.encryption import verifyLegacyCipherSupport

def main():
    corelogger = logging.getLogger(__name__)
    
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
    
    return 0

if __name__ == "__main__":
    main()