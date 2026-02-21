import sys
import subprocess
import logging

logging.basicConfig(
    filename="service_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_service(service_name):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "--quiet", service_name]
        )
        return result.returncode == 0
    except Exception as e:
        logging.error(f"Error checking service: {e}")
        sys.exit(1)

def start_service(service_name):
    try:
        # Habilitar servicio (no forzamos fallo si ya está habilitado)
        subprocess.run(
            ["systemctl", "enable", service_name],
            check=False,
            capture_output=True,
            text=True
        )

        # Intentar arrancarlo
        result = subprocess.run(
            ["systemctl", "start", service_name],
            check=True,
            capture_output=True,
            text=True
        )

        logging.info(f"Service {service_name} started successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(
            f"Failed to start service {service_name}. "
            f"Error: {e.stderr}"
        )
        print(f"Error starting {service_name}. Check logs.")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 service_monitor.py <service_name>")
        sys.exit(1)

    service_name = sys.argv[1]

    if check_service(service_name):
        logging.info(f"Service {service_name} is running.")
        print(f"{service_name} is running.")
    else:
        logging.warning(f"Service {service_name} is not running. Attempting restart.")
        print(f"{service_name} is not running. Starting...")
        start_service(service_name)

if __name__ == "__main__":
    main()
