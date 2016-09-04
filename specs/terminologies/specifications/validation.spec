Spec Validation Errors occuring during execution
===========================================

tags: validation

* In an empty directory initialize a project named "spec_exec_with_validation_err" with the current language

Spec execution with unimplemented step in scenarios
---------------------------------------------------

* Create a scenario "Sample scenario" in specification "Basic spec execution" with the following steps 

     |step text                |
     |-------------------------|
     |First unimplemented step |
     |Second unimplemented step|

* Create a scenario "Sample scenario2" in specification "Basic spec execution" with the following steps with implementation 

     |step text  |implementation      |
     |-----------|--------------------|
     |First step |"inside first step" |
     |Second step|"inside second step"|

* Execute the spec "Basic spec execution" and ensure failure
* Console should contain following lines in order 

     |console output                                              |
     |------------------------------------------------------------|
     |Step implementation not found => 'First unimplemented step' |
     |Step implementation not found => 'Second unimplemented step'|
     |inside first step                                           |
     |inside second step                                          |

* Statics generated should have

     |Statistics name|executed|passed|failed|skipped|
     |---------------|--------|------|------|-------|
     |Specifications |1       |1     |0     |0      |
     |Scenarios      |1       |1     |0     |1      |

* verify statistics in html with totalCount "1", passCount "1", failCount "0", skippedCount "0"

Spec execution with unimplemented step in context step
------------------------------------------------------

* Create a specification "Basic spec execution" with the following unimplemented contexts 

     |step text    |
     |-------------|
     |First context|

* Create a scenario "Sample scenario2" in specification "Basic spec execution" with the following steps with implementation 

     |step text  |implementation      |
     |-----------|--------------------|
     |First step |"inside first step" |
     |Second step|"inside second step"|

* Execute the spec "Basic spec execution" and ensure failure
* Console should contain following lines in order 

     |console output                                  |
     |------------------------------------------------|
     |Step implementation not found => 'First context'|

* Statics generated should have

     |Statistics name|executed|passed|failed|skipped|
     |---------------|--------|------|------|-------|
     |Specifications |0       |0     |0     |1      |
     |Scenarios      |0       |0     |0     |1      |

* verify statistics in html with totalCount "1", passCount "0", failCount "0", skippedCount "1"

Spec execution with unimplemented step in context step and scenario
-------------------------------------------------------------------

* Create a specification "Basic spec execution" with the following unimplemented contexts 

     |step text    |
     |-------------|
     |First context|

* Create a scenario "Sample scenario2" in specification "Basic spec execution" with the following steps with implementation 

     |step text  |implementation      |
     |-----------|--------------------|
     |First step |"inside first step" |
     |Second step|"inside second step"|

* Create a scenario "Sample scenario" in specification "Basic spec execution" with the following steps 

     |step text                |
     |-------------------------|
     |Second unimplemented step|

* Execute the spec "Basic spec execution" and ensure failure
* Console should contain following lines in order 

     |console output                                              |
     |------------------------------------------------------------|
     |Step implementation not found => 'First context'            |
     |Step implementation not found => 'Second unimplemented step'|

* Statics generated should have

     |Statistics name|executed|passed|failed|skipped|
     |---------------|--------|------|------|-------|
     |Specifications |0       |0     |0     |1      |
     |Scenarios      |0       |0     |0     |2      |

* verify statistics in html with totalCount "1", passCount "0", failCount "0", skippedCount "1"

Spec with no heading
--------------------

* Create a scenario "Sample scenario" in specification "" with the following steps 

     |step text                |
     |-------------------------|
     |First unimplemented step |
     |Second unimplemented step|

* Execute the spec "" and ensure failure
* Console should contain "Spec heading should have at least one character"

Scenario with no heading
------------------------

* Create a scenario "" in specification "Scenario with no heading" with the following steps 

     |step text                |
     |-------------------------|
     |First unimplemented step |
     |Second unimplemented step|

* Execute the spec "Scenario with no heading" and ensure failure
* Console should contain "Scenario heading should have at least one character"

Skip spec if all scenarios are skipped
--------------------------------------

* Create a scenario "Sample scenario" in specification "Basic spec execution" with the following steps 

     |step text                |
     |-------------------------|
     |First unimplemented step |
     |Second unimplemented step|

* Create a scenario "Sample scenario2" in specification "Basic spec execution" with the following steps 

     |step text                |
     |-------------------------|
     |Third unimplemented step |
     |Fourth unimplemented step|

* Execute the spec "Basic spec execution" and ensure failure
* Console should contain following lines in order 

     |console output                                              |
     |------------------------------------------------------------|
     |Step implementation not found => 'First unimplemented step' |
     |Step implementation not found => 'Second unimplemented step'|
     |Step implementation not found => 'Third unimplemented step' |
     |Step implementation not found => 'Fourth unimplemented step'|

* Statics generated should have

     |Statistics name|executed|passed|failed|skipped|
     |---------------|--------|------|------|-------|
     |Specifications |0       |0     |0     |1      |
     |Scenarios      |0       |0     |0     |2      |

* verify statistics in html with totalCount "1", passCount "0", failCount "0", skippedCount "1"
