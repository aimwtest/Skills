"""
Copyright start
MIT License
Copyright (c) 2026 <Your Organization>
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations, check_health
from .constants import LOGGER_NAME

logger = get_logger(LOGGER_NAME)


class SampleConnector(Connector):
    def execute(self, config, operation, params, *args, **kwargs):
        try:
            action = operations.get(operation)
            if action is None:
                raise ConnectorError("Unsupported operation: {}".format(operation))
            logger.info("Executing operation '%s'", operation)
            return action(config, params)
        except ConnectorError:
            raise
        except Exception as err:
            logger.exception("Operation '%s' failed: %s", operation, err)
            raise ConnectorError("Operation '{}' failed: {}".format(operation, err))

    def check_health(self, config):
        logger.info("Starting health check")
        check_health(config)
        logger.info("Health check passed")
