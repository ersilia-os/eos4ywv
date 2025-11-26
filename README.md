# MACAW (Molecular AutoenCoding Auto-Workaround)

MACAW (Molecular AutoenCoding Auto-Workaround) is a cheminformatic tool for Python that embeds molecules in a low-dimensional, continuous numerical space. It also enables the generation of new molecules on specification

This model was incorporated on 2025-10-13.Last packaged on 2025-10-16.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4ywv`
- **Slug:** `macaw`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Fixed`
- **Interpretation:** 100 features based on pretrained MACAW.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| dim_00 | float |  | MACAW dimension index 0 |
| dim_01 | float |  | MACAW dimension index 1 |
| dim_02 | float |  | MACAW dimension index 2 |
| dim_03 | float |  | MACAW dimension index 3 |
| dim_04 | float |  | MACAW dimension index 4 |
| dim_05 | float |  | MACAW dimension index 5 |
| dim_06 | float |  | MACAW dimension index 6 |
| dim_07 | float |  | MACAW dimension index 7 |
| dim_08 | float |  | MACAW dimension index 8 |
| dim_09 | float |  | MACAW dimension index 9 |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4ywv](https://hub.docker.com/r/ersiliaos/eos4ywv)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4ywv.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4ywv.zip)

### Resource Consumption
- **Model Size (Mb):** `4`
- **Environment Size (Mb):** `884`
- **Image Size (Mb):** `873.78`

**Computational Performance (seconds):**
- 10 inputs: `39.39`
- 100 inputs: `29.2`
- 10000 inputs: `311.81`

### References
- **Source Code**: [https://github.com/LBLQMM/MACAW/](https://github.com/LBLQMM/MACAW/)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acs.jcim.2c00229](https://pubs.acs.org/doi/10.1021/acs.jcim.2c00229)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [Marina18](https://github.com/Marina18)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4ywv
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4ywv
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
