from .common import *
import sentry_sdk
import sys

DEBUG=True

sentry_sdk.init(
    dsn="https://4d0a878ab23ada2c40af8f20731befcb@o4506253563330560.ingest.sentry.io/4506253569032192",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


def handler(t, i, s):
    print("uncaught")


sys.excepthook = handler