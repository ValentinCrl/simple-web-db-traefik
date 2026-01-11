# Simple Web App on Kubernetes — Production Ready Deployment

Ce projet démontre le déploiement complet d’une application web conteneurisée avec base de données PostgreSQL sur un cluster Kubernetes auto-hébergé, exposée publiquement via un Ingress Traefik derrière un LoadBalancer Hetzner, avec chiffrement HTTPS automatique grâce à Let’s Encrypt.

---

## 🎯 Objectifs du projet

* Conteneuriser une application web Flask + PostgreSQL
* Déployer l’application sur un cluster Kubernetes (kubeadm)
* Exposer l’application publiquement avec Traefik Ingress Controller
* Utiliser un LoadBalancer managé Hetzner
* Configurer un nom de domaine OVH
* Activer HTTPS automatique avec cert-manager + Let’s Encrypt
* Déployer l’infrastructure **as-code**

---

## 🏗️ Architecture

```
Internet
   ↓
DNS OVH (myapp.valdibien.ovh)
   ↓
LoadBalancer Hetzner
   ↓
Traefik Ingress Controller
   ↓
Ingress Kubernetes
   ↓
Service web-app
   ↓
Pods Flask
   ↓
PostgreSQL
```

---

## 📦 Stack technique

| Composant          | Technologie                  |
| ------------------ | ---------------------------- |
| Orchestrateur      | Kubernetes (kubeadm)         |
| Cloud provider     | Hetzner Cloud                |
| LoadBalancer       | Hetzner Cloud LoadBalancer   |
| Ingress Controller | Traefik                      |
| Certificats TLS    | cert-manager + Let’s Encrypt |
| Application        | Flask + Gunicorn             |
| Base de données    | PostgreSQL                   |
| Conteneurs         | Docker                       |
| DNS                | OVH                          |

---

## 📁 Arborescence du projet

```
simple-web-db-traefik/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── db/
│   └── Dockerfile
├── kubernetes/
│   ├── app/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   ├── db/
│   │   └── deployment.yaml
│   └── infra/
│       ├── traefik.yaml
│       └── cluster-issuer.yaml
├── Kubernetes/
│   └── cluster/
│       └── kubeadm-install.sh
└── README.md
```

---

## ⚙️ Prérequis

* 2 serveurs Hetzner (1 control-plane, 1 worker minimum)
* Ubuntu 22.04
* Un domaine chez OVH
* Docker
* Kubernetes (kubeadm)
* Helm
* kubectl

---

## 🚀 Déploiement du cluster Kubernetes

### Sur le control-plane

```bash
cd Kubernetes/cluster
chmod +x kubeadm-install.sh
./kubeadm-install.sh
```

Configurer kubectl :

```bash
export KUBECONFIG=/etc/kubernetes/admin.conf
```

---

## 👷 Ajouter un worker

Sur le worker :

```bash
kubeadm join <IP_CONTROL_PLANE>:6443 --token <TOKEN> --discovery-token-ca-cert-hash sha256:<HASH>
```

---

## 🌐 Installation du CNI (Calico)

```bash
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/calico.yaml
```

---

## 🔐 Installation de cert-manager

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
```

---

## 🔑 Création du ClusterIssuer Let’s Encrypt

```bash
kubectl apply -f kubernetes/infra/cluster-issuer.yaml
```

---

## 🚦 Installation de Traefik (Ingress Controller)

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update

helm install traefik traefik/traefik \
  --namespace traefik \
  --create-namespace \
  --set service.type=LoadBalancer
  --set service.annotations.loadbalancer\\.hetzner\\.cloud/location=hel1
```

---

## 🗄️ Déploiement de la base PostgreSQL

```bash
kubectl apply -f kubernetes/db/deployment.yaml
```

---

## 🌍 Déploiement de l’application web

```bash
kubectl apply -f kubernetes/app/deployment.yaml
kubectl apply -f kubernetes/app/service.yaml
kubectl apply -f kubernetes/app/ingress.yaml
```

---

## 🌐 Configuration DNS OVH

Créer un enregistrement DNS :

```
myapp.valdibien.ovh → IP du LoadBalancer Hetzner
```

---

## 🔐 Vérification du certificat

```bash
kubectl get certificate -n simple-web
```

Accès HTTPS :

```
https://myapp.valdibien.ovh
```

---

## 🧪 Tests

```bash
kubectl run curl-test -n simple-web --image=curlimages/curl -it --rm -- http://web-app
```

---

## 🏁 Résultat final

Application accessible publiquement :

```
https://myapp.valdibien.ovh
```

Avec certificat TLS Let’s Encrypt et reverse-proxy Traefik.

---

## 👨‍💻 Auteur

Projet réalisé par **Valentin Crl**
Déploiement Kubernetes complet avec cloud Hetzner & Traefik.

---

## 📜 Licence

MIT
