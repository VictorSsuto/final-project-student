from flask import Flask, request, jsonify, abort
import pymongo as pymongo
from pymongo import MongoClient
import json
import os
from Schema import schemaPost
from bson import json_util
from bson.objectid import ObjectId