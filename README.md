 ## Abstract
 
 This project demonstrates a data engineering pipeline showcasing the interaction between various data processing technologies within a containerized environment. Using Docker and docker-compose, the system deploys multiple components: three drone simulators and one central tower, all implemented in Python. Drones continuously generate coordinate data, which is transmitted via Apache Kafka topics. The tower component consumes these Kafka streams, performs an initial transformation by amending the incoming dataframes, and persists the processed coordinates into a PostgreSQL database. Further data transformation can occurs within PostgreSQL through the use of a database view. Finally, a Grafana instance connects to the PostgreSQL database to visualize the drone movements and status, applying a final transformation by displaying only the latest N coordinate points for monitoring purposes. This setup provides a practical example of stream processing, data storage, and real-time visualization using common industry tools.

 ## To run the application
 
 1. Pull the code from the repository then run in the folder

 `docker-compose up`

 2. Docker will spin up various servers.

 3. Then, in your browser go to: http://localhost:3000/ to see Grafana interface.

 4. Login into Grafana by using `admin` username and `admin` password

 5. Go to `Dashboards` then click on the dashboard to view the visualisations

 ## Troubleshooting

 Sometimes the Kafka server does not initiate due to resource constraints. Without Kafka server the application will not function correctly. After running `docker-compose up`, please monitor in Docker Desktop. If Kafka has stoped, please start it. Or, run shut down docker-compose by running `doccker-compose down`, and start again.

 ## Reduce resource requirements

 Currently the system launches 3 drone containers. To reduce resource requirements the number can be reduced to 1 by removing drone-2 and drone-3 services from the [docker-compose.yml](./docker-compose.yml) file.