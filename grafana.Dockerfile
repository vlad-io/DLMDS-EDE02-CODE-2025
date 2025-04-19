# Use a specific Grafana version or 'latest'
# Using 11.6.0 as mentioned in your external dashboard requires section
# FROM grafana/grafana:11.6.0
FROM grafana/grafana-oss

# ENV GF_SECURITY_ADMIN_PASSWORD=admin
# ENV GF_SECURITY_ADMIN_USER=admin
# ENV GF_DATASOURCE_POSTGRES_URL=postgres-db:5432
# ENV GF_DATASOURCE_POSTGRES_USER=appuser
# ENV GF_DATASOURCE_POSTGRES_DB=mydatabase
# ENV GF_DATASOURCE_POSTGRES_PASSWORD=password
# ENV GF_DATASOURCE_POSTGRES_SSLMODE=disable 

# Switch to root user to copy files and set permissions
USER root

# # Copy the datasource provisioning configuration
COPY datasource.yaml /etc/grafana/provisioning/datasources/datasource.yaml

# # Copy the dashboard provider configuration
COPY dashboard-provider.yaml /etc/grafana/provisioning/dashboards/dashboard-provider.yaml

# # Copy your specific dashboard JSON file into the directory Grafana scans
# # Renaming it slightly for clarity within the container
COPY grafana-dashboard-internal.json /etc/grafana/provisioning/dashboards/drone-path-dashboard.json

# # Set correct permissions for the grafana user (UID 472) to read the provisioning files
# RUN chown -R grafana:grafana /etc/grafana/provisioning/

# # Switch back to the default grafana user
# USER grafana

# (Optional) Expose Grafana default port
EXPOSE 3000
