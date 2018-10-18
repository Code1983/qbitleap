export SAPI_HOME=https://cloud.dwavesys.com/sapi
echo "update Token before running"
#export SAPI_TOKEN=DEV-1224b7fa170dde3cf0112542?????
curl -H "X-Auth-Token: $SAPI_TOKEN" $SAPI_HOME/solvers/remote/ >> init_script.out
