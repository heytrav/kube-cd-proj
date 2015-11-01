#!/bin/sh

#!/bin/sh

export VERSION=$1
: ${CONTROLLER:=django-app}
: ${CONTROLLER_FILE:=app-controller.yml}

RELEASE=$( git tag | grep $VERSION )
export BRANCH=$(git rev-parse --abbrev-ref HEAD | sed 's/\//-/g')
PULL_REQUEST=$(echo ${BRANCH} | grep pull)

if [  "$RELEASE" = "" ]; then
    KUBERNETES_CONTEXT=staging
else
    KUBERNETES_CONTEXT=production
fi
export DEPLOY_ENVIRONMENT=$KUBERNETES_CONTEXT
KUBE_CMD=${KUBERNETES_ROOT:-~/kubernetes}/cluster/kubectl.sh
$KUBE_CMD config use-context $KUBERNETES_CONTEXT
CURRENT_CONTROLLER=$($KUBE_CMD get rc | grep ${CONTROLLER} | cut -f 1 -d " ")
envsubst < kubernetes/$KUBERNETES_CONTEXT/${CONTROLLER_FILE}.template > $CONTROLLER_FILE
if [ "$DEPLOY_ENVIRONMENT" = "production" ]; then
    cat $CONTROLLER_FILE > $CIRCLE_ARTIFACTS/${CONTROLLER_FILE}
fi
if [ "$CURRENT_CONTROLLER" = "" ]; then
    $KUBE_CMD create -f ${CONTROLLER_FILE}
else
    $KUBE_CMD rolling-update $CURRENT_CONTROLLER -f ${CONTROLLER_FILE}
fi
