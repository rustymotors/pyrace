from distutils import core
from pyrace.shared.config import getConfig
import sentry_sdk

from pyrace.shared.encryption import verifyLegacyCipherSupport
from pyrace.gateway.gateway import getGateway
from pyrace.shared.logging import getLogger


def main():
    corelogger = getLogger(None)

    corelogger.info("Starting core server")

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

    configLogger = corelogger.getLogger("config")

    configuration = getConfig(logger=configLogger)

    corelogger.info(
        "Starting core server with the following configuration: %s", configuration
    )

    listeningPorts = [
        6660,
        7003,
        8228,
        8226,
        8227,
        9000,
        9001,
        9002,
        9003,
        9004,
        9005,
        9006,
        9007,
        9008,
        9009,
        9010,
        9011,
        9012,
        9013,
        9014,
        43200,
        43300,
        43400,
        53303,
    ]

    gatewayServer = getGateway(
        config=configuration,
        logger=corelogger.getLogger("gateway"),
        portList=listeningPorts,
    )
    gatewayServer.start()


if __name__ == "__main__":
    main()
    # curses.wrapper(main)
