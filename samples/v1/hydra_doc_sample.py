"""
Generated API Documentation for Server API using
                server_doc_gen.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "entrypoint": {
            "@id": "hydra:entrypoint",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "expectsHeader": "hydra:expectsHeader",
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "manages": "hydra:manages",
        "method": "hydra:method",
        "object": {
            "@id": "hydra:object",
            "@type": "@id"
        },
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readable": "hydra:readable",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "returnsHeader": "hydra:returnsHeader",
        "search": "hydra:search",
        "statusCode": "hydra:statusCode",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "subject": {
            "@id": "hydra:subject",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "writeable": "hydra:writeable",
        "xsd": "https://www.w3.org/TR/xmlschema-2/#"
    },
    "@id": "http://petstore.swagger.io/v2/vocab",
    "@type": "ApiDocumentation",
    "description": "This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.",
    "entrypoint": "http://petstore.swagger.io/v2",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "http://petstore.swagger.io/v2/vocab?resource=ApiResponse",
            "@type": "hydra:Class",
            "description": "ApiResponse",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "https://schema.org/Text",
                    "expectsHeader": [
                        {
                            "description": "successful operation",
                            "statusCode": 200
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "vocab:ApiResponse",
                    "returnsHeader": [],
                    "title": "uploads an image"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "code",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "type",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "message",
                    "writeable": "true"
                }
            ],
            "title": "ApiResponse"
        },
        {
            "@id": "http://petstore.swagger.io/v2/vocab?resource=Order",
            "@type": "hydra:Class",
            "description": "this is def",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Order",
                    "expectsHeader": [
                        {
                            "description": "successful operation",
                            "statusCode": 200
                        },
                        {
                            "description": "Invalid Order",
                            "statusCode": 400
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "vocab:Order",
                    "returnsHeader": [],
                    "title": "Place an order for a pet"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "https://schema.org/Integer",
                    "expectsHeader": [
                        {
                            "description": "successful operation",
                            "statusCode": 200
                        },
                        {
                            "description": "Invalid ID supplied",
                            "statusCode": 400
                        },
                        {
                            "description": "Order not found",
                            "statusCode": 404
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Order",
                    "returnsHeader": [],
                    "title": "Find purchase order by ID"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "id",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "petId",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "quantity",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "shipDate",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "status",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "complete",
                    "writeable": "true"
                }
            ],
            "title": "Order"
        },
        {
            "@id": "http://petstore.swagger.io/v2/vocab?resource=User",
            "@type": "hydra:Class",
            "description": "User",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:User",
                    "expectsHeader": [
                        {
                            "description": "Successful Operation",
                            "statusCode": 200
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "Create user"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "https://schema.org/Text",
                    "expectsHeader": [
                        {
                            "description": "successful operation",
                            "statusCode": 200
                        },
                        {
                            "description": "Invalid username supplied",
                            "statusCode": 400
                        },
                        {
                            "description": "User not found",
                            "statusCode": 404
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:User",
                    "returnsHeader": [],
                    "title": "Get user by user name"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:User",
                    "expectsHeader": [
                        {
                            "description": "Invalid user supplied",
                            "statusCode": 400
                        }
                    ],
                    "method": "PUT",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "Updated user"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "id",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "username",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "firstName",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "lastName",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "email",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "password",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "phone",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "userStatus",
                    "writeable": "true"
                }
            ],
            "title": "User"
        },
        {
            "@id": "http://petstore.swagger.io/v2/vocab?resource=Pet",
            "@type": "hydra:Class",
            "description": "Pet",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:Pet",
                    "expectsHeader": [
                        {
                            "description": "Invalid input",
                            "statusCode": 405
                        }
                    ],
                    "method": "POST",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "Add a new pet to the store"
                },
                {
                    "@type": "http://schema.org/AddAction",
                    "expects": "vocab:Pet",
                    "expectsHeader": [
                        {
                            "description": "Invalid ID supplied",
                            "statusCode": 400
                        }
                    ],
                    "method": "PUT",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": [],
                    "title": "Update an existing pet"
                },
                {
                    "@type": "http://schema.org/FindAction",
                    "expects": "https://schema.org/Text",
                    "expectsHeader": [
                        {
                            "description": "successful operation",
                            "statusCode": 200
                        }
                    ],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "vocab:Pet",
                    "returnsHeader": [],
                    "title": "get all pets"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "id",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "category",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "true",
                    "title": "name",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "true",
                    "title": "photoUrls",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "tags",
                    "writeable": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "",
                    "readable": "true",
                    "required": "false",
                    "title": "status",
                    "writeable": "true"
                }
            ],
            "title": "Pet"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readable": "false",
                    "required": "null",
                    "title": "members",
                    "writeable": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "http://petstore.swagger.io/v2#EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "http://petstore.swagger.io//v2#EntryPoint",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "expectsHeader": [],
                    "method": "GET",
                    "possibleStatus": [],
                    "returns": "null",
                    "returnsHeader": []
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The ApiResponse Class",
                    "hydra:title": "apiresponse",
                    "property": {
                        "@id": "http://petstore.swagger.io/v2/vocab?resource=EntryPoint/pet/uploadImage",
                        "@type": "hydra:Link",
                        "description": "ApiResponse",
                        "domain": "http://petstore.swagger.io/v2/vocab?resource=EntryPoint",
                        "label": "ApiResponse",
                        "range": "http://petstore.swagger.io/v2/vocab?resource=ApiResponse",
                        "supportedOperation": [
                            {
                                "@id": "uploads an image",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "https://schema.org/Text",
                                "expectsHeader": [
                                    {
                                        "description": "successful operation",
                                        "statusCode": 200
                                    }
                                ],
                                "label": "uploads an image",
                                "method": "POST",
                                "possibleStatus": [],
                                "returns": "vocab:ApiResponse",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                },
                {
                    "hydra:description": "The Order Class",
                    "hydra:title": "order",
                    "property": {
                        "@id": "http://petstore.swagger.io/v2/vocab?resource=EntryPoint/store/order",
                        "@type": "hydra:Link",
                        "description": "this is def",
                        "domain": "http://petstore.swagger.io/v2/vocab?resource=EntryPoint",
                        "label": "Order",
                        "range": "http://petstore.swagger.io/v2/vocab?resource=Order",
                        "supportedOperation": [
                            {
                                "@id": "place an order for a pet",
                                "@type": "http://schema.org/UpdateAction",
                                "description": "null",
                                "expects": "vocab:Order",
                                "expectsHeader": [
                                    {
                                        "description": "successful operation",
                                        "statusCode": 200
                                    },
                                    {
                                        "description": "Invalid Order",
                                        "statusCode": 400
                                    }
                                ],
                                "label": "Place an order for a pet",
                                "method": "POST",
                                "possibleStatus": [],
                                "returns": "vocab:Order",
                                "returnsHeader": []
                            },
                            {
                                "@id": "find purchase order by id",
                                "@type": "http://schema.org/FindAction",
                                "description": "null",
                                "expects": "https://schema.org/Integer",
                                "expectsHeader": [
                                    {
                                        "description": "successful operation",
                                        "statusCode": 200
                                    },
                                    {
                                        "description": "Invalid ID supplied",
                                        "statusCode": 400
                                    },
                                    {
                                        "description": "Order not found",
                                        "statusCode": 404
                                    }
                                ],
                                "label": "Find purchase order by ID",
                                "method": "GET",
                                "possibleStatus": [],
                                "returns": "vocab:Order",
                                "returnsHeader": []
                            }
                        ]
                    },
                    "readable": "true",
                    "required": "null",
                    "writeable": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "Swagger Petstore"
}
