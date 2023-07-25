# Auto generated from static_enums.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-25T11:51:06
# Schema: nwb_static_enums
#
# id: https://w3id.org/linkml/examples/nwb_static_enums
# description: this schema demonstrates the use of static enums
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
DEFAULT_ = CurieNamespace('', 'https://w3id.org/linkml/examples/nwb_static_enums/')


# Types

# Class references



@dataclass
class BrainSample(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML["examples/nwb_static_enums/BrainSample"]
    class_class_curie: ClassVar[str] = "linkml:examples/nwb_static_enums/BrainSample"
    class_name: ClassVar[str] = "BrainSample"
    class_model_uri: ClassVar[URIRef] = URIRef("https://w3id.org/linkml/examples/nwb_static_enums/BrainSample")

    cell_type: Union[str, "NeuronOrGlialCellTypeEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_type):
            self.MissingRequiredField("cell_type")
        if not isinstance(self.cell_type, NeuronOrGlialCellTypeEnum):
            self.cell_type = NeuronOrGlialCellTypeEnum(self.cell_type)

        super().__post_init__(**kwargs)


# Enumerations
class NeuronOrGlialCellTypeEnum(EnumDefinitionImpl):
    """
    Enumeration to capture various cell types found in the brain.
    """
    PYRAMIDAL_NEURON = PermissibleValue(
        text="PYRAMIDAL_NEURON",
        description="Neurons with a pyramidal shaped cell body (soma) and two distinct dendritic trees.",
        meaning=CL["0000598"])
    INTERNEURON = PermissibleValue(
        text="INTERNEURON",
        description="Neurons whose axons (and dendrites) are limited to a single brain area.",
        meaning=CL["0000099"])
    MOTOR_NEURON = PermissibleValue(
        text="MOTOR_NEURON",
        description="""Neurons whose cell body is located in the motor cortex, brainstem or the spinal cord,  and whose axon (fiber) projects to the spinal cord or outside of the spinal cord to directly  or indirectly control effector organs, mainly muscles and glands.""",
        meaning=CL["0000100"])
    ASTROCYTE = PermissibleValue(
        text="ASTROCYTE",
        description="Characteristic star-shaped glial cells in the brain and spinal cord.",
        meaning=CL["0000127"])
    OLIGODENDROCYTE = PermissibleValue(
        text="OLIGODENDROCYTE",
        description="""Type of neuroglia whose main functions are to provide support and insulation to axons  within the central nervous system (CNS) of jawed vertebrates.""",
        meaning=CL["0000128"])
    MICROGLIAL_CELL = PermissibleValue(
        text="MICROGLIAL_CELL",
        description="""Microglia are the resident immune cells of the brain and constantly patrol the cerebral  microenvironment to respond to pathogens and damage.""",
        meaning=CL["0000129"])

    _defn = EnumDefinition(
        name="NeuronOrGlialCellTypeEnum",
        description="Enumeration to capture various cell types found in the brain.",
    )

# Slots
class slots:
    pass

slots.cell_type = Slot(uri=DEFAULT_.cell_type, name="cell_type", curie=DEFAULT_.curie('cell_type'),
                   model_uri=DEFAULT_.cell_type, domain=None, range=Union[str, "NeuronOrGlialCellTypeEnum"])
