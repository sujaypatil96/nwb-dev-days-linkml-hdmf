# Auto generated from dynamic_enums.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-25T11:51:46
# Schema: nwb_dynamic_enums
#
# id: https://w3id.org/linkml/examples/nwb_dynamic_enums
# description: this schema demonstrates the use of dynamic enums
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/cl.owl')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://w3id.org/linkml/examples/nwb_dynamic_enums/')


# Types

# Class references



@dataclass
class BrainSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/nwb_dynamic_enums/BrainSample"]
    class_class_curie: ClassVar[str] = "linkml:examples/nwb_dynamic_enums/BrainSample"
    class_name: ClassVar[str] = "BrainSample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/nwb_dynamic_enums/BrainSample")

    cell_type: Union[str, "NeuronOrGlialCellTypeEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_type):
            self.MissingRequiredField("cell_type")
        if not isinstance(self.cell_type, NeuronOrGlialCellTypeEnum):
            self.cell_type = NeuronOrGlialCellTypeEnum(self.cell_type)

        super().__post_init__(**kwargs)


# Enumerations
class NeuronTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NeuronTypeEnum",
    )

class GlialCellTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GlialCellTypeEnum",
    )

class NeuronOrGlialCellTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NeuronOrGlialCellTypeEnum",
    )

# Slots
class slots:
    pass

slots.cell_type = Slot(uri=DEFAULT_.cell_type, name="cell_type", curie=DEFAULT_.curie('cell_type'),
                   model_uri=DEFAULT_.cell_type, domain=None, range=Union[str, "NeuronOrGlialCellTypeEnum"])
