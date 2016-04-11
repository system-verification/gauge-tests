Refactoring results in compilation error while adding a new param and param name is a keyword in java or a numeric value or keyword
===================================================================================================================================

tags: refactoring

* In an empty directory initialize a project named "refactoring_numeric_keyword_parameter" with the current language

* Create a scenario "scenario refactoring numeric and keyword parameter" in specification "spec refactoring numeric parameter" with the following steps with implementation 
     |step text               |implementation|
     |------------------------|--------------|
     |Step with "two" "params"|"inside step" |

Rephrase step with all new parameters
-------------------------------------

* Refactor step "Step with \"two\" \"params\"" to "Step with \"2\" \"new\""

* Execute the spec "spec refactoring numeric parameter" and ensure success

