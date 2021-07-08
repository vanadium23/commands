import logging.config

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s ( FUNC: %(funcName)s )"
                "[ LINE: %(lineno)d ] - %(message)s"
            ),
        }
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"}
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "services.example.service": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
            "formatter": "verbose",
        },
    },
}

logging.config.dictConfig(LOGGING)


SOME = 1
