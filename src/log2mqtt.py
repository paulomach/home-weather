"""Log data to MQTT broker."""
import time

import paho.mqtt.client as mqtt

from logger import log


class Log2MQTT:
    """Send logs to logging topic."""

    def __init__(self, host, topic):
        """Initialize the MQTT client."""
        self.mqtt_topic = topic
        self.mqtt_client = mqtt.Client(reconnect_on_failure=True)
        self.mqtt_client.connect(host)
        self.enum_names = {value: name for name, value in vars(
            mqtt).items() if name.__contains__("ERR")}

    def log2topic(self, data: dict, retries=3):
        """Send the log to the MQTT broker."""
        log_list = [f"{key[:4]}: {value}" for key, value in data.items()]

        result = self.mqtt_client.publish(
            self.mqtt_topic, "\n".join(log_list), qos=1, retain=True)
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            log(f"Error sending MQTT message. Error: {self.enum_names.get(result.rc)}")
            if retries > 0:
                log(f"Retrying..{retries}")
                self.mqtt_client.reconnect()
                time.sleep(1)
                self.log2topic(data, retries - 1)
            else:
                log(f"Error connecting to MQTT broker. Retries: {retries}")
        else:
            log("Successfully logged to MQTT broker.")


if __name__ == "__main__":
    import sys
    log2mqtt = Log2MQTT(sys.argv[1], sys.argv[2])
    log2mqtt.log2topic({"temperature": "20", "cloud_cover": "50", "radiation": "100"})
