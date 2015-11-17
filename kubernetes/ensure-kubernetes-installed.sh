#!/bin/sh

set -e

if [ -d ~/kubernetes ]; then
    echo "Kubernetes installed"
    exit 0
else
    echo "Installing kubernetes..."
fi


(cd ~ && git clone https://github.com/GoogleCloudPlatform/kubernetes.git)
(cd ~/kubernetes && hack/build-go.sh)
