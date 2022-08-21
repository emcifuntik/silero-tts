#!/bin/bash

VOICE=$1
echo "$2" | python /python/__init__.py ${VOICE} "$3"