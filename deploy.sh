#!/bin/sh

export VERSION=$1
: ${CONTROLLER:=app}
: ${CONTROLLER_FILE:=app-controller.yml}

# Find out if we're on a pull request
export BRANCH=$(git rev-parse --abbrev-ref HEAD | sed 's/\//-/g')
PULL_REQUEST=$(echo ${BRANCH} | grep pull)


# Find out if we're on an annotated tag
RELEASE=$( git tag | grep $VERSION )

# If on tag release to production
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

# Save controller file for production releases to artifacts.
if [ "$DEPLOY_ENVIRONMENT" = "production" ]; then
    cat $CONTROLLER_FILE > $CIRCLE_ARTIFACTS/${CONTROLLER}-${VERSION}.yml
fi

# Create new replication controller if app not running. Otherwise rolling
# update to new version.
if [ "$CURRENT_CONTROLLER" = "" ]; then
    $KUBE_CMD create -f ${CONTROLLER_FILE}
else
    $KUBE_CMD rolling-update $CURRENT_CONTROLLER -f ${CONTROLLER_FILE}
fi
