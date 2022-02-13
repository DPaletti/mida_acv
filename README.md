# SMeS: Secure Mobility in eScooters
The project has two main goals:
- estimating the mass of the rider(s)
- assessing the number of people on board
The data available comes from a Unipol Sensor Box installed on the scooter.

All the code is available as a [jupyter notebook](mida_acv.ipynb)
# Dataset Description
The dataset contains 19 tests performed by a single driver, leveraging a pool of drivers weighing between 35 and 115kg.
Three tests were carried out with two passengers on board. 
The combinations were chosen so that the sum of their weight was comparable to that of a single driver.

![Drivers Overview](resources/dataset_description.png?raw=true "Drivers Overview")

# Sensor Description
The box contains a 6-axes Inertial Measurement Unit (IMU). This means that included in the unit are:
 A tri-axial accelerometer, which provides acceleration along the x, y, z axes [m/s^2]. 
A tri-axial gyroscope, providing angular acceleration, hence roll, pitch, and yaw rates [rad/s]. 
An anti-aliasing low-pass filter was also applied at a cut-off frequency of 20Hz. The sampling frequency of the signals acquired by the IMU is 104Hz. Besides, there is a GPS, that samples latitude, longitude, and speed. The GPS values are sampled at 1Hz. In the shared dataset, the GPS signals were interpolated to bring their resolution to that of the IMU.
![Sensor Placement](resources/sensor_placement.png?raw=true "Sensor Placement")

# Classification Outcome
Number of passengers classification (0 means 1 person on board, 1 means 2 people on board):

![passengers classification](resources/passenger_classification.png?raw=true "Passenger Classification")

Weight estimation (by weight-class classification):

![weight classification](resources/weight_classification.png?raw=true "Weight Classification")

