# ☸️ Local Kubernetes (Kind) Learning Portfolio

Welcome to my local Kubernetes playground! This repository tracks my journey learning container orchestration, ingress routing, and microservice networking using **Kind (Kubernetes in Docker)** on Fedora Linux.

---

## 📂 Projects Directory

### 🚀 [Project 01: Basic Local Multi-Routing](./01-basic-echo-routing)
* **Concepts:** Cluster provisioning, basic HTTP-Echo servers, domain local routing.
* **Tech Stack:** Kind, NGINX Ingress Controller, YAML Manifests.
* 👉 [Click here to see Project 1 Setup & Code](./01-basic-echo-routing)

### 🐍 [Project 02: Advanced Python Microservices Suite](./02-python-microservices)
* **Concepts:** Multi-app host and path-based routing isolation, cross-container data fetching via frontend JavaScript, local Docker image builds.
* **Tech Stack:** Python (Flask), Docker, Kubernetes Deployments/Services, NGINX Ingress.
* 👉 [Click here to see Project 2 Setup & Code](./02-python-microservices)

### 🗄️ [Project 03: The Stateful Database Upgrade](./03-stateful-microservices)
* **Concepts:** Persistent Volumes (`PVC`), secure Kubernetes `Secrets` encoding, database state tracking, live SQL connections inside Python (`psycopg2`).
* **Tech Stack:** PostgreSQL 15, Python Flask, Kind Local Storage Provisioner.
* 👉 [Click here to see Project 3 Setup & Code](./03-stateful-microservices)

# 📊 Project 04: Production Observability Stack (Prometheus & Grafana)

Unlike previous projects that used local YAML manifests, this production metrics engine was deployed directly into the cluster using **Helm** to aggregate cluster-wide telemetry.

### 🧠 Core Architecture & Concepts
* **Metrics Aggregation:** Deployed Prometheus to automatically scrape memory, CPU, and network usage metrics across all nodes and pods.
* **Telemetry Visualization:** Provisioned Grafana, linked it to the live Prometheus data source, and loaded native Kubernetes dashboards.
* **Cluster Stress Testing:** Successfully verified telemetry streams by launching real-time multi-threaded stress tests (`stress-ng`) inside the cluster.

### 🛠️ Deployment Steps

1. **Add Helm Chart Repositories:**
   ```bash
   helm repo add prometheus-community [https://prometheus-community.github.io/helm-charts](https://prometheus-community.github.io/helm-charts)
   helm repo update

Deploy the Monitoring Stack into an Isolated Namespace:
kubectl create namespace monitoring
helm install monitor-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set grafana.adminPassword=admin

Accessing the Live Dashboard:
Securely tunnel into the cluster network from your local machine:
kubectl port-forward svc/monitor-stack-grafana 3000:80 -n monitoring

## 🔒 Project 05: Secure Ingress Traffic Control (TLS/HTTPS)

Upgraded the local web architecture from unencrypted HTTP to production-grade HTTPS (`https://shop.local`) by generating custom local cryptographic keypairs.

### 🧠 Core Architecture & Concepts
* **Local Certificate Authority:** Generated custom 2048-bit RSA keys and self-signed X.509 certificates using OpenSSL natively on Fedora.
* **Kubernetes TLS Secrets:** Cryptographically injected the generated `.key` and `.crt` files into the cluster namespace using native `kubernetes.io/tls` secret layers.
* **Automated SSL Redirection:** Configured NGINX Ingress annotations (`ssl-redirect: "true"`) to enforce automatic fallback routing from port 80 to encrypted port 443.
