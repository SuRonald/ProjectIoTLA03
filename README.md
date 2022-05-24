# Monitoring Suhu CPU dan Visualisasi Data

## Project IoT LA03 Mobile Application and Technology

Anggota:

- Daffa Hanif Padantya – 2440057602
- Maevy Marvella – 2440094402
- Ronald Sumichael Sunan – 2440003745

Code pada repository berikut merupakan code yang digunakan pada Project IoT ini. Project ini menggunakan data dari software third party yang merupakan [Core Temp](https://www.alcpu.com/CoreTemp/) untuk melakukan logging temperatur CPU yang diexport menjadi excel dan dikirimkan ke server pada [ThingsBoard](https://thingsboard.io/) untuk menampilkan visualisasi data menggunakan dashboard menggunakan koneksi MQTT. Code hasil akhir yang digunakan untuk project ini adalah **finalPublishData.py**.

### [client.py](https://github.com/SuRonald/ProjectIoTLA03/blob/main/client.py)

Code ini digunakan untuk mendapatkan data yang dikirim menggunakan koneksi MQTT ke server MQTT Broker yang merupakan [Mosquitto](https://mosquitto.org/).

### [connectMosquitto.py](https://github.com/SuRonald/ProjectIoTLA03/blob/main/connectMosquitto.py)

**Percobaan Pengiriman Data Menggunakan Mosquitto**

Code ini digunakan untuk megirimkan data yang didapat dari Core Temp ke [Mosquitto](https://mosquitto.org/) menggunakan koneksi MQTT.

### [connectThingsBoard.py](https://github.com/SuRonald/ProjectIoTLA03/blob/main/connectThingsBoard.py)

**Percobaan Pengiriman Data Menggunakan ThingsBoard**

Code ini digunakan untuk megirimkan data yang didapat dari Core Temp ke [ThingsBoard](https://thingsboard.io/) menggunakan koneksi MQTT.

### [finalPublishData.py](https://github.com/SuRonald/ProjectIoTLA03/blob/main/finalPublishData.py)

Code ini digunakan untuk megirimkan data yang didapat dari Core Temp ke [ThingsBoard](https://thingsboard.io/) atau [Mosquitto](https://mosquitto.org/) (Dapat dipilih salah satu) menggunakan koneksi MQTT. Yang dimana akan berjalan terus menurus selama data yang didapat tidak habis dengan jeda pengiriman setiap 5 detik.
