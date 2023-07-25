## Folder Structure

### Schemas

There are two illustrative examples in the [schemas](./schemas/) folder showcasing the capabilities and usage of LinkML enumerations:
* [static_enums.yaml](./schemas/static_enums.yaml)
  * LinkML schema illustrating the definition and usage of pre-defined/static enumerations
* [dynamic_enums.yaml](./schemas/dynamic_enums.yaml)
  * LinkML schema illustrating the definition and usage of dynamic value sets/enumerations which need not have a hardcoded list of terms

### Artifacts

There are a number of derived products/artifacts in this [folder](./artifacts/). These artifacts have been derived by running individual commands from within the [LinkML](https://github.com/linkml/linkml), [OAK](https://github.com/INCATools/ontology-access-kit) or [schemasheets](https://github.com/linkml/schemasheets) library on the schemas.

Note: `gen-python` is a generator built into the LinkML framework that allows you to generate Python dataclasses from LinkML YAML.

* [static_enums_dataclasses.py](./artifacts/static_enums_dataclasses.py)

```bash
gen-python ~/path/to/linkml-material/schemas/static_enums.yaml > ~/path/to/linkml-material/artifacts/static_enums_dataclasses.py
```

* [dynamic_enums_dataclasses.py](./artifacts/dynamic_enums_dataclasses.py)

```bash
gen-python ~/path/to/linkml-material/schemas/dynamic_enums.yaml > ~/path/to/linkml-material/artifacts/dynamic_enums_dataclasses.py
```

Note: `vskit expand` is a utility built into the OAK library that allows you to expand/materialize a dynamically specified enumeration into a static list of permissible values
* [dynamic_enums_expanded.yaml](./artifacts/dynamic_enums_expanded.yaml)

```bash
vskit expand -s ~/path/to/linkml-material/schemas/dynamic_enums.yaml -o ~/path/to/linkml-material/artifacts/dynamic_enums_expanded.yaml NeuronTypeEnum GlialCellTypeEnum NeuronOrGlialCellTypeEnum
```

* [enums_schemasheets.yaml](./artifacts/enums_schemasheets.yaml)

Note: `sheets2linkml` is a utility built into the schemasheets library that takes your spreadsheet data model exported as individual (or single monolithic) TSVs and converts it into a LinkML YAML representation of the data model.

```bash
sheets2linkml ~/path/to/linkml-material/schemasheets/*tsv --output ~/path/to/linkml-material/artifacts/enums_schemasheets.yaml 
```

A spreadsheet version of the data model used in the above example has been created and is accessible [here](https://docs.google.com/spreadsheets/d/1kX9wGd89wuAT3ncA9Ur-YleYvOpjsW6z1NOUOzR-a-o/edit?usp=sharing).
