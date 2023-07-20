# Auto generated from dynamic_enums_expanded.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-20T12:45:42
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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CL = CurieNamespace('cl', 'http://purl.obolibrary.org/obo/cl.owl')
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

    cell_type: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.cell_type):
            self.MissingRequiredField("cell_type")
        if not isinstance(self.cell_type, str):
            self.cell_type = str(self.cell_type)

        super().__post_init__(**kwargs)


# Enumerations
class NeuronTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NeuronTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CL:0000705",
            PermissibleValue(
                text="CL:0000705",
                description="R6 photoreceptor cell",
                meaning=CL["0000705"]))
        setattr(cls, "CL:4023108",
            PermissibleValue(
                text="CL:4023108",
                description="oxytocin-secreting magnocellular cell",
                meaning=CL["4023108"]))
        setattr(cls, "CL:0004240",
            PermissibleValue(
                text="CL:0004240",
                description="WF1 amacrine cell",
                meaning=CL["0004240"]))
        setattr(cls, "CL:0004242",
            PermissibleValue(
                text="CL:0004242",
                description="WF3-1 amacrine cell",
                meaning=CL["0004242"]))
        setattr(cls, "CL:1000380",
            PermissibleValue(
                text="CL:1000380",
                description="""type 1 vestibular sensory cell of epithelium of macula of saccule of membranous labyrinth""",
                meaning=CL["1000380"]))
        setattr(cls, "CL:4023128",
            PermissibleValue(
                text="CL:4023128",
                description="rostral periventricular region of the third ventricle KNDy neuron",
                meaning=CL["4023128"]))
        setattr(cls, "CL:0003020",
            PermissibleValue(
                text="CL:0003020",
                description="retinal ganglion cell C outer",
                meaning=CL["0003020"]))
        setattr(cls, "CL:4023094",
            PermissibleValue(
                text="CL:4023094",
                description="tufted pyramidal neuron",
                meaning=CL["4023094"]))
        setattr(cls, "CL:4023057",
            PermissibleValue(
                text="CL:4023057",
                description="cerebellar inhibitory GABAergic interneuron",
                meaning=CL["4023057"]))
        setattr(cls, "CL:2000049",
            PermissibleValue(
                text="CL:2000049",
                description="primary motor cortex pyramidal cell",
                meaning=CL["2000049"]))
        setattr(cls, "CL:0000119",
            PermissibleValue(
                text="CL:0000119",
                description="cerebellar Golgi cell",
                meaning=CL["0000119"]))
        setattr(cls, "CL:0004227",
            PermissibleValue(
                text="CL:0004227",
                description="flat bistratified amacrine cell",
                meaning=CL["0004227"]))
        setattr(cls, "CL:1000606",
            PermissibleValue(
                text="CL:1000606",
                description="kidney nerve cell",
                meaning=CL["1000606"]))
        setattr(cls, "CL:1001582",
            PermissibleValue(
                text="CL:1001582",
                description="lateral ventricle neuron",
                meaning=CL["1001582"]))
        setattr(cls, "CL:0000165",
            PermissibleValue(
                text="CL:0000165",
                description="neuroendocrine cell",
                meaning=CL["0000165"]))
        setattr(cls, "CL:0000555",
            PermissibleValue(
                text="CL:0000555",
                description="neuronal brush cell",
                meaning=CL["0000555"]))
        setattr(cls, "CL:0004231",
            PermissibleValue(
                text="CL:0004231",
                description="recurving diffuse amacrine cell",
                meaning=CL["0004231"]))
        setattr(cls, "CL:0000687",
            PermissibleValue(
                text="CL:0000687",
                description="R1 photoreceptor cell",
                meaning=CL["0000687"]))
        setattr(cls, "CL:0001031",
            PermissibleValue(
                text="CL:0001031",
                description="cerebellar granule cell",
                meaning=CL["0001031"]))
        setattr(cls, "CL:0003026",
            PermissibleValue(
                text="CL:0003026",
                description="retinal ganglion cell D1",
                meaning=CL["0003026"]))
        setattr(cls, "CL:4033035",
            PermissibleValue(
                text="CL:4033035",
                description="giant bipolar cell",
                meaning=CL["4033035"]))
        setattr(cls, "CL:4023009",
            PermissibleValue(
                text="CL:4023009",
                description="extratelencephalic-projecting glutamatergic cortical neuron",
                meaning=CL["4023009"]))
        setattr(cls, "CL:0010022",
            PermissibleValue(
                text="CL:0010022",
                description="cardiac neuron",
                meaning=CL["0010022"]))
        setattr(cls, "CL:0000287",
            PermissibleValue(
                text="CL:0000287",
                description="eye photoreceptor cell",
                meaning=CL["0000287"]))
        setattr(cls, "CL:0000488",
            PermissibleValue(
                text="CL:0000488",
                description="visible light photoreceptor cell",
                meaning=CL["0000488"]))
        setattr(cls, "CL:0003046",
            PermissibleValue(
                text="CL:0003046",
                description="M13 retinal ganglion cell",
                meaning=CL["0003046"]))
        setattr(cls, "CL:4023169",
            PermissibleValue(
                text="CL:4023169",
                description="trigeminal neuron",
                meaning=CL["4023169"]))
        setattr(cls, "CL:0005007",
            PermissibleValue(
                text="CL:0005007",
                description="Kolmer-Agduhr neuron",
                meaning=CL["0005007"]))
        setattr(cls, "CL:0005008",
            PermissibleValue(
                text="CL:0005008",
                description="macular hair cell",
                meaning=CL["0005008"]))
        setattr(cls, "CL:4023027",
            PermissibleValue(
                text="CL:4023027",
                description="L5 T-Martinotti sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023027"]))
        setattr(cls, "CL:4033032",
            PermissibleValue(
                text="CL:4033032",
                description="diffuse bipolar 6 cell",
                meaning=CL["4033032"]))
        setattr(cls, "CL:0008021",
            PermissibleValue(
                text="CL:0008021",
                description="anterior lateral line ganglion neuron",
                meaning=CL["0008021"]))
        setattr(cls, "CL:4023028",
            PermissibleValue(
                text="CL:4023028",
                description="L5 non-Martinotti sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023028"]))
        setattr(cls, "CL:4023063",
            PermissibleValue(
                text="CL:4023063",
                description="medial ganglionic eminence derived interneuron",
                meaning=CL["4023063"]))
        setattr(cls, "CL:4023032",
            PermissibleValue(
                text="CL:4023032",
                description="ON retinal ganglion cell",
                meaning=CL["4023032"]))
        setattr(cls, "CL:0003039",
            PermissibleValue(
                text="CL:0003039",
                description="M8 retinal ganglion cell",
                meaning=CL["0003039"]))
        setattr(cls, "CL:0000757",
            PermissibleValue(
                text="CL:0000757",
                description="type 5 cone bipolar cell (sensu Mus)",
                meaning=CL["0000757"]))
        setattr(cls, "CL:0000609",
            PermissibleValue(
                text="CL:0000609",
                description="vestibular hair cell",
                meaning=CL["0000609"]))
        setattr(cls, "CL:0004219",
            PermissibleValue(
                text="CL:0004219",
                description="A2 amacrine cell",
                meaning=CL["0004219"]))
        setattr(cls, "CL:4030028",
            PermissibleValue(
                text="CL:4030028",
                description="glycinergic amacrine cell",
                meaning=CL["4030028"]))
        setattr(cls, "CL:0002450",
            PermissibleValue(
                text="CL:0002450",
                description="tether cell",
                meaning=CL["0002450"]))
        setattr(cls, "CL:0002374",
            PermissibleValue(
                text="CL:0002374",
                description="ear hair cell",
                meaning=CL["0002374"]))
        setattr(cls, "CL:0004124",
            PermissibleValue(
                text="CL:0004124",
                description="retinal ganglion cell C1",
                meaning=CL["0004124"]))
        setattr(cls, "CL:0004115",
            PermissibleValue(
                text="CL:0004115",
                description="retinal ganglion cell B",
                meaning=CL["0004115"]))
        setattr(cls, "CL:1000384",
            PermissibleValue(
                text="CL:1000384",
                description="""type 2 vestibular sensory cell of epithelium of macula of saccule of membranous labyrinth""",
                meaning=CL["1000384"]))
        setattr(cls, "CL:2000037",
            PermissibleValue(
                text="CL:2000037",
                description="posterior lateral line neuromast hair cell",
                meaning=CL["2000037"]))
        setattr(cls, "CL:0000673",
            PermissibleValue(
                text="CL:0000673",
                description="Kenyon cell",
                meaning=CL["0000673"]))
        setattr(cls, "CL:4023052",
            PermissibleValue(
                text="CL:4023052",
                description="Betz upper motor neuron",
                meaning=CL["4023052"]))
        setattr(cls, "CL:0004243",
            PermissibleValue(
                text="CL:0004243",
                description="WF3-2 amacrine cell",
                meaning=CL["0004243"]))
        setattr(cls, "CL:1000222",
            PermissibleValue(
                text="CL:1000222",
                description="stomach neuroendocrine cell",
                meaning=CL["1000222"]))
        setattr(cls, "CL:0002310",
            PermissibleValue(
                text="CL:0002310",
                description="mammosomatotroph",
                meaning=CL["0002310"]))
        setattr(cls, "CL:4023066",
            PermissibleValue(
                text="CL:4023066",
                description="horizontal pyramidal neuron",
                meaning=CL["4023066"]))
        setattr(cls, "CL:0000379",
            PermissibleValue(
                text="CL:0000379",
                description="sensory processing neuron",
                meaning=CL["0000379"]))
        setattr(cls, "CL:0011006",
            PermissibleValue(
                text="CL:0011006",
                description="Lugaro cell",
                meaning=CL["0011006"]))
        setattr(cls, "CL:0004216",
            PermissibleValue(
                text="CL:0004216",
                description="type 5b cone bipolar cell",
                meaning=CL["0004216"]))
        setattr(cls, "CL:0004126",
            PermissibleValue(
                text="CL:0004126",
                description="retinal ganglion cell C2 outer",
                meaning=CL["0004126"]))
        setattr(cls, "CL:0000108",
            PermissibleValue(
                text="CL:0000108",
                description="cholinergic neuron",
                meaning=CL["0000108"]))
        setattr(cls, "CL:0011103",
            PermissibleValue(
                text="CL:0011103",
                description="sympathetic neuron",
                meaning=CL["0011103"]))
        setattr(cls, "CL:4023107",
            PermissibleValue(
                text="CL:4023107",
                description="reticulospinal neuron",
                meaning=CL["4023107"]))
        setattr(cls, "CL:4023002",
            PermissibleValue(
                text="CL:4023002",
                description="dynamic beta motor neuron",
                meaning=CL["4023002"]))
        setattr(cls, "CL:4030048",
            PermissibleValue(
                text="CL:4030048",
                description="striosomal D1 medium spiny neuron",
                meaning=CL["4030048"]))
        setattr(cls, "CL:4023163",
            PermissibleValue(
                text="CL:4023163",
                description="spherical bushy cell",
                meaning=CL["4023163"]))
        setattr(cls, "CL:4023061",
            PermissibleValue(
                text="CL:4023061",
                description="hippocampal CA4 neuron",
                meaning=CL["4023061"]))
        setattr(cls, "CL:0000532",
            PermissibleValue(
                text="CL:0000532",
                description="CAP motoneuron",
                meaning=CL["0000532"]))
        setattr(cls, "CL:0000526",
            PermissibleValue(
                text="CL:0000526",
                description="afferent neuron",
                meaning=CL["0000526"]))
        setattr(cls, "CL:0003003",
            PermissibleValue(
                text="CL:0003003",
                description="G2 retinal ganglion cell",
                meaning=CL["0003003"]))
        setattr(cls, "CL:0000530",
            PermissibleValue(
                text="CL:0000530",
                description="primary neuron",
                meaning=CL["0000530"]))
        setattr(cls, "CL:4023045",
            PermissibleValue(
                text="CL:4023045",
                description="medulla-projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023045"]))
        setattr(cls, "CL:3000004",
            PermissibleValue(
                text="CL:3000004",
                description="peripheral sensory neuron",
                meaning=CL["3000004"]))
        setattr(cls, "CL:0000544",
            PermissibleValue(
                text="CL:0000544",
                description="slowly adapting mechanoreceptor cell",
                meaning=CL["0000544"]))
        setattr(cls, "CL:4030047",
            PermissibleValue(
                text="CL:4030047",
                description="matrix D2 medium spiny neuron",
                meaning=CL["4030047"]))
        setattr(cls, "CL:0004220",
            PermissibleValue(
                text="CL:0004220",
                description="flag amacrine cell",
                meaning=CL["0004220"]))
        setattr(cls, "CL:4023125",
            PermissibleValue(
                text="CL:4023125",
                description="KNDy neuron",
                meaning=CL["4023125"]))
        setattr(cls, "CL:0004228",
            PermissibleValue(
                text="CL:0004228",
                description="broad diffuse amacrine cell",
                meaning=CL["0004228"]))
        setattr(cls, "CL:4023122",
            PermissibleValue(
                text="CL:4023122",
                description="oxytocin receptor sst GABAergic cortical interneuron",
                meaning=CL["4023122"]))
        setattr(cls, "CL:1000379",
            PermissibleValue(
                text="CL:1000379",
                description="""type 1 vestibular sensory cell of epithelium of macula of utricle of membranous labyrinth""",
                meaning=CL["1000379"]))
        setattr(cls, "CL:0011111",
            PermissibleValue(
                text="CL:0011111",
                description="gonadotropin-releasing hormone neuron",
                meaning=CL["0011111"]))
        setattr(cls, "CL:0003042",
            PermissibleValue(
                text="CL:0003042",
                description="M9-OFF retinal ganglion cell",
                meaning=CL["0003042"]))
        setattr(cls, "CL:0003030",
            PermissibleValue(
                text="CL:0003030",
                description="M3 retinal ganglion cell",
                meaning=CL["0003030"]))
        setattr(cls, "CL:0003011",
            PermissibleValue(
                text="CL:0003011",
                description="G8 retinal ganglion cell",
                meaning=CL["0003011"]))
        setattr(cls, "CL:0000202",
            PermissibleValue(
                text="CL:0000202",
                description="auditory hair cell",
                meaning=CL["0000202"]))
        setattr(cls, "CL:0002271",
            PermissibleValue(
                text="CL:0002271",
                description="type EC1 enteroendocrine cell",
                meaning=CL["0002271"]))
        setattr(cls, "CL:4023013",
            PermissibleValue(
                text="CL:4023013",
                description="corticothalamic-projecting glutamatergic cortical neuron",
                meaning=CL["4023013"]))
        setattr(cls, "CL:4023114",
            PermissibleValue(
                text="CL:4023114",
                description="calyx vestibular afferent neuron",
                meaning=CL["4023114"]))
        setattr(cls, "CL:0003045",
            PermissibleValue(
                text="CL:0003045",
                description="M12 retinal ganglion cell",
                meaning=CL["0003045"]))
        setattr(cls, "CL:0002487",
            PermissibleValue(
                text="CL:0002487",
                description="cutaneous/subcutaneous mechanoreceptor cell",
                meaning=CL["0002487"]))
        setattr(cls, "CL:4030053",
            PermissibleValue(
                text="CL:4030053",
                description="Island of Calleja granule cell",
                meaning=CL["4030053"]))
        setattr(cls, "CL:0000490",
            PermissibleValue(
                text="CL:0000490",
                description="photopic photoreceptor cell",
                meaning=CL["0000490"]))
        setattr(cls, "CL:2000023",
            PermissibleValue(
                text="CL:2000023",
                description="spinal cord ventral column interneuron",
                meaning=CL["2000023"]))
        setattr(cls, "CL:1000381",
            PermissibleValue(
                text="CL:1000381",
                description="""type 1 vestibular sensory cell of epithelium of crista of ampulla of semicircular duct of membranous labyrinth""",
                meaning=CL["1000381"]))
        setattr(cls, "CL:0003013",
            PermissibleValue(
                text="CL:0003013",
                description="G10 retinal ganglion cell",
                meaning=CL["0003013"]))
        setattr(cls, "CL:0000602",
            PermissibleValue(
                text="CL:0000602",
                description="pressoreceptor cell",
                meaning=CL["0000602"]))
        setattr(cls, "CL:4023039",
            PermissibleValue(
                text="CL:4023039",
                description="amygdala excitatory neuron",
                meaning=CL["4023039"]))
        setattr(cls, "CL:4030043",
            PermissibleValue(
                text="CL:4030043",
                description="matrix D1 medium spiny neuron",
                meaning=CL["4030043"]))
        setattr(cls, "CL:0000105",
            PermissibleValue(
                text="CL:0000105",
                description="pseudounipolar neuron",
                meaning=CL["0000105"]))
        setattr(cls, "CL:0004137",
            PermissibleValue(
                text="CL:0004137",
                description="retinal ganglion cell A2 inner",
                meaning=CL["0004137"]))
        setattr(cls, "CL:1001436",
            PermissibleValue(
                text="CL:1001436",
                description="hair-tylotrich neuron",
                meaning=CL["1001436"]))
        setattr(cls, "CL:1001503",
            PermissibleValue(
                text="CL:1001503",
                description="olfactory bulb tufted cell",
                meaning=CL["1001503"]))
        setattr(cls, "CL:0000406",
            PermissibleValue(
                text="CL:0000406",
                description="CNS short range interneuron",
                meaning=CL["0000406"]))
        setattr(cls, "CL:2000087",
            PermissibleValue(
                text="CL:2000087",
                description="dentate gyrus of hippocampal formation basket cell",
                meaning=CL["2000087"]))
        setattr(cls, "CL:0000534",
            PermissibleValue(
                text="CL:0000534",
                description="primary interneuron",
                meaning=CL["0000534"]))
        setattr(cls, "CL:0000246",
            PermissibleValue(
                text="CL:0000246",
                description="Mauthner neuron",
                meaning=CL["0000246"]))
        setattr(cls, "CL:0003027",
            PermissibleValue(
                text="CL:0003027",
                description="retinal ganglion cell D2",
                meaning=CL["0003027"]))
        setattr(cls, "CL:0000752",
            PermissibleValue(
                text="CL:0000752",
                description="cone retinal bipolar cell",
                meaning=CL["0000752"]))
        setattr(cls, "CL:0000410",
            PermissibleValue(
                text="CL:0000410",
                description="CNS long range interneuron",
                meaning=CL["0000410"]))
        setattr(cls, "CL:0009000",
            PermissibleValue(
                text="CL:0009000",
                description="sensory neuron of spinal nerve",
                meaning=CL["0009000"]))
        setattr(cls, "CL:0000754",
            PermissibleValue(
                text="CL:0000754",
                description="type 2 cone bipolar cell (sensu Mus)",
                meaning=CL["0000754"]))
        setattr(cls, "CL:0002309",
            PermissibleValue(
                text="CL:0002309",
                description="corticotroph",
                meaning=CL["0002309"]))
        setattr(cls, "CL:0010009",
            PermissibleValue(
                text="CL:0010009",
                description="camera-type eye photoreceptor cell",
                meaning=CL["0010009"]))
        setattr(cls, "CL:4023069",
            PermissibleValue(
                text="CL:4023069",
                description="medial ganglionic eminence derived GABAergic cortical interneuron",
                meaning=CL["4023069"]))
        setattr(cls, "CL:0000102",
            PermissibleValue(
                text="CL:0000102",
                description="polymodal neuron",
                meaning=CL["0000102"]))
        setattr(cls, "CL:0000694",
            PermissibleValue(
                text="CL:0000694",
                description="R3 photoreceptor cell",
                meaning=CL["0000694"]))
        setattr(cls, "CL:0004183",
            PermissibleValue(
                text="CL:0004183",
                description="retinal ganglion cell B3",
                meaning=CL["0004183"]))
        setattr(cls, "CL:0000693",
            PermissibleValue(
                text="CL:0000693",
                description="neurogliaform cell",
                meaning=CL["0000693"]))
        setattr(cls, "CL:0000760",
            PermissibleValue(
                text="CL:0000760",
                description="type 8 cone bipolar cell (sensu Mus)",
                meaning=CL["0000760"]))
        setattr(cls, "CL:4023001",
            PermissibleValue(
                text="CL:4023001",
                description="static beta motor neuron",
                meaning=CL["4023001"]))
        setattr(cls, "CL:1000424",
            PermissibleValue(
                text="CL:1000424",
                description="chromaffin cell of paraaortic body",
                meaning=CL["1000424"]))
        setattr(cls, "CL:0000120",
            PermissibleValue(
                text="CL:0000120",
                description="granule cell",
                meaning=CL["0000120"]))
        setattr(cls, "CL:0002312",
            PermissibleValue(
                text="CL:0002312",
                description="somatotroph",
                meaning=CL["0002312"]))
        setattr(cls, "CL:0000107",
            PermissibleValue(
                text="CL:0000107",
                description="autonomic neuron",
                meaning=CL["0000107"]))
        setattr(cls, "CL:2000047",
            PermissibleValue(
                text="CL:2000047",
                description="brainstem motor neuron",
                meaning=CL["2000047"]))
        setattr(cls, "CL:4023080",
            PermissibleValue(
                text="CL:4023080",
                description="""stellate L6 intratelencephalic projecting glutamatergic neuron of the primary motor cortex (Mmus)""",
                meaning=CL["4023080"]))
        setattr(cls, "CL:0000848",
            PermissibleValue(
                text="CL:0000848",
                description="microvillous olfactory receptor neuron",
                meaning=CL["0000848"]))
        setattr(cls, "CL:0004213",
            PermissibleValue(
                text="CL:0004213",
                description="type 3a cone bipolar cell",
                meaning=CL["0004213"]))
        setattr(cls, "CL:0000116",
            PermissibleValue(
                text="CL:0000116",
                description="pioneer neuron",
                meaning=CL["0000116"]))
        setattr(cls, "CL:4023187",
            PermissibleValue(
                text="CL:4023187",
                description="koniocellular cell",
                meaning=CL["4023187"]))
        setattr(cls, "CL:4023116",
            PermissibleValue(
                text="CL:4023116",
                description="type 2 spiral ganglion neuron",
                meaning=CL["4023116"]))
        setattr(cls, "CL:0008015",
            PermissibleValue(
                text="CL:0008015",
                description="inhibitory motor neuron",
                meaning=CL["0008015"]))
        setattr(cls, "CL:0003048",
            PermissibleValue(
                text="CL:0003048",
                description="L cone cell",
                meaning=CL["0003048"]))
        setattr(cls, "CL:1000082",
            PermissibleValue(
                text="CL:1000082",
                description="stretch receptor cell",
                meaning=CL["1000082"]))
        setattr(cls, "CL:0003031",
            PermissibleValue(
                text="CL:0003031",
                description="M3-ON retinal ganglion cell",
                meaning=CL["0003031"]))
        setattr(cls, "CL:1001474",
            PermissibleValue(
                text="CL:1001474",
                description="medium spiny neuron",
                meaning=CL["1001474"]))
        setattr(cls, "CL:0000745",
            PermissibleValue(
                text="CL:0000745",
                description="retina horizontal cell",
                meaning=CL["0000745"]))
        setattr(cls, "CL:0002515",
            PermissibleValue(
                text="CL:0002515",
                description="interrenal norepinephrine type cell",
                meaning=CL["0002515"]))
        setattr(cls, "CL:2000027",
            PermissibleValue(
                text="CL:2000027",
                description="cerebellum basket cell",
                meaning=CL["2000027"]))
        setattr(cls, "CL:0004225",
            PermissibleValue(
                text="CL:0004225",
                description="spider amacrine cell",
                meaning=CL["0004225"]))
        setattr(cls, "CL:4023031",
            PermissibleValue(
                text="CL:4023031",
                description="L4 sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023031"]))
        setattr(cls, "CL:0008038",
            PermissibleValue(
                text="CL:0008038",
                description="alpha motor neuron",
                meaning=CL["0008038"]))
        setattr(cls, "CL:4033030",
            PermissibleValue(
                text="CL:4033030",
                description="diffuse bipolar 3b cell",
                meaning=CL["4033030"]))
        setattr(cls, "CL:0000336",
            PermissibleValue(
                text="CL:0000336",
                description="adrenal medulla chromaffin cell",
                meaning=CL["0000336"]))
        setattr(cls, "CL:0000751",
            PermissibleValue(
                text="CL:0000751",
                description="rod bipolar cell",
                meaning=CL["0000751"]))
        setattr(cls, "CL:0008037",
            PermissibleValue(
                text="CL:0008037",
                description="gamma motor neuron",
                meaning=CL["0008037"]))
        setattr(cls, "CL:0003028",
            PermissibleValue(
                text="CL:0003028",
                description="M1 retinal ganglion cell",
                meaning=CL["0003028"]))
        setattr(cls, "CL:0003016",
            PermissibleValue(
                text="CL:0003016",
                description="G11-OFF retinal ganglion cell",
                meaning=CL["0003016"]))
        setattr(cls, "CL:0004239",
            PermissibleValue(
                text="CL:0004239",
                description="wavy bistratified amacrine cell",
                meaning=CL["0004239"]))
        setattr(cls, "CL:4023168",
            PermissibleValue(
                text="CL:4023168",
                description="somatosensory neuron",
                meaning=CL["4023168"]))
        setattr(cls, "CL:4023018",
            PermissibleValue(
                text="CL:4023018",
                description="pvalb GABAergic cortical interneuron",
                meaning=CL["4023018"]))
        setattr(cls, "CL:0004138",
            PermissibleValue(
                text="CL:0004138",
                description="retinal ganglion cell A2",
                meaning=CL["0004138"]))
        setattr(cls, "CL:0000750",
            PermissibleValue(
                text="CL:0000750",
                description="OFF-bipolar cell",
                meaning=CL["0000750"]))
        setattr(cls, "CL:0000709",
            PermissibleValue(
                text="CL:0000709",
                description="R8 photoreceptor cell",
                meaning=CL["0000709"]))
        setattr(cls, "CL:0004214",
            PermissibleValue(
                text="CL:0004214",
                description="type 3b cone bipolar cell",
                meaning=CL["0004214"]))
        setattr(cls, "CL:0003047",
            PermissibleValue(
                text="CL:0003047",
                description="M14 retinal ganglion cell",
                meaning=CL["0003047"]))
        setattr(cls, "CL:0015000",
            PermissibleValue(
                text="CL:0015000",
                description="cranial motor neuron",
                meaning=CL["0015000"]))
        setattr(cls, "CL:0003036",
            PermissibleValue(
                text="CL:0003036",
                description="M7 retinal ganglion cell",
                meaning=CL["0003036"]))
        setattr(cls, "CL:0000397",
            PermissibleValue(
                text="CL:0000397",
                description="ganglion interneuron",
                meaning=CL["0000397"]))
        setattr(cls, "CL:1001509",
            PermissibleValue(
                text="CL:1001509",
                description="glycinergic neuron",
                meaning=CL["1001509"]))
        setattr(cls, "CL:4023038",
            PermissibleValue(
                text="CL:4023038",
                description="L6b glutamatergic cortical neuron",
                meaning=CL["4023038"]))
        setattr(cls, "CL:0000112",
            PermissibleValue(
                text="CL:0000112",
                description="columnar neuron",
                meaning=CL["0000112"]))
        setattr(cls, "CL:0002517",
            PermissibleValue(
                text="CL:0002517",
                description="interrenal epinephrin secreting cell",
                meaning=CL["0002517"]))
        setattr(cls, "CL:1000383",
            PermissibleValue(
                text="CL:1000383",
                description="""type 2 vestibular sensory cell of epithelium of macula of utricle of membranous labyrinth""",
                meaning=CL["1000383"]))
        setattr(cls, "CL:0004116",
            PermissibleValue(
                text="CL:0004116",
                description="retinal ganglion cell C",
                meaning=CL["0004116"]))
        setattr(cls, "CL:4023113",
            PermissibleValue(
                text="CL:4023113",
                description="bouton vestibular afferent neuron",
                meaning=CL["4023113"]))
        setattr(cls, "CL:0003034",
            PermissibleValue(
                text="CL:0003034",
                description="M5 retinal ganglion cell",
                meaning=CL["0003034"]))
        setattr(cls, "CL:0011005",
            PermissibleValue(
                text="CL:0011005",
                description="GABAergic interneuron",
                meaning=CL["0011005"]))
        setattr(cls, "CL:0011105",
            PermissibleValue(
                text="CL:0011105",
                description="dopamanergic interplexiform cell",
                meaning=CL["0011105"]))
        setattr(cls, "CL:0000749",
            PermissibleValue(
                text="CL:0000749",
                description="ON-bipolar cell",
                meaning=CL["0000749"]))
        setattr(cls, "CL:0000498",
            PermissibleValue(
                text="CL:0000498",
                description="inhibitory interneuron",
                meaning=CL["0000498"]))
        setattr(cls, "CL:4023071",
            PermissibleValue(
                text="CL:4023071",
                description="L5/6 cck cortical GABAergic interneuron (Mmus)",
                meaning=CL["4023071"]))
        setattr(cls, "CL:1000245",
            PermissibleValue(
                text="CL:1000245",
                description="posterior lateral line ganglion neuron",
                meaning=CL["1000245"]))
        setattr(cls, "CL:0004139",
            PermissibleValue(
                text="CL:0004139",
                description="retinal ganglion cell A2 outer",
                meaning=CL["0004139"]))
        setattr(cls, "CL:0000531",
            PermissibleValue(
                text="CL:0000531",
                description="primary sensory neuron",
                meaning=CL["0000531"]))
        setattr(cls, "CL:0004125",
            PermissibleValue(
                text="CL:0004125",
                description="retinal ganglion cell C2 inner",
                meaning=CL["0004125"]))
        setattr(cls, "CL:4023064",
            PermissibleValue(
                text="CL:4023064",
                description="caudal ganglionic eminence derived interneuron",
                meaning=CL["4023064"]))
        setattr(cls, "CL:4030049",
            PermissibleValue(
                text="CL:4030049",
                description="striosomal D2 medium spiny neuron",
                meaning=CL["4030049"]))
        setattr(cls, "CL:0017002",
            PermissibleValue(
                text="CL:0017002",
                description="prostate neuroendocrine cell",
                meaning=CL["0017002"]))
        setattr(cls, "CL:0000756",
            PermissibleValue(
                text="CL:0000756",
                description="type 4 cone bipolar cell (sensu Mus)",
                meaning=CL["0000756"]))
        setattr(cls, "CL:0000707",
            PermissibleValue(
                text="CL:0000707",
                description="R7 photoreceptor cell",
                meaning=CL["0000707"]))
        setattr(cls, "CL:0000700",
            PermissibleValue(
                text="CL:0000700",
                description="dopaminergic neuron",
                meaning=CL["0000700"]))
        setattr(cls, "CL:0003002",
            PermissibleValue(
                text="CL:0003002",
                description="G1 retinal ganglion cell",
                meaning=CL["0003002"]))
        setattr(cls, "CL:1000001",
            PermissibleValue(
                text="CL:1000001",
                description="retrotrapezoid nucleus neuron",
                meaning=CL["1000001"]))
        setattr(cls, "CL:4023007",
            PermissibleValue(
                text="CL:4023007",
                description="L2/3 bipolar vip GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023007"]))
        setattr(cls, "CL:0000528",
            PermissibleValue(
                text="CL:0000528",
                description="nitrergic neuron",
                meaning=CL["0000528"]))
        setattr(cls, "CL:0000639",
            PermissibleValue(
                text="CL:0000639",
                description="basophil cell of pars distalis of adenohypophysis",
                meaning=CL["0000639"]))
        setattr(cls, "CL:0000849",
            PermissibleValue(
                text="CL:0000849",
                description="crypt olfactory receptor neuron",
                meaning=CL["0000849"]))
        setattr(cls, "CL:0011110",
            PermissibleValue(
                text="CL:0011110",
                description="histaminergic neuron",
                meaning=CL["0011110"]))
        setattr(cls, "CL:0005025",
            PermissibleValue(
                text="CL:0005025",
                description="visceromotor neuron",
                meaning=CL["0005025"]))
        setattr(cls, "CL:0003001",
            PermissibleValue(
                text="CL:0003001",
                description="bistratified retinal ganglion cell",
                meaning=CL["0003001"]))
        setattr(cls, "CL:0004241",
            PermissibleValue(
                text="CL:0004241",
                description="WF2 amacrine cell",
                meaning=CL["0004241"]))
        setattr(cls, "CL:4023019",
            PermissibleValue(
                text="CL:4023019",
                description="L5/6 cck, vip cortical GABAergic interneuron (Mmus)",
                meaning=CL["4023019"]))
        setattr(cls, "CL:4023040",
            PermissibleValue(
                text="CL:4023040",
                description="L2/3-6 intratelencephalic projecting glutamatergic cortical neuron",
                meaning=CL["4023040"]))
        setattr(cls, "CL:1001435",
            PermissibleValue(
                text="CL:1001435",
                description="periglomerular cell",
                meaning=CL["1001435"]))
        setattr(cls, "CL:4023127",
            PermissibleValue(
                text="CL:4023127",
                description="arcuate nucleus of hypothalamus KNDy neuron",
                meaning=CL["4023127"]))
        setattr(cls, "CL:0003007",
            PermissibleValue(
                text="CL:0003007",
                description="G4-OFF retinal ganglion cell",
                meaning=CL["0003007"]))
        setattr(cls, "CL:0000101",
            PermissibleValue(
                text="CL:0000101",
                description="sensory neuron",
                meaning=CL["0000101"]))
        setattr(cls, "CL:2000097",
            PermissibleValue(
                text="CL:2000097",
                description="midbrain dopaminergic neuron",
                meaning=CL["2000097"]))
        setattr(cls, "CL:4023095",
            PermissibleValue(
                text="CL:4023095",
                description="untufted pyramidal neuron",
                meaning=CL["4023095"]))
        setattr(cls, "CL:0003004",
            PermissibleValue(
                text="CL:0003004",
                description="G3 retinal ganglion cell",
                meaning=CL["0003004"]))
        setattr(cls, "CL:0000527",
            PermissibleValue(
                text="CL:0000527",
                description="efferent neuron",
                meaning=CL["0000527"]))
        setattr(cls, "CL:1000382",
            PermissibleValue(
                text="CL:1000382",
                description="type 2 vestibular sensory cell of stato-acoustic epithelium",
                meaning=CL["1000382"]))
        setattr(cls, "CL:4033019",
            PermissibleValue(
                text="CL:4033019",
                description="ON-blue cone bipolar cell",
                meaning=CL["4033019"]))
        setattr(cls, "CL:0000589",
            PermissibleValue(
                text="CL:0000589",
                description="cochlear inner hair cell",
                meaning=CL["0000589"]))
        setattr(cls, "CL:4023160",
            PermissibleValue(
                text="CL:4023160",
                description="cartwheel cell",
                meaning=CL["4023160"]))
        setattr(cls, "CL:1001437",
            PermissibleValue(
                text="CL:1001437",
                description="hair-down neuron",
                meaning=CL["1001437"]))
        setattr(cls, "CL:0011102",
            PermissibleValue(
                text="CL:0011102",
                description="parasympathetic neuron",
                meaning=CL["0011102"]))
        setattr(cls, "CL:2000029",
            PermissibleValue(
                text="CL:2000029",
                description="central nervous system neuron",
                meaning=CL["2000029"]))
        setattr(cls, "CL:4023115",
            PermissibleValue(
                text="CL:4023115",
                description="type 1 spiral ganglion neuron",
                meaning=CL["4023115"]))
        setattr(cls, "CL:0002311",
            PermissibleValue(
                text="CL:0002311",
                description="mammotroph",
                meaning=CL["0002311"]))
        setattr(cls, "CL:0003025",
            PermissibleValue(
                text="CL:0003025",
                description="retinal ganglion cell C3",
                meaning=CL["0003025"]))
        setattr(cls, "CL:4030050",
            PermissibleValue(
                text="CL:4030050",
                description="D1/D2-hybrid medium spiny neuron",
                meaning=CL["4030050"]))
        setattr(cls, "CL:4023118",
            PermissibleValue(
                text="CL:4023118",
                description="L5/6 non-Martinotti sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023118"]))
        setattr(cls, "CL:4023110",
            PermissibleValue(
                text="CL:4023110",
                description="amygdala pyramidal neuron",
                meaning=CL["4023110"]))
        setattr(cls, "CL:0002273",
            PermissibleValue(
                text="CL:0002273",
                description="type ECL enteroendocrine cell",
                meaning=CL["0002273"]))
        setattr(cls, "CL:0003050",
            PermissibleValue(
                text="CL:0003050",
                description="S cone cell",
                meaning=CL["0003050"]))
        setattr(cls, "CL:4023121",
            PermissibleValue(
                text="CL:4023121",
                description="sst chodl GABAergic cortical interneuron",
                meaning=CL["4023121"]))
        setattr(cls, "CL:4023020",
            PermissibleValue(
                text="CL:4023020",
                description="dynamic gamma motor neuron",
                meaning=CL["4023020"]))
        setattr(cls, "CL:0004246",
            PermissibleValue(
                text="CL:0004246",
                description="monostratified cell",
                meaning=CL["0004246"]))
        setattr(cls, "CL:0000495",
            PermissibleValue(
                text="CL:0000495",
                description="blue sensitive photoreceptor cell",
                meaning=CL["0000495"]))
        setattr(cls, "CL:0000029",
            PermissibleValue(
                text="CL:0000029",
                description="neural crest derived neuron",
                meaning=CL["0000029"]))
        setattr(cls, "CL:0004001",
            PermissibleValue(
                text="CL:0004001",
                description="local interneuron",
                meaning=CL["0004001"]))
        setattr(cls, "CL:0000551",
            PermissibleValue(
                text="CL:0000551",
                description="unimodal nocireceptor",
                meaning=CL["0000551"]))
        setattr(cls, "CL:0003006",
            PermissibleValue(
                text="CL:0003006",
                description="G4-ON retinal ganglion cell",
                meaning=CL["0003006"]))
        setattr(cls, "CL:4023011",
            PermissibleValue(
                text="CL:4023011",
                description="lamp5 GABAergic cortical interneuron",
                meaning=CL["4023011"]))
        setattr(cls, "CL:4023109",
            PermissibleValue(
                text="CL:4023109",
                description="vasopressin-secreting magnocellular cell",
                meaning=CL["4023109"]))
        setattr(cls, "CL:0000121",
            PermissibleValue(
                text="CL:0000121",
                description="Purkinje cell",
                meaning=CL["0000121"]))
        setattr(cls, "CL:0000678",
            PermissibleValue(
                text="CL:0000678",
                description="commissural neuron",
                meaning=CL["0000678"]))
        setattr(cls, "CL:0004252",
            PermissibleValue(
                text="CL:0004252",
                description="medium field retinal amacrine cell",
                meaning=CL["0004252"]))
        setattr(cls, "CL:0000103",
            PermissibleValue(
                text="CL:0000103",
                description="bipolar neuron",
                meaning=CL["0000103"]))
        setattr(cls, "CL:4033036",
            PermissibleValue(
                text="CL:4033036",
                description="OFFx cell",
                meaning=CL["4033036"]))
        setattr(cls, "CL:4023014",
            PermissibleValue(
                text="CL:4023014",
                description="L5 vip cortical GABAergic interneuron (Mmus)",
                meaning=CL["4023014"]))
        setattr(cls, "CL:0008031",
            PermissibleValue(
                text="CL:0008031",
                description="cortical interneuron",
                meaning=CL["0008031"]))
        setattr(cls, "CL:0008010",
            PermissibleValue(
                text="CL:0008010",
                description="cranial somatomotor neuron",
                meaning=CL["0008010"]))
        setattr(cls, "CL:0000637",
            PermissibleValue(
                text="CL:0000637",
                description="chromophil cell of anterior pituitary gland",
                meaning=CL["0000637"]))
        setattr(cls, "CL:0003014",
            PermissibleValue(
                text="CL:0003014",
                description="G11 retinal ganglion cell",
                meaning=CL["0003014"]))
        setattr(cls, "CL:4033029",
            PermissibleValue(
                text="CL:4033029",
                description="diffuse bipolar 3a cell",
                meaning=CL["4033029"]))
        setattr(cls, "CL:0002611",
            PermissibleValue(
                text="CL:0002611",
                description="neuron of the dorsal spinal cord",
                meaning=CL["0002611"]))
        setattr(cls, "CL:0010010",
            PermissibleValue(
                text="CL:0010010",
                description="cerebellar stellate cell",
                meaning=CL["0010010"]))
        setattr(cls, "CL:1000465",
            PermissibleValue(
                text="CL:1000465",
                description="chromaffin cell of ovary",
                meaning=CL["1000465"]))
        setattr(cls, "CL:0000761",
            PermissibleValue(
                text="CL:0000761",
                description="type 9 cone bipolar cell (sensu Mus)",
                meaning=CL["0000761"]))
        setattr(cls, "CL:0004226",
            PermissibleValue(
                text="CL:0004226",
                description="monostratified amacrine cell",
                meaning=CL["0004226"]))
        setattr(cls, "CL:0004253",
            PermissibleValue(
                text="CL:0004253",
                description="wide field retinal amacrine cell",
                meaning=CL["0004253"]))
        setattr(cls, "CL:4023075",
            PermissibleValue(
                text="CL:4023075",
                description="L6 tyrosine hydroxylase sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023075"]))
        setattr(cls, "CL:4023068",
            PermissibleValue(
                text="CL:4023068",
                description="thalamic excitatory neuron",
                meaning=CL["4023068"]))
        setattr(cls, "CL:1000377",
            PermissibleValue(
                text="CL:1000377",
                description="dense-core granulated cell of epithelium of trachea",
                meaning=CL["1000377"]))
        setattr(cls, "CL:4023089",
            PermissibleValue(
                text="CL:4023089",
                description="nest basket cell",
                meaning=CL["4023089"]))
        setattr(cls, "CL:4023189",
            PermissibleValue(
                text="CL:4023189",
                description="parasol ganglion cell of retina",
                meaning=CL["4023189"]))
        setattr(cls, "CL:0000856",
            PermissibleValue(
                text="CL:0000856",
                description="neuromast hair cell",
                meaning=CL["0000856"]))
        setattr(cls, "CL:4023025",
            PermissibleValue(
                text="CL:4023025",
                description="long-range projecting sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023025"]))
        setattr(cls, "CL:0003043",
            PermissibleValue(
                text="CL:0003043",
                description="M10 retinal ganglion cell",
                meaning=CL["0003043"]))
        setattr(cls, "CL:4023000",
            PermissibleValue(
                text="CL:4023000",
                description="beta motor neuron",
                meaning=CL["4023000"]))
        setattr(cls, "CL:4023048",
            PermissibleValue(
                text="CL:4023048",
                description="L4/5 intratelencephalic projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023048"]))
        setattr(cls, "CL:0000855",
            PermissibleValue(
                text="CL:0000855",
                description="sensory hair cell",
                meaning=CL["0000855"]))
        setattr(cls, "CL:4023070",
            PermissibleValue(
                text="CL:4023070",
                description="caudal ganglionic eminence derived GABAergic cortical interneuron",
                meaning=CL["4023070"]))
        setattr(cls, "CL:0002070",
            PermissibleValue(
                text="CL:0002070",
                description="type I vestibular sensory cell",
                meaning=CL["0002070"]))
        setattr(cls, "CL:2000028",
            PermissibleValue(
                text="CL:2000028",
                description="cerebellum glutamatergic neuron",
                meaning=CL["2000028"]))
        setattr(cls, "CL:0000533",
            PermissibleValue(
                text="CL:0000533",
                description="primary motor neuron",
                meaning=CL["0000533"]))
        setattr(cls, "CL:4023083",
            PermissibleValue(
                text="CL:4023083",
                description="chandelier cell",
                meaning=CL["4023083"]))
        setattr(cls, "CL:2000034",
            PermissibleValue(
                text="CL:2000034",
                description="anterior lateral line neuromast hair cell",
                meaning=CL["2000034"]))
        setattr(cls, "CL:0003015",
            PermissibleValue(
                text="CL:0003015",
                description="G11-ON retinal ganglion cell",
                meaning=CL["0003015"]))
        setattr(cls, "CL:0000204",
            PermissibleValue(
                text="CL:0000204",
                description="acceleration receptive cell",
                meaning=CL["0000204"]))
        setattr(cls, "CL:4033031",
            PermissibleValue(
                text="CL:4033031",
                description="diffuse bipolar 4 cell",
                meaning=CL["4033031"]))
        setattr(cls, "CL:0003024",
            PermissibleValue(
                text="CL:0003024",
                description="retinal ganglion cell C inner",
                meaning=CL["0003024"]))
        setattr(cls, "CL:4023074",
            PermissibleValue(
                text="CL:4023074",
                description="mammillary body neuron",
                meaning=CL["4023074"]))
        setattr(cls, "CL:2000089",
            PermissibleValue(
                text="CL:2000089",
                description="dentate gyrus of hippocampal formation granule cell",
                meaning=CL["2000089"]))
        setattr(cls, "CL:4033028",
            PermissibleValue(
                text="CL:4033028",
                description="diffuse bipolar 2 cell",
                meaning=CL["4033028"]))
        setattr(cls, "CL:0000110",
            PermissibleValue(
                text="CL:0000110",
                description="peptidergic neuron",
                meaning=CL["0000110"]))
        setattr(cls, "CL:4033002",
            PermissibleValue(
                text="CL:4033002",
                description="neuroendocrine cell of epithelium of crypt of Lieberkuhn",
                meaning=CL["4033002"]))
        setattr(cls, "CL:4033027",
            PermissibleValue(
                text="CL:4033027",
                description="diffuse bipolar 1 cell",
                meaning=CL["4033027"]))
        setattr(cls, "CL:3000003",
            PermissibleValue(
                text="CL:3000003",
                description="sympathetic cholinergic neuron",
                meaning=CL["3000003"]))
        setattr(cls, "CL:4023158",
            PermissibleValue(
                text="CL:4023158",
                description="octopus cell of the mammalian cochlear nucleus",
                meaning=CL["4023158"]))
        setattr(cls, "CL:0000118",
            PermissibleValue(
                text="CL:0000118",
                description="basket cell",
                meaning=CL["0000118"]))
        setattr(cls, "CL:0004223",
            PermissibleValue(
                text="CL:0004223",
                description="AB diffuse-1 amacrine cell",
                meaning=CL["0004223"]))
        setattr(cls, "CL:4030054",
            PermissibleValue(
                text="CL:4030054",
                description="RXFP1-positive interface island D1-medium spiny neuron",
                meaning=CL["4030054"]))
        setattr(cls, "CL:0002610",
            PermissibleValue(
                text="CL:0002610",
                description="raphe nuclei neuron",
                meaning=CL["0002610"]))
        setattr(cls, "CL:4023026",
            PermissibleValue(
                text="CL:4023026",
                description="direct pathway medium spiny neuron",
                meaning=CL["4023026"]))
        setattr(cls, "CL:4023016",
            PermissibleValue(
                text="CL:4023016",
                description="vip GABAergic cortical interneuron",
                meaning=CL["4023016"]))
        setattr(cls, "CL:0004237",
            PermissibleValue(
                text="CL:0004237",
                description="fountain amacrine cell",
                meaning=CL["0004237"]))
        setattr(cls, "CL:0003035",
            PermissibleValue(
                text="CL:0003035",
                description="M6 retinal ganglion cell",
                meaning=CL["0003035"]))
        setattr(cls, "CL:1001611",
            PermissibleValue(
                text="CL:1001611",
                description="cerebellar neuron",
                meaning=CL["1001611"]))
        setattr(cls, "CL:0000591",
            PermissibleValue(
                text="CL:0000591",
                description="warmth sensing thermoreceptor cell",
                meaning=CL["0000591"]))
        setattr(cls, "CL:0002613",
            PermissibleValue(
                text="CL:0002613",
                description="striatum neuron",
                meaning=CL["0002613"]))
        setattr(cls, "CL:0000496",
            PermissibleValue(
                text="CL:0000496",
                description="green sensitive photoreceptor cell",
                meaning=CL["0000496"]))
        setattr(cls, "CL:0007011",
            PermissibleValue(
                text="CL:0007011",
                description="enteric neuron",
                meaning=CL["0007011"]))
        setattr(cls, "CL:2000056",
            PermissibleValue(
                text="CL:2000056",
                description="Meynert cell",
                meaning=CL["2000056"]))
        setattr(cls, "CL:0003040",
            PermissibleValue(
                text="CL:0003040",
                description="M9 retinal ganglion cell",
                meaning=CL["0003040"]))
        setattr(cls, "CL:0004250",
            PermissibleValue(
                text="CL:0004250",
                description="bistratified retinal amacrine cell",
                meaning=CL["0004250"]))
        setattr(cls, "CL:0003029",
            PermissibleValue(
                text="CL:0003029",
                description="M2 retinal ganglion cell",
                meaning=CL["0003029"]))
        setattr(cls, "CL:4023017",
            PermissibleValue(
                text="CL:4023017",
                description="sst GABAergic cortical interneuron",
                meaning=CL["4023017"]))
        setattr(cls, "CL:0008028",
            PermissibleValue(
                text="CL:0008028",
                description="visual system neuron",
                meaning=CL["0008028"]))
        setattr(cls, "CL:0008039",
            PermissibleValue(
                text="CL:0008039",
                description="lower motor neuron",
                meaning=CL["0008039"]))
        setattr(cls, "CL:2000086",
            PermissibleValue(
                text="CL:2000086",
                description="neocortex basket cell",
                meaning=CL["2000086"]))
        setattr(cls, "CL:4023023",
            PermissibleValue(
                text="CL:4023023",
                description="L5,6 neurogliaform lamp5 GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023023"]))
        setattr(cls, "CL:0000697",
            PermissibleValue(
                text="CL:0000697",
                description="R4 photoreceptor cell",
                meaning=CL["0000697"]))
        setattr(cls, "CL:2000088",
            PermissibleValue(
                text="CL:2000088",
                description="Ammon's horn basket cell",
                meaning=CL["2000088"]))
        setattr(cls, "CL:0004232",
            PermissibleValue(
                text="CL:0004232",
                description="starburst amacrine cell",
                meaning=CL["0004232"]))
        setattr(cls, "CL:4023041",
            PermissibleValue(
                text="CL:4023041",
                description="L5 extratelencephalic projecting glutamatergic cortical neuron",
                meaning=CL["4023041"]))
        setattr(cls, "CL:0004121",
            PermissibleValue(
                text="CL:0004121",
                description="retinal ganglion cell B2",
                meaning=CL["0004121"]))
        setattr(cls, "CL:0000748",
            PermissibleValue(
                text="CL:0000748",
                description="retinal bipolar neuron",
                meaning=CL["0000748"]))
        setattr(cls, "CL:4023164",
            PermissibleValue(
                text="CL:4023164",
                description="globular bushy cell",
                meaning=CL["4023164"]))
        setattr(cls, "CL:0000536",
            PermissibleValue(
                text="CL:0000536",
                description="secondary motor neuron",
                meaning=CL["0000536"]))
        setattr(cls, "CL:1000466",
            PermissibleValue(
                text="CL:1000466",
                description="chromaffin cell of right ovary",
                meaning=CL["1000466"]))
        setattr(cls, "CL:0011001",
            PermissibleValue(
                text="CL:0011001",
                description="spinal cord motor neuron",
                meaning=CL["0011001"]))
        setattr(cls, "CL:0000755",
            PermissibleValue(
                text="CL:0000755",
                description="type 3 cone bipolar cell (sensu Mus)",
                meaning=CL["0000755"]))
        setattr(cls, "CL:0004238",
            PermissibleValue(
                text="CL:0004238",
                description="asymmetric bistratified amacrine cell",
                meaning=CL["0004238"]))
        setattr(cls, "CL:0004161",
            PermissibleValue(
                text="CL:0004161",
                description="510 nm-cone",
                meaning=CL["0004161"]))
        setattr(cls, "CL:0000198",
            PermissibleValue(
                text="CL:0000198",
                description="pain receptor cell",
                meaning=CL["0000198"]))
        setattr(cls, "CL:0003038",
            PermissibleValue(
                text="CL:0003038",
                description="M7-OFF retinal ganglion cell",
                meaning=CL["0003038"]))
        setattr(cls, "CL:0003033",
            PermissibleValue(
                text="CL:0003033",
                description="M4 retinal ganglion cell",
                meaning=CL["0003033"]))
        setattr(cls, "CL:0012001",
            PermissibleValue(
                text="CL:0012001",
                description="neuron of the forebrain",
                meaning=CL["0012001"]))
        setattr(cls, "CL:0011104",
            PermissibleValue(
                text="CL:0011104",
                description="interplexiform cell",
                meaning=CL["0011104"]))
        setattr(cls, "CL:0003049",
            PermissibleValue(
                text="CL:0003049",
                description="M cone cell",
                meaning=CL["0003049"]))
        setattr(cls, "CL:2000032",
            PermissibleValue(
                text="CL:2000032",
                description="peripheral nervous system neuron",
                meaning=CL["2000032"]))
        setattr(cls, "CL:0011100",
            PermissibleValue(
                text="CL:0011100",
                description="galanergic neuron",
                meaning=CL["0011100"]))
        setattr(cls, "CL:0008025",
            PermissibleValue(
                text="CL:0008025",
                description="noradrenergic neuron",
                meaning=CL["0008025"]))
        setattr(cls, "CL:0000122",
            PermissibleValue(
                text="CL:0000122",
                description="stellate neuron",
                meaning=CL["0000122"]))
        setattr(cls, "CL:0003005",
            PermissibleValue(
                text="CL:0003005",
                description="G4 retinal ganglion cell",
                meaning=CL["0003005"]))
        setattr(cls, "CL:0000699",
            PermissibleValue(
                text="CL:0000699",
                description="paraganglial type 1 cell",
                meaning=CL["0000699"]))
        setattr(cls, "CL:4033050",
            PermissibleValue(
                text="CL:4033050",
                description="catecholaminergic neuron",
                meaning=CL["4033050"]))
        setattr(cls, "CL:1001502",
            PermissibleValue(
                text="CL:1001502",
                description="mitral cell",
                meaning=CL["1001502"]))
        setattr(cls, "CL:0002069",
            PermissibleValue(
                text="CL:0002069",
                description="type II vestibular sensory cell",
                meaning=CL["0002069"]))
        setattr(cls, "CL:4023065",
            PermissibleValue(
                text="CL:4023065",
                description="meis2 expressing cortical GABAergic cell",
                meaning=CL["4023065"]))
        setattr(cls, "CL:4023077",
            PermissibleValue(
                text="CL:4023077",
                description="bitufted neuron",
                meaning=CL["4023077"]))
        setattr(cls, "CL:0000847",
            PermissibleValue(
                text="CL:0000847",
                description="ciliated olfactory receptor neuron",
                meaning=CL["0000847"]))
        setattr(cls, "CL:4023188",
            PermissibleValue(
                text="CL:4023188",
                description="midget ganglion cell of retina",
                meaning=CL["4023188"]))
        setattr(cls, "CL:2000090",
            PermissibleValue(
                text="CL:2000090",
                description="dentate gyrus of hippocampal formation stellate cell",
                meaning=CL["2000090"]))
        setattr(cls, "CL:0000568",
            PermissibleValue(
                text="CL:0000568",
                description="amine precursor uptake and decarboxylation cell",
                meaning=CL["0000568"]))
        setattr(cls, "CL:1000426",
            PermissibleValue(
                text="CL:1000426",
                description="chromaffin cell of adrenal gland",
                meaning=CL["1000426"]))
        setattr(cls, "CL:0000100",
            PermissibleValue(
                text="CL:0000100",
                description="motor neuron",
                meaning=CL["0000100"]))
        setattr(cls, "CL:0011109",
            PermissibleValue(
                text="CL:0011109",
                description="hypocretin-secreting neuron",
                meaning=CL["0011109"]))
        setattr(cls, "CL:4023171",
            PermissibleValue(
                text="CL:4023171",
                description="trigeminal motor neuron",
                meaning=CL["4023171"]))
        setattr(cls, "CL:1001434",
            PermissibleValue(
                text="CL:1001434",
                description="olfactory bulb interneuron",
                meaning=CL["1001434"]))
        setattr(cls, "CL:0000494",
            PermissibleValue(
                text="CL:0000494",
                description="UV sensitive photoreceptor cell",
                meaning=CL["0000494"]))
        setattr(cls, "CL:0004117",
            PermissibleValue(
                text="CL:0004117",
                description="retinal ganglion cell A",
                meaning=CL["0004117"]))
        setattr(cls, "CL:0000205",
            PermissibleValue(
                text="CL:0000205",
                description="thermoreceptor cell",
                meaning=CL["0000205"]))
        setattr(cls, "CL:0004217",
            PermissibleValue(
                text="CL:0004217",
                description="H1 horizontal cell",
                meaning=CL["0004217"]))
        setattr(cls, "CL:0000200",
            PermissibleValue(
                text="CL:0000200",
                description="touch receptor cell",
                meaning=CL["0000200"]))
        setattr(cls, "CL:4023111",
            PermissibleValue(
                text="CL:4023111",
                description="cerebral cortex pyramidal neuron",
                meaning=CL["4023111"]))
        setattr(cls, "CL:4032001",
            PermissibleValue(
                text="CL:4032001",
                description="reelin GABAergic cortical interneuron",
                meaning=CL["4032001"]))
        setattr(cls, "CL:4023076",
            PermissibleValue(
                text="CL:4023076",
                description="Martinotti neuron",
                meaning=CL["4023076"]))
        setattr(cls, "CL:0000753",
            PermissibleValue(
                text="CL:0000753",
                description="type 1 cone bipolar cell (sensu Mus)",
                meaning=CL["0000753"]))
        setattr(cls, "CL:1001451",
            PermissibleValue(
                text="CL:1001451",
                description="sensory neuron of dorsal root ganglion",
                meaning=CL["1001451"]))
        setattr(cls, "CL:4023021",
            PermissibleValue(
                text="CL:4023021",
                description="static gamma motor neuron",
                meaning=CL["4023021"]))
        setattr(cls, "CL:0002066",
            PermissibleValue(
                text="CL:0002066",
                description="Feyrter cell",
                meaning=CL["0002066"]))
        setattr(cls, "CL:0000598",
            PermissibleValue(
                text="CL:0000598",
                description="pyramidal neuron",
                meaning=CL["0000598"]))
        setattr(cls, "CL:0000702",
            PermissibleValue(
                text="CL:0000702",
                description="R5 photoreceptor cell",
                meaning=CL["0000702"]))
        setattr(cls, "CL:0008049",
            PermissibleValue(
                text="CL:0008049",
                description="Betz cell",
                meaning=CL["0008049"]))
        setattr(cls, "CL:0001033",
            PermissibleValue(
                text="CL:0001033",
                description="hippocampal granule cell",
                meaning=CL["0001033"]))
        setattr(cls, "CL:0000587",
            PermissibleValue(
                text="CL:0000587",
                description="cold sensing thermoreceptor cell",
                meaning=CL["0000587"]))
        setattr(cls, "CL:4023161",
            PermissibleValue(
                text="CL:4023161",
                description="unipolar brush cell",
                meaning=CL["4023161"]))
        setattr(cls, "CL:2000031",
            PermissibleValue(
                text="CL:2000031",
                description="lateral line ganglion neuron",
                meaning=CL["2000031"]))
        setattr(cls, "CL:4023119",
            PermissibleValue(
                text="CL:4023119",
                description="displaced amacrine cell",
                meaning=CL["4023119"]))
        setattr(cls, "CL:1001569",
            PermissibleValue(
                text="CL:1001569",
                description="hippocampal interneuron",
                meaning=CL["1001569"]))
        setattr(cls, "CL:4023130",
            PermissibleValue(
                text="CL:4023130",
                description="kisspeptin neuron",
                meaning=CL["4023130"]))
        setattr(cls, "CL:4023090",
            PermissibleValue(
                text="CL:4023090",
                description="small basket cell",
                meaning=CL["4023090"]))
        setattr(cls, "CL:4023033",
            PermissibleValue(
                text="CL:4023033",
                description="OFF retinal ganglion cell",
                meaning=CL["4023033"]))
        setattr(cls, "CL:4023112",
            PermissibleValue(
                text="CL:4023112",
                description="vestibular afferent neuron",
                meaning=CL["4023112"]))
        setattr(cls, "CL:0004234",
            PermissibleValue(
                text="CL:0004234",
                description="diffuse multistratified amacrine cell",
                meaning=CL["0004234"]))
        setattr(cls, "CL:0002082",
            PermissibleValue(
                text="CL:0002082",
                description="type II cell of adrenal medulla",
                meaning=CL["0002082"]))
        setattr(cls, "CL:0010011",
            PermissibleValue(
                text="CL:0010011",
                description="cerebral cortex GABAergic interneuron",
                meaning=CL["0010011"]))
        setattr(cls, "CL:4030052",
            PermissibleValue(
                text="CL:4030052",
                description="nucleus accumbens shell and olfactory tubercle D2 medium spiny neuron",
                meaning=CL["4030052"]))
        setattr(cls, "CL:0000604",
            PermissibleValue(
                text="CL:0000604",
                description="retinal rod cell",
                meaning=CL["0000604"]))
        setattr(cls, "CL:4030027",
            PermissibleValue(
                text="CL:4030027",
                description="GABAergic amacrine cell",
                meaning=CL["4030027"]))
        setattr(cls, "CL:1001561",
            PermissibleValue(
                text="CL:1001561",
                description="vomeronasal sensory neuron",
                meaning=CL["1001561"]))
        setattr(cls, "CL:0000210",
            PermissibleValue(
                text="CL:0000210",
                description="photoreceptor cell",
                meaning=CL["0000210"]))
        setattr(cls, "CL:4023012",
            PermissibleValue(
                text="CL:4023012",
                description="near-projecting glutamatergic cortical neuron",
                meaning=CL["4023012"]))
        setattr(cls, "CL:4023087",
            PermissibleValue(
                text="CL:4023087",
                description="fan Martinotti neuron",
                meaning=CL["4023087"]))
        setattr(cls, "CL:0000028",
            PermissibleValue(
                text="CL:0000028",
                description="CNS neuron (sensu Nematoda and Protostomia)",
                meaning=CL["0000028"]))
        setattr(cls, "CL:0000006",
            PermissibleValue(
                text="CL:0000006",
                description="neuronal receptor cell",
                meaning=CL["0000006"]))
        setattr(cls, "CL:0004247",
            PermissibleValue(
                text="CL:0004247",
                description="bistratified cell",
                meaning=CL["0004247"]))
        setattr(cls, "CL:0010012",
            PermissibleValue(
                text="CL:0010012",
                description="cerebral cortex neuron",
                meaning=CL["0010012"]))
        setattr(cls, "CL:0004245",
            PermissibleValue(
                text="CL:0004245",
                description="indoleamine-accumulating amacrine cell",
                meaning=CL["0004245"]))
        setattr(cls, "CL:0004224",
            PermissibleValue(
                text="CL:0004224",
                description="AB diffuse-2 amacrine cell",
                meaning=CL["0004224"]))
        setattr(cls, "CL:0003009",
            PermissibleValue(
                text="CL:0003009",
                description="G6 retinal ganglion cell",
                meaning=CL["0003009"]))
        setattr(cls, "CL:0000679",
            PermissibleValue(
                text="CL:0000679",
                description="glutamatergic neuron",
                meaning=CL["0000679"]))
        setattr(cls, "CL:0000166",
            PermissibleValue(
                text="CL:0000166",
                description="chromaffin cell",
                meaning=CL["0000166"]))
        setattr(cls, "CL:4023088",
            PermissibleValue(
                text="CL:4023088",
                description="large basket cell",
                meaning=CL["4023088"]))
        setattr(cls, "CL:4023024",
            PermissibleValue(
                text="CL:4023024",
                description="neurogliaform lamp5 GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023024"]))
        setattr(cls, "CL:0005024",
            PermissibleValue(
                text="CL:0005024",
                description="somatomotor neuron",
                meaning=CL["0005024"]))
        setattr(cls, "CL:4023049",
            PermissibleValue(
                text="CL:4023049",
                description="L5 intratelencephalic projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023049"]))
        setattr(cls, "CL:0000573",
            PermissibleValue(
                text="CL:0000573",
                description="retinal cone cell",
                meaning=CL["0000573"]))
        setattr(cls, "CL:4023123",
            PermissibleValue(
                text="CL:4023123",
                description="hypothalamus kisspeptin neuron",
                meaning=CL["4023123"]))
        setattr(cls, "CL:0000376",
            PermissibleValue(
                text="CL:0000376",
                description="humidity receptor cell",
                meaning=CL["0000376"]))
        setattr(cls, "CL:0004235",
            PermissibleValue(
                text="CL:0004235",
                description="AB broad diffuse-1 amacrine cell",
                meaning=CL["0004235"]))
        setattr(cls, "CL:0000106",
            PermissibleValue(
                text="CL:0000106",
                description="unipolar neuron",
                meaning=CL["0000106"]))
        setattr(cls, "CL:0001032",
            PermissibleValue(
                text="CL:0001032",
                description="cortical granule cell",
                meaning=CL["0001032"]))
        setattr(cls, "CL:0000561",
            PermissibleValue(
                text="CL:0000561",
                description="amacrine cell",
                meaning=CL["0000561"]))
        setattr(cls, "CL:4023093",
            PermissibleValue(
                text="CL:4023093",
                description="stellate pyramidal neuron",
                meaning=CL["4023093"]))
        setattr(cls, "CL:0000247",
            PermissibleValue(
                text="CL:0000247",
                description="Rohon-Beard neuron",
                meaning=CL["0000247"]))
        setattr(cls, "CL:0003008",
            PermissibleValue(
                text="CL:0003008",
                description="G5 retinal ganglion cell",
                meaning=CL["0003008"]))
        setattr(cls, "CL:0000203",
            PermissibleValue(
                text="CL:0000203",
                description="gravity sensitive cell",
                meaning=CL["0000203"]))
        setattr(cls, "CL:0003037",
            PermissibleValue(
                text="CL:0003037",
                description="M7-ON retinal ganglion cell",
                meaning=CL["0003037"]))
        setattr(cls, "CL:0004221",
            PermissibleValue(
                text="CL:0004221",
                description="flag A amacrine cell",
                meaning=CL["0004221"]))
        setattr(cls, "CL:0000638",
            PermissibleValue(
                text="CL:0000638",
                description="acidophil cell of pars distalis of adenohypophysis",
                meaning=CL["0000638"]))
        setattr(cls, "CL:0004229",
            PermissibleValue(
                text="CL:0004229",
                description="A2-like amacrine cell",
                meaning=CL["0004229"]))
        setattr(cls, "CL:4023120",
            PermissibleValue(
                text="CL:4023120",
                description="cochlea auditory hair cell",
                meaning=CL["4023120"]))
        setattr(cls, "CL:0008032",
            PermissibleValue(
                text="CL:0008032",
                description="rosehip neuron",
                meaning=CL["0008032"]))
        setattr(cls, "CL:0008027",
            PermissibleValue(
                text="CL:0008027",
                description="rod bipolar cell (sensu Mus)",
                meaning=CL["0008027"]))
        setattr(cls, "CL:0000497",
            PermissibleValue(
                text="CL:0000497",
                description="red sensitive photoreceptor cell",
                meaning=CL["0000497"]))
        setattr(cls, "CL:4023062",
            PermissibleValue(
                text="CL:4023062",
                description="dentate gyrus neuron",
                meaning=CL["4023062"]))
        setattr(cls, "CL:0002516",
            PermissibleValue(
                text="CL:0002516",
                description="interrenal chromaffin cell",
                meaning=CL["0002516"]))
        setattr(cls, "CL:0004119",
            PermissibleValue(
                text="CL:0004119",
                description="retinal ganglion cell B1",
                meaning=CL["0004119"]))
        setattr(cls, "CL:4030039",
            PermissibleValue(
                text="CL:4030039",
                description="von Economo neuron",
                meaning=CL["4030039"]))
        setattr(cls, "CL:4023036",
            PermissibleValue(
                text="CL:4023036",
                description="chandelier pvalb GABAergic cortical interneuron",
                meaning=CL["4023036"]))
        setattr(cls, "CL:0000117",
            PermissibleValue(
                text="CL:0000117",
                description="CNS neuron (sensu Vertebrata)",
                meaning=CL["0000117"]))
        setattr(cls, "CL:4023015",
            PermissibleValue(
                text="CL:4023015",
                description="sncg GABAergic cortical interneuron",
                meaning=CL["4023015"]))
        setattr(cls, "CL:4033033",
            PermissibleValue(
                text="CL:4033033",
                description="flat midget bipolar cell",
                meaning=CL["4033033"]))
        setattr(cls, "CL:0000626",
            PermissibleValue(
                text="CL:0000626",
                description="olfactory granule cell",
                meaning=CL["0000626"]))
        setattr(cls, "CL:0004218",
            PermissibleValue(
                text="CL:0004218",
                description="H2 horizontal cell",
                meaning=CL["0004218"]))
        setattr(cls, "CL:0004233",
            PermissibleValue(
                text="CL:0004233",
                description="DAPI-3 amacrine cell",
                meaning=CL["0004233"]))
        setattr(cls, "CL:0003021",
            PermissibleValue(
                text="CL:0003021",
                description="retinal ganglion cell C4",
                meaning=CL["0003021"]))
        setattr(cls, "CL:0000489",
            PermissibleValue(
                text="CL:0000489",
                description="scotopic photoreceptor cell",
                meaning=CL["0000489"]))
        setattr(cls, "CL:4023159",
            PermissibleValue(
                text="CL:4023159",
                description="double bouquet cell",
                meaning=CL["4023159"]))
        setattr(cls, "CL:0002612",
            PermissibleValue(
                text="CL:0002612",
                description="neuron of the ventral spinal cord",
                meaning=CL["0002612"]))
        setattr(cls, "CL:0000476",
            PermissibleValue(
                text="CL:0000476",
                description="thyrotroph",
                meaning=CL["0000476"]))
        setattr(cls, "CL:4033034",
            PermissibleValue(
                text="CL:4033034",
                description="invaginating midget bipolar cell",
                meaning=CL["4033034"]))
        setattr(cls, "CL:4023029",
            PermissibleValue(
                text="CL:4023029",
                description="indirect pathway medium spiny neuron",
                meaning=CL["4023029"]))
        setattr(cls, "CL:0004236",
            PermissibleValue(
                text="CL:0004236",
                description="AB broad diffuse-2 amacrine cell",
                meaning=CL["0004236"]))
        setattr(cls, "CL:0003017",
            PermissibleValue(
                text="CL:0003017",
                description="retinal ganglion cell B3 outer",
                meaning=CL["0003017"]))
        setattr(cls, "CL:0000759",
            PermissibleValue(
                text="CL:0000759",
                description="type 7 cone bipolar cell (sensu Mus)",
                meaning=CL["0000759"]))
        setattr(cls, "CL:0000740",
            PermissibleValue(
                text="CL:0000740",
                description="retinal ganglion cell",
                meaning=CL["0000740"]))
        setattr(cls, "CL:0004120",
            PermissibleValue(
                text="CL:0004120",
                description="retinal ganglion cell A1",
                meaning=CL["0004120"]))
        setattr(cls, "CL:3000002",
            PermissibleValue(
                text="CL:3000002",
                description="sympathetic noradrenergic neuron",
                meaning=CL["3000002"]))
        setattr(cls, "CL:0003023",
            PermissibleValue(
                text="CL:0003023",
                description="retinal ganglion cell C6",
                meaning=CL["0003023"]))
        setattr(cls, "CL:0000690",
            PermissibleValue(
                text="CL:0000690",
                description="R2 photoreceptor cell",
                meaning=CL["0000690"]))
        setattr(cls, "CL:4023047",
            PermissibleValue(
                text="CL:4023047",
                description="L2/3 intratelencephalic projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023047"]))
        setattr(cls, "CL:4023022",
            PermissibleValue(
                text="CL:4023022",
                description="canopy lamp5 GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023022"]))
        setattr(cls, "CL:4023060",
            PermissibleValue(
                text="CL:4023060",
                description="hippocampal CA1-3 neuron",
                meaning=CL["4023060"]))
        setattr(cls, "CL:0000758",
            PermissibleValue(
                text="CL:0000758",
                description="type 6 cone bipolar cell (sensu Mus)",
                meaning=CL["0000758"]))
        setattr(cls, "CL:0000535",
            PermissibleValue(
                text="CL:0000535",
                description="secondary neuron",
                meaning=CL["0000535"]))
        setattr(cls, "CL:4023055",
            PermissibleValue(
                text="CL:4023055",
                description="corticothalamic VAL/VM projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023055"]))
        setattr(cls, "CL:1000467",
            PermissibleValue(
                text="CL:1000467",
                description="chromaffin cell of left ovary",
                meaning=CL["1000467"]))
        setattr(cls, "CL:0011002",
            PermissibleValue(
                text="CL:0011002",
                description="lateral motor column neuron",
                meaning=CL["0011002"]))
        setattr(cls, "CL:0004244",
            PermissibleValue(
                text="CL:0004244",
                description="WF4 amacrine cell",
                meaning=CL["0004244"]))
        setattr(cls, "CL:1000223",
            PermissibleValue(
                text="CL:1000223",
                description="lung neuroendocrine cell",
                meaning=CL["1000223"]))
        setattr(cls, "CL:1000385",
            PermissibleValue(
                text="CL:1000385",
                description="""type 2 vestibular sensory cell of epithelium of crista of ampulla of semicircular duct of membranous labyrinth""",
                meaning=CL["1000385"]))
        setattr(cls, "CL:0000691",
            PermissibleValue(
                text="CL:0000691",
                description="stellate interneuron",
                meaning=CL["0000691"]))
        setattr(cls, "CL:4023008",
            PermissibleValue(
                text="CL:4023008",
                description="intratelencephalic-projecting glutamatergic cortical neuron",
                meaning=CL["4023008"]))
        setattr(cls, "CL:4023044",
            PermissibleValue(
                text="CL:4023044",
                description="""non-medulla, extratelencephalic-projecting glutamatergic neuron of the primary motor cortex""",
                meaning=CL["4023044"]))
        setattr(cls, "CL:0000850",
            PermissibleValue(
                text="CL:0000850",
                description="serotonergic neuron",
                meaning=CL["0000850"]))
        setattr(cls, "CL:0000695",
            PermissibleValue(
                text="CL:0000695",
                description="Cajal-Retzius cell",
                meaning=CL["0000695"]))
        setattr(cls, "CL:0003051",
            PermissibleValue(
                text="CL:0003051",
                description="UV cone cell",
                meaning=CL["0003051"]))
        setattr(cls, "CL:0000402",
            PermissibleValue(
                text="CL:0000402",
                description="CNS interneuron",
                meaning=CL["0000402"]))
        setattr(cls, "CL:0005023",
            PermissibleValue(
                text="CL:0005023",
                description="branchiomotor neuron",
                meaning=CL["0005023"]))
        setattr(cls, "CL:4023043",
            PermissibleValue(
                text="CL:4023043",
                description="L5/6 near-projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023043"]))
        setattr(cls, "CL:0004162",
            PermissibleValue(
                text="CL:0004162",
                description="360 nm-cone",
                meaning=CL["0004162"]))
        setattr(cls, "CL:0011003",
            PermissibleValue(
                text="CL:0011003",
                description="magnocellular neurosecretory cell",
                meaning=CL["0011003"]))
        setattr(cls, "CL:0004230",
            PermissibleValue(
                text="CL:0004230",
                description="diffuse bistratified amacrine cell",
                meaning=CL["0004230"]))
        setattr(cls, "CL:1001505",
            PermissibleValue(
                text="CL:1001505",
                description="parvocellular neurosecretory cell",
                meaning=CL["1001505"]))
        setattr(cls, "CL:0011106",
            PermissibleValue(
                text="CL:0011106",
                description="GABAnergic interplexiform cell",
                meaning=CL["0011106"]))
        setattr(cls, "CL:0000437",
            PermissibleValue(
                text="CL:0000437",
                description="gonadtroph",
                meaning=CL["0000437"]))
        setattr(cls, "CL:4023010",
            PermissibleValue(
                text="CL:4023010",
                description="alpha7 GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023010"]))
        setattr(cls, "CL:4023046",
            PermissibleValue(
                text="CL:4023046",
                description="L6b subplate glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023046"]))
        setattr(cls, "CL:0000109",
            PermissibleValue(
                text="CL:0000109",
                description="adrenergic neuron",
                meaning=CL["0000109"]))
        setattr(cls, "CL:0011000",
            PermissibleValue(
                text="CL:0011000",
                description="dorsal horn interneuron",
                meaning=CL["0011000"]))
        setattr(cls, "CL:0000251",
            PermissibleValue(
                text="CL:0000251",
                description="extramedullary cell",
                meaning=CL["0000251"]))
        setattr(cls, "CL:0003044",
            PermissibleValue(
                text="CL:0003044",
                description="M11 retinal ganglion cell",
                meaning=CL["0003044"]))
        setattr(cls, "CL:4023053",
            PermissibleValue(
                text="CL:4023053",
                description="spinal interneuron synapsing Betz cell",
                meaning=CL["4023053"]))
        setattr(cls, "CL:1000378",
            PermissibleValue(
                text="CL:1000378",
                description="type 1 vestibular sensory cell of stato-acoustic epithelium",
                meaning=CL["1000378"]))
        setattr(cls, "CL:4023124",
            PermissibleValue(
                text="CL:4023124",
                description="dentate gyrus kisspeptin neuron",
                meaning=CL["4023124"]))
        setattr(cls, "CL:1000427",
            PermissibleValue(
                text="CL:1000427",
                description="adrenal cortex chromaffin cell",
                meaning=CL["1000427"]))
        setattr(cls, "CL:0000207",
            PermissibleValue(
                text="CL:0000207",
                description="olfactory receptor cell",
                meaning=CL["0000207"]))
        setattr(cls, "CL:4023162",
            PermissibleValue(
                text="CL:4023162",
                description="bushy cell",
                meaning=CL["4023162"]))
        setattr(cls, "CL:2000019",
            PermissibleValue(
                text="CL:2000019",
                description="compound eye photoreceptor cell",
                meaning=CL["2000019"]))
        setattr(cls, "CL:4023086",
            PermissibleValue(
                text="CL:4023086",
                description="T Martinotti neuron",
                meaning=CL["4023086"]))
        setattr(cls, "CL:0003012",
            PermissibleValue(
                text="CL:0003012",
                description="G9 retinal ganglion cell",
                meaning=CL["0003012"]))
        setattr(cls, "CL:0002270",
            PermissibleValue(
                text="CL:0002270",
                description="type EC2 enteroendocrine cell",
                meaning=CL["0002270"]))
        setattr(cls, "CL:2000024",
            PermissibleValue(
                text="CL:2000024",
                description="spinal cord medial motor column neuron",
                meaning=CL["2000024"]))
        setattr(cls, "CL:0003022",
            PermissibleValue(
                text="CL:0003022",
                description="retinal ganglion cell C5",
                meaning=CL["0003022"]))
        setattr(cls, "CL:0000104",
            PermissibleValue(
                text="CL:0000104",
                description="multipolar neuron",
                meaning=CL["0000104"]))
        setattr(cls, "CL:4023050",
            PermissibleValue(
                text="CL:4023050",
                description="L6 intratelencephalic projecting glutamatergic neuron of the primary motor cortex",
                meaning=CL["4023050"]))
        setattr(cls, "CL:4023030",
            PermissibleValue(
                text="CL:4023030",
                description="L2/3/5 fan Martinotti sst GABAergic cortical interneuron (Mmus)",
                meaning=CL["4023030"]))
        setattr(cls, "CL:0000741",
            PermissibleValue(
                text="CL:0000741",
                description="spinal accessory motor neuron",
                meaning=CL["0000741"]))
        setattr(cls, "CL:4033010",
            PermissibleValue(
                text="CL:4033010",
                description="neuroendocrine cell of epithelium of lobar bronchus",
                meaning=CL["4033010"]))
        setattr(cls, "CL:1000425",
            PermissibleValue(
                text="CL:1000425",
                description="chromaffin cell of paraganglion",
                meaning=CL["1000425"]))
        setattr(cls, "CL:4030051",
            PermissibleValue(
                text="CL:4030051",
                description="nucleus accumbens shell and olfactory tubercle D1 medium spiny neuron",
                meaning=CL["4030051"]))
        setattr(cls, "CL:0000567",
            PermissibleValue(
                text="CL:0000567",
                description="polymodal nocireceptor",
                meaning=CL["0000567"]))
        setattr(cls, "CL:0004215",
            PermissibleValue(
                text="CL:0004215",
                description="type 5a cone bipolar cell",
                meaning=CL["0004215"]))
        setattr(cls, "CL:0003032",
            PermissibleValue(
                text="CL:0003032",
                description="M3-OFF retinal ganglion cell",
                meaning=CL["0003032"]))
        setattr(cls, "CL:4023079",
            PermissibleValue(
                text="CL:4023079",
                description="midbrain-derived inhibitory neuron",
                meaning=CL["4023079"]))
        setattr(cls, "CL:0000099",
            PermissibleValue(
                text="CL:0000099",
                description="interneuron",
                meaning=CL["0000099"]))
        setattr(cls, "CL:0000253",
            PermissibleValue(
                text="CL:0000253",
                description="eurydendroid cell",
                meaning=CL["0000253"]))
        setattr(cls, "CL:0008013",
            PermissibleValue(
                text="CL:0008013",
                description="cranial visceromotor neuron",
                meaning=CL["0008013"]))
        setattr(cls, "CL:0005000",
            PermissibleValue(
                text="CL:0005000",
                description="spinal cord interneuron",
                meaning=CL["0005000"]))
        setattr(cls, "CL:0004222",
            PermissibleValue(
                text="CL:0004222",
                description="flag B amacrine cell",
                meaning=CL["0004222"]))
        setattr(cls, "CL:0000617",
            PermissibleValue(
                text="CL:0000617",
                description="GABAergic neuron",
                meaning=CL["0000617"]))
        setattr(cls, "CL:0003010",
            PermissibleValue(
                text="CL:0003010",
                description="G7 retinal ganglion cell",
                meaning=CL["0003010"]))
        setattr(cls, "CL:0000577",
            PermissibleValue(
                text="CL:0000577",
                description="type EC enteroendocrine cell",
                meaning=CL["0000577"]))
        setattr(cls, "CL:0003018",
            PermissibleValue(
                text="CL:0003018",
                description="retinal ganglion cell B3 inner",
                meaning=CL["0003018"]))
        setattr(cls, "CL:0002083",
            PermissibleValue(
                text="CL:0002083",
                description="type I cell of adrenal medulla",
                meaning=CL["0002083"]))
        setattr(cls, "CL:4023081",
            PermissibleValue(
                text="CL:4023081",
                description="""inverted L6 intratelencephalic projecting glutamatergic neuron of the primary motor cortex (Mmus)""",
                meaning=CL["4023081"]))
        setattr(cls, "CL:0004251",
            PermissibleValue(
                text="CL:0004251",
                description="narrow field retinal amacrine cell",
                meaning=CL["0004251"]))
        setattr(cls, "CL:4023092",
            PermissibleValue(
                text="CL:4023092",
                description="inverted pyramidal neuron",
                meaning=CL["4023092"]))
        setattr(cls, "CL:0002608",
            PermissibleValue(
                text="CL:0002608",
                description="hippocampal neuron",
                meaning=CL["0002608"]))
        setattr(cls, "CL:0008048",
            PermissibleValue(
                text="CL:0008048",
                description="upper motor neuron",
                meaning=CL["0008048"]))
        setattr(cls, "CL:0011113",
            PermissibleValue(
                text="CL:0011113",
                description="spiral ganglion neuron",
                meaning=CL["0011113"]))
        setattr(cls, "CL:0000601",
            PermissibleValue(
                text="CL:0000601",
                description="cochlear outer hair cell",
                meaning=CL["0000601"]))
        setattr(cls, "CL:0003041",
            PermissibleValue(
                text="CL:0003041",
                description="M9-ON retinal ganglion cell",
                meaning=CL["0003041"]))
        setattr(cls, "CL:4023042",
            PermissibleValue(
                text="CL:4023042",
                description="L6 corticothalamic-projecting glutamatergic cortical neuron",
                meaning=CL["4023042"]))
        setattr(cls, "CL:0000199",
            PermissibleValue(
                text="CL:0000199",
                description="mechanoreceptor cell",
                meaning=CL["0000199"]))
        setattr(cls, "CL:1001571",
            PermissibleValue(
                text="CL:1001571",
                description="hippocampal pyramidal neuron",
                meaning=CL["1001571"]))
        setattr(cls, "CL:2000048",
            PermissibleValue(
                text="CL:2000048",
                description="anterior horn motor neuron",
                meaning=CL["2000048"]))
        setattr(cls, "CL:4023170",
            PermissibleValue(
                text="CL:4023170",
                description="trigeminal sensory neuron",
                meaning=CL["4023170"]))
        setattr(cls, "CL:0002614",
            PermissibleValue(
                text="CL:0002614",
                description="neuron of the substantia nigra",
                meaning=CL["0002614"]))

class GlialCellTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GlialCellTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CL:1000236",
            PermissibleValue(
                text="CL:1000236",
                description="posterior lateral line nerve glial cell",
                meaning=CL["1000236"]))
        setattr(cls, "CL:0002603",
            PermissibleValue(
                text="CL:0002603",
                description="astrocyte of the cerebellum",
                meaning=CL["0002603"]))
        setattr(cls, "CL:1001581",
            PermissibleValue(
                text="CL:1001581",
                description="lateral ventricle glial cell",
                meaning=CL["1001581"]))
        setattr(cls, "CL:4023154",
            PermissibleValue(
                text="CL:4023154",
                description="myelinating glial cell",
                meaning=CL["4023154"]))
        setattr(cls, "CL:0000692",
            PermissibleValue(
                text="CL:0000692",
                description="terminal Schwann cell",
                meaning=CL["0000692"]))
        setattr(cls, "CL:0000126",
            PermissibleValue(
                text="CL:0000126",
                description="macroglial cell",
                meaning=CL["0000126"]))
        setattr(cls, "CL:0002606",
            PermissibleValue(
                text="CL:0002606",
                description="astrocyte of the spinal cord",
                meaning=CL["0002606"]))
        setattr(cls, "CL:0000636",
            PermissibleValue(
                text="CL:0000636",
                description="Mueller cell",
                meaning=CL["0000636"]))
        setattr(cls, "CL:0002605",
            PermissibleValue(
                text="CL:0002605",
                description="astrocyte of the cerebral cortex",
                meaning=CL["0002605"]))
        setattr(cls, "CL:0012000",
            PermissibleValue(
                text="CL:0012000",
                description="astrocyte of the forebrain",
                meaning=CL["0012000"]))
        setattr(cls, "CL:0000681",
            PermissibleValue(
                text="CL:0000681",
                description="radial glial cell",
                meaning=CL["0000681"]))
        setattr(cls, "CL:4040002",
            PermissibleValue(
                text="CL:4040002",
                description="enteroglial cell",
                meaning=CL["4040002"]))
        setattr(cls, "CL:0002576",
            PermissibleValue(
                text="CL:0002576",
                description="perineurial cell",
                meaning=CL["0002576"]))
        setattr(cls, "CL:2000005",
            PermissibleValue(
                text="CL:2000005",
                description="brain macroglial cell",
                meaning=CL["2000005"]))
        setattr(cls, "CL:2000025",
            PermissibleValue(
                text="CL:2000025",
                description="spinal cord oligodendrocyte",
                meaning=CL["2000025"]))
        setattr(cls, "CL:0010020",
            PermissibleValue(
                text="CL:0010020",
                description="cardiac glial cell",
                meaning=CL["0010020"]))
        setattr(cls, "CL:0000128",
            PermissibleValue(
                text="CL:0000128",
                description="oligodendrocyte",
                meaning=CL["0000128"]))
        setattr(cls, "CL:0002628",
            PermissibleValue(
                text="CL:0002628",
                description="immature microglial cell",
                meaning=CL["0002628"]))
        setattr(cls, "CL:0002085",
            PermissibleValue(
                text="CL:0002085",
                description="tanycyte",
                meaning=CL["0002085"]))
        setattr(cls, "CL:0013000",
            PermissibleValue(
                text="CL:0013000",
                description="forebrain radial glial cell",
                meaning=CL["0013000"]))
        setattr(cls, "CL:1000239",
            PermissibleValue(
                text="CL:1000239",
                description="anterior lateral line nerve glial cell",
                meaning=CL["1000239"]))
        setattr(cls, "CL:1001579",
            PermissibleValue(
                text="CL:1001579",
                description="cerebral cortex glial cell",
                meaning=CL["1001579"]))
        setattr(cls, "CL:0002627",
            PermissibleValue(
                text="CL:0002627",
                description="mature astrocyte",
                meaning=CL["0002627"]))
        setattr(cls, "CL:0002629",
            PermissibleValue(
                text="CL:0002629",
                description="mature microglial cell",
                meaning=CL["0002629"]))
        setattr(cls, "CL:0002376",
            PermissibleValue(
                text="CL:0002376",
                description="non-myelinating Schwann cell",
                meaning=CL["0002376"]))
        setattr(cls, "CL:0000644",
            PermissibleValue(
                text="CL:0000644",
                description="Bergmann glial cell",
                meaning=CL["0000644"]))
        setattr(cls, "CL:4033015",
            PermissibleValue(
                text="CL:4033015",
                description="retinal astrocyte",
                meaning=CL["4033015"]))
        setattr(cls, "CL:0002573",
            PermissibleValue(
                text="CL:0002573",
                description="Schwann cell",
                meaning=CL["0002573"]))
        setattr(cls, "CL:0002626",
            PermissibleValue(
                text="CL:0002626",
                description="immature astrocyte",
                meaning=CL["0002626"]))
        setattr(cls, "CL:1000050",
            PermissibleValue(
                text="CL:1000050",
                description="lateral line nerve glial cell",
                meaning=CL["1000050"]))
        setattr(cls, "CL:0011028",
            PermissibleValue(
                text="CL:0011028",
                description="olfactory ensheathing cell",
                meaning=CL["0011028"]))
        setattr(cls, "CL:0000218",
            PermissibleValue(
                text="CL:0000218",
                description="myelinating Schwann cell",
                meaning=CL["0000218"]))
        setattr(cls, "CL:0000645",
            PermissibleValue(
                text="CL:0000645",
                description="pituicyte",
                meaning=CL["0000645"]))
        setattr(cls, "CL:1000073",
            PermissibleValue(
                text="CL:1000073",
                description="spinal cord radial glial cell",
                meaning=CL["1000073"]))
        setattr(cls, "CL:0000127",
            PermissibleValue(
                text="CL:0000127",
                description="astrocyte",
                meaning=CL["0000127"]))
        setattr(cls, "CL:0002377",
            PermissibleValue(
                text="CL:0002377",
                description="immature Schwann cell",
                meaning=CL["0002377"]))
        setattr(cls, "CL:0000129",
            PermissibleValue(
                text="CL:0000129",
                description="microglial cell",
                meaning=CL["0000129"]))
        setattr(cls, "CL:0000683",
            PermissibleValue(
                text="CL:0000683",
                description="ependymoglial cell",
                meaning=CL["0000683"]))
        setattr(cls, "CL:1001580",
            PermissibleValue(
                text="CL:1001580",
                description="hippocampal glial cell",
                meaning=CL["1001580"]))
        setattr(cls, "CL:0002604",
            PermissibleValue(
                text="CL:0002604",
                description="hippocampal astrocyte",
                meaning=CL["0002604"]))

# Slots
class slots:
    pass

slots.cell_type = Slot(uri=DEFAULT_.cell_type, name="cell_type", curie=DEFAULT_.curie('cell_type'),
                   model_uri=DEFAULT_.cell_type, domain=None, range=str)
