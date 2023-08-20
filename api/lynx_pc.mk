#!/bin/bash

API_URL="http://localhost:3003/get_objects"

objects_data=$(curl -s $API_URL)

for object_name in "object1" "object2" "object3"; do
    object_data=$(echo $objects_data | jq -r ".${object_name}")
    size=$(echo $object_data | jq -r '.size')
    weight=$(echo $object_data | jq -r '.weight')
    status=$(echo $object_data | jq -r '.status')
    quantity=$(echo $object_data | jq -r '.quantity')
    
    if [ "$status" == "0" ]; then
        echo "0 ${object_name}_size size=$size weight=$weight"
    elif [ "$status" == "1" ]; then
        echo "1 ${object_name}_size size=$size weight=$weight"
    else
        echo "2 ${object_name}_size size=$size weight=$weight"
    fi

    echo "0 ${object_name}_quantity quantity=$quantity"
done
