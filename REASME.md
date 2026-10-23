# IoT Agro-Environmental Data Logger: Arduino & Python Integration

An end-to-end, hardware-to-software data acquisition system designed to monitor microclimate variables (ambient temperature and light intensity). This project demonstrates a production-ready approach to collecting raw environmental signals and processing them into structured, analysis-ready datasets for smart farming and greenhouse automation.

## System Architecture & Workflow
1. **Data Acquisition (Hardware):** An Arduino microcontroller reads analog signals from a thermal sensor and a photodiode at 3-second intervals.
2. **Signal Conditioning (Firmware):** The raw 10-bit ADC signals are calibrated and converted into physical metrics (°C and a scaled light intensity percentage) via custom mathematical mapping.
3. **Data Logging (Software):** A Python automation script continuously polls the USB Serial port, extracts incoming tokens, appends precise ISO-like timestamps, and stores the logs into a robust CSV file structure.


## Tech Stack & Implementation Details

### Firmware (Arduino / C++)
* **Precision Calibration:** Adjusted the analog-to-voltage baseline calculation to a measured `4.75V` reference for accurate sensor voltage mapping.
* **Custom Sensor Interfacing:** Implemented custom calibration curves to translate raw voltage offsets into accurate temperature readings, alongside a linear scaling formula to output light levels.
* **Efficient Serial Telemetry:** Streams data as structured semicoloned tokens (`temp;luxScala`) over a `9600 baud` hardware serial bridge.

### Software (Python 3)
* **Robust Data Ingestion:** Utilizes `pySerial` with non-blocking timeouts to stream hardware telemetry safely.
* **Exception & IO Handling:** Implemented `try-except` structures to handle file initializations safely (`FileExistsError`) and prevent data corruption during manual termination (`KeyboardInterrupt`).
* **Excel Compatibility:** Uses `utf-8-sig` character encoding to guarantee seamless Unicode rendering (such as the `°C` symbol) natively inside Microsoft Excel and data analytics suites.
