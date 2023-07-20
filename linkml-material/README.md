## Folder Structure

### Schemas

There are two illustrative examples in the [schemas](./schemas/) folder showcasing the capabilities and usage of LinkML enumerations:
* [static_enums.yaml](./schemas/static_enums.yaml)
  * LinkML schema illustrating the definition and usage of pre-defined/static enumerations
* [dynamic_enums.yaml](./schemas/dynamic_enums.yaml)
  * LinkML schema illustrating the definition and usage of dynamic value sets/enumerations which need not have a hardcoded list of terms

### Artifacts

There are a number of derived products/artifacts in this [folder](./artifacts/). These artifacts have been derived by running individal commands from within the LinkML or OAK library on the schemas.

Note: `gen-python` is a generator built into the LinkML framework that allows you to generate Python dataclasses from LinkML YAML.

* [static_enums_dataclasses.py](./artifacts/static_enums_dataclasses.py)

```bash
gen-python ~/path/to/schemas/static_enums.yaml > ~/path/to/artifacts/static_enums_dataclasses.py
```

* [dynamic_enums_dataclasses.py](./artifacts/dynamic_enums_dataclasses.py)

```bash
gen-python ~/path/to/schemas/dynamic_enums.yaml > ~/path/to/artifacts/dynamic_enums_dataclasses.py
```

Note: `vskit expand` is a utility built into the OAK library that allows you to expand/materialize a dynamically specified enumeration into a static list of permissible values
* [dynamic_enums_expanded.yaml](./artifacts/dynamic_enums_expanded.yaml)

```bash
vskit expand -s ~/path/to/schemas/dynamic_enums.yaml -o ~/path/to/artifacts/dynamic_enums_expanded.yaml NeuronTypeEnum GlialCellTypeEnum
```
