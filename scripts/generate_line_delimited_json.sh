#!/bin/bash 
# makes json readable from pandas "read_csv" method
cat ../../${YEAR}_data.json | jq -c '.[]' > ../../${YEAR}.json

