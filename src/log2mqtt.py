"""Log data to MQTT broker."""
import paho.mqtt.client as mqtt


class Log2MQTT:
    """Send logs to logging topic."""

    def __init__(self, host, topic):
        """Initialize the MQTT client."""
        self.mqtt_topic = topic
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(host)

    def log(self, data: dict):
        """Send the log to the MQTT broker."""
        log_list = [f"{key[:4]}: {value}" for key, value in data.items()]

        result = self.mqtt_client.publish(self.mqtt_topic, "\n".join(log_list))
        if result.rc != mqtt.MQTT_ERR_SUCCESS:
            print(f"Error sending MQTT message. Return code: {result.rc}")


if __name__ == "__main__":
    import sys
    log2mqtt = Log2MQTT(sys.argv[1], sys.argv[2])
    log2mqtt.log({"temperature": "20", "cloud_cover": "50", "radiation": "1"})
