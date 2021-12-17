"""Log data to MQTT broker."""
import time

import paho.mqtt.client as mqtt


class Log2MQTT:
    """Send logs to logging topic."""

    def __init__(self, host, topic):
        """Initialize the MQTT client."""
        self.mqtt_topic = topic
        self.mqtt_client = mqtt.Client(reconnect_on_failure=True)
        self.mqtt_client.connect(host)

    def log(self, data: dict, retries=3):
        """Send the log to the MQTT broker."""
        log_list = [f"{key[:4]}: {value}" for key, value in data.items()]

        result = self.mqtt_client.publish(
            self.mqtt_topic, "\n".join(log_list), qos=1, retain=True)
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            print(f"Error sending MQTT message. Return code: {result.rc}")
            if retries > 0:
                print(f"Retrying..{retries}")
                self.mqtt_client.reconnect()
                time.sleep(1)
                self.log(data, retries - 1)
            else:
                print(f"Error connecting to MQTT broker. Retries: {retries}")


if __name__ == "__main__":
    import sys
    log2mqtt = Log2MQTT(sys.argv[1], sys.argv[2])
    log2mqtt.log({"temperature": "20", "cloud_cover": "50", "radiation": "100"})
