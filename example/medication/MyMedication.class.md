---
fhir_parent: MedicationStatement
references:
  - class: Patient
    cardinality: "1..1"
    fhir_attribute: subject
  - class: visit
    cardinality: "1..1"
    fhir_attribute: context
variables:
  - var: MEDICATIONID
    primary_key: true
  - var: THER_ANTIINFECTIVES_ATCCODE
  - var: THER_ANTIINFECTIVES_ATCSYSTEM
  - var: THER_ANTIINFECTIVES_DRUGNAME
  - var: THER_ANTIINFECTIVES_START
    fhir_attribute: effectivePeriod.start
  - var: THER_ANTIINFECTIVES_END
    fhir_attribute: effectivePeriod.end
---
