#!/usr/bin/env bash

# Paths to useful directories.
SCRIPT_FOLDER=$( dirname -- "$( readlink -f -- "$0"; )"; )
SOURCE_FOLDER=$SCRIPT_FOLDER/..

# Load variables from the .env file.
# source: https://gist.github.com/mihow/9c7f559807069a03e302605691f85572?permalink_comment_id=3770590#gistcomment-3770590
export $(echo $(cat "$SOURCE_FOLDER/.env" | sed 's/#.*//g'| xargs) | envsubst)

# Guess protocol based on environment variables.
HTTP_OR_HTTPS=https
if [ $PLAIN_HTTP == "yes" ]
then
    HTTP_OR_HTTPS=http
fi

# Send request.
curl -k -v \
    -X POST "$HTTP_OR_HTTPS://127.0.0.1:$SERVER_PORT/v1/patient" \
    -u "$AUTH_USERNAME:$AUTH_PASSWORD" \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "uid": {
            "value": "11111111-1111-1111-1111-111111111111",
            "_type": "HIER_OBJECT_ID"
        },
        "name": {
            "value": "foo",
            "defining_code": {
                "terminology_id": {
                    "value": "bar",
                    "_type": "TERMINOLOGY_ID"
                },
                "code_string": "baz",
                "_type": "CODE_PHRASE"
            },
            "_type": "DV_CODED_TEXT"
        },
        "archetype_node_id": "at0000_1",
        "identities": [
            {
                "name": {
                    "value": "foo",
                    "defining_code": {
                        "terminology_id": {
                            "value": "bar",
                            "_type": "TERMINOLOGY_ID"
                        },
                        "code_string": "baz",
                        "_type": "CODE_PHRASE"
                    },
                    "_type": "DV_CODED_TEXT"
                },
                "archetype_node_id": "at0000_1",
                "details": {
                    "name": {
                        "value": "foo",
                        "defining_code": {
                            "terminology_id": {
                                "value": "bar",
                                "_type": "TERMINOLOGY_ID"
                            },
                            "code_string": "baz",
                            "_type": "CODE_PHRASE"
                        },
                        "_type": "DV_CODED_TEXT"
                    },
                    "archetype_node_id": "at0001",
                    "items": [
                        {
                            "name": {
                                "value": "foo",
                                "defining_code": {
                                    "terminology_id": {
                                        "value": "bar",
                                        "_type": "TERMINOLOGY_ID"
                                    },
                                    "code_string": "baz",
                                    "_type": "CODE_PHRASE"
                                },
                                "_type": "DV_CODED_TEXT"
                            },
                            "archetype_node_id": "at0003",
                            "items": [
                                {
                                    "name": {
                                        "value": "foo",
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": "bar",
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": "baz",
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0012",
                                    "_type": "ELEMENT"
                                },
                                {
                                    "name": {
                                        "value": "foo",
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": "bar",
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": "baz",
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0013",
                                    "_type": "ELEMENT"
                                }
                            ],
                            "_type": "CLUSTER"
                        },
                        {
                            "name": {
                                "value": "foo",
                                "defining_code": {
                                    "terminology_id": {
                                        "value": "bar",
                                        "_type": "TERMINOLOGY_ID"
                                    },
                                    "code_string": "baz",
                                    "_type": "CODE_PHRASE"
                                },
                                "_type": "DV_CODED_TEXT"
                            },
                            "archetype_node_id": "at0006",
                            "items": [
                                {
                                    "name": {
                                        "value": "foo",
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": "bar",
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": "baz",
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0018",
                                    "_type": "ELEMENT"
                                },
                                {
                                    "name": {
                                        "value": "foo",
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": "bar",
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": "baz",
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0019",
                                    "_type": "ELEMENT"
                                }
                            ],
                            "_type": "CLUSTER"
                        },
                        {
                            "name": {
                                "value": "foo",
                                "defining_code": {
                                    "terminology_id": {
                                        "value": "bar",
                                        "_type": "TERMINOLOGY_ID"
                                    },
                                    "code_string": "baz",
                                    "_type": "CODE_PHRASE"
                                },
                                "_type": "DV_CODED_TEXT"
                            },
                            "archetype_node_id": "at0008",
                            "_type": "ELEMENT"
                        }
                    ],
                    "_type": "ITEM_TREE"
                },
                "_type": "PARTY_IDENTITY"
            }
        ],
        "_type": "PERSON"
    }'
