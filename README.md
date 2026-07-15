# Delete any conflicting ghost clusters
kind delete cluster

# Ensure Docker is active on Fedora
sudo systemctl start docker

# Create the cluster with host port mappings (80/443)
kind create cluster --config kind-config.yaml

# Apply the Kind-specific NGINX Ingress controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

# Wait for the controller to be ready (takes ~1-2 minutes)
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s

  # Navigate to your manifests folder
cd ~/Documents/mini-k8s-project/K8s

# Deploy App 1, App 2, and the Ingress resource
kubectl apply -f app1.yaml
kubectl apply -f app2.yaml
kubectl apply -f ingress.yaml

# Verify everything is running correctly
kubectl get deployments,services,ingress

# Open your hosts file
sudo vi /etc/hosts

# Add this line to the very bottom of the file and save:
127.0.0.1  app1.local app2.local

# Test Host-Based Routing (Separate domains)
curl http://app1.local
curl http://app2.local

# Test Path-Based Routing (Same domain, different sub-folders)
curl http://localhost/app1
curl http://localhost/app2

