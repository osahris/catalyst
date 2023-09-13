---
fhir_profile: MedicationStatement
references:
  - class: visit
    cardinality: "1..1"
variables:
  - var: MEDICATIONID
    primary_key: true
  - var: THER_ANTIINFECTIVES_ATCCODE
  - var: THER_ANTIINFECTIVES_ATCSYSTEM
  - var: THER_ANTIINFECTIVES_DRUGNAME
  - var: THER_ANTIINFECTIVES_START
  - var: THER_ANTIINFECTIVES_END
---
