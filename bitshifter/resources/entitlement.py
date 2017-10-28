from bitshifter import app
from flask import jsonify, request


# --------------------------------------------------------------------------
# POST: /API/ORG/<ORG_ID>/USER/<USER_ID>/ENTITLEMENT
# --------------------------------------------------------------------------
# Create an entitlement for a given user id in a given organization
@app.route('/_org/<org_id>/_user/<user_id>/_entitlement', methods=['POST'])
def post_org(org_id, user_id):
    
    # First we validate org_id and user_id are present
    if org_id is None or user_id is None:
        return jsonify(
            { "msg": "You must provide a valid org_id and user_id" }
        ), 400
    
    # Now we verify that the request contains actual JSON payload     
    if not request.is_json:
        return jsonify(
            {"msg": "Unsupported Content-Type. Only JSON is supported"}
        ), 400
        
    pass


# --------------------------------------------------------------------------
# GET: /API/ORGS
# --------------------------------------------------------------------------
# List all entitlements a given user has in a given organization
@app.route('/_org/<org_id>/_user/<user_id>/_entitlement', methods=['GET'])
def get_orgs(org_id, user_id):
    pass


# --------------------------------------------------------------------------
# GET: /API/ORG
# --------------------------------------------------------------------------
@app.route('/_org/<org_id>/_user/<user_id>/_entitlement/<entitlement_id>', methods=['GET'])
def get_org(org_id, user_id, entitlement_id):
    pass


# --------------------------------------------------------------------------
# PUT: /API/ORG/<ORG_ID>
# --------------------------------------------------------------------------
@app.route('/_org/<org_id>/_user/<user_id>/_entitlement/<entitlement_id>', methods=['PUT'])
def put_org(org_id, user_id, entitlement_id):
    pass


# --------------------------------------------------------------------------
# DELETE: /API/ORG/<ORG_ID>
# --------------------------------------------------------------------------
@app.route('/_org/<org_id>/_user/<user_id>/_entitlement/<entitlement_id>', methods=['DELETE'])
def delete_org(org_id, user_id, entitlement_id):
    pass