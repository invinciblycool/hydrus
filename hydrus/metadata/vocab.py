vocab = {
    "supportedClass": [
        {
            "supportedProperty": [
                {
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "required": "null",
                    "readonly": "false",
                    "hydra:description": "The members of this collection.",
                    "writeonly": "false",
                    "hydra:title": "members"
                }
            ],
            "supportedOperation": [],
            "hydra:description": "null",
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "hydra:title": "Collection"
        },
        {
            "supportedProperty": [],
            "supportedOperation": [],
            "hydra:description": "null",
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "hydra:title": "Resource"
        },
        {
            "supportedProperty": [
                {
                    "property": {
                        "range": "vocab:CotsCollection",
                        "@type": "hydra:Link",
                        "supportedOperation": [
                            {
                                "expects": "null",
                                "returns": "vocab:CotsCollection",
                                "method": "GET",
                                "label": "Retrieves all Cots entities",
                                "statusCodes": [],
                                "description": "null",
                                "@id": "_:cots_collection_retrieve",
                                "@type": "hydra:Operation"
                            }
                        ],
                        "domain": "vocab:EntryPoint",
                        "description": "The Cots collection",
                        "@id": "vocab:EntryPoint/Cots",
                        "label": "Cots"
                    },
                    "required": "null",
                    "readonly": "true",
                    "hydra:description": "The Cots collection",
                    "writeonly": "false",
                    "hydra:title": "cots"
                }
            ],
            "@type": "hydra:Class",
            "supportedOperation": [
                {
                    "expects": "null",
                    "returns": "vocab:EntryPoint",
                    "method": "GET",
                    "label": "The APIs main entry point.",
                    "statusCodes": [],
                    "description": "null",
                    "@id": "_:entry_point",
                    "@type": "hydra:Operation"
                }
            ],
            "subClassOf": "null",
            "description": "The main entry point or homepage of the API.",
            "@id": "vocab:EntryPoint",
            "label": "EntryPoint"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "required": "null",
                    "readonly": "false",
                    "hydra:description": "The cots",
                    "writeonly": "false",
                    "hydra:title": "members"
                }
            ],
            "@type": "hydra:Class",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems?format=jsonld",
                    "returns": "http://ontology.projectchronos.eu/subsystems?format=jsonld",
                    "method": "POST",
                    "label": "Creates a new Cots entity",
                    "statusCodes": [
                        {
                            "code": 201,
                            "description": "If the Cots entity was created successfully."
                        }
                    ],
                    "description": "null",
                    "@id": "_:cots_create",
                    "@type": "http://schema.org/AddAction"
                },
                {
                    "expects": "null",
                    "returns": "vocab:CotsCollection",
                    "method": "GET",
                    "label": "Retrieves all Cots entities",
                    "statusCodes": [],
                    "description": "null",
                    "@id": "_:cots_collection_retrieve",
                    "@type": "hydra:Operation"
                }
            ],
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "description": "A collection of cots",
            "@id": "vocab:CotsCollection",
            "label": "CotsCollection"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "cubicMillimeters",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "returns": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "statusCodes": [],
                    "label": "Creates a new cubicMillimeters entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:cubicMillimeters_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "returns": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the cubicMillimeters entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing cubicMillimeters entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:cubicMillimeters_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a cubicMillimeters entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:cubicMillimeters_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the cubicMillimeters entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a cubicMillimeters entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:cubicMillimeters_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "unit of measure for volume",
            "@id": "http://ontology.projectchronos.eu/subsystems/cubicMillimeters",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/objective",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/isComponentOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVoltage",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Detector",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Detector entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Detector_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Detector entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Detector entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Detector_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Detector entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Detector_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Detector entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Detector entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Detector_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "A space detector is a sensor supported by another device that let it collect data, that is deployed into a spacecraft and works outside Earth lower atmosphere",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/typeOfPropellant",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Propulsion.",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Propulsion. entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Propulsion._create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Propulsion. entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Propulsion. entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Propulsion._replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Propulsion. entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Propulsion._delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Propulsion. entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Propulsion. entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Propulsion._retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Complex devices-subsystems used for impelling (processes of applying a force which results in translational motion) a spacecraft, in the specific http://umbel.org/umbel/rc/ProjectilePropelling",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Propulsion",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasEfficiency",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVoltage",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_PrimaryPower.",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_PrimaryPower. entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_PrimaryPower._create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_PrimaryPower. entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_PrimaryPower. entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_PrimaryPower._replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_PrimaryPower. entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_PrimaryPower._delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_PrimaryPower. entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_PrimaryPower. entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_PrimaryPower._retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Complex devices-subsystems used for collecting energy.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_PrimaryPower",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_BackupPower",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_BackupPower entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_BackupPower_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_BackupPower entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_BackupPower entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_BackupPower_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_BackupPower entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_BackupPower_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_BackupPower entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_BackupPower entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_BackupPower_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Complex devices-subsystems used for storing energy.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_BackupPower",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Thermal",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Thermal entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Thermal entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Thermal entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Thermal entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Shields, shells or any device insulation from/reflecting radiation exploiting emission and absorption events",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Thermal_PassiveDevice",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Thermal_PassiveDevice entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_PassiveDevice entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Thermal_PassiveDevice entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Thermal_PassiveDevice entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_PassiveDevice entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Thermal_PassiveDevice entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_PassiveDevice_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "They are passive because they mostly transform radiation into heating/cooling ",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_PassiveDevice",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Thermal_ActiveDevice",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Thermal_ActiveDevice entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_ActiveDevice entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Thermal_ActiveDevice entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Thermal_ActiveDevice entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Thermal_ActiveDevice entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Thermal_ActiveDevice entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Thermal_ActiveDevice_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Complex devices-subsystems used to protect sensors or electronic devices from over/under-heating, like refrigeration absorption.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Thermal_ActiveDevice",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/standsMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Structure",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Structure entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Structure_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Structure entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Structure entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Structure_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Structure entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Structure_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Structure entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Structure entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Structure_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "It's the skeleton and framework of the spacecraft.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Structure",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVoltage",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxClock",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinClock",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasDataStorage",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasDataStorageExternal",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasRAM",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_CDH",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_CDH entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_CDH_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_CDH entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_CDH entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_CDH_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_CDH entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_CDH_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_CDH entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_CDH entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_CDH_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "The DH system shall: Enable HK and science data flow \u2013 Housekeeping data (Temperatures, Pressures, Voltages, Currents, Status,...) \u2013 Attitude data \u2013 Payload data (e.g., Science data) - Receive and distribute commands - Perform TM and TC protocols - Distribute timing signals - Synchronization of data \u2013 Time stamping of data - Provide data storage - Execute commands and schedules - Control subsystems and payloads - Monitor spacecraft health - Make autonomous decisions - Perform data compression.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_CDH",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/spacecraft/isSubsystemOf",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_Communication",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_Communication entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_Communication_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Communication entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_Communication entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_Communication_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_Communication entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_Communication_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_Communication entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_Communication entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_Communication_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Complex devices-subsystems used for transmitting/receiving radio waves.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Communication",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/function",
                    "title": "function",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "The function and the objective what the device performs or make possible",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/subSystemType",
                    "title": "subSystemType",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the subsystem to the kind of the devices it holds.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/isStandard",
                    "title": "isStandard",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "A property that references the standard platform for which the subsystem has been designed.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasVolume",
                    "title": "hasVolume",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMinAmpere",
                    "title": "hasMinAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMaxAmpere",
                    "title": "hasMaxAmpere",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMass",
                    "title": "hasMass",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/minWorkingTemperature",
                    "title": "minWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/maxWorkingTemperature",
                    "title": "maxWorkingTemperature",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasPower",
                    "title": "hasPower",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasSpecificImpulse",
                    "title": "hasSpecificImpulse",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasMonetaryValue",
                    "title": "hasMonetaryValue",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "Amount of money it can be bought for, or an esteem of value.",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "title": "hasWireInWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device receive input from another device",
                    "@type": "SupportedProperty"
                },
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireOutWith",
                    "title": "hasWireOutWith",
                    "required": "false",
                    "readonly": "false",
                    "writeonly": "false",
                    "description": "This device send output to another device",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsytems/function",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/standsMaxTemperature",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_AODCS",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_AODCS entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_AODCS entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_AODCS entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_AODCS entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Complex devices-subsystems used to set the direction and the position of the spacecraft, it controls flight dynamics.",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_AODCS_Active",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_AODCS_Active entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_Active_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_Active entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_AODCS_Active entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_Active_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_AODCS_Active entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_Active_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_Active entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_AODCS_Active entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_Active_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "Do NOT use any additional power from the spacecraft generator",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_ActiveDevice",
            "@type": "Class"
        },
        {
            "supportedProperty": [
                {
                    "property": "http://ontology.projectchronos.eu/subsystems/manufacturer",
                    "title": "manufacturer",
                    "readonly": "false",
                    "required": "false",
                    "writeonly": "false",
                    "@type": "SupportedProperty"
                },
                {
                    "required": "false",
                    "property": "http://ontology.projectchronos.eu/subsystems/hasWireInWith",
                    "writeonly": "false",
                    "readonly": "false",
                    "@type": "SupportedProperty"
                }
            ],
            "title": "Spacecraft_AODCS_PassiveDevice",
            "supportedOperation": [
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "statusCodes": [],
                    "label": "Creates a new Spacecraft_AODCS_PassiveDevice entity",
                    "method": "POST",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_create",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_PassiveDevice entity wasn't found."
                        }
                    ],
                    "label": "Replaces an existing Spacecraft_AODCS_PassiveDevice entity",
                    "method": "PUT",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_replace",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "null",
                    "statusCodes": [],
                    "label": "Deletes a Spacecraft_AODCS_PassiveDevice entity",
                    "method": "DELETE",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_delete",
                    "@type": "hydraspec:Operation"
                },
                {
                    "expects": "null",
                    "returns": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
                    "statusCodes": [
                        {
                            "code": 404,
                            "description": "If the Spacecraft_AODCS_PassiveDevice entity wasn't found."
                        }
                    ],
                    "label": "Retrieves a Spacecraft_AODCS_PassiveDevice entity",
                    "method": "GET",
                    "description": "null",
                    "@id": "_:Spacecraft_AODCS_PassiveDevice_retrieve",
                    "@type": "hydraspec:Operation"
                }
            ],
            "description": "DO use any additional power from the spacecraft generator",
            "@id": "http://ontology.projectchronos.eu/subsystems/Spacecraft_AODCS_PassiveDevice",
            "@type": "Class"
        }
    ],
    "@id": "http://hydrus.com//api/vocab",
    "@type": "ApiDocumentation",
    "@context": {
        "vocab": "http://hydrus.com//api/vocab#",
        "supportedProperty": "hydra:supportedProperty",
        "method": "hydra:method",
        "supportedClass": "hydra:supportedClass",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "code": "hydra:statusCode",
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "statusCodes": "hydra:statusCodes",
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "readonly": "hydra:readonly",
        "writeonly": "hydra:writeonly",
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "supportedOperation": "hydra:supportedOperation",
        "owl": "http://www.w3.org/2002/07/owl#",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "label": "rdfs:label",
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "rdfs:comment",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    }
}
